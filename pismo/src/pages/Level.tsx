import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import MainBar from '../components/MainBar'
import Button from '@mui/material/Button'

function Level() {
    return (
        <>
        <MainBar />
        <h1>Выберете уровень владенния русским языком</h1>
        <Grid container spacing={2}>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Upper-Intemediate / Fluent
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Intermediate
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    PreIntemediate
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Beginner
                </Paper>
            </Grid>
        </Grid>

        <br />
        <br />

        <Button variant="contained">Зарегистрироваться</Button>
        </>
    )
}
export default Level