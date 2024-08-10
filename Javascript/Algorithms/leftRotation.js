function rotateLeft(d, arr) {
    for (let i = 0; i < d; i++) {
        let start = arr[0];
        for (let j = 0; j < arr.length; j++) {
            arr[j] = arr[j + 1];
        }
        arr[arr.length- 1] = start;
    }
return arr;
}
