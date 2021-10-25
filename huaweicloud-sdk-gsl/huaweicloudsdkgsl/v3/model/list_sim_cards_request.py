# coding: utf-8

import re
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
        'real_named': 'bool'
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
        'real_named': 'real_named'
    }

    def __init__(self, main_search_type=None, main_search_key=None, limit=None, offset=None, sim_status=None, device_status=None, tag_id=None, sim_type=None, order=None, sort=None, msisdn=None, customer_attribute1=None, customer_attribute2=None, customer_attribute3=None, customer_attribute4=None, customer_attribute5=None, customer_attribute6=None, real_named=None):
        """ListSimCardsRequest - a model defined in huaweicloud sdk"""
        
        

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
        self._real_named = None
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
        if real_named is not None:
            self.real_named = real_named

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
        :type: int
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
        :type: str
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
        :type: int
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
        :type: int
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
        :type: int
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
        :type: int
        """
        self._device_status = device_status

    @property
    def tag_id(self):
        """Gets the tag_id of this ListSimCardsRequest.

        标签ID，最多支持传50个

        :return: The tag_id of this ListSimCardsRequest.
        :rtype: list[int]
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ListSimCardsRequest.

        标签ID，最多支持传50个

        :param tag_id: The tag_id of this ListSimCardsRequest.
        :type: list[int]
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
        :type: int
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
        :type: str
        """
        self._order = order

    @property
    def sort(self):
        """Gets the sort of this ListSimCardsRequest.

        排序的属性，目前支持:cid（容器ID）、flow_used（已用流量）、flow_left（剩余流量）

        :return: The sort of this ListSimCardsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListSimCardsRequest.

        排序的属性，目前支持:cid（容器ID）、flow_used（已用流量）、flow_left（剩余流量）

        :param sort: The sort of this ListSimCardsRequest.
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._customer_attribute6 = customer_attribute6

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
        :type: bool
        """
        self._real_named = real_named

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
