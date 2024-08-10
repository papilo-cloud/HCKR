function gradingStudents(grades) {
    var bn=[] ;
    for (let i in grades) {
        if (grades[i] >= 38) {
            const x =((grades[i] - grades[i]%5) + 5) - grades[i]
            grades[i] = x < 3 ? grades[i] + x : grades[i]
        }
        bn.push(grades[i])
    }
      return bn   
}