export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      let studentGrade = 'N/A';
      newGrades.forEach((theGrade) => {
        if (theGrade.studentId === student.id) studentGrade = theGrade.grade;
      });
      return { ...student, grade: studentGrade };
    });
}
