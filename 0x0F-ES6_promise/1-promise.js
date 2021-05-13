export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      const myObj = {
        status: 200,
        body: 'Success',
      };
      resolve(myObj);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
