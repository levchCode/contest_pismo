import MainBar from '../components/MainBar'
import background from '../assets/background.svg'
import Button from '@mui/material/Button'
import {useState, useEffect} from 'react';
import { get } from '../services/GeneralService'
import Countdown from 'react-countdown';

import '../css/main.css';

function Home() {

    const [state, setState] = useState({
        contest: {
            id: '',
            year: 0,
            start: new Date(),
            finish: new Date(),
            topics: []
        },
        isFetching: true
    })

    useEffect(() => {
        get('/api/contests/last')
        .then((data) => {
            data.id = data._id['$oid']
            localStorage.setItem('contestId', data.id);
            localStorage.setItem('year', data.year);
            data.start = new Date(data.start * 1000)
            data.finish = new Date(data.finish * 1000)
            localStorage.setItem('startDate', data.start);
            localStorage.setItem('finishDate', data.finish);
            setState({ contest: data, isFetching: false });
        });
    }, [])

    const renderMainAction = () => {
        const current = (new Date())

        if (state.contest.start < current && current > state.contest.finish) {
            return <Button size="large" variant="contained" className='centered'>Участвовать</Button>
        } else {
            return <Button size="large" variant="contained" className='centered'>Правила</Button>
        }
    }

    const renderCountdown = () => { 
        const current = (new Date())

        if (state.contest.start > current) {
            return <>
                <p>До начала конкурса: </p>
                <Countdown date={state.contest.start} />,
            </>
        } else {
            if (state.contest.start < current && current < state.contest.finish) {
                return <>
                    <p>До конца конкурса осталось: </p>
                    <Countdown date={state.contest.finish} />
                </>
            }
        } 
    }

    return (
        <div className="mainscreen" style={{ backgroundImage: `url(${background})` }}>
            <MainBar />
            <h1 className='main-center'>Конкурс письменных работ на русском языке</h1>
            {renderCountdown()}
            {renderMainAction()}
        </div>
    )
}
export default Home