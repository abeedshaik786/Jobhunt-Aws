$(document).ready(function (){
    console.log("working document.ready");
$('#company_button').on("click",function(){
    console.log("working function");
    $('#multiCollapseExample2').addClass('d-none');
   })
});
function search_fun(){
  
    $('#dropdown_search').removeClass('d-none');
    $('#binocular').css({'color':'#9e9d24'});
    console.log('working search model');
}
function close_search_modal(){
    $('#binocular').css({'color':'#e6ee9c'});
    $('#dropdown_search').addClass('d-none');
}