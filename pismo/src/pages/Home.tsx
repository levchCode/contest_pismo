import MainBar from '../components/MainBar'
import background from '../assets/background.svg'
import Button from '@mui/material/Button'

import '../css/main.css';


function Home() {
    return (
        <div className="mainscreen" style={{ backgroundImage: `url(${background})` }}>
            <MainBar />
            <h1 className='main-center'>Конкурс письменных работ на русском языке</h1>
            <Button size="large" variant="contained" className='centered'>Участвовать</Button>
        </div>
    )
}
export default Home