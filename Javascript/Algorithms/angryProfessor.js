function angryProfessor(k, a) {
    let H=0
    for (let i = 0; i < a.length; i++) {
        if (a[i] <=0) {
            H += 1 
        }
    }     
    if (H >= k ) {
        return 'NO'
    } else {
        return 'YES'
    }
}