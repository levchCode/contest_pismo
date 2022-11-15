import Paper from '@mui/material/Paper'
import MainBar from '../components/MainBar'
import Stack from '@mui/material/Stack';
import { Rating } from '@mui/material';
import Grid from '@mui/material/Grid';
import { get } from '../services/GeneralService';
import {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

function Work(this: any) {
    interface Review  {
        judge: string,
        grammar: number,
        vocabulary: number,
        relevance: number,
        comment: string
    }

    const [state, setState] = useState({
        essay: {
            user: '',
            contest: '',
            active: 0,
            date: '',
            title: '',
            text: '',
            reviews: []
        },
        isFetching: true
    })

    const { id } = useParams();

    useEffect(() => {
        get('/api/essay/' + id)
        .then((data) => {
            setState({ essay: data, isFetching: false });
        });
    }, [])

    const getFinalScore = (reviews: Review[]) => {
        let finalScore = 0;

        for(let i = 0; i < reviews.length; i++) {
            finalScore += (reviews[i].vocabulary + reviews[i].grammar + reviews[i].relevance) / 3
        }

        return reviews.length > 0 ? (finalScore / reviews.length) : 0;
    }

    return (
        <div className='grey mainscreen'>
            <MainBar />

            <Stack spacing={2} alignItems="center">
                <div>
                    <h2>Работа участника {state.essay.user}</h2>
                </div>
                <div>
                    <h4>{state.essay.title}</h4>
                    <Paper className='work'>
                        {state.essay.text}
                    </Paper>
                </div>
                <div>
                    <Grid container direction="column"  spacing={2}>
                        <Grid item container >
                            <div>
                                {state.essay.reviews.map(function(review: Review) {
                                    return <>
                                        <span>{review.judge}</span><br />
                                        <span>Лексика:</span><Rating name="read-only" value={review.vocabulary} readOnly /><br />
                                        <span>Грамматика:</span><Rating name="read-only" value={review.grammar} readOnly /><br />
                                        <span>Соответствие теме:</span><Rating name="read-only" value={review.relevance} readOnly /><br />
                                        <span>Комментарий</span><p>{review.comment}</p><br />
                                    </>
                                })}
                            </div>
                        </Grid>
                        <Grid item container>
                            <Paper className='workTotal'> 
                                <span>Баллы за работу</span>
                                <br/>
                                <span>{getFinalScore(state.essay.reviews)} / 5</span>
                            </Paper>
                        </Grid>
                    </Grid>
                </div>
            </Stack>
            
        </div>
    )
}
export default Work