//This function for AJAX POST request to load the model with respective the brand choosen.
function m_load() {
   var a = document.getElementById('b_name').value;
   jQuery.ajax({
   url: "/get_model",
   data: "brand="+a,
   type: "POST",
   success:function(b_model){
      console.log(b_model)
      
      document.getElementById('model').innerHTML = '';
      for(let i=0;i<b_model.length;i++){
         document.getElementById('model').innerHTML += "<option>"+b_model[i]+"</option>";
       }
      
   },
   error:function (){}
   });
}
//This function for AJAX POST request to load the processors with respective the processor brand choosen.
function p_load() {
         
   var p = document.getElementById('processor_brand').value;
   console.log(p)
   jQuery.ajax({
   url: "/get_processor",
   data: "p_brand="+p,
   type: "POST",
   success:function(p_model){
      console.log(p_model)
      
      document.getElementById('p_model').innerHTML = '';
      for(let i=0;i<p_model.length;i++){
         document.getElementById('p_model').innerHTML += "<option>"+p_model[i]+"</option>";
       }
      // $("#model").html(b_model);
      
   },
   error:function (){}
   });
}