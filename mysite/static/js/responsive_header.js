
responsive_menu = document.getElementById('responsive_menu');


window.onload = function(){

    // ヘッダー：ハンバーガーメニュー開閉
    document.getElementById('OpenBtn').onclick = function(){
        responsive_menu.style.display = 'block';
        // document.getElementById('sp_ul').classList.toggle('disp');
        // document.getElementById('bar1').classList.toggle('bar1_act');
        // document.getElementById('bar2').classList.toggle('bar2_act');
        // document.getElementById('bar3').classList.toggle('bar3_act');
    }

    document.getElementById('CloseBtn').onclick = function(){
        responsive_menu.style.display = 'none';
        // document.getElementById('sp_ul').classList.toggle('disp');
        // document.getElementById('bar1').classList.toggle('bar1_act');
        // document.getElementById('bar2').classList.toggle('bar2_act');
        // document.getElementById('bar3').classList.toggle('bar3_act');
    }
    
}