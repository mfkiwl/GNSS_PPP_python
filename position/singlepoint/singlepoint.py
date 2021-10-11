import time
from position.singlepoint import *
from position.common import *
from position.rtkpoint import *

if __name__ == '__main__':
    # 读取广播星历数据
    nav_data_list = NAVDATA.NavData().initNavData("D:/Desktop/SatellitePosition-master/data/nav.21N")
    print(nav_data_list)
    # 读取观测量数据
    OBS_DATA = OBSDATA.ObsData().initObsData("D:/Desktop/SatellitePosition-master/data/Obs_gps.21O")
    # sol = solustion.positionsol()
    rtkParam = RTKPOSITION.RTKPARAM()
    # for i in range(len(OBS_DATA)):
    print("开始处理时间：", time.time())
    rtkParam = SINGLEPOINTPOSITION.SinglePointPosition().exesinglepoint(OBS_DATA[0], nav_data_list, rtkParam)
    sol = rtkParam.sol
    print("GPS week = ", sol.gpsweek, " GPS sec = ", sol.gpssec, " POS = ", sol.X,
          " NS = ", sol.ns, "AGE = ", sol.age, " POS TYPE = ", sol.pos_type)
    print("结束处理时间：", time.time())
