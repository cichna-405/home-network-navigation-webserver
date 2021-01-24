const deleteUrl = (url_id, device_id) => {
    let deleteForm = document.getElementById('url_delete_form');
    deleteForm.setAttribute('action', `/device/${device_id}/urls/${url_id}/delete`);
    deleteForm.submit();
}