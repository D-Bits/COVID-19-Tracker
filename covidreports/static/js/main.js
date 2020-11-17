/*
* Custom client-side JavaScript functions
*/ 


// Function for search box(es)
/* Param "tableId": the HTML ID of the table
* Param "inputId": the HTML ID of the input element
* Param "index": The column to be searched (0 for the left-most column)
*/
function findData(tableId, inputId, index) {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById(inputId);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableId);
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[index];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}


// Function for sorting column values
// NOT YET WORKING
// Basic example
var asc = 0;
function sort_table(table, col) {
  $('.sortorder').remove();
  if (asc == 2) { asc = -1; } else { asc = 2; }
  var rows = table.tBodies[0].rows;
  var rlen = rows.length - 1;
  var arr = new Array();
  var i, j, cells, clen;
  // fill the array with values from the table
  for (i = 0; i < rlen; i++) {
    cells = rows[i].cells;
    clen = cells.length;
    arr[i] = new Array();
    for (j = 0; j < clen; j++) { arr[i][j] = cells[j].innerHTML; }
  }
  // sort the array by the specified column number (col) and order (asc)
  arr.sort(function (a, b) {
    var retval = 0;
    var col1 = a[col].toLowerCase().replace(',', '').replace('$', '').replace(' usd', '')
    var col2 = b[col].toLowerCase().replace(',', '').replace('$', '').replace(' usd', '')
    var fA = parseFloat(col1);
    var fB = parseFloat(col2);
    if (col1 != col2) {
      if ((fA == col1) && (fB == col2)) { retval = (fA > fB) ? asc : -1 * asc; } //numerical
      else { retval = (col1 > col2) ? asc : -1 * asc; }
    }
    return retval;
  });
  for (var rowidx = 0; rowidx < rlen; rowidx++) {
    for (var colidx = 0; colidx < arr[rowidx].length; colidx++) { table.tBodies[0].rows[rowidx].cells[colidx].innerHTML = arr[rowidx][colidx]; }
  }

  hdr = table.rows[0].cells[col];
  if (asc == -1) {
    $(hdr).html($(hdr).html() + '<span class="sortorder">▲</span>');
  } else {
    $(hdr).html($(hdr).html() + '<span class="sortorder">▼</span>');
  }
}
