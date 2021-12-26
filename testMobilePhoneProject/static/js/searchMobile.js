const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");
tableOutput.style.display='none';
const mainTable = document.querySelector(".main-table");
const tbodyOutput = document.querySelector(".table-body-output");
const noResults = document.querySelector(".no-results");




searchField.addEventListener('keyup', (e) => {
const searchValue = e.target.value;

if(searchValue.trim().length > 0){
//console.log("searcrValue", searchValue);
tbodyOutput.innerHTML = "";
fetch("/search-mobile", {

body: JSON.stringify({ searchText: searchValue}),
method: "POST",
})
  .then((res) => res.json())
  .then((data) => {
//   console.log("data", data)
   mainTable.style.display='none';
   tableOutput.style.display='block';


   if(data.length===0){

          noResults.style.display='block';
          tableOutput.style.display='none';



   }else{
          noResults.style.display='none';

   data.forEach((item) => {
   tbodyOutput.innerHTML += `
   <tr>
          <td>${item.brand_name}</td>
    <td>${item.model}</td>
    <td>${item.color}</td>
    <td>${item.jan_code}</td>

   </tr> `;
   });


   }



  });


}else{
   mainTable.style.display='block';
      tableOutput.style.display='none';
          noResults.style.display='none';


}
});

