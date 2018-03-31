<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        Hello
      </div>
      <div class="col-md-6">
        Hello
      </div>
    </div>
  </div>


</template>



<script>
import Tweet from '../components/Tweet'
export default {
  name: 'Home',
  data () {
    return {
      tweets: [
        {
          isRetweeted: true,
          user: 'M',
          orgUser: 'DB',
          text: 'fuck off!',
          numOfLikes: 1,
          numOfRetweet: 2
        },
        {
          isRetweeted: false,
          user: undefined,
          orgUser: 'M',
          text: 'fuck0 ON!',
          numOfLikes: 1000,
          numOfRetweet: 3
        },
        {
          isRetweeted: true,
          user: 'M',
          orgUser: 'DB',
          text: 'fuck off!',
          numOfLikes: 1,
          numOfRetweet: 2
        }
      ]
    }
  },
  components: {
    Tweet
  }
}
</script>



<style>



</style>
