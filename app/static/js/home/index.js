function deleteFormSubmit(device_name, form_id) {
    if (confirm(`Vážně chcete smazat zařízení '${device_name}' z databáze? Tuhle akci nelze vrátit.`))
    {
        $(`#${form_id}`).submit();
    }
}