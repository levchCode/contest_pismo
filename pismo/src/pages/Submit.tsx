import TextareaAutosize from '@mui/material/TextareaAutosize'
import Button from '@mui/material/Button'
import MainBar from '../components/MainBar'
import { TextField } from '@mui/material'
import { FormEvent, useState } from 'react';
import { request } from '../services/EssayService';

function Submit() {

    const handleSubmit= (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        let data = {
            text: text,
            title: title,
            user: '1234',//localStorage.getItem('userId'),
            contest: '1988'//localStorage.getItem('contestId')
        }

        request('/api/essay/submit', 'POST', data)
        .then((data) => {
          if (data['status'] === 1) {
            window.location.href = data.url
          }
        });
        
    }

    const [title, setTitle] = useState("");
    const [text, setText] = useState("");

    return (
        <>
        <MainBar />
        <h1>Загрузить работу</h1>

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