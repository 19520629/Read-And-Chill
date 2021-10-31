const musicContainer = document.querySelector('.music-player')
const playBtn = document.querySelector('#play')
const prevBtn = document.querySelector('#prev')
const nextBtn = document.querySelector('#next')
const audio = document.querySelector('#audio')
const progress = document.querySelector('.progress')
const progressContainer = document.querySelector('.progress-container')
const titleSong = document.querySelector('#title-song')
const cover = document.querySelector('#cover')


// Song title
const songs = ['Nhạc đàn piano thư giãn', 'Xích linh', 'Tỳ bà hành', 'Nhạc đàn tranh thư giãn', 'Game Hoa OST']

// 
let songIndex = 0

loadSong(songs[songIndex])


function loadSong(song) {
    var a = songIndex
    if(a == 0) {
        titleSong.innerHTML = song
        audio.src = `./asset/music/hoa-ost-full-soundtrack.mp3`
        cover.src = `./asset/img/music/nhac-piano.png`
    }
    else if(a == 1) {
        titleSong.innerHTML = song
        audio.src = `./asset/music/XichLinh.mp3`
        cover.src = `./asset/img/music/nhac-xich-linh.jpg`
       
    }
    else if(a == 2) {
        titleSong.innerHTML = song
        audio.src = `./asset/music/TyBaHanh.mp3`
        cover.src = `./asset/img/music/nhac-dan-ty-ba.jpg`
    }
    else if(a == 3) {
        titleSong.innerHTML = song
        audio.src = `./asset/music/KiepSauNguyenLamMotDoaSenDanTranhCover-DanTranh-5975590.mp3`
        cover.src = `./asset/img/music/nhac-dan-tranh.png`
    }
    else if(a == 4) {
        titleSong.innerHTML = song
        audio.src = `./asset/music/hoa-ost-full-soundtrack.mp3`
        cover.src = `./asset/img/music/nhac-game-hoa.jpg`
    }

}

function playSong() {
    musicContainer.classList.add('play')
    playBtn.querySelector('i.fas').classList.remove('fa-play')
    playBtn.querySelector('i.fas').classList.add('fa-pause')


    audio.play()
}

function pauseSong() {
    musicContainer.classList.remove('play')
    playBtn.querySelector('i.fas').classList.add('fa-play')
    playBtn.querySelector('i.fas').classList.remove('fa-pause')

    audio.pause()
}

function prevSong() {
    songIndex--

    if(songIndex < 0) {
        songIndex = songs.length - 1
    }

    loadSong(songs[songIndex])

    playSong()
}

function nextSong() {
    songIndex++

    if(songIndex > songs.length - 1) {
        songIndex = 0
    }

    loadSong(songs[songIndex])

    playSong()
}

function updateProgress(e) {
    const { duration, currentTime } = e.srcElement
    const progressPercent = (currentTime / duration) * 100
    progress.style.width = `${progressPercent}%`
}

function setProgress(e) {
    const width = this.clientWidth
    const clickX = e.offsetX
    const duration = audio.duration

    audio.currentTime = (clickX / width) * duration
}






playBtn.addEventListener('click', () => {
    const isPlaying = musicContainer.classList.contains('play');

    if(isPlaying) {
        pauseSong();
    } else {
        playSong();
    }
})


prevBtn.addEventListener('click', prevSong)
nextBtn.addEventListener('click', nextSong)

audio.addEventListener('timeupdate', updateProgress)

progressContainer.addEventListener('click', setProgress)

audio.addEventListener('ended', nextSong);


const songItem = document.querySelectorAll('.song')

songItem.forEach(function clicked(e) {
    e.addEventListener('click', () => {
       songIndex = e.dataset.index
       loadSong(songs[songIndex])

       playSong()

    });
})