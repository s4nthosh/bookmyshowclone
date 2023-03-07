const container = document.querySelector('.seats');
const seats = document.querySelectorAll('.SeatRow1 .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');
const number = document.getElementById('number');
const movieselect = document.getElementById('price');

populateUI();

// Save selected movie index and price
function setMovieData(movieIndex, moviePrice) {
    localStorage.setItem('selectedMovieIndex', movieIndex);
    localStorage.setItem('selectedMoviePrice', moviePrice);
  }


  // get data from localstorage and populate ui
function populateUI() {
    const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
    if (selectedSeats !== null && selectedSeats.length > 0) {
      seats.forEach((seat, index) => {
        if (selectedSeats.indexOf(index) > -1) {
          seat.classList.add('selected');
        }
      });
    }
  
    const selectedMovieIndex = localStorage.getItem('selectedMovieIndex');
  
    if (selectedMovieIndex !== null) {
      movieSelect.selectedIndex = selectedMovieIndex;
    }
  }

function updateselectedcount() {
    const selectedseats = document.querySelectorAll('.SeatRow1 .seat.selected')
    const seatsIndex = [...selectedseats].map((seat) => [...seats].indexOf(seat));

    
    
    const selectedseatscount = selectedseats.length;

    count.innerText = selectedseatscount;  
    
    };
    
seats.forEach(price => {
   price.addEventListener('click',() =>{
        const movp = price.getAttribute('data-value'); 
        const selectedsa =  document.querySelectorAll('.SeatRow1 .seat.selected')
        const sc = selectedsa.length+1; 
        if (movp ==='0'){
            price.dataset.value = price.dataset.originalvalue;
        } else{
            price.dataset.originalvalue = movp;
            price.dataset.value = '0';
        }
        total.innerText =  movp * sc ;
        
    });
    
});

seats.forEach(price => {
    price.addEventListener('click',() =>{
         const seat_ty=price.getAttribute('data-set');  
         if (seat_ty ==='0'){
             price.dataset.value = price.dataset.originalvalue;
         } else{
             price.dataset.originalvalue = seat_ty;
             price.dataset.value = '0';
         }
         values.push(seat_ty);
         number.innerText=values.join(',');
         
     });
     
 });
 const values = [];

    
    




container.addEventListener('click',(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');
    



    
    updateselectedcount();
}

    
});

updateselectedcount();



