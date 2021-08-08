async function send(){
  var response = await fetch('/send', {
    method: 'POST',
    body: JSON.stringify({
      message: document.getElementsByTagName('input')[0].value
    }),
    headers: new Headers()
  });
  var data = await response.text();
  //if (data != 'ok'){
  //  alert("The message wasn't delivered")
  //};
};

async function request(){
  var response = await fetch('/json');
  var data = await response.json();
  document.getElementsByTagName('p')[0].innerHTML = data.join('<br>');
};

try{
  var timerId = setInterval(request, 5000);
} catch (error){
  clearTimeout(timerId);
  alert(error.name);
};
