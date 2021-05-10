function getResponseFromAPI() {
  const myProm = new Promise((resolve) => {
    resolve('completed');
  });
  return myProm;
}
export default getResponseFromAPI;
