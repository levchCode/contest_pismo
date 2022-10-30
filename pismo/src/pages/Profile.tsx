import MainBar from '../components/MainBar'
import Button from '@mui/material/Button'
import Stack from '@mui/material/Stack'
import Paper from '@mui/material/Paper'

import {
    Link
} from "react-router-dom";

function Profile() {
    return (
        <div className='grey mainscreen'>
            <MainBar />
            <Stack spacing={3} alignItems="center">
                <h1>Личный кабинет</h1>
                <Paper elevation={3} className='profile'>
                    <p><b>Ник:</b></p>
                    <p>leVch</p>

                    <br/>

                    <p><b>Уровень участника:</b></p>
                    <p>Upper-Intermediate</p>

                    <br/>

                    <div>
                        <Button component={Link} to='/works' variant="contained">Предыдущие работы</Button>
                        <Button component={Link} to='/work' variant="contained">Моя работа</Button>
                    </div>
                </Paper>
            </Stack>
        </div> 
    )
}
export default Profile