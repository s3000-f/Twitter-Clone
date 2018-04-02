<template>
  <div class="new-tweet-container">
      <div class="control">
        <div class="field">
          <textarea class="textarea" v-model="text" placeholder="Write a tweet...">{{text}}</textarea>
          <div class="level">
            <div class="level-left">
              <div class="level-item">
                <span v-bind:class="{ bad: tooLong}" class="num-background">
                  {{charsLeft}}
                </span>
              </div>
            </div>
            <div class="level-right">
              <div class="level-item">
                <button class="button tweet-button" :disabled="tooLong" v-on:click="newTweet">Tweet</button>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>

</template>


<script>
  import axios from 'axios'
  import qs from 'qs'
  let ax = axios.create({
    baseURL: 'http://localhost:5000/api/',
    timeout: 5000,
    headers: {'Content-type': 'application/x-www-form-urlencoded'}
  })
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
  	name: 'NewTweetComponent',
    data () {
      return {
        text: '',
      }
    },
    methods: {
  		newTweet: function () {
			  if (this.text) {
			  	
          ax.post('newtweet',
              qs.stringify({'token': this.$parent.$parent.$data.token}) + '&' + qs.stringify({'body': this.text})
            )
            .then( (response) => {
              if (response.data.ans.indexOf('Post Added') !== -1)
              {
	              
	              this.$data.text = '';
                ax.post('showhome',
                  qs.stringify({'token': this.$parent.$parent.$data.token})
                ).then( response => {
                  this.$parent.$data.tweets = makePostArray(response.data.ans);
                  
                }).catch(function (error) {
                  console.error(error)
                })
              }})
            .catch(function (error) {
                console.error(error)
            })
        }
		  }
    },
    computed: {
  	charsLeft: function () {
      return 250 - this.text.length
	  },
	  tooLong: function () {
      return this.charsLeft < 0;
	  }
    }
  
  }
</script>

<style>
  .tweet-button {
    background-color: dodgerblue;
    color: white;
    font-weight: bold;
  }
  
  .bad {
    background-color: crimson;
    color: white;
  }
</style>