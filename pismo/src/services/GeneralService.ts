export async function post(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
      body: JSON.stringify(data)
    });
    return response.json();
  }

export async function get(url = '') {
    const response = await fetch(url, {
      method: 'GET',
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
    });
    return response.json();
  }