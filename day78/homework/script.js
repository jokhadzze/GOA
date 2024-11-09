// შევქმნათ ფუნქცია, რომელიც დააბრუნებს ორი გადაცემული მატრიცის ( 2D მასივის ) ჯამს. მაგ:
// [[1,3],[1,4]], [[4,1],[2,2]] —> [[5,4],[5,5]]

function addition(first, second){
    let res = []
    for(let i = 0; i < first.length; i++){
        for(let d = 0; d < second.length; d++){
            res.push(first[i] + second[d])
        }
    }

    console.log(res)
}

addition([[1,3],[1,4]],[[4,1],[2,2]])


// შევქმნათ ფუნქცია რომელიც გადაცემულ მატრიცას გაუცვლის რიგებს და სვეტებს

function switcher(arr){
    let a = arr[0]
    let b = arr[1]
    let res  = []
    for(let i = 0; i < arr.lenth; i++){
        d  = a[i] + b[i]
        res.push(d)
    }

    console.log(res)
}

switcher([[1,2], [3,4]])



// შევქმნათ ფუნქცია რომელიც გადაცემულდ nXn მატრიცის დიაგონალურად განწყობილი ელემენტების ჯამს დააბრუნებს (უნდა დაბრუნდეს ორი რიცხვი).