function clicked()
{
      console.log('was clicked')
      var h1 = document.querySelector('h1')
      h1.style.backgroundColor = 'firebrick'

      h1.style.onmouseover=function () {
            h1.style.backgroundColor= 'green'

      }
}

function addclass(){
      var h1 = querySelector('h1')
      console.log(h1.classlist.contains)

}

// ON change event


function showname(input){
      console.log(input.value)

}






////////////////////////////////////////


