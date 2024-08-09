function beautifulDays(i, j, k) {
    let beautiful = 0
    for (let x = i; x <= j; x++) {
        let str = x.toString()
        let num = [...str].reverse().join('')
        let ans = (((x - num)/k)%1 == 0)
        if (ans) {
            beautiful += 1
        }
    }
    return beautiful
}