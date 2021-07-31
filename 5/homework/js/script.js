let sign = document.getElementById('sign-up');
let log = document.getElementById('log-in');

sign.onclick = function(){
    this.classList.add('active');
    log.classList.remove('active');
};

log.onclick = function(){
    this.classList.add('active');
    sign.classList.remove('active');
};