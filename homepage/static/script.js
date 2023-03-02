let slideIndex = 2;
let timeoutId = null;
const slides = document.getElementsByClassName("mySlides");
let dots = document.getElementsByClassName("dot");
for (let i = 0; i < slides.length; i++) {
	slides[i].style.display = "none";
}
slides[0].style.display = "flex";
slides[1].style.display = "flex";
slides[2].style.display = "flex";
showSlides();

function plusSlides() {
	clearTimeout(timeoutId);
	timeoutId = setTimeout(showSlides, 2300);
	showSlides();
}

function minusSlides() {
	slideIndex--;
  if (slideIndex < 2) {
    slideIndex = slides.length - 1;
    for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
    slides[slideIndex - 2].style.display = "flex";
	slides[slideIndex - 1].style.display = "flex";
	slides[slideIndex].style.display = "flex";
  } else {
	slides[slideIndex - 2].style.display = "flex";
	slides[slideIndex + 1].style.display = "none";
  }	
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex-2].className += " active";
  dots[slideIndex-1].className += " active";
  dots[slideIndex].className += " active";
  clearTimeout(timeoutId);
  timeoutId = setTimeout(showSlides, 2300);
}

function currentSlide(n) {
	for (let i = 0; i < slides.length; i++) {
	slides[i].style.display = "none";
}
  slides[n-1].style.display = "flex";
  slides[n].style.display = "flex";
  slides[n+1].style.display = "flex";
  slideIndex=n;
  clearTimeout(timeoutId);
  timeoutId = setTimeout(showSlides, 2300);
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex-1].className += " active";
  dots[slideIndex].className += " active";
  dots[slideIndex+1].className += " active";
}

function showSlides() {
  slideIndex++;
  if (slideIndex >= slides.length) {
    slideIndex = 2;
    for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
    slides[0].style.display = "flex";
	slides[1].style.display = "flex";
	slides[2].style.display = "flex";
  } else {
	slides[slideIndex - 3].style.display = "none";
	slides[slideIndex].style.display = "flex";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex-2].className += " active";
  dots[slideIndex-1].className += " active";
  dots[slideIndex].className += " active";
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
  timeoutId = setTimeout(showSlides, 2300); // Change image every 5 seconds
}

window.addEventListener('scroll', e => {
	document.documentElement.style.setProperty('--scrollTop', `${this.scrollY}px`)
})


const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const num = entry.target.querySelector('#year');
    const num1 = entry.target.querySelector('#workers');
    const num2 = entry.target.querySelector('#pobyta');
    const num3 = entry.target.querySelector('#partner');

    if (entry.isIntersecting) {
      num.classList.add('year');
      num1.classList.add('workers');
      num2.classList.add('pobyta');
      num3.classList.add('partner');
	  return; // if we added the class, exit the function
    }

    num.classList.remove('year');
    num1.classList.remove('workers');
    num2.classList.remove('pobyta');
    num3.classList.remove('partner');
  });
});

observer.observe(document.querySelector('.num-container'));