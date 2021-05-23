import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(studentList) {
  const studentIds = getListStudentIds(studentList);
  const reducer = (acc, currVal) => acc + currVal;
  return studentIds.reduce(reducer);
}
