import request from '@/utils/request'

export function newtask(data) {
  return request({
    url: '/api/task/new',
    method: 'post',
    data
  })
}

export function gettask(data) {
  return request({
    url: '/api/task/get',
    method: 'post',
    data: data
  })
}

// 调用真实删除数据库接口
export function apitaskDelete(id) {
  return request({
    url: '/api/task/delete',
    method: 'delete',
    params: {
      'task_id': id
    }
  })
}
