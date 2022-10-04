import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import MainBar from '../components/MainBar'

function Rules() {
    return (
        <>
        <MainBar />
        <h1>Правила конкурса</h1>
        <Grid container spacing={2}>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Правило 1
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Правило 2
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Правило 3
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Правило 4
                </Paper>
            </Grid>
            <Grid item xs={12}>
                <Paper elevation={3} >
                    Правило 5
                </Paper>
            </Grid>
        </Grid>
        </>
    )
}
export default Rules