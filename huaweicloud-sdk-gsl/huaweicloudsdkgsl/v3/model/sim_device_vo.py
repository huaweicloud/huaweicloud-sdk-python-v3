# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimDeviceVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'account_id': 'str',
        'cid': 'str',
        'sim_pool_id': 'int',
        'imei': 'str',
        'sim_status': 'int',
        'device_status': 'int',
        'device_model': 'str',
        'act_date': 'datetime',
        'device_status_date': 'datetime',
        'node_id': 'str',
        'iccid': 'str',
        'network_type': 'str',
        'dbm': 'str',
        'signal_level': 'str',
        'sim_type': 'int',
        'tag_names': 'str',
        'order_id': 'int',
        'expire_time': 'datetime',
        'price_plan_name': 'str',
        'sim_price_plan_id': 'int',
        'flow_left': 'float',
        'flow_used': 'float',
        'operator_status': 'int',
        'msisdn': 'str',
        'imsi': 'str',
        'customer_attribute1': 'str',
        'customer_attribute2': 'str',
        'customer_attribute3': 'str',
        'customer_attribute4': 'str',
        'customer_attribute5': 'str',
        'customer_attribute6': 'str',
        'real_named': 'bool',
        'cut_net_flag': 'bool',
        'exceed_cut_net_flag': 'bool',
        'exceed_cut_net_quota': 'int',
        'imei_bind_remain_times': 'int',
        'speed_value': 'int'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'account_id': 'account_id',
        'cid': 'cid',
        'sim_pool_id': 'sim_pool_id',
        'imei': 'imei',
        'sim_status': 'sim_status',
        'device_status': 'device_status',
        'device_model': 'device_model',
        'act_date': 'act_date',
        'device_status_date': 'device_status_date',
        'node_id': 'node_id',
        'iccid': 'iccid',
        'network_type': 'network_type',
        'dbm': 'dbm',
        'signal_level': 'signal_level',
        'sim_type': 'sim_type',
        'tag_names': 'tag_names',
        'order_id': 'order_id',
        'expire_time': 'expire_time',
        'price_plan_name': 'price_plan_name',
        'sim_price_plan_id': 'sim_price_plan_id',
        'flow_left': 'flow_left',
        'flow_used': 'flow_used',
        'operator_status': 'operator_status',
        'msisdn': 'msisdn',
        'imsi': 'imsi',
        'customer_attribute1': 'customer_attribute1',
        'customer_attribute2': 'customer_attribute2',
        'customer_attribute3': 'customer_attribute3',
        'customer_attribute4': 'customer_attribute4',
        'customer_attribute5': 'customer_attribute5',
        'customer_attribute6': 'customer_attribute6',
        'real_named': 'real_named',
        'cut_net_flag': 'cut_net_flag',
        'exceed_cut_net_flag': 'exceed_cut_net_flag',
        'exceed_cut_net_quota': 'exceed_cut_net_quota',
        'imei_bind_remain_times': 'imei_bind_remain_times',
        'speed_value': 'speed_value'
    }

    def __init__(self, sim_card_id=None, account_id=None, cid=None, sim_pool_id=None, imei=None, sim_status=None, device_status=None, device_model=None, act_date=None, device_status_date=None, node_id=None, iccid=None, network_type=None, dbm=None, signal_level=None, sim_type=None, tag_names=None, order_id=None, expire_time=None, price_plan_name=None, sim_price_plan_id=None, flow_left=None, flow_used=None, operator_status=None, msisdn=None, imsi=None, customer_attribute1=None, customer_attribute2=None, customer_attribute3=None, customer_attribute4=None, customer_attribute5=None, customer_attribute6=None, real_named=None, cut_net_flag=None, exceed_cut_net_flag=None, exceed_cut_net_quota=None, imei_bind_remain_times=None, speed_value=None):
        """SimDeviceVO

        The model defined in huaweicloud sdk

        :param sim_card_id: sim卡id
        :type sim_card_id: int
        :param account_id: 账户id
        :type account_id: str
        :param cid: 容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)
        :type cid: str
        :param sim_pool_id: 流量池ID
        :type sim_pool_id: int
        :param imei: 设备IMEI
        :type imei: str
        :param sim_status: sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机
        :type sim_status: int
        :param device_status: 设备状态
        :type device_status: int
        :param device_model: 设备模组
        :type device_model: str
        :param act_date: 激活日期 例如2020-01-31T16:00:00.000Z
        :type act_date: datetime
        :param device_status_date: 设备状态变更时间 例如2020-01-31T16:00:00.000Z
        :type device_status_date: datetime
        :param node_id: 设备标识
        :type node_id: str
        :param iccid: 码号iccid
        :type iccid: str
        :param network_type: 网络类型
        :type network_type: str
        :param dbm: 信号强度
        :type dbm: str
        :param signal_level: 信号等级:1.差  2.良  3.良 4.优（该参数只有eSIM,vSIM返回，实体卡不返回）
        :type signal_level: str
        :param sim_type: sim卡类型 1.vSIM  2.eSIM  3.实体卡
        :type sim_type: int
        :param tag_names: 标签名
        :type tag_names: str
        :param order_id: 批次号
        :type order_id: int
        :param expire_time: 到期时间 例如2021-06-30T00:00:00.000Z
        :type expire_time: datetime
        :param price_plan_name: 在用套餐名
        :type price_plan_name: str
        :param sim_price_plan_id: 套餐订购实例ID
        :type sim_price_plan_id: int
        :param flow_left: 剩余流量(单位M)，数据默认截止到昨日24点。
        :type flow_left: float
        :param flow_used: 已用流量(单位M)，数据默认截止到昨日24点。
        :type flow_used: float
        :param operator_status: 运营商状态 -1.正常（非停机状态） 1.停机（超流量停机） 2.停机（超流量阈值停机） 3.停机（流量池停机） 4.停机（套餐到期停机） 5.停机（主动停机） 6.停机（违规停机） 7.停机（机卡分离停机）
        :type operator_status: int
        :param msisdn: MSISDN
        :type msisdn: str
        :param imsi: IMSI
        :type imsi: str
        :param customer_attribute1: 自定义属性一
        :type customer_attribute1: str
        :param customer_attribute2: 自定义属性二
        :type customer_attribute2: str
        :param customer_attribute3: 自定义属性三
        :type customer_attribute3: str
        :param customer_attribute4: 自定义属性四
        :type customer_attribute4: str
        :param customer_attribute5: 自定义属性五
        :type customer_attribute5: str
        :param customer_attribute6: 自定义属性六
        :type customer_attribute6: str
        :param real_named: 是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。
        :type real_named: bool
        :param cut_net_flag: 是否单独断网 true:断网，false:未断网 （当前只支持联通、移动的组池卡，电信卡不限制）
        :type cut_net_flag: bool
        :param exceed_cut_net_flag: 是否达量断网 true:达量断网，false:未达量断网 （当前只支持联通、移动的组池卡，电信卡不限制）
        :type exceed_cut_net_flag: bool
        :param exceed_cut_net_quota: 达量断网阈值（单位MB 当前仅电信卡支持）
        :type exceed_cut_net_quota: int
        :param imei_bind_remain_times: 本月机卡绑定剩余次数（当前仅电信卡支持）
        :type imei_bind_remain_times: int
        :param speed_value: 网络限制速率（单位Kbps,当前电信联通卡支持）
        :type speed_value: int
        """
        
        

        self._sim_card_id = None
        self._account_id = None
        self._cid = None
        self._sim_pool_id = None
        self._imei = None
        self._sim_status = None
        self._device_status = None
        self._device_model = None
        self._act_date = None
        self._device_status_date = None
        self._node_id = None
        self._iccid = None
        self._network_type = None
        self._dbm = None
        self._signal_level = None
        self._sim_type = None
        self._tag_names = None
        self._order_id = None
        self._expire_time = None
        self._price_plan_name = None
        self._sim_price_plan_id = None
        self._flow_left = None
        self._flow_used = None
        self._operator_status = None
        self._msisdn = None
        self._imsi = None
        self._customer_attribute1 = None
        self._customer_attribute2 = None
        self._customer_attribute3 = None
        self._customer_attribute4 = None
        self._customer_attribute5 = None
        self._customer_attribute6 = None
        self._real_named = None
        self._cut_net_flag = None
        self._exceed_cut_net_flag = None
        self._exceed_cut_net_quota = None
        self._imei_bind_remain_times = None
        self._speed_value = None
        self.discriminator = None

        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if account_id is not None:
            self.account_id = account_id
        if cid is not None:
            self.cid = cid
        if sim_pool_id is not None:
            self.sim_pool_id = sim_pool_id
        if imei is not None:
            self.imei = imei
        if sim_status is not None:
            self.sim_status = sim_status
        if device_status is not None:
            self.device_status = device_status
        if device_model is not None:
            self.device_model = device_model
        if act_date is not None:
            self.act_date = act_date
        if device_status_date is not None:
            self.device_status_date = device_status_date
        if node_id is not None:
            self.node_id = node_id
        if iccid is not None:
            self.iccid = iccid
        if network_type is not None:
            self.network_type = network_type
        if dbm is not None:
            self.dbm = dbm
        if signal_level is not None:
            self.signal_level = signal_level
        if sim_type is not None:
            self.sim_type = sim_type
        if tag_names is not None:
            self.tag_names = tag_names
        if order_id is not None:
            self.order_id = order_id
        if expire_time is not None:
            self.expire_time = expire_time
        if price_plan_name is not None:
            self.price_plan_name = price_plan_name
        if sim_price_plan_id is not None:
            self.sim_price_plan_id = sim_price_plan_id
        if flow_left is not None:
            self.flow_left = flow_left
        if flow_used is not None:
            self.flow_used = flow_used
        if operator_status is not None:
            self.operator_status = operator_status
        if msisdn is not None:
            self.msisdn = msisdn
        if imsi is not None:
            self.imsi = imsi
        if customer_attribute1 is not None:
            self.customer_attribute1 = customer_attribute1
        if customer_attribute2 is not None:
            self.customer_attribute2 = customer_attribute2
        if customer_attribute3 is not None:
            self.customer_attribute3 = customer_attribute3
        if customer_attribute4 is not None:
            self.customer_attribute4 = customer_attribute4
        if customer_attribute5 is not None:
            self.customer_attribute5 = customer_attribute5
        if customer_attribute6 is not None:
            self.customer_attribute6 = customer_attribute6
        if real_named is not None:
            self.real_named = real_named
        if cut_net_flag is not None:
            self.cut_net_flag = cut_net_flag
        if exceed_cut_net_flag is not None:
            self.exceed_cut_net_flag = exceed_cut_net_flag
        if exceed_cut_net_quota is not None:
            self.exceed_cut_net_quota = exceed_cut_net_quota
        if imei_bind_remain_times is not None:
            self.imei_bind_remain_times = imei_bind_remain_times
        if speed_value is not None:
            self.speed_value = speed_value

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this SimDeviceVO.

        sim卡id

        :return: The sim_card_id of this SimDeviceVO.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this SimDeviceVO.

        sim卡id

        :param sim_card_id: The sim_card_id of this SimDeviceVO.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def account_id(self):
        """Gets the account_id of this SimDeviceVO.

        账户id

        :return: The account_id of this SimDeviceVO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SimDeviceVO.

        账户id

        :param account_id: The account_id of this SimDeviceVO.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def cid(self):
        """Gets the cid of this SimDeviceVO.

        容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)

        :return: The cid of this SimDeviceVO.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this SimDeviceVO.

        容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)

        :param cid: The cid of this SimDeviceVO.
        :type cid: str
        """
        self._cid = cid

    @property
    def sim_pool_id(self):
        """Gets the sim_pool_id of this SimDeviceVO.

        流量池ID

        :return: The sim_pool_id of this SimDeviceVO.
        :rtype: int
        """
        return self._sim_pool_id

    @sim_pool_id.setter
    def sim_pool_id(self, sim_pool_id):
        """Sets the sim_pool_id of this SimDeviceVO.

        流量池ID

        :param sim_pool_id: The sim_pool_id of this SimDeviceVO.
        :type sim_pool_id: int
        """
        self._sim_pool_id = sim_pool_id

    @property
    def imei(self):
        """Gets the imei of this SimDeviceVO.

        设备IMEI

        :return: The imei of this SimDeviceVO.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this SimDeviceVO.

        设备IMEI

        :param imei: The imei of this SimDeviceVO.
        :type imei: str
        """
        self._imei = imei

    @property
    def sim_status(self):
        """Gets the sim_status of this SimDeviceVO.

        sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机

        :return: The sim_status of this SimDeviceVO.
        :rtype: int
        """
        return self._sim_status

    @sim_status.setter
    def sim_status(self, sim_status):
        """Sets the sim_status of this SimDeviceVO.

        sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机

        :param sim_status: The sim_status of this SimDeviceVO.
        :type sim_status: int
        """
        self._sim_status = sim_status

    @property
    def device_status(self):
        """Gets the device_status of this SimDeviceVO.

        设备状态

        :return: The device_status of this SimDeviceVO.
        :rtype: int
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """Sets the device_status of this SimDeviceVO.

        设备状态

        :param device_status: The device_status of this SimDeviceVO.
        :type device_status: int
        """
        self._device_status = device_status

    @property
    def device_model(self):
        """Gets the device_model of this SimDeviceVO.

        设备模组

        :return: The device_model of this SimDeviceVO.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this SimDeviceVO.

        设备模组

        :param device_model: The device_model of this SimDeviceVO.
        :type device_model: str
        """
        self._device_model = device_model

    @property
    def act_date(self):
        """Gets the act_date of this SimDeviceVO.

        激活日期 例如2020-01-31T16:00:00.000Z

        :return: The act_date of this SimDeviceVO.
        :rtype: datetime
        """
        return self._act_date

    @act_date.setter
    def act_date(self, act_date):
        """Sets the act_date of this SimDeviceVO.

        激活日期 例如2020-01-31T16:00:00.000Z

        :param act_date: The act_date of this SimDeviceVO.
        :type act_date: datetime
        """
        self._act_date = act_date

    @property
    def device_status_date(self):
        """Gets the device_status_date of this SimDeviceVO.

        设备状态变更时间 例如2020-01-31T16:00:00.000Z

        :return: The device_status_date of this SimDeviceVO.
        :rtype: datetime
        """
        return self._device_status_date

    @device_status_date.setter
    def device_status_date(self, device_status_date):
        """Sets the device_status_date of this SimDeviceVO.

        设备状态变更时间 例如2020-01-31T16:00:00.000Z

        :param device_status_date: The device_status_date of this SimDeviceVO.
        :type device_status_date: datetime
        """
        self._device_status_date = device_status_date

    @property
    def node_id(self):
        """Gets the node_id of this SimDeviceVO.

        设备标识

        :return: The node_id of this SimDeviceVO.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SimDeviceVO.

        设备标识

        :param node_id: The node_id of this SimDeviceVO.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def iccid(self):
        """Gets the iccid of this SimDeviceVO.

        码号iccid

        :return: The iccid of this SimDeviceVO.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this SimDeviceVO.

        码号iccid

        :param iccid: The iccid of this SimDeviceVO.
        :type iccid: str
        """
        self._iccid = iccid

    @property
    def network_type(self):
        """Gets the network_type of this SimDeviceVO.

        网络类型

        :return: The network_type of this SimDeviceVO.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this SimDeviceVO.

        网络类型

        :param network_type: The network_type of this SimDeviceVO.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def dbm(self):
        """Gets the dbm of this SimDeviceVO.

        信号强度

        :return: The dbm of this SimDeviceVO.
        :rtype: str
        """
        return self._dbm

    @dbm.setter
    def dbm(self, dbm):
        """Sets the dbm of this SimDeviceVO.

        信号强度

        :param dbm: The dbm of this SimDeviceVO.
        :type dbm: str
        """
        self._dbm = dbm

    @property
    def signal_level(self):
        """Gets the signal_level of this SimDeviceVO.

        信号等级:1.差  2.良  3.良 4.优（该参数只有eSIM,vSIM返回，实体卡不返回）

        :return: The signal_level of this SimDeviceVO.
        :rtype: str
        """
        return self._signal_level

    @signal_level.setter
    def signal_level(self, signal_level):
        """Sets the signal_level of this SimDeviceVO.

        信号等级:1.差  2.良  3.良 4.优（该参数只有eSIM,vSIM返回，实体卡不返回）

        :param signal_level: The signal_level of this SimDeviceVO.
        :type signal_level: str
        """
        self._signal_level = signal_level

    @property
    def sim_type(self):
        """Gets the sim_type of this SimDeviceVO.

        sim卡类型 1.vSIM  2.eSIM  3.实体卡

        :return: The sim_type of this SimDeviceVO.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this SimDeviceVO.

        sim卡类型 1.vSIM  2.eSIM  3.实体卡

        :param sim_type: The sim_type of this SimDeviceVO.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def tag_names(self):
        """Gets the tag_names of this SimDeviceVO.

        标签名

        :return: The tag_names of this SimDeviceVO.
        :rtype: str
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this SimDeviceVO.

        标签名

        :param tag_names: The tag_names of this SimDeviceVO.
        :type tag_names: str
        """
        self._tag_names = tag_names

    @property
    def order_id(self):
        """Gets the order_id of this SimDeviceVO.

        批次号

        :return: The order_id of this SimDeviceVO.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SimDeviceVO.

        批次号

        :param order_id: The order_id of this SimDeviceVO.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def expire_time(self):
        """Gets the expire_time of this SimDeviceVO.

        到期时间 例如2021-06-30T00:00:00.000Z

        :return: The expire_time of this SimDeviceVO.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this SimDeviceVO.

        到期时间 例如2021-06-30T00:00:00.000Z

        :param expire_time: The expire_time of this SimDeviceVO.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def price_plan_name(self):
        """Gets the price_plan_name of this SimDeviceVO.

        在用套餐名

        :return: The price_plan_name of this SimDeviceVO.
        :rtype: str
        """
        return self._price_plan_name

    @price_plan_name.setter
    def price_plan_name(self, price_plan_name):
        """Sets the price_plan_name of this SimDeviceVO.

        在用套餐名

        :param price_plan_name: The price_plan_name of this SimDeviceVO.
        :type price_plan_name: str
        """
        self._price_plan_name = price_plan_name

    @property
    def sim_price_plan_id(self):
        """Gets the sim_price_plan_id of this SimDeviceVO.

        套餐订购实例ID

        :return: The sim_price_plan_id of this SimDeviceVO.
        :rtype: int
        """
        return self._sim_price_plan_id

    @sim_price_plan_id.setter
    def sim_price_plan_id(self, sim_price_plan_id):
        """Sets the sim_price_plan_id of this SimDeviceVO.

        套餐订购实例ID

        :param sim_price_plan_id: The sim_price_plan_id of this SimDeviceVO.
        :type sim_price_plan_id: int
        """
        self._sim_price_plan_id = sim_price_plan_id

    @property
    def flow_left(self):
        """Gets the flow_left of this SimDeviceVO.

        剩余流量(单位M)，数据默认截止到昨日24点。

        :return: The flow_left of this SimDeviceVO.
        :rtype: float
        """
        return self._flow_left

    @flow_left.setter
    def flow_left(self, flow_left):
        """Sets the flow_left of this SimDeviceVO.

        剩余流量(单位M)，数据默认截止到昨日24点。

        :param flow_left: The flow_left of this SimDeviceVO.
        :type flow_left: float
        """
        self._flow_left = flow_left

    @property
    def flow_used(self):
        """Gets the flow_used of this SimDeviceVO.

        已用流量(单位M)，数据默认截止到昨日24点。

        :return: The flow_used of this SimDeviceVO.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        """Sets the flow_used of this SimDeviceVO.

        已用流量(单位M)，数据默认截止到昨日24点。

        :param flow_used: The flow_used of this SimDeviceVO.
        :type flow_used: float
        """
        self._flow_used = flow_used

    @property
    def operator_status(self):
        """Gets the operator_status of this SimDeviceVO.

        运营商状态 -1.正常（非停机状态） 1.停机（超流量停机） 2.停机（超流量阈值停机） 3.停机（流量池停机） 4.停机（套餐到期停机） 5.停机（主动停机） 6.停机（违规停机） 7.停机（机卡分离停机）

        :return: The operator_status of this SimDeviceVO.
        :rtype: int
        """
        return self._operator_status

    @operator_status.setter
    def operator_status(self, operator_status):
        """Sets the operator_status of this SimDeviceVO.

        运营商状态 -1.正常（非停机状态） 1.停机（超流量停机） 2.停机（超流量阈值停机） 3.停机（流量池停机） 4.停机（套餐到期停机） 5.停机（主动停机） 6.停机（违规停机） 7.停机（机卡分离停机）

        :param operator_status: The operator_status of this SimDeviceVO.
        :type operator_status: int
        """
        self._operator_status = operator_status

    @property
    def msisdn(self):
        """Gets the msisdn of this SimDeviceVO.

        MSISDN

        :return: The msisdn of this SimDeviceVO.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        """Sets the msisdn of this SimDeviceVO.

        MSISDN

        :param msisdn: The msisdn of this SimDeviceVO.
        :type msisdn: str
        """
        self._msisdn = msisdn

    @property
    def imsi(self):
        """Gets the imsi of this SimDeviceVO.

        IMSI

        :return: The imsi of this SimDeviceVO.
        :rtype: str
        """
        return self._imsi

    @imsi.setter
    def imsi(self, imsi):
        """Sets the imsi of this SimDeviceVO.

        IMSI

        :param imsi: The imsi of this SimDeviceVO.
        :type imsi: str
        """
        self._imsi = imsi

    @property
    def customer_attribute1(self):
        """Gets the customer_attribute1 of this SimDeviceVO.

        自定义属性一

        :return: The customer_attribute1 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute1

    @customer_attribute1.setter
    def customer_attribute1(self, customer_attribute1):
        """Sets the customer_attribute1 of this SimDeviceVO.

        自定义属性一

        :param customer_attribute1: The customer_attribute1 of this SimDeviceVO.
        :type customer_attribute1: str
        """
        self._customer_attribute1 = customer_attribute1

    @property
    def customer_attribute2(self):
        """Gets the customer_attribute2 of this SimDeviceVO.

        自定义属性二

        :return: The customer_attribute2 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute2

    @customer_attribute2.setter
    def customer_attribute2(self, customer_attribute2):
        """Sets the customer_attribute2 of this SimDeviceVO.

        自定义属性二

        :param customer_attribute2: The customer_attribute2 of this SimDeviceVO.
        :type customer_attribute2: str
        """
        self._customer_attribute2 = customer_attribute2

    @property
    def customer_attribute3(self):
        """Gets the customer_attribute3 of this SimDeviceVO.

        自定义属性三

        :return: The customer_attribute3 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute3

    @customer_attribute3.setter
    def customer_attribute3(self, customer_attribute3):
        """Sets the customer_attribute3 of this SimDeviceVO.

        自定义属性三

        :param customer_attribute3: The customer_attribute3 of this SimDeviceVO.
        :type customer_attribute3: str
        """
        self._customer_attribute3 = customer_attribute3

    @property
    def customer_attribute4(self):
        """Gets the customer_attribute4 of this SimDeviceVO.

        自定义属性四

        :return: The customer_attribute4 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute4

    @customer_attribute4.setter
    def customer_attribute4(self, customer_attribute4):
        """Sets the customer_attribute4 of this SimDeviceVO.

        自定义属性四

        :param customer_attribute4: The customer_attribute4 of this SimDeviceVO.
        :type customer_attribute4: str
        """
        self._customer_attribute4 = customer_attribute4

    @property
    def customer_attribute5(self):
        """Gets the customer_attribute5 of this SimDeviceVO.

        自定义属性五

        :return: The customer_attribute5 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute5

    @customer_attribute5.setter
    def customer_attribute5(self, customer_attribute5):
        """Sets the customer_attribute5 of this SimDeviceVO.

        自定义属性五

        :param customer_attribute5: The customer_attribute5 of this SimDeviceVO.
        :type customer_attribute5: str
        """
        self._customer_attribute5 = customer_attribute5

    @property
    def customer_attribute6(self):
        """Gets the customer_attribute6 of this SimDeviceVO.

        自定义属性六

        :return: The customer_attribute6 of this SimDeviceVO.
        :rtype: str
        """
        return self._customer_attribute6

    @customer_attribute6.setter
    def customer_attribute6(self, customer_attribute6):
        """Sets the customer_attribute6 of this SimDeviceVO.

        自定义属性六

        :param customer_attribute6: The customer_attribute6 of this SimDeviceVO.
        :type customer_attribute6: str
        """
        self._customer_attribute6 = customer_attribute6

    @property
    def real_named(self):
        """Gets the real_named of this SimDeviceVO.

        是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。

        :return: The real_named of this SimDeviceVO.
        :rtype: bool
        """
        return self._real_named

    @real_named.setter
    def real_named(self, real_named):
        """Sets the real_named of this SimDeviceVO.

        是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。

        :param real_named: The real_named of this SimDeviceVO.
        :type real_named: bool
        """
        self._real_named = real_named

    @property
    def cut_net_flag(self):
        """Gets the cut_net_flag of this SimDeviceVO.

        是否单独断网 true:断网，false:未断网 （当前只支持联通、移动的组池卡，电信卡不限制）

        :return: The cut_net_flag of this SimDeviceVO.
        :rtype: bool
        """
        return self._cut_net_flag

    @cut_net_flag.setter
    def cut_net_flag(self, cut_net_flag):
        """Sets the cut_net_flag of this SimDeviceVO.

        是否单独断网 true:断网，false:未断网 （当前只支持联通、移动的组池卡，电信卡不限制）

        :param cut_net_flag: The cut_net_flag of this SimDeviceVO.
        :type cut_net_flag: bool
        """
        self._cut_net_flag = cut_net_flag

    @property
    def exceed_cut_net_flag(self):
        """Gets the exceed_cut_net_flag of this SimDeviceVO.

        是否达量断网 true:达量断网，false:未达量断网 （当前只支持联通、移动的组池卡，电信卡不限制）

        :return: The exceed_cut_net_flag of this SimDeviceVO.
        :rtype: bool
        """
        return self._exceed_cut_net_flag

    @exceed_cut_net_flag.setter
    def exceed_cut_net_flag(self, exceed_cut_net_flag):
        """Sets the exceed_cut_net_flag of this SimDeviceVO.

        是否达量断网 true:达量断网，false:未达量断网 （当前只支持联通、移动的组池卡，电信卡不限制）

        :param exceed_cut_net_flag: The exceed_cut_net_flag of this SimDeviceVO.
        :type exceed_cut_net_flag: bool
        """
        self._exceed_cut_net_flag = exceed_cut_net_flag

    @property
    def exceed_cut_net_quota(self):
        """Gets the exceed_cut_net_quota of this SimDeviceVO.

        达量断网阈值（单位MB 当前仅电信卡支持）

        :return: The exceed_cut_net_quota of this SimDeviceVO.
        :rtype: int
        """
        return self._exceed_cut_net_quota

    @exceed_cut_net_quota.setter
    def exceed_cut_net_quota(self, exceed_cut_net_quota):
        """Sets the exceed_cut_net_quota of this SimDeviceVO.

        达量断网阈值（单位MB 当前仅电信卡支持）

        :param exceed_cut_net_quota: The exceed_cut_net_quota of this SimDeviceVO.
        :type exceed_cut_net_quota: int
        """
        self._exceed_cut_net_quota = exceed_cut_net_quota

    @property
    def imei_bind_remain_times(self):
        """Gets the imei_bind_remain_times of this SimDeviceVO.

        本月机卡绑定剩余次数（当前仅电信卡支持）

        :return: The imei_bind_remain_times of this SimDeviceVO.
        :rtype: int
        """
        return self._imei_bind_remain_times

    @imei_bind_remain_times.setter
    def imei_bind_remain_times(self, imei_bind_remain_times):
        """Sets the imei_bind_remain_times of this SimDeviceVO.

        本月机卡绑定剩余次数（当前仅电信卡支持）

        :param imei_bind_remain_times: The imei_bind_remain_times of this SimDeviceVO.
        :type imei_bind_remain_times: int
        """
        self._imei_bind_remain_times = imei_bind_remain_times

    @property
    def speed_value(self):
        """Gets the speed_value of this SimDeviceVO.

        网络限制速率（单位Kbps,当前电信联通卡支持）

        :return: The speed_value of this SimDeviceVO.
        :rtype: int
        """
        return self._speed_value

    @speed_value.setter
    def speed_value(self, speed_value):
        """Sets the speed_value of this SimDeviceVO.

        网络限制速率（单位Kbps,当前电信联通卡支持）

        :param speed_value: The speed_value of this SimDeviceVO.
        :type speed_value: int
        """
        self._speed_value = speed_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimDeviceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
