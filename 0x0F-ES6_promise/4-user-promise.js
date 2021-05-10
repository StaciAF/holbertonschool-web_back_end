const signUpUser = (firstName, lastName) => Promise.resolve({
  firstName: `${firstName}`,
  lastName: `${lastName}`,
});
export default signUpUser;
