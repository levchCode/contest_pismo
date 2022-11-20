import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import { get } from '../services/GeneralService';

import {
  Link
} from "react-router-dom";


const settings = 
[
    {
      name: 'Личный кабинет',
      link: '/profile'
    },
    {
      name: 'Выход',
      link: '/logout'
    }
]


const ResponsiveAppBar = () => {
  const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

    const [state, setState] = React.useState({
      contest: {
          id: '',
          year: 0,
          start: new Date(),
          finish: new Date(),
          topics: []
      },
      activeEssay: '',
      isFetching: true
  })

  React.useEffect(() => {
      get('/api/contests/last')
      .then((data) => {
          data.id = data._id['$oid']
          data.start = new Date(data.start * 1000)
          data.finish = new Date(data.finish * 1000)
          setState({ contest: state.contest, activeEssay: '', isFetching: false });

          const current = (new Date());

          if (data.start < current && current < data.finish) {
            get('/api/essay/active/' + localStorage.getItem('userId'))
            .then((data) => {
              data.id = data._id['$oid']
              setState({ contest: state.contest, activeEssay: data.id, isFetching: false });
            });
          } 
            
      });
  }, [])

  const pages = {
    hiatus: [
      {
        name: 'Правила',
        link: '/rules',
      },
      {
        name: 'Работы участников',
        link: '/works/' + state.contest.id,
      }
    ],
    compete: [
      {
        name: 'Правила',
        link: '/rules',
      },
      {
        name: 'Моя работа',
        link: state.activeEssay !== '' ?  '/work/' + state.activeEssay : '/submit' ,
      }
    ]
  };

  const checkDate = () => {
    const current = (new Date());
    const start = state.contest.start
    const finish = state.contest.finish

    if (start && finish) {
      return (start < current && current < finish)
    }
  }

  const renderTabs = () => {
    if (state.contest && checkDate()) {
      return <>
      {
        pages.compete.map((page: { name: string, link: string }) => (
          <MenuItem key={page.name} onClick={handleCloseNavMenu}>
            <Link to={page.link} style={{ textDecoration: 'none'}}>
              <Typography textAlign="center">{page.name}</Typography>
            </Link>
          </MenuItem>
        ))
      }
    </>
    } else {
      return <>
      {
        pages.hiatus.map((page: { name: string, link: string }) => (
          <MenuItem key={page.name} onClick={handleCloseNavMenu}>
            <Link to={page.link} style={{ textDecoration: 'none'}}>
              <Typography textAlign="center">{page.name}</Typography>
            </Link>
          </MenuItem>
        ))
      }
    </>
    }
  }

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            Письмо
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >

            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {
                renderTabs()
              }
            </Menu>
          </Box>
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LOGO
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              {
                renderTabs()
              }
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem component={Link} to={setting.link} key={setting.name} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting.name}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default ResponsiveAppBar;