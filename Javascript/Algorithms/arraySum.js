function simpleArraySum(ar) {
    let ans = 0
    for (const element of ar) {
        ans += element
    }
    return ans 
}

console.log(simpleArraySum([1,2,3,4,5, 6]))