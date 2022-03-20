window.addEventListener('DOMContentLoaded', function(){
    var driveRail = document.querySelectorAll('.drive .cont span');
    driveRail.forEach(function(el){
        var num = Number(el.children[0].innerText);
        if(num > 0) el.className = 'positive';
        if(num < 0) el.className = 'negative';
    })
});
