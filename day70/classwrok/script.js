const cars = ['BMW', 'Audi', 'Pagani']

const cities = ['Tbilisi', 'Batumi', 'Poti']

const languages = ['Georgian', 'English', 'Japanese']

cars.forEach((values)=>{
    console.log(values)
})

cities.forEach((values, index)=>{
    console.log(values)
    console.log(index)
})

languages.forEach((values, index, arr)=>{
    console.log(values)
    console.log(index)
    console.log(arr)
})



function manualForEach(arr, costumFunc){
    for(let i = 0; i < arr.length; i++){
        costumFunc(arr[i], i, arr)
    }
}

manualForEach(cars, (values)=>{
    console.log(values)
})



const nums = [1,2,3,4,5]

const doubled = nums.map(num => num * 2)

console.log(doubled)


function manualMap(arr, costumFunc){
    res = []
    
    for(let i = 0; i< arr.length; i++){
        res.push(costumFunc(arr[i], i, arr))
    }
    return res
}

const newNums = manualMap(nums, (num)=>{
    return -num
})

console.log(newNums)




const numbers = [0, -6, 7, 9, 1]

const filtered = numebers.filter((number)=>{
    return number > 0
})

console.log(filtered)


function manualFilter(arr, costumFunc){
    const res = []
    for(let i = 0; i< arr.length; i++){
        if(costumFunc(arr[i], i, arr)){
            res.push(arr[i])
        }
    }
    return res
}



