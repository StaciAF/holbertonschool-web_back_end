const getFullResponseFromAPI = (success) => {
  const myProm = new Promise((resolve, reject) => {
    if (success === true) {
      const myObj = {
        status: 200,
        body: 'Success',
      };
      resolve(myObj);
    } else {
      reject(new Error('The fake API is not working correctly'));
    }
  });
  return myProm;
};

export default getFullResponseFromAPI;
