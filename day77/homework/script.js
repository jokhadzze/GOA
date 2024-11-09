//  ფუნქცია რომელსაც გადაეცემა სვეტი და რიგი (row, col) და გამოპრინტავს 
// თითოეული ელემენტის პოზიციას სვეტი-სვეტ , მაგ: ( 2, 2 ) --->  row: 1 col:1, row: 1 col:2, row: 2 col: 1, row:2 col: 2;

function rowsCols(rows, cols){
    for(let row = 0; row <= rows; row++){
        for(let col = 0; col <= cols; col++){
            console.log(`rows: ${row}, columns ${col}`)
        }
    }
}

rowsCols(3, 9)



// ფუნქცია რომელიც ქმნის გამრავლების ტაბულას 1-10 და აბრუნებს მათ 2D მასივის ფორმაში ანუ ასეთში:  [  [1,2,3...],  [2,4,6...],  [3,6...]...  ]

function multiply(){
    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    let res = []
    for(let i = 0; i < nums.length; i++){
        for(let d = 0; d < nums.length; d++){
            res.push(nums[i] * nums[d])
        }
        console.log(res)
    }
}

multiply()




// ფუნქცია რომელსაც გადაეცემა რიცხვი და გამოპრინტავს ყველა იმ რიცხვის მაგალითს სადაც მეორე რიცხვი მეტია პირველზე,
//  ანუ თუ გადავეცით რიცხვი სამი, ყველა
//  წყვილი იქნებოდა: (1,1) (1,2) (1,3) (2,1) (2,2) (2,3) (3,1) (3,2) (3,3) ----> აქედან უუნდა გამოვიტანოთ მხოლოდ (1,2), (2,3), (1,3)

function bigger(num){
    let res = []
    for(let i = 1; i < num; i++){
        for(let d = i + 1; d <= num; d++){
            if(i < d){
                res.push(`${i},${d}`)
            }
        }
    }

    console.log(res)
}

bigger(7)