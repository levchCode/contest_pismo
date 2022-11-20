import WorkList from '../components/WorkList';
import MainBar from '../components/MainBar'
import { get } from '../services/GeneralService';
import {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

function WorksReview() {
    const { contest } = useParams();

    const [state, setState] = useState({
        works: [],
        isFetching: true
    })

    useEffect(() => {
        get('/api/essay/raiting/' + contest)
        .then((data) => {
            setState({ works: data, isFetching: false });
        });
    }, [])

    return (
        <div className='grey mainscreen'>
        <MainBar />

        <h1>Работы участников (2022)</h1>
        <WorkList works={state.works} mode='review'/>
        </div>
    )
}
export default WorksReview