window.onload = function(){
  document.onload = function(){
    getButtons();
  }
}



function getButtons(){
  profiles = document.getElementsByClassName('profile-template');
  buttons = []
  for (profile in profiles) {
    profile.style.backgroundColor = "yellow";
    /*buttons.push(profile.getElementsByTagName('input'))*/
  };


  for (button in buttons) {
    button.addEventListener("click",function(){
      window.location.href = '/profiles/button.name';
    });
  };


}

getButtons();
