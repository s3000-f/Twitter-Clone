import Vue from 'vue'
import Router from 'vue-router'

import Navbar from './components/Navbar'
import SubNavbar from './components/SubNavbar'


import Home from './views/Home'
import PageOne from './views/PageOne'
import PageTwo from './views/PageTwo'
import Login from './views/Login'
import Main from './views/Main.vue'
import EmptyComp from './components/EmptyComp'
import Users from './views/Users.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            components: {
                main: Main
            }
        },
        {
            path: '/one',
            components: {
                navbar: Navbar,
                subnavbar: SubNavbar,
                main: PageOne
            }
        },
        {
            path: '/two',
            components: {
                navbar: Navbar,
                subnavbar: SubNavbar,
                main: PageTwo
            }
        },
        {
            path: '/three',
            components: {
                navbar: Navbar,
                subnavbar: SubNavbar,
                main:  EmptyComp
            }
        },
	    {
		    path: '/home',
		    components: {
			    navbar: Navbar,
			    subnavbar: SubNavbar,
			    main: Home
		    }
	    },
      {
        path: '/users',
        components: {
          navbar: Navbar,
          subnavbar: SubNavbar,
          main: Users
        }
      }
    ]
})
