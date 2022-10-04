import TextareaAutosize from '@mui/material/TextareaAutosize'
import Button from '@mui/material/Button'
import MainBar from '../components/MainBar'

function Submit() {
    return (
        <>
        <MainBar />
        <h1>Загрузить работу</h1>

        <p>Напишите или вставьте текст Вашей работы</p>

        <TextareaAutosize aria-label="empty textarea" style={{ width: 800, height: 800 }}/>
        <br/>
        <br/>
        <Button variant="contained">Загрузить</Button>
        </>
    )
}
export default Submit