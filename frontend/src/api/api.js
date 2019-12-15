


export const allocate = async (userInput) => {

  return fetch('http://0.0.0.0/allocate', {
    method: 'POST',

    body: JSON.stringify(userInput),
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
  });
}
