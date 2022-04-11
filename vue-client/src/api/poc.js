import request from '@/utils/request'

export function apiPocList(requestBody) {
  return request({
    url: '/api/poc/list',
    method: 'POST',
    data: requestBody
  })
}

// 产品选择项目列表
// export function apiAppsProduct() {
//   return request({
//     url: '/api/application/product',
//     method: 'get'
//   })
// }
