// Activate Lucide icons
lucide.createIcons();

/* ======================
   TYPEWRITER EFFECT
====================== */

const text =
"I work at the intersection of AI systems and distributed engineering";

let index = 0;
const speed = 50;

function typeEffect() {
  if (index < text.length) {
    document.getElementById("typing").innerHTML += text.charAt(index);
    index++;
    setTimeout(typeEffect, speed);
  }
}

typeEffect();


/* ======================
   THEME SYSTEM
====================== */

const toggleBtn = document.getElementById("themeToggle");

function setTheme(theme) {

  if(theme === "light"){
    document.body.classList.add("light-mode");
    toggleBtn.innerHTML = '<i data-lucide="sun"></i>';
  }
  else{
    document.body.classList.remove("light-mode");
    toggleBtn.innerHTML = '<i data-lucide="moon"></i>';
  }

  lucide.createIcons();

}


/* Load saved theme */

const savedTheme = localStorage.getItem("theme");

if(savedTheme){
  setTheme(savedTheme);
}else{
  setTheme("dark");
}


/* Toggle button */

toggleBtn.addEventListener("click",()=>{

  const newTheme = document.body.classList.contains("light-mode")
  ? "dark"
  : "light";

  localStorage.setItem("theme",newTheme);

  setTheme(newTheme);

});