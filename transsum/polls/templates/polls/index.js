var btn1 = document.getElementById('sum-btn');
var div1 = document.getElementById('content');

btn1.addEventListener("click",function(){
    btn1.setAttribute("style","visibility:hidden");
    showSummary();
});

function showSummary(){

    var p = document.createElement('label');
    // p.innerText = 'Summary....';
    p.innerText = 'The summarizer is a Chrome extension that works with YouTube to extract the key points of a video and make them accessible to the user.There are large number of videos on youtube for every particular topic. It is not neccessary that each video will contain the information that you needed. So in order to save time firstly we can read the summary of video using this chrome extension and then we can decide whether to watch it or not, in order to save time.';
    // div1.appendChild(document.createElement('center'));
    div1.appendChild(p);
    
}
