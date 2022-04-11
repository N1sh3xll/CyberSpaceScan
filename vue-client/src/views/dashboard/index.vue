<template>
<!--  <div class="dashboard-container">-->

  <div class="dashboard-editor-container">
<!--    <div class="dashboard-text">name: {{ name }}</div>-->
    <panel-group />

    <el-row :gutter="32">
      <el-col :xs="24" :sm="12" :lg="12">
<!--        <mallki class-name="mallki-text" text="硬件" />-->
        <div class="chart-wrapper">
          <mallki class-name="mallki-text" text="指纹Banner" />
          <banner />
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :lg="12">
        <div class="chart-wrapper">
          <mallki class-name="mallki-text" text="任务统计" />
          <bar-chart />
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="24" :sm="12" :lg="12">
        <div class="chart-wrapper">
          <mallki class-name="mallki-text" text="支撑系统" />
          <pie-chart />
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :lg="12">
        <div class="chart-wrapper">
          <mallki class-name="mallki-text" text="漏洞统计" />
          <bar-chart />
        </div>
      </el-col>
    </el-row>
<!--    #043e5e-->
    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <mallki class-name="mallki-text" style="margin-bottom: 10px;" text="资产地理位置信息测绘" />
      <mapChart  />
    </el-row>
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
// import RaddarChart from './components/RaddarChart'
import PanelGroup from './components/PanelGroup'
import PieChart from './components/PieChart'
import BarChart from './components/BarChart'
import mapChart from './components/mapChart'
import banner from './components/banner'

import Mallki from '@/components/TextHoverEffect/Mallki'

export default {
  name: 'Dashboard',
  components: {
    PanelGroup,
    PieChart,
    BarChart,
    mapChart,
    Mallki,
    banner
  }
  // computed: {
  //   ...mapGetters([
  //     'name'
  //   ])
  // }
}
</script>

<style lang="scss" scoped>
//.dashboard {
//  &-container {
//    margin: 30px;
//  }
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
  //&-text {
  //  font-size: 30px;
  //  line-height: 46px;
  //}
}
@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
