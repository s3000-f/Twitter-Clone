<template>
  <section class="container">
    <div >
      <new-tweet-component></new-tweet-component>
    </div>
    <div  v-for="(tweet, key) in tweets">
      <div >
        <tweet v-bind:key="key" v-bind="tweet"></tweet>
      </div>
    </div>
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
  })
  export default {
    name: 'Home',
    data () {
      return {
        tweets: []
      }
    },
    created: function () {
	    console.log('created');
	    /*ax.post('newtweet' ,
         qs.stringify({'token': this.$parent.$data.token}) + '&' + qs.stringify({'body': 'some fucking shit #not asrf #as #a #b #c #d #e \n' +
	      '#f #asff #ojgb #KVJDLKA #112 #etg'})
      ).then((response)=> {
		    console.log(response.data.ans);
	    })*/
      ax.post('showhome',
        qs.stringify({'token': this.$parent.$data.token})
      ).then( response => {
	      this.$data.tweets = (response.data.ans[0]);
	      this.$data.tweets.sort((a,b)=> {return ( parseFloat(b.time) - parseFloat(a.time))});
	      console.log(this.$data.tweets);
      })
    },
    components: {
      Tweet,
      NewTweetComponent
    }
  }
</script>



<style>



</style>
