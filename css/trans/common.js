var path = window.location.pathname; //http - xxx.html
var page = path.split("/").pop(); //#xxx.html
var cssName = page.split(".")[0]+".css"; 
var url = (""+window.location).split("/"); 
url.pop(); //update Array, but return remove element
var cssAddress = url.join("/")+"/"+cssName //http - xxx.css
var lihkDOM = document.querySelector("link[href=''");
lihkDOM.setAttribute("href", cssAddress);