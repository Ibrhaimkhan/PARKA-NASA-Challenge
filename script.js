var downbtn = document.getElementById('downarrow')
var buttons = document.querySelector('.buttons')
var pictures = document.querySelector('.pictures')
const pictureList = ['picture1', 'picture2', 'picture3', 'picture4'];

downbtn.addEventListener('click', (e) => {
    console.log("CLICKED YAY");
    if (!buttons.style.display || buttons.style.display == 'none') {
        console.log('this');
        buttons.style.display = 'flex';
        downbtn.style.rotate = '180deg';
        downbtn.style.top = '177px';
    } else {
        buttons.style.display = 'none';
        downbtn.style.rotate = '0deg';
        downbtn.style.top = '180px';
    }
});

var i = 0;

var imageElement = document.getElementById(pictureList[i]);

function changeImage() {
    imageElement.style.opacity = "0%";
    i++;
    if (i === 4) {
        i = 0;
    }
    imageElement = document.getElementById(pictureList[i]);
    
    imageElement.style.opacity = "100%";
}

setInterval(changeImage, 4500);

// while (i != 3) {
//     if (i === 3) {
//         setTimeout(() => {
//             console.log('its working');
//             pictureList[3].style.opacity = '0%';
//             pictureList[0].style.opacity = '100%';
//         }, 1000); 
//     } else {
//         setTimeout(() => {
//             console.log('its working')
//             pictureList[i].style.opacity = '0%';
//             pictureList[i+1].style.opacity = '100%';
//         }, 1000); 
//     }
//     i++;
// }


