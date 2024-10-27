function findsimilar(arr1 , arr2){
    let res = []
    for (let i = 0 ; i < arr1.length ; i++){
        for (let x = 0 ; x < arr2.length ; x++){
            if (arr1[i] == arr2[x]){
                res.push(arr1[i])
            }
        }
    }
    console.log(res)
}
findsimilar([1 , 2 , 3 , 4] , [11, 2, 13 ,4])
