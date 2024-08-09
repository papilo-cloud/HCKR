function alternatingCharacters(s) {
    var str = 0
    for (let i = 0; i < s.length; i++) {
        let j = i + 1
    
        if (s[i] == s[j]) {
            str++
        }
    }
    return str
}