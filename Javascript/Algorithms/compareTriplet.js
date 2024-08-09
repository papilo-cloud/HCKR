function compareTriplets(a, b) {
    var an = 0
    var bn = 0
    for (var i = 0; i < a.length; i++) {
        if (a[i] > b[i]) {
            an += 1
        }
        if (a[i] < b[i]) {
            bn += 1
        }
    }
    const ans = [an,bn]
    return ans
}