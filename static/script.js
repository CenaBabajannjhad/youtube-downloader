const form = document.querySelector("#ytdl-form");
const formInput = document.querySelector("#form-input");



// convert url to base64
const convertUrlToBase64 = url => {// Replace `+` with `-`  ||    // Replace `/` with `_`  ||  // Remove any `=` padding characters
    return btoa(url).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');  
}
// make full url
const makeUrl = url => { 
    let base64 = convertUrlToBase64(url);
    let URL = `http://127.0.0.1:5000/api/${base64}`
    return URL;
}
// fetch data
const formHandler = e => {
    e.preventDefault();
    // get input value
    let inputValue = formInput.value.trim(); 
    // send input vlaue for makeUrl function
    let URL = makeUrl(inputValue);
    // send url for fetching data
    fetchData(URL);
}
// event when form submited , call formHandler function
form.addEventListener('submit' , formHandler);

// fetch data , now just send a request
const fetchData = async (url) => {
    try{
        let res = await fetch(url , {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({link : url})
        })
        console.log(res);

    }catch(e){
        console.error('error is : ' , e);
    }
}



