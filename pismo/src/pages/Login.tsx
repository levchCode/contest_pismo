import React from 'react';
import { GoogleLogin } from 'react-google-login'

import MainBar from '../components/MainBar'
import Paper from '@mui/material/Paper'
import Select, { SelectChangeEvent } from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import TextField from '@mui/material/TextField';

import {clientId} from '../consts'
import { Stack } from '@mui/material';

function Login() {
    const onSuccess = (res) => {
        console.log(res)
    }

    const onFailure = (res) => {
        console.log(res)
    }

    return (
        <div className='grey mainscreen'>
            <MainBar />
            <Stack spacing={2} alignItems="center">
                <h1>Вход / Регистрация</h1>
                <Paper className='rule' elevation={3} >
                    
                    <TextField
                        id="outlined-helperText"
                        label="Ваш логин"
                        defaultValue=""
                    />

                    <br/>
                    <br/>

                    <Select
                        labelId="demo-simple-select-helper-label"
                        id="demo-simple-select-helper"
                        value={1}
                        label="Уровень"
                    >
                        <MenuItem value={1}>Beginner</MenuItem>
                        <MenuItem value={2}>Pre-Intermediate</MenuItem>
                        <MenuItem value={3}>Intermediate</MenuItem>
                        <MenuItem value={4}>Upper-Intermediate</MenuItem>
                    </Select>

                    <br/>
                    <br/>

                    <GoogleLogin
                        clientId={clientId}
                        buttonText="Login"
                        onSuccess={onSuccess}
                        onFailure={onFailure}
                        cookiePolicy={'single_host_origin'}
                        isSignedIn={true}
                    />
                </Paper>
            </Stack>
        </div>
    )
}
export default Login