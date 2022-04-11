<template>
  <div class="app-container">
    <!--:data 绑定data()的数组值,会动态根据其变化而变化-->
    <el-table
      v-loading="listLoading"
      style="width: 100%;"
      :data="list"
      element-loading-text="拼命加载中"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="序号" width="95">
        <template v-slot="scope">
          {{ scope.row.poc_id }}
        </template>
      </el-table-column>
      <el-table-column label="名称">
        <template v-slot="scope">
          {{ scope.row.poc_name }}
        </template>
      </el-table-column>

      <el-table-column label="漏洞描述" width="200" align="center">
        <template v-slot="scope">
          {{ scope.row.poc_path }}
        </template>
      </el-table-column>

      <el-table-column label="危害级别" width="180px" align="center">
<!--        <template v-slot="{row}">-->
<!--          <svg-icon v-for="n in +row.poc_level" :key="n" icon-class="star" class="meta-item__icon" />-->
<!--        </template>-->
        <template v-slot="{row}">
          <el-rate
          v-model ="row.poc_level"
          disabled
          show-score
          :colors="['#F7BA2A', '#FF9900', '#fc4d3e']"
          text-color="#ff9900"
          :score-template=row.poc_level >
          </el-rate>
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="漏洞利用" width="110" align="center">
        <template v-slot="scope">
          <el-tag :type="scope.row.poc_attack | statusFilter">{{ scope.row.poc_attack }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" label="修改时间" width="250">
        <template v-slot="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.poc_time | FormatDate('yyyy-MM-dd HH:mm:ss') }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" width="180" class-name="small-padding fixed-width">
        <template v-slot="scope">
          <el-button type="primary" size="mini" @click="handleClick(scope.row)">详情</el-button>
          <el-button size="mini" type="danger" @click="Alertdialog('删除')">删除</el-button>
        </template>
      </el-table-column>

      <!--对话框嵌套表，使用el-dialog-->
      <el-dialog title="POC内容详情" :visible.sync="dialogFormVisible" :append-to-body="true" width="40%">
        <el-descriptions :column="1" :model="templist" border>
          <el-descriptions-item label="名称">{{ templist.name }}</el-descriptions-item>
          <el-descriptions-item label="漏洞描述">{{ templist.descriptions }}</el-descriptions-item>
          <el-descriptions-item label="文件名">{{ templist.path }}</el-descriptions-item>
          <el-descriptions-item label="等级">
<!--            <svg-icon v-for="n in +templist.level" :key="n" icon-class="star" class="meta-item__icon" />-->
<!--            <template v-slot="{row}">-->
              <el-rate
                value ="3.5"
                disabled
                show-score
                :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                text-color="#ff9900"
                :score-template=value >
              </el-rate>
<!--            </template>-->
          </el-descriptions-item>
          <el-descriptions-item label="漏洞利用"><el-tag :type="templist.attack | statusFilter" size="small">{{ templist.attack }}</el-tag></el-descriptions-item>
          <el-descriptions-item label="修改时间">{{ templist.create_time | FormatDate('yyyy-MM-dd HH:mm:ss') }}</el-descriptions-item>
        </el-descriptions>

        <div slot="footer" class="dialog-footer">
          <el-button @click="Alertdialog('编辑')">编辑</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">取消</el-button>
        </div>
      </el-dialog>

    </el-table>
    <div class="pagination-container">
      <el-pagination
        align="right"
        style="margin: 8px"
        background
        :current-page.sync="search.currentPage"
        :page-sizes="[10, 20, 30, 50]"
        :page-size="search.pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>

  </div>
</template>

<script>
// 引用src/api/poc配置的请求列表方法

import { apiPocList } from '@/api/poc'

import { scrollTo } from '@/utils/scroll-to'

export default {
  name: 'InlineEditTable',
  filters: {
    statusFilter(attack) {
      const statusMap = {
        // 可利用: 'success',
        False: 'info',
        True: 'danger'
      }
      return statusMap[attack]
    },
    Scroll: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      list: [],
      total: 0,
      listLoading: false,
      search: {
        currentPage: 1,
        pageSize: 10
      },
      templist: {
        id: undefined,
        name: '',
        level: '',
        create_time: '',
        attack: '',
        path: '',
        descriptions: ''
      },
      // 控制嵌套表单显示和隐藏
      dialogFormVisible: false
    }
  },
  // 页面生命周期中的创建阶段调用
  created() {
    this.listLoading = true
    this.searchClick()
  },
  methods: {
    searchClick() {
      apiPocList(this.search).then(response => {
        // console.log(response.code)
        if (response.code === 20000) {
          this.list = response.data
          this.total = response.total
          // console.log(response.data)
          // Just to simulate the time of the request
          setTimeout(() => {
            this.listLoading = false
          }, 1 * 1000)
        } else {
          this.$message.error('数据请求失败，请刷新后重试！')
        }
      })
    },
    // searchClick() {
    //   apiAppsSearch(this.search).then(response => {
    //     // 将返回的结果赋值给表格自动匹配
    //     this.tableData = response.data
    //     this.total = response.total
    //   })
    // },
    handleSizeChange(val) {
      this.listLoading = true
      if (this.Scroll) {
        scrollTo(0, 800)
      }
      this.search.pageSize = val
      this.searchClick()
      // this.listLoading = false
      console.log(`每页 ${val} 条`)
    },
    handleCurrentChange(val) {
      this.listLoading = true
      scrollTo(0, 800)
      this.search.currentPage = val
      this.searchClick()
      console.log(`当前页: ${val}`)
    },
    Alertdialog(info) {
      this.dialogFormVisible = false
      const message = info
      this.$message.error('暂不支持' + message + '!')
      // this.$message.error('暂不支持删除!')
    },
    handleClick(row) {
      this.dialogFormVisible = true // 控制弹窗显示
      this.templist.id = row.poc_id
      this.templist.name = row.poc_name
      this.templist.path = row.poc_path
      this.templist.level = row.poc_level
      this.templist.attack = row.poc_attack
      this.templist.create_time = row.poc_time
      this.templist.descriptions = row.poc_descriptions
      // 这里是因为有时候接口传过来的字符串为空需要做个判断，JSON.parse()方法对数据也比较严格，报错写在后面
      this.templist.level = row.poc_level !== '' ? JSON.parse(row.poc_level) : {}
      this.templist.descriptions = row.poc_descriptions !== '' ? JSON.parse(row.poc_descriptions) : {}
    }
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

.pagination-container {
  background: #fff;
  padding: 32px 16px;
}

.app-container.hidden {
  display: none;
}

.pagination-container.hidden {
  display: none;
}

.el-table--scrollable-x .el-table__body-wrapper {
  overflow: scroll !important;
  height: 29rem !important;
}
</style>
