import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignUp = (firstName, lastName, fileName) => Promise.allSettled([
  signUpUser(firstName, lastName),
  uploadPhoto(fileName)]);

export default handleProfileSignUp;
