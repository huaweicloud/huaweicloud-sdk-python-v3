# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'size': 'int',
        'share_type': 'str',
        'charge_mode': 'str',
        'name': 'str',
        'billing_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'share_type': 'share_type',
        'charge_mode': 'charge_mode',
        'name': 'name',
        'billing_info': 'billing_info'
    }

    def __init__(self, id=None, size=None, share_type=None, charge_mode=None, name=None, billing_info=None):
        """BandwidthResp

        The model defined in huaweicloud sdk

        :param id: - 功能说明：带宽ID
        :type id: str
        :param size: - 功能说明：带宽大小
        :type size: int
        :param share_type: - 功能说明：类型  \&quot;WHOLE\&quot;为共享带宽，\&quot;PER\&quot;为独占带宽
        :type share_type: str
        :param charge_mode: - 功能说明：带宽计费模式
        :type charge_mode: str
        :param name: - 功能说明：带宽名称
        :type name: str
        :param billing_info: - 功能说明：带宽的订单信息
        :type billing_info: str
        """
        
        

        self._id = None
        self._size = None
        self._share_type = None
        self._charge_mode = None
        self._name = None
        self._billing_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if share_type is not None:
            self.share_type = share_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if name is not None:
            self.name = name
        if billing_info is not None:
            self.billing_info = billing_info

    @property
    def id(self):
        """Gets the id of this BandwidthResp.

        - 功能说明：带宽ID

        :return: The id of this BandwidthResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BandwidthResp.

        - 功能说明：带宽ID

        :param id: The id of this BandwidthResp.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this BandwidthResp.

        - 功能说明：带宽大小

        :return: The size of this BandwidthResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BandwidthResp.

        - 功能说明：带宽大小

        :param size: The size of this BandwidthResp.
        :type size: int
        """
        self._size = size

    @property
    def share_type(self):
        """Gets the share_type of this BandwidthResp.

        - 功能说明：类型  \"WHOLE\"为共享带宽，\"PER\"为独占带宽

        :return: The share_type of this BandwidthResp.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this BandwidthResp.

        - 功能说明：类型  \"WHOLE\"为共享带宽，\"PER\"为独占带宽

        :param share_type: The share_type of this BandwidthResp.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BandwidthResp.

        - 功能说明：带宽计费模式

        :return: The charge_mode of this BandwidthResp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BandwidthResp.

        - 功能说明：带宽计费模式

        :param charge_mode: The charge_mode of this BandwidthResp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def name(self):
        """Gets the name of this BandwidthResp.

        - 功能说明：带宽名称

        :return: The name of this BandwidthResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandwidthResp.

        - 功能说明：带宽名称

        :param name: The name of this BandwidthResp.
        :type name: str
        """
        self._name = name

    @property
    def billing_info(self):
        """Gets the billing_info of this BandwidthResp.

        - 功能说明：带宽的订单信息

        :return: The billing_info of this BandwidthResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this BandwidthResp.

        - 功能说明：带宽的订单信息

        :param billing_info: The billing_info of this BandwidthResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

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
        if not isinstance(other, BandwidthResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
