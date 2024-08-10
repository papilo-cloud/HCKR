function timeConversion(s) {
    const y = s.split(':')[0]
    const num = Number(y) + 12
    const am = s.substr(0, s.indexOf('AM'))
    const x = y == 12 ?'12' + s.substr(2,6): num + s.substr(2,6)

    if (s.includes('PM')) {
        return x
    }
    const ans = y == 12 ? '00' +s.substr(2,6) : am
    return ans
}