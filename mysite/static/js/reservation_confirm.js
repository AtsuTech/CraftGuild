const reservation_form = document.getElementById("reservation");
const confirm_reservation = document.getElementById("confirm_reservation");

let validation = new Object();


reservation_form.onsubmit = function(e){

    // if (reservation_form.checkValidity() == false) {
        
    //     alert("全ての項目を入力してください");
    // }

    //フォーム送信による画面更新を無効
    e.preventDefault();

    //フォームから入力内容取得
    //if(reservation_form.child_name1.value) validation['child_name1'] ="お子様の氏名(漢字)は必須です"
    const child_name1 = reservation_form.child_name1.value;

    //if(reservation_form.child_name2.value) validation['child_name2'] ="お子様の氏名(ふりがな)は必須です"
    const child_name2 = reservation_form.child_name2.value;

    const parent_name1 = reservation_form.parent_name1.value;
    const parent_name2 = reservation_form.parent_name2.value;
    const email = reservation_form.email.value;
    const phone_number = reservation_form.phone_number.value;
    const schedule = reservation_form.schedule.value;
    const schedule_text = reservation_form.querySelector('input[name="schedule"]:checked').getAttribute('data-schedule');
    const content = reservation_form.content.value;
    const content_text = reservation_form.querySelector('input[name="content"]:checked').getAttribute('data-content');
    const comment = reservation_form.comment.value;

    reservation_form.style.display = "none";
    confirm_reservation.style.display = "block";
    

    //確認画面に値を渡す
    document.getElementById("confirm_child_name1").textContent = child_name1;
    document.getElementById("child_name1").value = child_name1;
    document.getElementById("validation_child_name1").value = validation['child_name1'];
    

    document.getElementById("confirm_child_name2").textContent = child_name2;
    document.getElementById("child_name2").value = child_name2;

    document.getElementById("confirm_parent_name1").textContent = parent_name1;
    document.getElementById("parent_name1").value = parent_name1;

    document.getElementById("confirm_parent_name2").textContent = parent_name2;
    document.getElementById("parent_name2").value = parent_name2;

    document.getElementById("confirm_email").textContent = email;
    document.getElementById("email").value = email;

    document.getElementById("confirm_phone_number").textContent = phone_number;
    document.getElementById("phone_number").value = phone_number;

    document.getElementById("confirm_schedule").textContent = schedule_text;
    document.getElementById("schedule").value = schedule;

    document.getElementById("confirm_content").textContent = content_text;
    document.getElementById("content").value = content;

    document.getElementById("confirm_comment").textContent = comment;
    document.getElementById("comment").value = comment;


}