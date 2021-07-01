var i = 0;
var missiontitle = 'OUR MISSION';
var missiontxt = 'Growing Entertainment market across the world through the production, promotion and recording of high quaility entertainment';
var speed = 50;

function displayText() {
    if ( i < missiontitle.length){
        document.getElementById("mssnttl").innerHTML += missiontitle.charAt(i);
        i++;
        setTimeout(displayText , speed);
    }

    if ( i < missiontxt.length){
        document.getElementById("mssntxt").innerHTML += missiontxt.charAt(i);
        i++;
        setTimeout(displayText , speed);
    }
}
