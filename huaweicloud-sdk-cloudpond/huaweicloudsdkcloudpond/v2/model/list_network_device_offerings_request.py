# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkDeviceOfferingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_code': 'str',
        'storage_type': 'list[str]',
        'pay_mode': 'list[str]',
        'period_num': 'list[int]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'zone_code': 'zone_code',
        'storage_type': 'storage_type',
        'pay_mode': 'pay_mode',
        'period_num': 'period_num',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, zone_code=None, storage_type=None, pay_mode=None, period_num=None, limit=None, marker=None):
        r"""ListNetworkDeviceOfferingsRequest

        The model defined in huaweicloud sdk

        :param zone_code: 地区编码
        :type zone_code: str
        :param storage_type: 存储类型
        :type storage_type: list[str]
        :param pay_mode: 付费模式
        :type pay_mode: list[str]
        :param period_num: 购买时长
        :type period_num: list[int]
        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        """
        
        

        self._zone_code = None
        self._storage_type = None
        self._pay_mode = None
        self._period_num = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if zone_code is not None:
            self.zone_code = zone_code
        if storage_type is not None:
            self.storage_type = storage_type
        if pay_mode is not None:
            self.pay_mode = pay_mode
        if period_num is not None:
            self.period_num = period_num
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def zone_code(self):
        r"""Gets the zone_code of this ListNetworkDeviceOfferingsRequest.

        地区编码

        :return: The zone_code of this ListNetworkDeviceOfferingsRequest.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this ListNetworkDeviceOfferingsRequest.

        地区编码

        :param zone_code: The zone_code of this ListNetworkDeviceOfferingsRequest.
        :type zone_code: str
        """
        self._zone_code = zone_code

    @property
    def storage_type(self):
        r"""Gets the storage_type of this ListNetworkDeviceOfferingsRequest.

        存储类型

        :return: The storage_type of this ListNetworkDeviceOfferingsRequest.
        :rtype: list[str]
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this ListNetworkDeviceOfferingsRequest.

        存储类型

        :param storage_type: The storage_type of this ListNetworkDeviceOfferingsRequest.
        :type storage_type: list[str]
        """
        self._storage_type = storage_type

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this ListNetworkDeviceOfferingsRequest.

        付费模式

        :return: The pay_mode of this ListNetworkDeviceOfferingsRequest.
        :rtype: list[str]
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this ListNetworkDeviceOfferingsRequest.

        付费模式

        :param pay_mode: The pay_mode of this ListNetworkDeviceOfferingsRequest.
        :type pay_mode: list[str]
        """
        self._pay_mode = pay_mode

    @property
    def period_num(self):
        r"""Gets the period_num of this ListNetworkDeviceOfferingsRequest.

        购买时长

        :return: The period_num of this ListNetworkDeviceOfferingsRequest.
        :rtype: list[int]
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ListNetworkDeviceOfferingsRequest.

        购买时长

        :param period_num: The period_num of this ListNetworkDeviceOfferingsRequest.
        :type period_num: list[int]
        """
        self._period_num = period_num

    @property
    def limit(self):
        r"""Gets the limit of this ListNetworkDeviceOfferingsRequest.

        每页的数量

        :return: The limit of this ListNetworkDeviceOfferingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNetworkDeviceOfferingsRequest.

        每页的数量

        :param limit: The limit of this ListNetworkDeviceOfferingsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListNetworkDeviceOfferingsRequest.

        分页标识

        :return: The marker of this ListNetworkDeviceOfferingsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListNetworkDeviceOfferingsRequest.

        分页标识

        :param marker: The marker of this ListNetworkDeviceOfferingsRequest.
        :type marker: str
        """
        self._marker = marker

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNetworkDeviceOfferingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
