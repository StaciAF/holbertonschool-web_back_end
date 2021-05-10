import { uploadPhoto, createUser } from './utils';

const handleProfileSignup = () => {
  Promise.all([uploadPhoto(), createUser()]).then((values) => {
    console.log(values[0].body, values[1].firstName, values[1].lastName);
  });
};
export default handleProfileSignup;
