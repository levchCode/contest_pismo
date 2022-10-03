import MainBar from '../components/MainBar'
import background from '../assets/background.svg'


function Home() {
    return (
        <>
            <MainBar />
            <div className="background" style={{ backgroundImage: `url(${background})`, width: '100%',
  height: '800px',  backgroundSize: 'cover' }}>
                <h1>Конкурс письменный работ на русском языке</h1>
            </div>
        </> 
    )
}
export default Home