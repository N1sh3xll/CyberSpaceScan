import Cookies from 'js-cookie'
import { localStorageGetItem, localStorageSetItem } from '@/utils/index'

const TokenKey = 'vue_admin_template_token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}
const userInfoKey = 'userInfo'
const EXP = 7 // day
export function setUserInfo(data, persistent = false) {
  if (persistent) {
    localStorageSetItem(userInfoKey, data)
  } else {
    sessionStorage.setItem(userInfoKey, JSON.stringify(data))
  }
}

// EXP * 24 * 60 * 60 * 1 * 1000
export function getUserInfo() {
  if (sessionStorage.getItem(userInfoKey)) {
    return JSON.parse(sessionStorage.getItem(userInfoKey))
  } else {
    return localStorageGetItem(userInfoKey, EXP * 24 * 60 * 60 * 1 * 1000)
  }
}
