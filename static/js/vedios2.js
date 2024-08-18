
    // Load the YouTube Player API asynchronously
    function loadYouTubePlayerAPI() {
      const tag = document.createElement('script');
      tag.src = 'https://www.youtube.com/iframe_api';
      const firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    }

    // Callback function called when the YouTube Player API is ready
    let player;
    function onYouTubeIframeAPIReady() {
      player = new YT.Player('player', {
        height: '315',
        width: '100%',
        videoId: 'krfDL0NVNd8',
        events: {
          'onReady': onPlayerReady,
          'onStateChange': onPlayerStateChange
        }
      });
    }

    // Callback function called when the player is ready
    function onPlayerReady(event) {
      // You can do something here if needed
    }

    // Callback function called when the player's state changes
    function onPlayerStateChange(event) {
      if (event.data == YT.PlayerState.ENDED) {
        // Video has ended, enable the button
        const button = document.getElementById('next1');
        button.removeAttribute('disabled');
        console.log('The first YouTube video has ended.');
      }
    }

    // Load the YouTube Player API when the DOM content is loaded
    document.addEventListener('DOMContentLoaded', function() {
      loadYouTubePlayerAPI();
    });

    // Add event listener to the "Next" button for the first video
    const nextButton1 = document.getElementById('next1');
    nextButton1.addEventListener('click', function() {
      // Hide the first video and the button
      const videoContainer = document.getElementById('player');
      const button = document.getElementById('next1');
      videoContainer.style.display = 'none';
      document.getElementById("fristVideoContainer").style.display = 'none';
      button.style.display = 'none';
      document.getElementById("ts3limatVedio1").classList.add("d-none")
      // Show the second video and the second button
      const secondVideoContainer = document.getElementById('secondVideoContainer');
      const secondPlayer = new YT.Player('secondPlayer', {
        height: '315',
        width: '100%',
        videoId: 'SQmeKkpPij8',
        events: {
          'onReady': onSecondPlayerReady,
          'onStateChange': onSecondPlayerStateChange
        }
      });
      secondVideoContainer.style.display = 'block';
    });

    // Callback function called when the second player is ready
    function onSecondPlayerReady(event) {
      // You can do something here if needed
    }

    // Callback function called when the second player's state changes
    function onSecondPlayerStateChange(event) {
      if (event.data == YT.PlayerState.ENDED) {
        // Video has ended, enable the second button
        const button = document.getElementById('next2');
        button.removeAttribute('disabled');
       
        console.log('The second YouTube video has ended.');
      }
    };
// =============================vedio4==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton2 = document.getElementById('next2');
nextButton2.addEventListener('click', function() {
  // Hide the second video and the button
  const secondVideoContainer = document.getElementById('secondVideoContainer');
  const button = document.getElementById('next2');
  secondVideoContainer.style.display = 'none';
  button.style.display = 'none';

// Show the third video and the 4 button
const v4VideoContainer = document.getElementById('v4VideoContainer');
const v4Player = new YT.Player('v4Player', {
  height: '315',
  width: '100%',
  videoId: 'qPyG_l3Wf7o', // Update this with the ID of your third video
  events: {
    'onReady': onv4PlayerReady,
    'onStateChange': onv4PlayerStateChange
  }
});
v4VideoContainer.style.display = 'block';
});

// Callback function called when the third player is ready
function onv4PlayerReady(event) {
  // You can do something here if needed
}

// Callback function called when the third player's state changes
function onv4PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {
      // Video has ended, enable the third button
      const button = document.getElementById('next4');
      button.removeAttribute('disabled');
      // button.classList.add("d-none");


  }
}

// =============================vedio5==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton4 = document.getElementById('next4');
nextButton4.addEventListener('click', function() {
  // Hide the second video and the button
  const v4VideoContainer = document.getElementById('v4VideoContainer');
  const button = document.getElementById('next4');
  v4VideoContainer.style.display = 'none';
  button.style.display = 'none';

// Show the third video and the 4 button
const v5VideoContainer = document.getElementById('v5VideoContainer');
const v5Player = new YT.Player('v5Player', {
  height: '315',
  width: '100%',
  videoId: '-S1BDuPgDzM', // Update this with the ID of your third video
  events: {
    'onReady': onv5PlayerReady,
    'onStateChange': onv5PlayerStateChange
  }
});
v5VideoContainer.style.display = 'block';
});


function onv5PlayerReady(event) {

}

function onv5PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next5');
      button.removeAttribute('disabled');

  }
}
 
// =============================vedio6==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton5 = document.getElementById('next5');
nextButton5.addEventListener('click', function() {
  // Hide the second video and the button
  const v5VideoContainer = document.getElementById('v5VideoContainer');
  const button = document.getElementById('next5');
  v5VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v6VideoContainer = document.getElementById('v6VideoContainer');
const v6Player = new YT.Player('v6Player', {
  height: '315',
  width: '100%',
  videoId: 'ojC0VthnX1k', // Update this with the ID of your third video
  events: {
    'onReady': onv6PlayerReady,
    'onStateChange': onv6PlayerStateChange
  }
});
v6VideoContainer.style.display = 'block';
});

function onv6PlayerReady(event) {
}

function onv6PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next6');
      button.removeAttribute('disabled');

  }
}

// =============================vedio7==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton6 = document.getElementById('next6');
nextButton6.addEventListener('click', function() {
  // Hide the second video and the button
  const v6VideoContainer = document.getElementById('v6VideoContainer');
  const button = document.getElementById('next6');
  v6VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v7VideoContainer = document.getElementById('v7VideoContainer');
const v7Player = new YT.Player('v7Player', {
  height: '315',
  width: '100%',
  videoId: 'Q8t6encPoX4', // Update this with the ID of your third video
  events: {
    'onReady': onv7PlayerReady,
    'onStateChange': onv7PlayerStateChange
  }
});
v7VideoContainer.style.display = 'block';
});

function onv7PlayerReady(event) {
}

function onv7PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next7');
      button.removeAttribute('disabled');

  }
}

// =============================vedio8==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton7 = document.getElementById('next7');
nextButton7.addEventListener('click', function() {
  // Hide the second video and the button
  const v7VideoContainer = document.getElementById('v7VideoContainer');
  const button = document.getElementById('next7');
  v7VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v8VideoContainer = document.getElementById('v8VideoContainer');
const v8Player = new YT.Player('v8Player', {
  height: '315',
  width: '100%',
  videoId: 'ERpsKnsjRLs', // Update this with the ID of your third video
  events: {
    'onReady': onv8PlayerReady,
    'onStateChange': onv8PlayerStateChange
  }
});
v8VideoContainer.style.display = 'block';
});

function onv8PlayerReady(event) {
}

function onv8PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next8');
      button.removeAttribute('disabled');

  }
}

// =============================vedio9==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton8 = document.getElementById('next8');
nextButton8.addEventListener('click', function() {
  // Hide the second video and the button
  const v8VideoContainer = document.getElementById('v8VideoContainer');
  const button = document.getElementById('next8');
  v8VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v9VideoContainer = document.getElementById('v9VideoContainer');
const v9Player = new YT.Player('v9Player', {
  height: '315',
  width: '100%',
  videoId: 'NMcVih2euQM', // Update this with the ID of your third video
  events: {
    'onReady': onv9PlayerReady,
    'onStateChange': onv9PlayerStateChange
  }
});
v9VideoContainer.style.display = 'block';
});

function onv9PlayerReady(event) {
}

function onv9PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next9');
      button.removeAttribute('disabled');

  }
}

// =============================vedio10==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton9 = document.getElementById('next9');
nextButton9.addEventListener('click', function() {
  // Hide the second video and the button
  const v9VideoContainer = document.getElementById('v9VideoContainer');
  const button = document.getElementById('next9');
  v9VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v10VideoContainer = document.getElementById('v10VideoContainer');
const v10Player = new YT.Player('v10Player', {
  height: '315',
  width: '100%',
  videoId: 'J_tEHh_jXTI', // Update this with the ID of your third video
  events: {
    'onReady': onv10PlayerReady,
    'onStateChange': onv10PlayerStateChange
  }
});
v10VideoContainer.style.display = 'block';
});

function onv10PlayerReady(event) {
}

function onv10PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next10');
      button.removeAttribute('disabled');

  }
}

// =============================vedio11==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton10 = document.getElementById('next10');
nextButton10.addEventListener('click', function() {
  // Hide the second video and the button
  const v10VideoContainer = document.getElementById('v10VideoContainer');
  const button = document.getElementById('next10');
  v10VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v11VideoContainer = document.getElementById('v11VideoContainer');
const v11Player = new YT.Player('v11Player', {
  height: '315',
  width: '100%',
  videoId: 'wtlw8ceneJU', // Update this with the ID of your third video
  events: {
    'onReady': onv11PlayerReady,
    'onStateChange': onv11PlayerStateChange
  }
});
v11VideoContainer.style.display = 'block';
});

function onv11PlayerReady(event) {
}

function onv11PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next11');
      button.removeAttribute('disabled');

  }
}

// =============================vedio12==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton11 = document.getElementById('next11');
nextButton11.addEventListener('click', function() {
  // Hide the second video and the button
  const v11VideoContainer = document.getElementById('v11VideoContainer');
  const button = document.getElementById('next11');
  v11VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v12VideoContainer = document.getElementById('v12VideoContainer');
const v12Player = new YT.Player('v12Player', {
  height: '315',
  width: '100%',
  videoId: '8_DBIodrhJY', // Update this with the ID of your third video
  events: {
    'onReady': onv12PlayerReady,
    'onStateChange': onv12PlayerStateChange
  }
});
v12VideoContainer.style.display = 'block';
});

function onv12PlayerReady(event) {
}

function onv12PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next12');
      button.removeAttribute('disabled');

  }
}

// =============================vedio13==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton12 = document.getElementById('next12');
nextButton12.addEventListener('click', function() {
  // Hide the second video and the button
  const v12VideoContainer = document.getElementById('v12VideoContainer');
  const button = document.getElementById('next12');
  v12VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v13VideoContainer = document.getElementById('v13VideoContainer');
const v13Player = new YT.Player('v13Player', {
  height: '315',
  width: '100%',
  videoId: '2n3bKF8xNjY', // Update this with the ID of your third video
  events: {
    'onReady': onv13PlayerReady,
    'onStateChange': onv13PlayerStateChange
  }
});
v13VideoContainer.style.display = 'block';
});

function onv13PlayerReady(event) {
}

function onv13PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next13');
      button.removeAttribute('disabled');

  }
}

// =============================vedio14==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton13 = document.getElementById('next13');
nextButton13.addEventListener('click', function() {
  // Hide the second video and the button
  const v13VideoContainer = document.getElementById('v13VideoContainer');
  const button = document.getElementById('next13');
  v13VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v14VideoContainer = document.getElementById('v14VideoContainer');
const v14Player = new YT.Player('v14Player', {
  height: '315',
  width: '100%',
  videoId: 'qporeqIhNTQ', // Update this with the ID of your third video
  events: {
    'onReady': onv14PlayerReady,
    'onStateChange': onv14PlayerStateChange
  }
});
v14VideoContainer.style.display = 'block';
});

function onv14PlayerReady(event) {
}

function onv14PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next14');
      button.removeAttribute('disabled');

  }
}


// =============================vedio15==============================
// Add event listener to the "Next" button for the vedio4 video
const nextButton14 = document.getElementById('next14');
nextButton14.addEventListener('click', function() {
  // Hide the second video and the button
  const v14VideoContainer = document.getElementById('v14VideoContainer');
  const button = document.getElementById('next14');
  v14VideoContainer.style.display = 'none';
  button.style.display = 'none';


const v15VideoContainer = document.getElementById('v15VideoContainer');
const v15Player = new YT.Player('v15Player', {
  height: '315',
  width: '100%',
  videoId: '5TPpAabMmhs', // Update this with the ID of your third video
  events: {
    'onReady': onv15PlayerReady,
    'onStateChange': onv15PlayerStateChange
  }
});
v15VideoContainer.style.display = 'block';
});

function onv15PlayerReady(event) {
}

function onv15PlayerStateChange(event) {
  if (event.data == YT.PlayerState.ENDED) {

      const button = document.getElementById('next15');
      button.removeAttribute('disabled');

  }
}


// =============================vedio16==============================
document.getElementById("next15").addEventListener("click" , function () {
  document.getElementById("activity").style.display = 'block'  
  document.getElementById("v15VideoContainer").style.display = 'none'         
})

// =============================vedio17==============================
document.getElementById("finish").addEventListener("click" , function () {
  document.getElementById("test").style.display = 'block'  
  document.getElementById("activity").style.display = 'none'         
})