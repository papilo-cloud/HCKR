function utopianTree(n) {
    let H=0
    for (let i = 0; i <= n; i++) {
        if (i == 0 ) {
            H = 1
        }
        if (i == 1) {
            H = 2
        }
        if (i> 1 && i % 2 == 0) {
            H += 1
        } if (i > 1 && i %2 != 0) {
            H *= 2
        }
    }
    return H
}