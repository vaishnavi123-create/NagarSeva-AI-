// NagarSeva AI

console.log("NagarSeva AI Loaded Successfully");

function showInfo(type){

    if(type=="upload"){
        Swal.fire({
            title:"📷 Upload Image",
            text:"Upload complaint photos as proof for faster verification.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

    else if(type=="location"){
        Swal.fire({
            title:"📍 Live Location",
            text:"Provide the exact issue location for quick government response.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

    else if(type=="ai"){
        Swal.fire({
            title:"🤖 AI Detection",
            text:"AI helps identify complaint categories automatically.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

    else if(type=="department"){
        Swal.fire({
            title:"🏢 Department Assignment",
            text:"The complaint is forwarded to the correct government department.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

    else if(type=="tracking"){
        Swal.fire({
            title:"📊 Complaint Tracking",
            text:"Track your complaint status in real time using the Complaint ID.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

    else if(type=="safety"){
        Swal.fire({
            title:"🛡️ Community Safety",
            text:"Help build a safer community by reporting civic issues quickly.",
            icon:"info",
            confirmButtonColor:"#2563eb"
        });
    }

}