class book{
    constructor(name, author, pages){
        this.name = name
        this.author = author
        this.pages = pages
    }

    get concatenation(){
        return this.concatenate()
    }

    concatenate(){
        return this.name + " book has " + this.pages + " pages and is written by " + this.author + "🔥"
    }

}

const book1 = new book('no longer human', 'Osamu Dazai', 200)
console.log(book1.concatenation)