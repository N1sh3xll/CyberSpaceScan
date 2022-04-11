<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      stripe
      highlight-current-row
    >
      <el-table-column align="center" label="任务序号" width="80">
        <template v-slot="scope">
          {{ scope.$index+1 }}
        </template>
      </el-table-column>
      <el-table-column label="任务名称" align="center" >
        <template v-slot="scope">
          {{ scope.row.task_name }}
        </template>
      </el-table-column>
      <el-table-column label="目标" width="250" align="center">
        <template v-slot="scope">
          <span>{{ scope.row.task_target }}</span>
        </template>
      </el-table-column>
      <el-table-column label="存活IP" width="150" align="center">
        <template v-slot="scope">
          <span>{{ scope.row.task_ip }}</span>
        </template>
      </el-table-column>
      <el-table-column label="端口" width="150" align="center">
        <template v-slot="scope">
          {{ scope.row.task_poc }}
        </template>
      </el-table-column>

      <el-table-column label="漏洞" width="150" align="center">
        <template v-slot="scope">
          {{ scope.row.task_poc }}
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="进度" width="150" align="center">
        <el-progress type="circle" width="50" :percentage="10" status=""></el-progress>
      </el-table-column>

      <el-table-column align="center" prop="created_at" label="创建时间" width="200">
        <template  v-slot="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.creat_time | FormatDate('yyyy-MM-dd HH:mm:ss') }}</span>
        </template>
      </el-table-column>

      <el-table-column  label="操作" align="center" width="180" class-name="small-padding fixed-width">
        <template v-slot="scope">
          <el-button type="primary" size="mini" @click="Alertdialog('查看任务')" >任务详情
          </el-button>
          <el-button  size="mini" type="danger" @click="Removetask(scope.row.task_id)">删除
          </el-button>
        </template>
      </el-table-column>

      <pagination v-show="total>0" :total="total"  @pagination="fetchData" />
    </el-table>
  </div>
</template>
<script>
// 引用src/api/poc配置的请求列表方法

import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import { gettask, apitaskDelete } from '@/api/task'

export default {
  name: 'InlineEditTable',
  components: { Pagination },
  filters: {
    statusFilter(attack) {
      const statusMap = {
        // 可利用: 'success',
        False: 'info',
        True: 'danger'
      }
      return statusMap[attack]
    }
  },
  data() {
    return {
      list: [],
      listLoading: true,
      total: 0,
      search: {
        currentPage: 1,
        pageSize: 10
      }
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      //  this.listLoading = true
      gettask(this.search).then(response => {
        console.log(response.code)
        if (response.code === 20000) {
          this.listLoading = false
          this.list = response.data
          this.total = response.total
        } else {
          this.$message.error('数据请求失败，请刷新后重试！')
        }
      })
    },
    Alertdialog(info) {
      this.dialogFormVisible = false
      const message = info
      this.$message.error('暂不支持' + message + '!')
      // this.$message.error('暂不支持删除!')
    },
    Removetask(id) {
      // 对应的参数是 (提示内容，标题 {自定义确定按钮文案，自定义取消按钮文案, 对话框类型}
      this.$confirm('此操作将永久删除该任务, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
        // then 点击confirmButton后执行的方法，否则是不执行关闭对话框
      }).then(() => {
        // vue click时候传d的id需要定义参数
        apitaskDelete(id).then(res => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          // 重新查询刷新数据显示
          this.fetchData()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
    // handleSizeChange(val) {
    //   this.size = val
    //   this.fetchData()
    //   console.log(`每页 ${val} 条`)
    // },
    // handleCurrentChange(val) {
    //   this.current = val
    //   this.fetchData()
    //   console.log(`当前页: ${val}`)
    // }
  }
}

</script>

<style scoped>
.demo-pagination-block + .demo-pagination-block {
  margin-top: 10px;
}
.demo-pagination-block .demonstration {
  margin-bottom: 16px;
}
.edit-input {
  padding-right: 100px;
}

.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}

.el-table--scrollable-x .el-table__body-wrapper {
  overflow: scroll !important;
  height: 29rem !important;
}
</style>
