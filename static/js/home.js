// Image zooming model

// var modal = document.getElementsByClassName("modal");

// for (var i = 0; i < modal.length; i++) {

//     var lmodal = modal[i]
// }

// var modalImg = document.getElementsByClassName("img01");

// for (var i = 0; i < modalImg.length; i++) {

//     var lmoalImg = modalImg[i]
// }

// var img = document.getElementsByClassName("geeks");


// for (i = 0; i < img.length; i++) {
//     img[i].onclick = function () {
//         lmodal.style.display = "block";
//         lmoalImg.src = this.src;
//     }
// }

// var span = document.getElementsByClassName("close");

// for (i = 0; i < span.length; i++) {
//     span[i].onclick = function () {
//         lmodal.style.display = "none";
//     }
// }


// Image slider JS


// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("geeks");
var modalImg = document.getElementById("img01");
img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}




