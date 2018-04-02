<template>
  <section class="container">
    <div >
      <new-tweet-component></new-tweet-component>
    </div>
    <template v-if="hasTweet">
      <div  v-for="(tweet, key) in tweets">
      <div >
        <tweet v-bind:key="key" v-bind="tweet"></tweet>
      </div>
    </div>
    </template>
  </section>
  

</template>



<script>
  import NewTweetComponent from '../components/NewTweetComponent.vue'
  import Tweet from '../components/Tweet'
  import axios from 'axios'
  import qs from 'qs'
  let ax = axios.create({
    baseURL: 'http://localhost:5000/api/',
    timeout: 5000,
    headers: {'Content-type': 'application/x-www-form-urlencoded'}
  });
  function makePostArray(ans) {
  	let postArray = [];
    for (let i = 0 ; i < ans.length ; i++)
    {
    	for (let j = 0 ; j < ans[i].length ; j++)
      {
      	postArray.push(ans[i][j]);
      }
    }
    postArray.sort(
    	(a, b) =>
      {
      	return ( parseFloat(b.time) - parseFloat(a.time))
      }
    );
    return postArray;
  }
  export default {
    name: 'Home',
    data () {
      return {
        tweets: []
      }
    },
    created: function () {
	    console.log('created');
      ax.post('showhome',
        qs.stringify({'token': this.$parent.$data.token})
      ).then( response => {
	      console.log(response.data.ans);
	      console.log(response.data.ans[0]);
	      if( response.data.ans[0] !== 'I') {
	      	this.$data.tweets = makePostArray(response.data.ans);
	      }
        console.log('Home view: this.$data.tweets', this.$data.tweets);
	      console.log('Home view: response.data.ans', response.data.ans);
      }).catch( (error) =>{
      	console.error(error)
      })
    },
    components: {
      Tweet,
      NewTweetComponent
    },
    computed: {
    	hasTweet: function () {
        return this.$data.tweets.length > 0;
	    }
    }
  }
</script>



<style>



</style>
