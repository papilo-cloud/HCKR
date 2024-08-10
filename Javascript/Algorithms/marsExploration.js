function marsExploration(s) {
    let res = [...s].map((d, i) => (i) % 3 == 0 ? ' ' + d : d).join('')
    let r = res.split(' ')

    let p;
    let count = 0
    for (let i = 1; i < r.length; i++) {
        p = r[i]
        if (p[0] !== 'S') {
            count++
        }
        if (p[1] !== 'O') {
            count++
        }
        if (p[2] !== 'S') {
            count++
        }
    }
    return count
}