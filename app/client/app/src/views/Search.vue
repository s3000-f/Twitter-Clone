<template>
    <div class="columns">
      <div class="column is-half">
        <h1 class="title">
          &nbsp;&nbsp;Top Hashtags
        </h1>
        <table class="table">
          <thead>
            <tr>
              <th>\</th>
              <th>Hashtag Name</th>
              <th>Number of Use</th>
            </tr>
          </thead>
          <tbody>
            <hashtag-card v-for="(takrar, esm, key) in topHashtags"
                          v-bind:key="key"
                          v-bind:hid="key+1"
                          v-bind:hashtag-name="esm"
                          v-bind:num-of-repetition="takrar">
            </hashtag-card>
          </tbody>
        </table>
      </div>
      
      <div class="column is-half">
        <h1 class="title">
          &nbsp;&nbsp;Search Hashtags
        </h1>
        <div class="field has-addons">
          <div class="control">
            <input class="input" v-model="searchValue" type="text" placeholder="Search a hashtag">
          </div>
          <div class="control">
            <a class="button is-info" v-on:click="search(searchValue)">
              Search
            </a>
          </div>
        </div>
          <div  v-for="(tweet, key) in tweets">
            <div>
              <tweet v-bind:key="key" v-bind="tweet"></tweet>
            </div>
          </div>
      </div>
      
    </div>
</template>

<script>
  import HashtagCard from '../components/HashtagCard.vue'
  import Tweet from '../components/Tweet'
  import axios from 'axios'
  import qs from 'qs'
  let ax = axios.create({
    baseURL: 'http://localhost:5000/api/',
    timeout: 5000,
    headers: {'Content-type': 'application/x-www-form-urlencoded'}
  })
  export default {
  	name: 'Search',
    components: {
  		HashtagCard,
      Tweet
    },
    data() {
  		return {
  			topHashtags: {},
        searchValue: '',
        tweets: {}
      }
    },
    created: function () {
      ax.post('tophashtags',)
        .then( response => {
	      this.$data.topHashtags = response.data.ans;
	        console.log(this.$data.topHashtags);
        })
        .catch( (error) =>{
      	console.error(error)
        })
    },
    methods: {
  		search: function (v) {
        ax.post('hashtag', qs.stringify({'hashtag': v}) )
        .then( response => {
	        this.$data.tweets = response.data.ans;
	        this.$data.tweets.sort((a, b) => {
			      return ( parseFloat(b.time) - parseFloat(a.time))
		      });
	        if (this.$data.tweets.length === 0){
	        	alert('No post with this hashtag found...')
          }
        })
        .catch( (error) =>{
      	console.error(error)
        })
		  }
    }
  }
</script>

