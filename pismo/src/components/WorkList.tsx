import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Stack from '@mui/material/Stack'

import {
    Link
} from "react-router-dom";

interface Review  {
    judge: string,
    grammar: number,
    vocabulary: number,
    relevance: number,
    comment: string
}

interface Essay {
    id: string,
    user: string,
    contest: string,
    active: number,
    date: string,
    title: string,
    text: string,
    reviews: Array<Review>
}

interface workListProps {
    works: Array<Essay>,
    mode: string
}

function WorkList({works, mode} : workListProps) {
    return (
        <div>
            <Stack spacing={2} alignItems="center">
                <Grid container spacing={2}>
                    {works.map((work: Essay) => {
                        return <Grid item xs={12}>
                            <Link style={{ textDecoration: 'none'}} to={(mode === 'review' ? '/review/' : '/work/' ) + work.id }>
                                <Paper className='rule' elevation={3} >
                                    {work.user + '  ' + work.title}
                                </Paper>
                            </Link>
                        </Grid>
                    })}
                </Grid>
            </Stack>
        </div>
    )
}
export default WorkList