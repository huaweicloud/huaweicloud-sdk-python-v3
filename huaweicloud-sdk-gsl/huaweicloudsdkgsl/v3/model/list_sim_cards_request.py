# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimCardsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_search_type': 'int',
        'main_search_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'sim_status': 'int',
        'device_status': 'int',
        'tag_id': 'list[int]',
        'sim_type': 'int',
        'order': 'str',
        'sort': 'str',
        'msisdn': 'str',
        'customer_attribute1': 'str',
        'customer_attribute2': 'str',
        'customer_attribute3': 'str',
        'customer_attribute4': 'str',
        'customer_attribute5': 'str',
        'customer_attribute6': 'str',
        'min_used_flow': 'int',
        'max_used_flow': 'int',
        'min_left_flow': 'int',
        'max_left_flow': 'int',
        'real_named': 'bool',
        'order_id': 'int',
        'filter_downtime_period': 'bool',
        'order_ids': 'list[int]',
        'price_plan_id': 'list[str]'
    }

    attribute_map = {
        'main_search_type': 'main_search_type',
        'main_search_key': 'main_search_key',
        'limit': 'limit',
        'offset': 'offset',
        'sim_status': 'sim_status',
        'device_status': 'device_status',
        'tag_id': 'tag_id',
        'sim_type': 'sim_type',
        'order': 'order',
        'sort': 'sort',
        'msisdn': 'msisdn',
        'customer_attribute1': 'customer_attribute1',
        'customer_attribute2': 'customer_attribute2',
        'customer_attribute3': 'customer_attribute3',
        'customer_attribute4': 'customer_attribute4',
        'customer_attribute5': 'customer_attribute5',
        'customer_attribute6': 'customer_attribute6',
        'min_used_flow': 'min_used_flow',
        'max_used_flow': 'max_used_flow',
        'min_left_flow': 'min_left_flow',
        'max_left_flow': 'max_left_flow',
        'real_named': 'real_named',
        'order_id': 'order_id',
        'filter_downtime_period': 'filter_downtime_period',
        'order_ids': 'order_ids',
        'price_plan_id': 'price_plan_id'
    }

    def __init__(self, main_search_type=None, main_search_key=None, limit=None, offset=None, sim_status=None, device_status=None, tag_id=None, sim_type=None, order=None, sort=None, msisdn=None, customer_attribute1=None, customer_attribute2=None, customer_attribute3=None, customer_attribute4=None, customer_attribute5=None, customer_attribute6=None, min_used_flow=None, max_used_flow=None, min_left_flow=None, max_left_flow=None, real_named=None, order_id=None, filter_downtime_period=None, order_ids=None, price_plan_id=None):
        """ListSimCardsRequest

        The model defined in huaweicloud sdk

        :param main_search_type: 查询关键标识类型： 1.容器ID(不同类型卡含义如下:ICCID(实体卡)，EID（eSIM）CID（vSIM)) 2.批次号 3.设备IMEI
        :type main_search_type: int
        :param main_search_key: 查询关键标识值：根据查询关键标识类型进行查询，例如想根据ICCID&#x3D;xxx进行查询，则main_search_type&#x3D;1&amp;main_search_key&#x3D;xxx
        :type main_search_key: str
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        :param sim_status: sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机
        :type sim_status: int
        :param device_status: 设备状态: 1.注册 2.重启 3.在线 4.离线
        :type device_status: int
        :param tag_id: 标签ID，最多支持传10个
        :type tag_id: list[int]
        :param sim_type: sim卡类型：  1.vSIM  2.eSIM  3.实体卡
        :type sim_type: int
        :param order: 排序的顺序，asc表示顺序排序，desc表示倒序排序，不传则默认asc
        :type order: str
        :param sort: 排序的属性，目前支持:cid（容器ID）、flow_used（已用流量）、flow_left（剩余流量）、act_date（激活时间）、expire_time（到期时间）
        :type sort: str
        :param msisdn: MSISDN
        :type msisdn: str
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
        :param min_used_flow: 最小使用流量(MB)
        :type min_used_flow: int
        :param max_used_flow: 最大使用流量(MB)
        :type max_used_flow: int
        :param min_left_flow: 最小剩余流量(MB)
        :type min_left_flow: int
        :param max_left_flow: 最大剩余流量(MB)
        :type max_left_flow: int
        :param real_named: 是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。
        :type real_named: bool
        :param order_id: 订单号
        :type order_id: int
        :param filter_downtime_period: 是否过滤停机保号的卡
        :type filter_downtime_period: bool
        :param order_ids: 订单批次号集合
        :type order_ids: list[int]
        :param price_plan_id: 套餐id集合，最多支持传30个
        :type price_plan_id: list[str]
        """
        
        

        self._main_search_type = None
        self._main_search_key = None
        self._limit = None
        self._offset = None
        self._sim_status = None
        self._device_status = None
        self._tag_id = None
        self._sim_type = None
        self._order = None
        self._sort = None
        self._msisdn = None
        self._customer_attribute1 = None
        self._customer_attribute2 = None
        self._customer_attribute3 = None
        self._customer_attribute4 = None
        self._customer_attribute5 = None
        self._customer_attribute6 = None
        self._min_used_flow = None
        self._max_used_flow = None
        self._min_left_flow = None
        self._max_left_flow = None
        self._real_named = None
        self._order_id = None
        self._filter_downtime_period = None
        self._order_ids = None
        self._price_plan_id = None
        self.discriminator = None

        if main_search_type is not None:
            self.main_search_type = main_search_type
        if main_search_key is not None:
            self.main_search_key = main_search_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sim_status is not None:
            self.sim_status = sim_status
        if device_status is not None:
            self.device_status = device_status
        if tag_id is not None:
            self.tag_id = tag_id
        if sim_type is not None:
            self.sim_type = sim_type
        if order is not None:
            self.order = order
        if sort is not None:
            self.sort = sort
        if msisdn is not None:
            self.msisdn = msisdn
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
        if min_used_flow is not None:
            self.min_used_flow = min_used_flow
        if max_used_flow is not None:
            self.max_used_flow = max_used_flow
        if min_left_flow is not None:
            self.min_left_flow = min_left_flow
        if max_left_flow is not None:
            self.max_left_flow = max_left_flow
        if real_named is not None:
            self.real_named = real_named
        if order_id is not None:
            self.order_id = order_id
        if filter_downtime_period is not None:
            self.filter_downtime_period = filter_downtime_period
        if order_ids is not None:
            self.order_ids = order_ids
        if price_plan_id is not None:
            self.price_plan_id = price_plan_id

    @property
    def main_search_type(self):
        """Gets the main_search_type of this ListSimCardsRequest.

        查询关键标识类型： 1.容器ID(不同类型卡含义如下:ICCID(实体卡)，EID（eSIM）CID（vSIM)) 2.批次号 3.设备IMEI

        :return: The main_search_type of this ListSimCardsRequest.
        :rtype: int
        """
        return self._main_search_type

    @main_search_type.setter
    def main_search_type(self, main_search_type):
        """Sets the main_search_type of this ListSimCardsRequest.

        查询关键标识类型： 1.容器ID(不同类型卡含义如下:ICCID(实体卡)，EID（eSIM）CID（vSIM)) 2.批次号 3.设备IMEI

        :param main_search_type: The main_search_type of this ListSimCardsRequest.
        :type main_search_type: int
        """
        self._main_search_type = main_search_type

    @property
    def main_search_key(self):
        """Gets the main_search_key of this ListSimCardsRequest.

        查询关键标识值：根据查询关键标识类型进行查询，例如想根据ICCID=xxx进行查询，则main_search_type=1&main_search_key=xxx

        :return: The main_search_key of this ListSimCardsRequest.
        :rtype: str
        """
        return self._main_search_key

    @main_search_key.setter
    def main_search_key(self, main_search_key):
        """Sets the main_search_key of this ListSimCardsRequest.

        查询关键标识值：根据查询关键标识类型进行查询，例如想根据ICCID=xxx进行查询，则main_search_type=1&main_search_key=xxx

        :param main_search_key: The main_search_key of this ListSimCardsRequest.
        :type main_search_key: str
        """
        self._main_search_key = main_search_key

    @property
    def limit(self):
        """Gets the limit of this ListSimCardsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListSimCardsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSimCardsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListSimCardsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSimCardsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListSimCardsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSimCardsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListSimCardsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sim_status(self):
        """Gets the sim_status of this ListSimCardsRequest.

        sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机

        :return: The sim_status of this ListSimCardsRequest.
        :rtype: int
        """
        return self._sim_status

    @sim_status.setter
    def sim_status(self, sim_status):
        """Sets the sim_status of this ListSimCardsRequest.

        sim卡状态：  10.可测试  11.未激活  13.可激活  14.已停用  20.在用  30.已拆机

        :param sim_status: The sim_status of this ListSimCardsRequest.
        :type sim_status: int
        """
        self._sim_status = sim_status

    @property
    def device_status(self):
        """Gets the device_status of this ListSimCardsRequest.

        设备状态: 1.注册 2.重启 3.在线 4.离线

        :return: The device_status of this ListSimCardsRequest.
        :rtype: int
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """Sets the device_status of this ListSimCardsRequest.

        设备状态: 1.注册 2.重启 3.在线 4.离线

        :param device_status: The device_status of this ListSimCardsRequest.
        :type device_status: int
        """
        self._device_status = device_status

    @property
    def tag_id(self):
        """Gets the tag_id of this ListSimCardsRequest.

        标签ID，最多支持传10个

        :return: The tag_id of this ListSimCardsRequest.
        :rtype: list[int]
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ListSimCardsRequest.

        标签ID，最多支持传10个

        :param tag_id: The tag_id of this ListSimCardsRequest.
        :type tag_id: list[int]
        """
        self._tag_id = tag_id

    @property
    def sim_type(self):
        """Gets the sim_type of this ListSimCardsRequest.

        sim卡类型：  1.vSIM  2.eSIM  3.实体卡

        :return: The sim_type of this ListSimCardsRequest.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this ListSimCardsRequest.

        sim卡类型：  1.vSIM  2.eSIM  3.实体卡

        :param sim_type: The sim_type of this ListSimCardsRequest.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def order(self):
        """Gets the order of this ListSimCardsRequest.

        排序的顺序，asc表示顺序排序，desc表示倒序排序，不传则默认asc

        :return: The order of this ListSimCardsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListSimCardsRequest.

        排序的顺序，asc表示顺序排序，desc表示倒序排序，不传则默认asc

        :param order: The order of this ListSimCardsRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort(self):
        """Gets the sort of this ListSimCardsRequest.

        排序的属性，目前支持:cid（容器ID）、flow_used（已用流量）、flow_left（剩余流量）、act_date（激活时间）、expire_time（到期时间）

        :return: The sort of this ListSimCardsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListSimCardsRequest.

        排序的属性，目前支持:cid（容器ID）、flow_used（已用流量）、flow_left（剩余流量）、act_date（激活时间）、expire_time（到期时间）

        :param sort: The sort of this ListSimCardsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def msisdn(self):
        """Gets the msisdn of this ListSimCardsRequest.

        MSISDN

        :return: The msisdn of this ListSimCardsRequest.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        """Sets the msisdn of this ListSimCardsRequest.

        MSISDN

        :param msisdn: The msisdn of this ListSimCardsRequest.
        :type msisdn: str
        """
        self._msisdn = msisdn

    @property
    def customer_attribute1(self):
        """Gets the customer_attribute1 of this ListSimCardsRequest.

        自定义属性一

        :return: The customer_attribute1 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute1

    @customer_attribute1.setter
    def customer_attribute1(self, customer_attribute1):
        """Sets the customer_attribute1 of this ListSimCardsRequest.

        自定义属性一

        :param customer_attribute1: The customer_attribute1 of this ListSimCardsRequest.
        :type customer_attribute1: str
        """
        self._customer_attribute1 = customer_attribute1

    @property
    def customer_attribute2(self):
        """Gets the customer_attribute2 of this ListSimCardsRequest.

        自定义属性二

        :return: The customer_attribute2 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute2

    @customer_attribute2.setter
    def customer_attribute2(self, customer_attribute2):
        """Sets the customer_attribute2 of this ListSimCardsRequest.

        自定义属性二

        :param customer_attribute2: The customer_attribute2 of this ListSimCardsRequest.
        :type customer_attribute2: str
        """
        self._customer_attribute2 = customer_attribute2

    @property
    def customer_attribute3(self):
        """Gets the customer_attribute3 of this ListSimCardsRequest.

        自定义属性三

        :return: The customer_attribute3 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute3

    @customer_attribute3.setter
    def customer_attribute3(self, customer_attribute3):
        """Sets the customer_attribute3 of this ListSimCardsRequest.

        自定义属性三

        :param customer_attribute3: The customer_attribute3 of this ListSimCardsRequest.
        :type customer_attribute3: str
        """
        self._customer_attribute3 = customer_attribute3

    @property
    def customer_attribute4(self):
        """Gets the customer_attribute4 of this ListSimCardsRequest.

        自定义属性四

        :return: The customer_attribute4 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute4

    @customer_attribute4.setter
    def customer_attribute4(self, customer_attribute4):
        """Sets the customer_attribute4 of this ListSimCardsRequest.

        自定义属性四

        :param customer_attribute4: The customer_attribute4 of this ListSimCardsRequest.
        :type customer_attribute4: str
        """
        self._customer_attribute4 = customer_attribute4

    @property
    def customer_attribute5(self):
        """Gets the customer_attribute5 of this ListSimCardsRequest.

        自定义属性五

        :return: The customer_attribute5 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute5

    @customer_attribute5.setter
    def customer_attribute5(self, customer_attribute5):
        """Sets the customer_attribute5 of this ListSimCardsRequest.

        自定义属性五

        :param customer_attribute5: The customer_attribute5 of this ListSimCardsRequest.
        :type customer_attribute5: str
        """
        self._customer_attribute5 = customer_attribute5

    @property
    def customer_attribute6(self):
        """Gets the customer_attribute6 of this ListSimCardsRequest.

        自定义属性六

        :return: The customer_attribute6 of this ListSimCardsRequest.
        :rtype: str
        """
        return self._customer_attribute6

    @customer_attribute6.setter
    def customer_attribute6(self, customer_attribute6):
        """Sets the customer_attribute6 of this ListSimCardsRequest.

        自定义属性六

        :param customer_attribute6: The customer_attribute6 of this ListSimCardsRequest.
        :type customer_attribute6: str
        """
        self._customer_attribute6 = customer_attribute6

    @property
    def min_used_flow(self):
        """Gets the min_used_flow of this ListSimCardsRequest.

        最小使用流量(MB)

        :return: The min_used_flow of this ListSimCardsRequest.
        :rtype: int
        """
        return self._min_used_flow

    @min_used_flow.setter
    def min_used_flow(self, min_used_flow):
        """Sets the min_used_flow of this ListSimCardsRequest.

        最小使用流量(MB)

        :param min_used_flow: The min_used_flow of this ListSimCardsRequest.
        :type min_used_flow: int
        """
        self._min_used_flow = min_used_flow

    @property
    def max_used_flow(self):
        """Gets the max_used_flow of this ListSimCardsRequest.

        最大使用流量(MB)

        :return: The max_used_flow of this ListSimCardsRequest.
        :rtype: int
        """
        return self._max_used_flow

    @max_used_flow.setter
    def max_used_flow(self, max_used_flow):
        """Sets the max_used_flow of this ListSimCardsRequest.

        最大使用流量(MB)

        :param max_used_flow: The max_used_flow of this ListSimCardsRequest.
        :type max_used_flow: int
        """
        self._max_used_flow = max_used_flow

    @property
    def min_left_flow(self):
        """Gets the min_left_flow of this ListSimCardsRequest.

        最小剩余流量(MB)

        :return: The min_left_flow of this ListSimCardsRequest.
        :rtype: int
        """
        return self._min_left_flow

    @min_left_flow.setter
    def min_left_flow(self, min_left_flow):
        """Sets the min_left_flow of this ListSimCardsRequest.

        最小剩余流量(MB)

        :param min_left_flow: The min_left_flow of this ListSimCardsRequest.
        :type min_left_flow: int
        """
        self._min_left_flow = min_left_flow

    @property
    def max_left_flow(self):
        """Gets the max_left_flow of this ListSimCardsRequest.

        最大剩余流量(MB)

        :return: The max_left_flow of this ListSimCardsRequest.
        :rtype: int
        """
        return self._max_left_flow

    @max_left_flow.setter
    def max_left_flow(self, max_left_flow):
        """Sets the max_left_flow of this ListSimCardsRequest.

        最大剩余流量(MB)

        :param max_left_flow: The max_left_flow of this ListSimCardsRequest.
        :type max_left_flow: int
        """
        self._max_left_flow = max_left_flow

    @property
    def real_named(self):
        """Gets the real_named of this ListSimCardsRequest.

        是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。

        :return: The real_named of this ListSimCardsRequest.
        :rtype: bool
        """
        return self._real_named

    @real_named.setter
    def real_named(self, real_named):
        """Sets the real_named of this ListSimCardsRequest.

        是否已实名认证: true表示是，false表示否，系统SIM卡实名认证状态非实时。

        :param real_named: The real_named of this ListSimCardsRequest.
        :type real_named: bool
        """
        self._real_named = real_named

    @property
    def order_id(self):
        """Gets the order_id of this ListSimCardsRequest.

        订单号

        :return: The order_id of this ListSimCardsRequest.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListSimCardsRequest.

        订单号

        :param order_id: The order_id of this ListSimCardsRequest.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def filter_downtime_period(self):
        """Gets the filter_downtime_period of this ListSimCardsRequest.

        是否过滤停机保号的卡

        :return: The filter_downtime_period of this ListSimCardsRequest.
        :rtype: bool
        """
        return self._filter_downtime_period

    @filter_downtime_period.setter
    def filter_downtime_period(self, filter_downtime_period):
        """Sets the filter_downtime_period of this ListSimCardsRequest.

        是否过滤停机保号的卡

        :param filter_downtime_period: The filter_downtime_period of this ListSimCardsRequest.
        :type filter_downtime_period: bool
        """
        self._filter_downtime_period = filter_downtime_period

    @property
    def order_ids(self):
        """Gets the order_ids of this ListSimCardsRequest.

        订单批次号集合

        :return: The order_ids of this ListSimCardsRequest.
        :rtype: list[int]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this ListSimCardsRequest.

        订单批次号集合

        :param order_ids: The order_ids of this ListSimCardsRequest.
        :type order_ids: list[int]
        """
        self._order_ids = order_ids

    @property
    def price_plan_id(self):
        """Gets the price_plan_id of this ListSimCardsRequest.

        套餐id集合，最多支持传30个

        :return: The price_plan_id of this ListSimCardsRequest.
        :rtype: list[str]
        """
        return self._price_plan_id

    @price_plan_id.setter
    def price_plan_id(self, price_plan_id):
        """Sets the price_plan_id of this ListSimCardsRequest.

        套餐id集合，最多支持传30个

        :param price_plan_id: The price_plan_id of this ListSimCardsRequest.
        :type price_plan_id: list[str]
        """
        self._price_plan_id = price_plan_id

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
        if not isinstance(other, ListSimCardsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
