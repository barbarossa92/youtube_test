<template>
<div class="container">
    <div class="row">
        <div class="sorting">
            <h4>Сортировать по</h4>
            <label><img width="30" height="30" src="@/assets/view.png"/><input type="radio" name="sort" v-on:click="sorting" value="views"/></label>
            <label><img width="30" height="30" src="@/assets/like.png"/><input type="radio" name="sort" v-on:click="sorting" value="likes"/></label>
        </div>
        <div class="row">
            <div class="col-lg-3 col-md-4 col-xs-6 thumb" v-for="video in videos" :key="video.id">
                <a class="thumbnail" href="#" v-on:click="choiceVideo(video)" data-toggle="modal" data-title="" data-video="video.code"
                   data-target="#image-gallery">
                    <img class="img-thumbnail"
                         :src="video.thumb"
                         alt="Another alt text">
                    <p>{{ video.title }}</p>
                </a>
            </div>
        </div>
        <div class="modal fade" id="image-gallery" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" ref="modalWin">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title" id="image-gallery-title">{{ activeVideo.title }}</h4>
                        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <youtube :video-id="activeVideo.code" ref="youtube"></youtube>
                        <p><span><img width="30" height="30" src="@/assets/like.png"/></span>{{ activeVideo.like_count }}</p>
                        <p><span><img width="30" height="30" src="@/assets/view.png"/></span>{{ activeVideo.view_count }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
var axios = require('axios')
var $ = require('jquery')
const host = 'http://localhost:5000/videos'
export default {
  data: function () {
    return {videos: [], activeVideo: {}}
  },
  mounted: function () {
    axios.get(host).then((response) => (this.videos = response.data.videos))
    $(this.$refs.modalWin).on('hidden.bs.modal', this.stopVideo)
  },
  methods: {
    choiceVideo: function (video) {
      this.activeVideo = video
    },
    stopVideo: function () {
      this.$refs.youtube.player.stopVideo()
    },
    sorting: function (e) {
      axios.get(host + '?sort=' + e.target.value).then((response) => (this.videos = response.data.videos))
    }
  }
}
</script>
