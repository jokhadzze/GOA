const me = {
    name: 'nina',
    lastName: 'jokhadze',
    height: 180,
    genderFemale: true
}

me.name = 'nini'
delete me.genderFemale

console.log(me)


const country = {
    name: 'Georgia',
    population: '3.7m',
    area: "69.7km*2",
    capital: 'Tbilisi',
    size: 'small',
    pupolationOf(){
        console.log(this.population)
    },
    placeToLive(){
        console.log("it's ight")
    }
}

// ობიექტი არის კუთვნილებების შემმცველი სივრცე/კონტეინერი და თითოეულ მათგანს გააჩნია მნიშვნელობა

// მეთოდი არის ფუნქცია, ღომელიც გაამოიყენება კონკრეტულ ობიექტში

// this key word გამოიყენება იმისთვის რომ, ობიქტში შეწმნილ ფუნქციაში აღვნიშნოტ ობიექტის სახელი

// შეგვიძლია კუთვნილებების მნიშვნელობა რომ შევცვალოთ, ამისთვის ვწერთ  ობიქტის სახელს --> წერტილი --> კუთვნილების სახელი და ვუტოლებთ
// ახალ მნიშვმნელობას

// წაშლას რაც ეხება, ვიყენებთ დოტ ნოტაციას: delete key word --> obj name --> dot --> property name