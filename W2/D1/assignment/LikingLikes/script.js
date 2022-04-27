var likes = 0;
var likesElement = document.querySelector("#likes");
console.log(likesElement);
function add1() {
      likes++;
      likesElement.innerText = "" + likes;
      console.log(likes);
      
}