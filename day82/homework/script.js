let obj1 = {
    thing: 'glove',
    amount: 3
}

let obj2 = {
    thing: 'mouse',
    color: 'purple'
}

let obj3 = {
    thing: 'gift',
    cause: 'cristmas'
}

objArr = [obj1, obj2, obj3]

for(d of objArr){
    let a = d
    for(i in a){
        console.log(a[i])
}
}