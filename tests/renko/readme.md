砖图数据及示范策略回测

回测数据tick
    
    - 砖图数据通过tick生成
    - 回测数据tick，可通过自行采购的tick原始数据，或者tdx接口下载
    - 数据一般存在 项目目录/tick_data, 数据量巨大。 
    - windows下存放小量数据，用作测试。
    - linux下， 可使用NFS共享多台测试服务器，挂接为 tick_data使用
    - tdx 下载的数据目录 项目目录/tick_data/tdx, future为期货数据，stock为股票数据
    - tdx 接口见 项目目录/vnpy/data/tdx/tdx_future_data.py 和 tdx_stock_data.py
    - tdx 期货，接口方法：get_history_transaction_data()， 
        当设置cache_folder为 项目目录/tick_data/tdx，即可在下载时，自动保存缓存文件.
    - tdx 股票，接口方法：get_history_transaction_data(),
        当设置cache_folder为 项目目录/tick_data/tdx，即可在下载时，自动保存缓存文件.

Renko Bar（砖图K线）
    
    - 砖图数据生成后，可存储在csv文件中，或者数据库中，供后续策略回测或实盘前加载使用。
    
    - 当前目录/test_rebuild_future.py
      该程序演示了如何通过tdx future tick数据，从开始时间~结束时间，构造砖图数据，并存储至数据库FutureRenko。
      
    - 当前目录/test_rebuild_stock.py
      该程序演示了如何通过tdx stock tick数据，从开始时间~结束时间，构造砖图数据，并存储至数据库StockRenko。
     
砖图历史数据加载 

    - 项目目录/vnpy/data/renko/renko_source.py
    - 使用方法样例，参见 strategy_triple_ma_v2.py

回测
    
