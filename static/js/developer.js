function copyAPI(){

    const key =
        document.getElementById("apikey").innerText.trim();

    navigator.clipboard.writeText(key);

    alert("API Key Copied 🚀");

}

function copyEndpoint(){

    navigator.clipboard.writeText(
        "/api/v1/ingest"
    );

    alert("Endpoint Copied 🚀");

}
function copyEmbedCode(){

    const code =
        document
        .getElementById("embedCode")
        .innerText;

    navigator.clipboard
        .writeText(code);

    alert("Embed Code Copied 🚀");

}
async function sendTestData(){

    const apiKey =
        document.getElementById("apikey").innerText.trim();

    try{

        const response = await fetch("/api/v1/ingest",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                api_key:apiKey,

                revenue:Math.floor(Math.random()*10000)+1000,

                visitors:Math.floor(Math.random()*500)+100,

                orders:Math.floor(Math.random()*50)+5,

                profit:Math.floor(Math.random()*5000)+500

            })

        });

        const data = await response.json();

        alert(data.message);

    }

    catch(err){

        console.error(err);

        alert("Something went wrong.");

    }

}