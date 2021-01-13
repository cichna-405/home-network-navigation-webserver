function submitForm(button_id, form_id) {
    if (confirm(`Vážně chcete smazat zařízení ${button_id.split('_')[1]} z databáze? Tuhle akci nelze vrátit.`))
    {
        document.getElementById(form_id).submit();
    }
}