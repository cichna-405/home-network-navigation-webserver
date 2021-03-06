function addUrl() {
    let urlTable = document.getElementById('url_table');
    let urlTableRows = urlTable.rows;
    let newIndex = 1 + Number(urlTableRows[urlTableRows.length - 1].id.substr(4, Infinity));

    if(urlTableRows.length >= 2) urlTableRows[urlTableRows.length - 1].getElementsByClassName('btn-outline-secondary')[0].classList.add('disabled');

    let newRow = urlTable.insertRow(-1);
    let id_cell = newRow.insertCell(0);
    let name_cell = newRow.insertCell(1);
    let url_cell = newRow.insertCell(2);
    let remove_cell = newRow.insertCell(3);

    newRow.id = `url_${newIndex}`;
    newRow.classList.add('text-center');

    id_cell.id = `url_${newIndex}_id`;
    id_cell.classList.add('align-middle');
    id_cell.innerHTML = newIndex.toString();

    let nameInput = document.createElement('input')
    nameInput.setAttribute('name', `url_${newIndex}_name`);
    nameInput.setAttribute('type', 'text');
    nameInput.setAttribute('placeholder', 'popis URL');
    nameInput.classList.add('form-control');
    name_cell.appendChild(nameInput);

    let urlInput = document.createElement('input')
    urlInput.setAttribute('name', `url_${newIndex}_url`);
    urlInput.setAttribute('type', 'text');
    urlInput.setAttribute('placeholder', 'URL adresa');
    urlInput.classList.add('form-control');
    url_cell.appendChild(urlInput);

    let removeButton = document.createElement('button');
    removeButton.setAttribute('type', 'button');
    removeButton.setAttribute('class', 'btn btn-outline-secondary');
    removeButton.setAttribute('onclick', `removeTableRow(this.parentElement.parentElement);`);
    removeButton.innerHTML = `<i class="bi bi-trash"></i>`;
    remove_cell.appendChild(removeButton);
}

function removeTableRow(row) {
    row.remove();
    let tableRows = document.getElementById('url_table').rows;
    if (tableRows.length > 2)
        tableRows[tableRows.length - 1].getElementsByClassName('btn-outline-secondary')[0].classList.remove('disabled');
}