import {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import MainBar from '../components/MainBar';
import WorkList from '../components/WorkList';
import { get } from '../services/GeneralService';

function WorksUser() {
    const { userId } = useParams();

    const [state, setState] = useState({
        works: [],
        isFetching: true
    })

    useEffect(() => {
        get('/api/essay/by/' + userId)
        .then((data) => {
            setState({ works: data, isFetching: false });
        });
    }, [])

    return (
        <div className='grey mainscreen'>
        <MainBar />

        <h1>Работы участника (ник)</h1>
        <WorkList works={state.works} mode='user'/>
        </div>
    )
}
export default WorksUser