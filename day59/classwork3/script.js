const b1 = document.getElementById('b1')
const p = document.getElementById('p')



let number = 0

b1.addEventListener("click",function(){
    number += 1
    p.textContent = number
    console.log(number)
})

