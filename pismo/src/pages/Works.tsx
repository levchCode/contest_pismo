import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Stack from '@mui/material/Stack'
import MainBar from '../components/MainBar'
import {
    Link
} from "react-router-dom";

function Works() {
    return (
        <div className='grey mainscreen'>
        <MainBar />
        <Stack spacing={2} alignItems="center">
            <h1>Работы участников (2022)</h1>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <Paper className='rule' elevation={3} >
                        leVch
                    </Paper>
                </Grid>
                <Grid item xs={12}>
                    <Paper className='rule' elevation={3} >
                        Cevch
                    </Paper>
                </Grid>
                <Grid item xs={12}>
                    <Paper className='rule' elevation={3} >
                        Правило 3
                    </Paper>
                </Grid>
                <Grid item xs={12}>
                    <Paper className='rule' elevation={3} >
                        Правило 4
                    </Paper>
                </Grid>
                <Grid item xs={12}>
                    <Paper className='rule' elevation={3} >
                        Правило 5
                    </Paper>
                </Grid>
            </Grid>
        </Stack>
        </div>
    )
}
export default Works