// Create js document
function getXhr(){
    if (window.XMLHttpRequest){
        // alert('该浏览器支持xhr')
        // var xhr = new XMLHttpRequest()
        return  new XMLHttpRequest()
    }else{
        alert('该浏览器不支持xhr')
        return  new ActiveXObject('Microsoft.XMLHTTP') 
    }    
}
