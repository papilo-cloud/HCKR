function camelcase(s) {

    let count = 1;
    let y = s.toUpperCase()
    for (let i in s) {
        if (s[i] == y[i]) {
            count++
        }
    }
    return count
}