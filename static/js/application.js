$( document ).ready( function(){
  var player;
  buildPopover();
});

function buildPopover(){
    var options = {
    animation:true, 
    placement: 'right', 
    trigger: 'hover', 
    delay: { show: 50, hide: 500 },
    container: '#the-player'
  }
  $('#player-hover').popover(options);
}

function onYouTubePlayerReady(theArray) {
  	player = document.getElementById("the-player");
  	player.addEventListener("onStateChange", "onPlayerStateChange");
    player.playVideo();
}

function playNext(){
  loadingState();
  window.location.href=window.location.href;
}
