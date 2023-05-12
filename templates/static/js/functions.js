function analyzeData(){
    let input = document.getElementById("sequenceInpt").value
    if(checkInput(input)){
      $.ajax({
        type: "POST",
        url: "/analyze",
        dataType:'Json',
        data: JSON.stringify(
            {"dna_sequence":input}),
        success: function(data){
            window.location = "/analyze"

        }

    })
  }
  else{
    // if (document.getElementsByClassName("invalid-feedback").length == 0){
    //   console.log("did it do it?")
    //   let input = document.getElementById("input-group")
    //   let invalid = document.createElement("div")
    //   invalid.classList.add("invalid-feedback")
    //   invalid.innerHTML = "Invalid DNA Sequence! Please Try Again"
    //   input.appendChild(invalid)
    alert("Invalid sequence. Please try again!")
    
  }
  }
  

function checkInput(input_string){
    if(/[-{1}[G|U|A|T][d|r|m][o|s]*]*/.test(input_string)){
      // let input = document.getElementById("input-group")
      // input.removeChild(document.getElementsByClassName("invalid-feedback"))
      return true
    }
    else{
      return false
    }

}