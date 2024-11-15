// bubble sort

function bubbleSort(arr){
  let n = arr.length
  for(let i = 1; i < n; i++)
    for(let j = 0; j < n - 1; j++){
      if (arr[j] > arr[j + 1]){
        let temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
      }
      console.log(arr)
    }
}
bubbleSort([5,6,9,10,7,11,2,1,3,4])


// დაწერეთ პროგრამა, რომელიც კლავიატურიდან შეტანილი 
// მთელი რიცხვისთვის დაადგენს თუ რამდენი კენტი ციფრისგან 
// შედგება  იგი და შედეგს გამოიტანს ეკრანზე.

function countOdds(arr){
    count = 0
    for(i = 0; i < arr.length; i++){
        if (arr[i] % 2 !==0){
            count += 1
        }
    }
    console.log(count)
}

countOdds([1,2,3,4,5])