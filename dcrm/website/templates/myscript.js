function myFunction() {
    var x = document.getElementById("mySelect").value;
    
}

window.onload = function() {
    var select = document.getElementById('mySelect');
    
    select.addEventListener('change', function() {
        var x = this.value;
        if (x === "option1") {
            changecolor('blue')
          }
          if (x === "option2") {
            changecolor('red')
          } 
          if (x === "option3") {
              changecolor('green')
          }
    });
    
    document.querySelector('button').addEventListener('click', changeColor);
};

function changecolor(col){
    document.getElementById("mydiv").style.backgroundColor = col;
}
