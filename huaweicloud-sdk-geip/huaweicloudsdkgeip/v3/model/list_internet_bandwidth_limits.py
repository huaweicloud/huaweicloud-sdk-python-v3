# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetBandwidthLimits:

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
        'charge_mode': 'str',
        'min_size': 'int',
        'ext_limit': 'ExtLimitPojo',
        'max_size': 'int',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'charge_mode': 'charge_mode',
        'min_size': 'min_size',
        'ext_limit': 'ext_limit',
        'max_size': 'max_size',
        'type': 'type'
    }

    def __init__(self, id=None, charge_mode=None, min_size=None, ext_limit=None, max_size=None, type=None):
        """ListInternetBandwidthLimits

        The model defined in huaweicloud sdk

        :param id: 全域公网带宽限制的ID
        :type id: str
        :param charge_mode: 全域公网带宽的计费模式
        :type charge_mode: str
        :param min_size: 该类型全域公网带宽可购买的最小size
        :type min_size: int
        :param ext_limit: 
        :type ext_limit: :class:`huaweicloudsdkgeip.v3.ExtLimitPojo`
        :param max_size: 该类型全域公网带宽可购买的最大size
        :type max_size: int
        :param type: 全域公网带宽类型
        :type type: str
        """
        
        

        self._id = None
        self._charge_mode = None
        self._min_size = None
        self._ext_limit = None
        self._max_size = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if min_size is not None:
            self.min_size = min_size
        if ext_limit is not None:
            self.ext_limit = ext_limit
        if max_size is not None:
            self.max_size = max_size
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ListInternetBandwidthLimits.

        全域公网带宽限制的ID

        :return: The id of this ListInternetBandwidthLimits.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInternetBandwidthLimits.

        全域公网带宽限制的ID

        :param id: The id of this ListInternetBandwidthLimits.
        :type id: str
        """
        self._id = id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListInternetBandwidthLimits.

        全域公网带宽的计费模式

        :return: The charge_mode of this ListInternetBandwidthLimits.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListInternetBandwidthLimits.

        全域公网带宽的计费模式

        :param charge_mode: The charge_mode of this ListInternetBandwidthLimits.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def min_size(self):
        """Gets the min_size of this ListInternetBandwidthLimits.

        该类型全域公网带宽可购买的最小size

        :return: The min_size of this ListInternetBandwidthLimits.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this ListInternetBandwidthLimits.

        该类型全域公网带宽可购买的最小size

        :param min_size: The min_size of this ListInternetBandwidthLimits.
        :type min_size: int
        """
        self._min_size = min_size

    @property
    def ext_limit(self):
        """Gets the ext_limit of this ListInternetBandwidthLimits.

        :return: The ext_limit of this ListInternetBandwidthLimits.
        :rtype: :class:`huaweicloudsdkgeip.v3.ExtLimitPojo`
        """
        return self._ext_limit

    @ext_limit.setter
    def ext_limit(self, ext_limit):
        """Sets the ext_limit of this ListInternetBandwidthLimits.

        :param ext_limit: The ext_limit of this ListInternetBandwidthLimits.
        :type ext_limit: :class:`huaweicloudsdkgeip.v3.ExtLimitPojo`
        """
        self._ext_limit = ext_limit

    @property
    def max_size(self):
        """Gets the max_size of this ListInternetBandwidthLimits.

        该类型全域公网带宽可购买的最大size

        :return: The max_size of this ListInternetBandwidthLimits.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this ListInternetBandwidthLimits.

        该类型全域公网带宽可购买的最大size

        :param max_size: The max_size of this ListInternetBandwidthLimits.
        :type max_size: int
        """
        self._max_size = max_size

    @property
    def type(self):
        """Gets the type of this ListInternetBandwidthLimits.

        全域公网带宽类型

        :return: The type of this ListInternetBandwidthLimits.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInternetBandwidthLimits.

        全域公网带宽类型

        :param type: The type of this ListInternetBandwidthLimits.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListInternetBandwidthLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
