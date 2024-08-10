function plusMinus(arr) {
    const x = arr.length;
    let post = 0
    let negt = 0
    let zero = 0
    for(let i of arr){
        if(i < 1 && i !=0){
            negt += 1
        }
        if(i >= 1){
            post += 1           
        }
        if(i ==0){
            zero += 1
        }        
    }
    console.log((post/x).toFixed(6))
    console.log((negt/x).toFixed(6))
    console.log((zero/x).toFixed(6))
}