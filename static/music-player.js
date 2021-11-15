
const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);
const heading = $('.name-music h2')
const cdThumb = $('.img-music')
const audio = $('#audio')
const cd = $('.img-music')
const playBtn = $('.btn-toggle-play')
const player = $('.player')
const progress = $('.progress')
const nextBtn = $('.btn-next')
const prevBtn = $('.btn-prev')
const randomBtn = $('.btn-random')
const repeatBtn = $('.btn-repeat')
const playList = $('.play-list')
const PLAYER_STORAGE_KEY = 'LEVIN_PLAYER'

const muteBtn = $('.nav__mobile-item.mute-Btn')
const volumeBtn = $('#volume')
const firstPage = $('.first-background')
const infoBtn = $('.info-song')



const app = {
    currentIndex: 0,
    isPlaying: false,
    isRandom: false,
    isRepeat: false,
    isMuted: false,
    isInfo: false,
    config: JSON.parse(localStorage.getItem(PLAYER_STORAGE_KEY)) || {} ,
    setConfig: function(key, value) {
        this.config[key] = value
        localStorage.setItem(PLAYER_STORAGE_KEY, JSON.stringify(this.config))
    },
    songs : [
                        {% block content_nhac %} {% for item in nhac %} {% if nhac %}
                        {
                            name: '{{ item.song_tenbaihat }}',
                            singer: '{{ item.song_casi_id}}',
                            path: '{{ item.song_file }}',
                            img: '{{ item.song_anhbia }}'
                        },
                        {% endif %} {% endfor %} {% endblock %}
             ],
     render: function() {
        const htmls = this.songs.map((song,index) => {
            return `
                <div data-index=${index} class="song ${index === this.currentIndex ? 'active' : ''} ">
                    <div class="thumb" style="background-image: url(${song.img});">
                    </div>
                    <div class="body">
                        <h3 class="title">${song.name}</h3>
                        <p class="author">${song.singer}</p>
                    </div>
                    <label for="nav-mobile-input" class="option nav-mobile-input">
                        <i class="fas fa-ellipsis-h"></i>
                    </label>
                </div>
            `
        })
        $('.play-list').innerHTML = htmls.join('');
    },
    defineProperties: function() {
        Object.defineProperty(this, 'currentSong', {
            get: function() {
                return this.songs[this.currentIndex]
            }
        })
    },
    handleEvents: function() {
        const _this = this
        const cdWidth = cd.offsetWidth
        const cdHeight = cd.offsetHeight

        // Xử lý phóng to, thu nhỏ CD khi kéo thanh cuộn
        document.onscroll = function() {
            const scrollTop = window.scrollY || document.documentElement.scrollTop
            const newCdWidth = cdWidth - scrollTop
            const newCdHeight = cdHeight - scrollTop

            cd.style.width = newCdWidth > 5 ? newCdWidth + 'px' : 0
            cd.style.height = newCdHeight > 5 ? newCdHeight + 'px' : 0
            cd.style.opacity = newCdHeight / cdHeight
        }

        // Xử lý khi click Play
        playBtn.onclick = function() {
            if(_this.isPlaying)
            {
                audio.pause()
            } else {
                audio.play()
            }
        }

        //Khi bài hát được phát
        audio.onplay = function() {
            _this.isPlaying = true
            player.classList.add('playing')
            cdThumbAnimate.play()
        }

        //Khi bài hát dừng lại
        audio.onpause = function() {
            _this.isPlaying = false
            player.classList.remove('playing')
            cdThumbAnimate.pause()
        }

        //Khi tiến độ bài hát thay đổi
        audio.ontimeupdate = function() {
            if(audio.duration) {
                const progressPercent = Math.floor(audio.currentTime / audio.duration *100)
                progress.value = progressPercent
            }
        }

        //Khi tua bài hát thì xử lý onchang
        progress.oninput = function(e) {
            audio.currentTime = e.target.value * audio.duration / 100
        }

        //Xử lý khi CD xoay vòng / dừng lại
        const cdThumbAnimate = cdThumb.animate([
            {transform: 'rotate(360deg)'}
        ],{
            duration: 10000,
            iterations: Infinity
        })
        cdThumbAnimate.pause()

        //Khi next bài hát
        nextBtn.onclick = function () {
            if(_this.isRandom) {
                _this.randomSong()
            } else {
                _this.nextSong()
            }
            audio.play()
            _this.render()
            _this.scrollToActiveSong()
        }

         //Khi prev bài hát
         prevBtn.onclick = function () {
            if(_this.isRandom) {
                _this.randomSong()
            } else {
                _this.prevSong()
            }
            audio.play()
            _this.render()
            _this.scrollToActiveSong()
        }

        //Khi random bài hát
        randomBtn.onclick = function () {
            _this.isRandom = !_this.isRandom
            _this.setConfig('isRandom', _this.isRandom)
            randomBtn.classList.toggle('active', _this.isRandom)
        }

        //Khi hết bài thì next/repeat song
        audio.onended = function() {
            if(_this.isRepeat){
                audio.play()
            } else {
                nextBtn.click()
            }
        }

        //Xử lý lặp lại 1 bài hát
        repeatBtn.onclick = function () {
            _this.isRepeat = !_this.isRepeat
            _this.setConfig('isRepeat', _this.isRepeat)
            repeatBtn.classList.toggle('active', _this.isRepeat)
        }

        //Lắng nghe hành vi click vào playlist
        playList.onclick = function(e) {
            const songNode = e.target.closest('.song:not(.active)')

            console.log(songNode)
            if( songNode || e.target.closest('.option')) {

                //Khi click vào song
                if(songNode) {
                    _this.currentIndex = Number(songNode.dataset.index)
                    _this.loadCurrentSong()
                    _this.render()
                    audio.play()
                }

                //Khi click vào option
                 if(e.target.closest('.option')) {

                 }
            }
        }

        //Xử lý khi nhấn mute / unmute
        muteBtn.onclick = function() {
            muteBtn.classList.toggle('muted', _this.isMuted)
            if (_this.isMuted) {
                audio.muted = true

            } else {
                audio.muted = false
            }
            _this.isMuted = !_this.isMuted
        }



        // Khi tua âm lương xử lý onchange
        volumeBtn.oninput = function(e) {
            audio.volume = e.target.value / 100
        }

        firstPage.onclick = function() {
            firstPage.classList.add('move-out')
        }

    },
    loadCurrentSong: function() {

        heading.textContent = this.currentSong.name
        cdThumb.style.backgroundImage = `url(${this.currentSong.img})`
        audio.src = this.currentSong.path
    },
    loadConfig: function() {
        this.isRandom = this.config.isRandom
        this.isRepeat = this.config.isRepeat
    },
    nextSong: function() {
        this.currentIndex++
        if(this.currentIndex >= this.songs.length) {
            this.currentIndex = 0
        }
        this.loadCurrentSong()
    },
    prevSong: function() {
        this.currentIndex--
        if(this.currentIndex < 0) {
            this.currentIndex = this.songs.length - 1
        }
        this.loadCurrentSong()
    },
    randomSong: function() {
        let newIndex
        do {
            newIndex = Math.floor(Math.random() * this.songs.length)
        } while (newIndex == this.currentIndex)

        this.currentIndex = newIndex
        this.loadCurrentSong()

    },
    scrollToActiveSong: function() {
        setTimeout(() => {
            if(this.currentIndex == 0 || this.currentIndex == 1 || this.currentIndex == 2 || this.currentIndex == 3) {
                $('.song.active').scrollIntoView({
                behavior: 'smooth',
                block: 'center' })
            } else {
                $('.song.active').scrollIntoView({
                behavior: 'smooth',
                block: 'nearest' })
            }
        },350)

    },
    start: function() {
        //Gắn cầu hình từ config vào ứng dụng
        this.loadConfig()

        // Định nghĩa các thuộc tính cho Object
        this.defineProperties()

        // Lắng nghe / xử lý các sự kiện
        this. handleEvents()

        // Tải thông tin bài hát đầu tiên vào UI khi chạy ứng dụng
        this.loadCurrentSong()

        // Render playlist
        this.render()

        //Hiển thị trạng thái ban đầu của button random & repeat
        randomBtn.classList.toggle('active', this.isRandom)
        repeatBtn.classList.toggle('active', this.isRepeat)
    }
}



app.start();