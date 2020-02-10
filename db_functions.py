import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import json
from datetime import datetime as dt

def init():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    CREDENTIAL_FILE = 'credentials.json'
    TOKEN_FILE = 'token.pickle'
    credentials = None
    
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            credentials = pickle.load(token)
    
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIAL_FILE, SCOPES)
            credentials = flow.run_local_server(port=10800)

        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(credentials, token)

    service = build('sheets', 'v4', credentials=credentials)

    return service.spreadsheets()

# Регистрация участников
def register(nick, pwd, email):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Users!A2:D").execute()
    rows = result.get('values', [])
    last_user = int(rows[len(rows)-1][0])
    
    row = [last_user+1, nick, pwd, email]

    sheet.values().append(spreadsheetId='1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg', valueInputOption="RAW", range="Users", body={'values': [row]}).execute()
    return True

# Вход для участников
def login(nick, pwd):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Users!A2:D").execute()
    rows = result.get('values', [])
    users = pd.DataFrame.from_records(rows)
    res = users.loc[(users[1] == nick) & (users[2] == pwd)]

    return res.values.tolist()[0][0]

# Получить все работы за конкурс
def get_submitions():
    sheet = init()

    users = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Users!A2:D").execute()
    user_rows = users.get('values', [])

    subs = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Submissions!A2:G").execute()
    subs_rows = subs.get('values', [])

    tasks = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Tasks!A2:C").execute()
    tasks_rows = tasks.get('values', [])

    users = pd.DataFrame.from_records(user_rows)
    subs = pd.DataFrame.from_records(subs_rows)
    tasks = pd.DataFrame.from_records(tasks_rows)

    joined = pd.merge(users, subs,  how='left', left_on=0, right_on=1).dropna()
    joined = pd.merge(joined, tasks,  how='left', left_on="2_y", right_on=0).dropna()

    needed_rows = joined[['0_y', 1, '1_x', 4, 5, 6]]

    needed_rows["avg"] = (needed_rows[4].astype('int64') + needed_rows[5].astype('int64') + needed_rows[6].astype('int64'))/3

    needed_rows = needed_rows.sort_values(by='avg', ascending=False)

    return needed_rows.values.tolist()

def submit(user_id, task_id, answer, complete):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Submissions!A2:G").execute()
    rows = result.get('values', [])
    last_sub = int(rows[len(rows)-1][0])
    
    row = [last_sub+1, user_id, task_id, answer, 0, 0, 0, complete]

    sheet.values().append(spreadsheetId='1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg', valueInputOption="RAW", range="Submissions", body={'values': [row]}).execute()
    return last_sub+1

def get_sub(sub_id, user_id):
    sheet = init()
    
    users = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Users!A2:D").execute()
    user_rows = users.get('values', [])

    subs = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Submissions!A2:G").execute()
    subs_rows = subs.get('values', [])

    tasks = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Tasks!A2:C").execute()
    tasks_rows = tasks.get('values', [])

    ces = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="CE!A2:G").execute()
    ces_rows = ces.get('values', [])

    users = pd.DataFrame.from_records(user_rows)
    subs = pd.DataFrame.from_records(subs_rows)
    tasks = pd.DataFrame.from_records(tasks_rows)
    ces = pd.DataFrame.from_records(ces_rows)

    joined = pd.merge(users, subs,  how='left', left_on=0, right_on=1).dropna()
    joined = pd.merge(joined, tasks,  how='left', left_on="2_y", right_on=0).dropna()

    result = joined.loc[joined['0_y'] == str(sub_id)]
    result_comments = ces.loc[ces[1] == str(sub_id)]

    result_comments = pd.merge(users, result_comments,  how='left', left_on=0, right_on=2).dropna()

    response = result[['0_y', 1, '1_x', '3_y', 4, 5, 6, 2]]

    user_commented = result_comments[result_comments['0_x'] == user_id]

    return response.values.tolist(), result_comments.values.tolist(), not user_commented.empty

def get_tasks():
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Tasks!A2:C").execute()
    rows = result.get('values', [])

    return rows

def get_task(t_id):
    tasks = get_tasks()
    tasks = pd.DataFrame.from_records(tasks)
    res = tasks.loc[tasks[0] == t_id]
    return res.values.tolist()[0]

def get_user(u_id):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Users!A2:D").execute()
    rows = result.get('values', [])

    users = pd.DataFrame.from_records(rows)
    res = users.loc[users[0] == u_id]
    return res.values.tolist()[0]

def update_avg(sub_id):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="CE!A2:G").execute()
    rows = result.get('values', [])

    grades = pd.DataFrame.from_records(rows)
    grades = grades.loc[grades[1] == str(sub_id)]

    n_row = sub_id + 1 
    re_row = [grades[3].astype('int32').mean().item(), grades[4].astype('int32').mean().item(), grades[5].astype('int32').mean().item()]

  
    rag = "Submissions!E" + str(n_row) + ":G" + str(n_row)

    body = {
        "values": [re_row]
    }

    result = sheet.values().update(spreadsheetId='1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg', valueInputOption="RAW", range=rag, body=body).execute()

def comment(sub_id, u_id, g_s, v_s, tr_s, comment):
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="CE!A2:G").execute()
    rows = result.get('values', [])
    last_comment = int(rows[len(rows)-1][0])
    
    row = [last_comment+1, sub_id, u_id, g_s, v_s, tr_s, comment]

    sheet.values().append(spreadsheetId='1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg', valueInputOption="RAW", range="CE", body={'values': [row]}).execute()
    update_avg(int(sub_id))

def check_date():
    sheet = init()

    result = sheet.values().get(spreadsheetId="1Iw5g-FcjnUp2X0ErIdiffpLzCwcU4u4HAeTtyvAo4Gg", range="Dates!A2:E").execute()
    row = result.get('values', [])[0]

    start_contest = dt.strptime(row[0], "%d.%m.%Y %H:%M:%S")
    stop_contest = dt.strptime(row[1], "%d.%m.%Y %H:%M:%S")
    start_vote = dt.strptime(row[2], "%d.%m.%Y %H:%M:%S")
    stop_vote = dt.strptime(row[3], "%d.%m.%Y %H:%M:%S") 
    result = dt.strptime(row[4], "%d.%m.%Y %H:%M:%S") 
    today = dt.now()

    if today > start_contest and today < stop_contest:
        td = stop_contest-today
        secs = td.total_seconds()
        hours = str(int(secs / 3600))
        minutes = str(int(secs / 60) % 60)
        seconds = str(int(secs % 60))
        return ["Идет конкурс. Осталось", hours + ":" + minutes + ":" + seconds, "", 1]
    elif today > start_vote and today < stop_vote:
        return ["Голосование. Осталось", (stop_vote-today).days, "дней", 2]
    else:
        return ["Конкурс начнется через", (start_contest-today).days, "дней", 3]

def get_results():
    subs = get_submitions()
    subs = pd.DataFrame.from_records(subs)

    n_1 = subs.loc[subs[1] == "Перевод Английский-Русский"]
    n_2 = subs.loc[subs[1] == "Перевод Русский-Английский"]
    n_3 = subs.loc[subs[1] == "Сочинение"]

    return n_1.values.tolist()[:3], n_2.values.tolist()[:3], n_3.values.tolist()[:3]