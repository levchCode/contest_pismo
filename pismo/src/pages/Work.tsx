import Paper from '@mui/material/Paper'
import MainBar from '../components/MainBar'
import Grid from '@mui/material/Grid'

function Work() {
    return (
        <>
        <MainBar />
        <h1>Работа участника levch</h1>
        <br/>
        <br/>
        <Grid container spacing={2}>
            <Grid item xs={3}>
                <Paper>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec egestas quis ipsum et hendrerit. Donec sit amet accumsan nunc, ac convallis nisi. Nam mollis cursus orci, ut iaculis metus dictum non. In placerat, massa a tempus hendrerit, odio sapien posuere metus, at tristique eros augue in lectus. Nulla nec orci imperdiet, ultricies nisi ac, tincidunt ante. Curabitur gravida id lorem sit amet porta. Ut a ante enim. Donec malesuada libero vitae ante venenatis, eu fermentum sem efficitur. In viverra tincidunt felis, a condimentum libero. Praesent est ex, venenatis sodales bibendum ac, sagittis vel augue. Cras mollis ac erat eget eleifend. Proin at purus a arcu fermentum gravida. Maecenas consectetur cursus scelerisque. Aliquam pellentesque lacus lobortis, ultricies nulla id, ultricies quam.

Sed non rutrum odio. Proin tristique ante sed fringilla venenatis. Vestibulum vel tellus vehicula, placerat sapien vitae, mollis odio. Aliquam aliquam purus lectus, eget interdum ligula elementum ac. Quisque gravida, massa sit amet vehicula elementum, neque tortor imperdiet erat, non condimentum orci ex sed nisi. Aenean pulvinar elementum nisi non elementum. Morbi vel massa ac ipsum molestie interdum. Aenean ut congue lorem. Ut est purus, venenatis at mattis nec, elementum et tellus. Sed semper nisl id magna dapibus fermentum. In ultrices aliquam lectus, vitae bibendum enim faucibus at. Praesent non gravida leo. Aenean eu mattis nisl.

Nullam fringilla lobortis lacus, in condimentum urna iaculis eu. Phasellus tellus nisl, tristique at purus quis, tempor imperdiet purus. Duis sit amet cursus leo. Curabitur vel est dictum, convallis nisl ac, fringilla purus. Cras ac tellus et orci tristique pretium sit amet in sem. Duis ut tellus sit amet turpis ullamcorper convallis. Curabitur ut mauris ut nulla tempor egestas. Morbi vel eros nunc. Nullam suscipit lobortis euismod. Nullam et vulputate enim. Vivamus nec lorem ante. 
                </Paper>
            </Grid>
        </Grid>
        </>
    )
}
export default Work