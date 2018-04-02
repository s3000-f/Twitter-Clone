<template>
    <div class="tweet-container">
      <div class="retweet-data" v-if="retweetFlag">
        <i class="fas fa-retweet"></i>
        <span class="retweet-username">&nbsp; </span>
      </div>
      <div class="tweet-data">
        <span class="tweet-original-user">{{username}}</span>
        <span class="tweet-original-user-id">@{{user_id}}</span>
        <p class="tweet-text">{{body}}</p>
      </div>
      <div class="utility-bar">
          <!-- chize, yedune is likedbyUser ro pass bedim:?  -->
          <button class="m-button like-button" v-on:click="likeTweet(id)">
            <i class="fas fa-heart"></i>
          </button>
          <span class="number-of-like">{{likeCnt}}</span>
          <!-- ba isRetweetedByUser property, toggle esho control konim:? -->
          <button class="m-button retweet-button" @click="retweetTweet(id)">
            <i class="fas fa-retweet"></i>
          </button>
          <p class="help has-text-right">{{postDate}}</p>
          <div class="horizontal-line"></div>

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
  import TimeAgo from 'javascript-time-ago'
  import en from 'javascript-time-ago/locale/en'
  TimeAgo.locale(en)
  const timeAgo = new TimeAgo('en-US')
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
    name: 'Tweet',
    data () {
      return {
      }
    },
    props: {
      retweet: String,
      user_id: String,
      username: String,
      time: String,
      body: String,
      likeCnt: String,
      id: String
    },
    computed: {
    	retweetFlag: function () {
        return this.$props.retweet === 'True';
	    },
      postDate: function () {
        return timeAgo.format(new Date(parseFloat(this.$props.time) * 1000))
        
      },
    },
    methods: {
    	likeTweet: function (postid) {
        ax.post('liketweet',
           qs.stringify({'token': this.$parent.$parent.$data.token}) + '&' +  qs.stringify({'postid': postid})
        ).then( response => {
        	if (response.data.ans.indexOf('Already Liked') !== -1)
          {
          	alert('you alredy liked this post')
          }
          else if (response.data.ans.indexOf('Liked') !== -1)
          {
	          console.log('Tweet Comp likeTweet, postid=', this.$props.id,' is Liked');
	          if (this.$router.currentRoute.path.indexOf('/home') !== -1)
            {
            	ax.post('showhome',
                      qs.stringify({'token': this.$parent.$parent.$data.token})
                    ).then( response => {
                      this.$parent.$data.tweets = makePostArray(response.data.ans);
                      console.log('Tweet Component retweetTweet this.$parent.$data.tweets= ', this.$parent.$data.tweets);
                    }).catch(function (error) {
                      	console.error(error)
                      })
            }
            else if (this.$router.currentRoute.path.indexOf('/search') !== -1)
            {
	            ax.post('hashtag', qs.stringify({'hashtag': this.$parent.$data.searchValue}))
                .then( response => {
	                this.$parent.$data.tweets = response.data.ans;
	                this.$parent.$data.tweets.sort( (a,b)=> {
	                	return ( parseFloat(b.time) - parseFloat(a.time));
                  })
                })
                .catch( (error) =>{
                	console.error(error)
                })
            }
          }
        }).catch(e => {console.error(e)})
	    },
      retweetTweet: function (postid) {
        ax.post('retweet',
           qs.stringify({'token': this.$parent.$parent.$data.token}) + '&' +  qs.stringify({'postid': postid})
        ).then( response => {
          if (response.data.ans.indexOf('Post Added') !== -1)
          {
            if (this.$router.currentRoute.path.indexOf('/home') !== -1)
            {
            	ax.post('showhome',
                      qs.stringify({'token': this.$parent.$parent.$data.token})
                    ).then( response => {
                      this.$parent.$data.tweets = makePostArray(response.data.ans);
                      console.log('Tweet Component retweetTweet this.$parent.$data.tweets= ', this.$parent.$data.tweets);
                    }).catch(function (error) {
                      	console.error(error)
                      })
            }
            else if (this.$router.currentRoute.path.indexOf('/search') !== -1)
            {
            	ax.post('hashtag', qs.stringify({'hashtag': this.$parent.$data.searchValue}))
                .then( response => {
                	this.$parent.$data.tweets = response.data.ans;
	                this.$parent.$data.tweets.sort( (a,b)=> {
	                	return ( parseFloat(b.time) - parseFloat(a.time));
                  })
                })
                .catch( (error) =>{
                	console.error(error)
                })
            }
          }
        }).catch(e => {console.error(e)})
	    }
    },
    created: function () {
      this.$data.likeCount = parseInt(this.$props.likeCnt);
    }
  }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i,900');

* {
  font-family: Roboto, sans-serif;
}


.tweet-container {
  background-color: #ffffff;
  padding-top: 10px;
}
p {
  margin-top: 10px;
  padding-right: 20px;
  white-space: pre-wrap;
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
  margin-bottom: 20px;
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
