// var x = 10
// if (true) {
//   var x = 20  // This changes the value of x everywhere
// }
// console.log(x) // Outputs: 20


// let y = 10
// if (true) {
//   let y = 20  // This y only exists inside this block
// }
// console.log(y) // Outputs: 10


// const namme = 'Nina' // This will cause an error because 
// name = 'Luka'       //you can't reassign a const

       


// const addd = (a, b) => a + b  // no need to write keyword 
// //                             'function'



// const name = 'Nina'
// console.log(`Hello, ${name}!`)


// function greet(name = 'user') {
//     return `Hello, ${name}`
// }



// const [a, b] = [1, 2]   //😜😜😜😜😜


// const fruitss = ['banana', 'cherry'];

// const updated = ['apple,', ...fruitss, 'mango']



// const arr = [1, 2, 3]
// const newArr = [...arr, 4, 5]   //🤘🤘🤘🤘🤘



// const fetchData = () => new Promise((resolve, reject) => {
//     setTimeout(() => resolve('Data fetched'), 1000)
// })
// fetchData().then(result => console.log(result))



// class Animal {
//     constructor(name) {
//       this.name = name
//     }
//     speak() {
//       console.log(`${this.name} makes a sound.`)
//     }
// }


// // In a file called math.js
// export const add = (a, b) => a + b

// // In another file
// import { add } from './math.js'
// console.log(add(2, 3))




let imgDIvs = document.getElementsByClassName('img-divs')

let btns = document.getElementsByTagName('button')

Array.from(btns).forEach((btn, i)=>{
  btn.addEventListener('click', ()=>{
    div = imgDIvs[i]
    if(div.style.visibility != 'visible'){
      div.style.visibility = 'visible'
      div.style.position = 'relative'
    }
    else{
      div.style.visibility = 'hidden'
      div.style.position = 'absolute'
    }
  })
})