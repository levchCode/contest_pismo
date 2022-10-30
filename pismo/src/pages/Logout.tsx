import React from 'react';
import { GoogleLogout } from 'react-google-login';

import {clientId} from '../consts';

function Logout() {
  const onSuccess = () => {
    console.log('Logout made successfully');
  };

  return (
    <div>
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
      ></GoogleLogout>
    </div>
  );
}

export default Logout;