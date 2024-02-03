export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }

  const studentIdsSum = students.reduce((sum, student) => sum + student.id, 0);

  return studentIdsSum;
}
