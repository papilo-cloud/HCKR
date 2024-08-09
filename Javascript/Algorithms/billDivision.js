function bonAppetit(bill, k, b) {
    const annaSum = bill.filter((x,i) =>  (i != k) )
    const sum = annaSum.reduce((a,b) => a + b)
    const totalBill = bill.reduce((a,b) => a + b)
    
    const total = sum / 2
    if (b == total) {
        console.log('Bon Appetit')
    } else {
        const refund = (totalBill/2) - total
        console.log(`${refund}`)
    }
}