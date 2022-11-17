import Paper from '@mui/material/Paper'
import MainBar from '../components/MainBar'
import Stack from '@mui/material/Stack';
import { Rating, TextField } from '@mui/material';
import Grid from '@mui/material/Grid';
import { get, post } from '../services/GeneralService';
import {useState, useEffect, FormEvent} from 'react';
import { useParams } from 'react-router-dom';

function Review(this: any) {
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

    const [vocabulary, setVocabulary] = useState("");
    const [grammar, setGrammar] = useState("");
    const [relevance, setRelevance] = useState("");
    const [comment, setComment] = useState("");

    const { id } = useParams();

    useEffect(() => {
        get('/api/essay/' + id)
        .then((data) => {
            setState({ essay: data, isFetching: false });
        });
    }, [])

    const handleSubmit= (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        let data = {
            grammar: grammar,
            vocabulary: vocabulary,
            relevance: relevance,
            comment: comment,
            judge: '1234',//localStorage.getItem('userId')
        }

        post('/api/essay/review/' + id, data)
        .then((data) => {
          if (data['status'] === 1) {
            window.location.href = data.url
          }
        });
        
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
                            <div>
                            <form onSubmit={e => {handleSubmit(e)}}>
                                <h4>Ваша оценка</h4>
                                <span>Лексика:</span><Rating name="vocabulary" precision={0.5}  onChange={e => setVocabulary(((e.target) as HTMLInputElement).value)} /><br />
                                <span>Грамматика:</span><Rating name="grammar" precision={0.5}  onChange={e => setGrammar(((e.target) as HTMLInputElement).value)} /><br />
                                <span>Соответствие теме:</span><Rating name="relevance" precision={0.5} onChange={e => setRelevance(((e.target) as HTMLInputElement).value)} /><br />
                                <span>Комментарий</span><TextField
                                    name='comment'
                                    id="standard-basic"
                                    label="Название сочинения"
                                    variant="standard"
                                    onChange={e => setComment(e.target.value) }
                            />
                            </form>
                            </div>
                        </Grid>
                    </Grid>
                </div>
            </Stack>
            
        </div>
    )
}
export default Review