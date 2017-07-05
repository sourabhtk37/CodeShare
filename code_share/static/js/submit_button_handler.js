
// disables the submit button upon document ready
window.onload = function() {

  if (document.getElementById("submit_new")){
    document.getElementById("submit_new").disabled = true;
  }
  
  if (document.getElementById("submit_edit")){
    document.getElementById("submit_edit").disabled = true;
  }

};


/* 
  EventListener on Keyup on the textarea(code_snippet) calls this method.
  Content in the textarea is checked and according to that 
  submit buttons are disabled/enabled.
*/

function control_submit_button(){

  if (document.getElementById("code_snippet").value != ""){

    if (document.getElementById("submit_new")){
      document.getElementById("submit_new").disabled = false;
    }
    if (document.getElementById("submit_edit")){
      document.getElementById("submit_edit").disabled = false;
    }

  }
  
  else {
    
    if (document.getElementById("submit_new")){
      document.getElementById("submit_new").disabled = true;
    }

    if (document.getElementById("submit_edit")){
      document.getElementById("submit_edit").disabled = true;
    }
  }

}