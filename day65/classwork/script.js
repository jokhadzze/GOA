document.body.children[0].textContent = 'goodbye, world!'
document.body.children[0].style.color = 'red'

console.dir(document)



function manualGetElementByID(id){
    const elements = document.all;

    for(let i = 0; i < elements.length; i ++){
        if (elements[i].id === id){
            return elements[i]
        }
    }
}

console.log(ManualgetElementByID('text'))




function manualGetElementsByTagName(tagName) {
    const elements = document.all;
    const result = [];

    for(let i = 0; i < elements.length; i++) {
        if(elements[i].tagName === tagName.toUpperCase()) {
            result.push(elements[i]);
        }
    }

    return result;
}





function manualGetElementsByClassName(className) {
    const elements = document.all;
    const result = [];

    for(let i = 0; i < elements.length; i++) {
        if(elements[i].classList.contains(className)) {
            result.push(elements[i]);
        }
    }

    return result;
}