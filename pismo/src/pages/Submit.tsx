import TextareaAutosize from '@mui/material/TextareaAutosize'
import Button from '@mui/material/Button'
import MainBar from '../components/MainBar'
import { TextField } from '@mui/material'
import { FormEvent, useState, useEffect } from 'react';
import { get, post } from '../services/GeneralService';

function Submit() {

    const handleSubmit= (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        let data = {
            text: text,
            title: title,
            user: localStorage.getItem('userId'),
            contest: localStorage.getItem('contestId')
        }

        post('/api/essay/submit', data)
        .then((data) => {
          if (data['status'] === 1) {
            window.location.href = data.url
          }
        });
        
    }

    useEffect(() => {
        const contestId = localStorage.getItem('contestId')
        const userLevel = localStorage.getItem('level')

        if (userLevel && contestId) {
            get('/api/contests/' + contestId)
            .then((data) => {
                setTopic(data.contest.topics[userLevel].title)
            });
        } 
    }, [])

    const [title, setTitle] = useState("");
    const [text, setText] = useState("");
    const [topic, setTopic] = useState("")

    return (
        <>
        <MainBar />
        <h1>Загрузить работу</h1>

        <p>Тема конкурса: <b>{topic}</b></p>

        <p>Напишите или вставьте текст Вашей работы</p>
        <form onSubmit={e => {handleSubmit(e)}}>
            <TextField 
                name='title'
                id="standard-basic"
                label="Название сочинения"
                variant="standard"
                value={title}
                onChange={e => setTitle(e.target.value) }
            />
            <br />
            <br />
            <TextareaAutosize
                name='text'
                aria-label="empty textarea"
                style={{ width: 800, height: 800 }}
                onChange={e => setText(e.target.value) }
            />
        
            <Button type='submit' variant="contained">Загрузить</Button>
        </form>
        </>
    )
}
export default Submit