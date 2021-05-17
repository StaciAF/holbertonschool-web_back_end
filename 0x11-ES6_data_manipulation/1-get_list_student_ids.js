export default function getListStudentIds(objArray) {
  const mtArray = [];
  if (!Array.isArray(objArray)) {
    return mtArray;
  }
  return objArray.map((eachObj) => eachObj.id);
}
