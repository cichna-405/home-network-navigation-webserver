function deleteFormSubmit(device_name, form_id) {
    if (confirm(`Vážně chcete smazat zařízení '${device_name}' z databáze? Tuhle akci nelze vrátit.`))
    {
        $(`#${form_id}`).submit();
    }
}


/* DELETE / EDIT / GOTOURL buttons in the table */
$('.prevent_redirect').click(caller => {
    if(caller.id === 'delete')
    {

    }
    else if (caller.id.startsWith('edit_')) {

    }
    else return false
})