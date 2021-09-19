var bg = document.querySelector(".bg");
var formBox = document.querySelector(".form_cont")
var btn = document.querySelectorAll(".authCard .btnBox button");
var Card = document.querySelector(".authCard");

function tog(op){
    if(op == "logup"){
        console.log("logup")
        btn[1].style.color = "white";
        btn[0].style.color = "black";
        formBox.style.margin = "0 -333px 0";
        bg.style.left="50%";
        Card.style.height = "470px";
    }else{
        btn[1].style.color = "black";
        btn[0].style.color = "white";
        bg.style.left= 0;
        formBox.style.margin = "0 0 0 0 ";
        Card.style.height="320px"
    }
}