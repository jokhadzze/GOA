const divElements = document.getElementsByTagName('div')

for(const div of divElements){
    
    div.addEventListener('click', function(){
        console.log('clicked on div with id: ' + String(div.id))
    })
}

// bubling method - მოვლენა ვრცელდება შიდა ელმენტიდან გარე ლემენეტისკენ

// capturing - მოვლენა ვრცელდება გარე ელმენტიდან შიდა ლემენეტისკენ

const prev = document.querySelector('#prev');
const next = document.querySelector('#next');
const img = document.querySelector('img');

const imgArr = ['/day68/photos/berserk1.png', '/day68/photos/berserk2.png', '/day68/photos/berserk3.png', '/day68/photos/berserk4.png', '/day68/photos/berserk5.png'];
let index = 0;

next.addEventListener('click', function() {
    index++;
    if(index >= imgArr.length) {
        index = 0;
    }
    img.src = imgArr[index];
})


prev.addEventListener('click', function() {
    index--;
    if(index < 0) {
        index = 4;
    }
    img.src = imgArr[index];
})

