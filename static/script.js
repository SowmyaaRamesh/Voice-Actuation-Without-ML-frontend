const playAudio = () => {
  let audioFile = document.getElementById("audioFile").value;

  let audioSrc = audioFile.substr(12);
  let AudioController = document.getElementById("audioSource");
  AudioController.setAttribute("src", audioSrc);
  var audio = document.getElementById("audio");
  audio.load();
  //   audio.play();
};

const submitData = () => {
  document.getElementById("form").submit();
};
