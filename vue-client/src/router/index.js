import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes host mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '首页', icon: 'dashboard', affix: true }
    }]
  },

  {
    path: '/task',
    component: Layout,
    redirect: '/task/menu1',
    name: 'form',
    meta: {
      title: '任务', icon: 'form'
    },
    children: [
      {
        path: 'menu1',
        name: 'Form',
        component: () => import('@/views/task/menu1/index'),
        meta: { title: '新建扫描任务' }
      },
      {
        path: 'menu2',
        component: () => import('@/views/task/menu2/index'),
        name: 'Menu2',
        meta: { title: '任务列表' }
      }
    ]
  },
  {
    path: '/host',
    component: Layout,
    redirect: '/host/menu1',
    name: 'host',
    meta: {
      title: '资产',
      icon: 'host'
    },
    children: [
      {
        path: 'menu1',
        component: () => import('@/views/host/menu1/index'), // Parent router-view
        name: 'Menu1',
        meta: { title: '指纹库' }
      },
      {
        path: 'menu2',
        component: () => import('@/views/host/menu2/index'), // Parent router-view
        name: 'Menu2',
        meta: { title: '资产统计' }
      }
    ]
  },

  {
    path: '/vul',
    component: Layout,
    redirect: '/vul/menu1',
    name: 'vul',
    meta: {
      title: '漏洞',
      icon: 'vul'
    },
    children: [
      {
        path: 'menu1',
        component: () => import('@/views/vul/menu1/index'), // Parent router-view
        name: 'Menu1',
        meta: { title: '漏洞统计 ' }
      },
      {
        path: 'menu2',
        component: () => import('@/views/vul/menu2/index'),
        name: 'Menu2',
        meta: { title: 'POC管理' }
      }
    ]
  },
  {
    path: '/example',
    component: Layout,
    redirect: '/example/table',
    name: 'example',
    meta: { title: '报告', icon: 'el-icon-s-help' },
    children: [
      {
        path: 'table',
        name: 'Table',
        component: () => import('@/views/table/index'),
        meta: { title: '生成报表', icon: 'table' }
      },
      {
        path: 'tree',
        name: 'Tree',
        component: () => import('@/views/tree/index'),
        meta: { title: '网络结点', icon: 'tree' }
      }
    ]
  },
  {
    path: '/about',
    component: Layout,
    redirect: '/about/index',
    name: 'example',
    children: [
      {
        name: 'about',
        path: 'about',
        component: () => import('@/views/about/index'),
        meta: { title: '关于项目', icon: 'link' }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
