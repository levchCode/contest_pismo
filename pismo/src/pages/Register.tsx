import React from 'react';
import { GoogleLogin } from 'react-google-login'

import MainBar from '../components/MainBar'
import Paper from '@mui/material/Paper'
import Select, { SelectChangeEvent } from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import TextField from '@mui/material/TextField';

import {clientId} from '../consts'
import { Stack } from '@mui/material';

function Register() {
    const onSuccess = (res: any) => {
        console.log(res)
    }

    const onFailure = (res: any) => {
        console.log(res)
    }

    return (
        <div className='grey mainscreen'>
            <MainBar />
            <Stack spacing={2} alignItems="center">
                <h1> Регистрация</h1>
                <Paper className='rule' elevation={3} >
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
export default Register