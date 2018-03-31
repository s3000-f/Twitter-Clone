<template>
    <div class="tweet-container">
      <div class="retweet-data" v-if="isRetweeted">
        <i class="fas fa-retweet"></i>
        <span class="retweet-username">&nbsp;{{user}} Retweeted </span>
      </div>
      <div class="tweet-data">
        <span class="tweet-original-user">{{orgUser}}</span>
        <span class="tweet-original-user-id">@{{orgUser}}</span>
        <p class="tweet-text">{{text}}</p>
      </div>
      <div class="utility-bar">
          <!-- chize, yedune is likedbyUser ro pass bedim:?  -->
          <button class="m-button like-button">
            <i class="fas fa-heart"></i>
          </button>
          <span class="number-of-like">{{numOfLikes}}</span>
          <!-- ba isRetweetedByUser property, toggle esho control konim:? -->
          <button class="m-button retweet-button">
            <i class="fas fa-retweet"></i>
          </button>
          <span class="number-of-retweet">{{numOfRetweet}}</span>
          <div class="horizontal-line"></div>

      </div>
    </div>

</template>
<script>
  export default {
    name: 'tweet',
    data () {
      return {

      }
    },
    props: {
      isRetweeted: Boolean,
      user: String,
      orgUser: String,
      text: String,
      numOfLikes: Number,
      numOfRetweet: Number
    }
  }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i,900');

* {
  font-family: Roboto, sans-serif;
}


.tweet-container {
  background-color: #fff;
}
p {
  margin-top: 10px;
}

.tweet-original-user {
  font-weight: 900;
}
.tweet-original-user-id {
  color: #ccc;
}

.tweet-data {
  text-align: left;
  padding-left: 20px;
}
.horizontal-line {
  border: 0.5px solid #ddd;
}
.retweet-data {
    color: #ddd;
    font-size: 14px;
    text-align: left;
    padding-bottom: 3px;
    padding-top: 2px;
    margin-bottom: 3px;

}



.tweet-text {
  font-weight: 500;
  background-color : inherit;

}

.m-button {
  font-weight: 900;
  font-size: 20px;
  margin: 0px 0px 5px 20px;
  background: inherit;
  border: inherit;
}

.m-button:hover {
}

.retweet-button {


}

.retweet-button:hover {
  color: hsla(120, 73%, 42%, 1);

}
.like-button:hover {
  color: hsla(0, 73%, 42%, 1);
}

.icon-like {

}
</style>
