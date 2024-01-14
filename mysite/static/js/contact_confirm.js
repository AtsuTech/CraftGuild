
// console.log('Hello from your_script.js!');

const contact_form = document.getElementById("contact");
const contact_confirm_page = document.getElementById("contact_confirm_page");

contact_form.onsubmit = function(e){

    //フォーム送信による画面更新を無効
    e.preventDefault();

    //フォームから入力内容取得
    const child_name1 = contact_form.child_name1.value;
    const child_name2 = contact_form.child_name2.value;
    const parent_name1 = contact_form.parent_name1.value;
    const parent_name2 = contact_form.parent_name2.value;
    const email = contact_form.email.value;
    const phone_number = contact_form.phone_number.value;

    // selectオプションのテキストを取得
    const categorySelect = contact_form.contact_category;
    const category = categorySelect.value;
    const category_text = categorySelect.options[categorySelect.selectedIndex].text;

    const comment = contact_form.comment.value;

    contact_form.style.display = "none";
    contact_confirm_page.style.display = "block";
    

    //確認画面に値を渡す
    document.getElementById("confirm_child_name1").textContent = child_name1;
    document.getElementById("child_name1").value = child_name1;

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

    document.getElementById("confirm_contact_category").textContent = category_text;
    document.getElementById("contact_category").value = category;

    document.getElementById("confirm_comment").textContent = comment;
    document.getElementById("comment").value = comment;


}


function back_contact_input(){
    contact_confirm_page.style.display = "none";
    contact_form.style.display = "block";
}