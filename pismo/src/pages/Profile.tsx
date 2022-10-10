import MainBar from '../components/MainBar'
import Button from '@mui/material/Button'
import Paper from '@mui/material/Paper'

function Profile() {
    return (
        <>
            <MainBar />
            <Paper elevation={3} >
                <h1>Личный кабинет</h1>

                <p>Ник:</p>
                <p>leVch</p>

                <br/>
                <br/>

                <p>Уровень участника:</p>
                <p>Upper-Intewrmediate</p>

                <div>
                    <Button variant="contained">Мои работы</Button>
                    <Button variant="contained">Загрузить работу</Button>
                </div>
            </Paper>
        </> 
    )
}
export default Profile