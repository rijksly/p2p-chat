async function send(){
  var response = await fetch('/send', {
    method: 'POST',
    body: JSON.stringify({
      message: document.getElementsByTagName('input')[0].value
    }),
    headers: new Headers()
  });
  document.getElementsByTagName('input')[0].value = '';
};

async function json(){
  var response = await fetch('/json');
  var data = await response.json();
  document.getElementsByTagName('p')[0].innerHTML = data.join('<br>');
};

function sleep(ms){
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function receive(){
  var response = await fetch('/receive');
  await sleep(3000);
  receive();
};

receive();

try{
  var timerId = setInterval(json, 5000);
} catch (error){
  clearTimeout(timerId);
  alert(error.name);
};
