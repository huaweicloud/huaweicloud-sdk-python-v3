# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'share_type': 'str',
        'charging_mode': 'str',
        'id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'share_type': 'share_type',
        'charging_mode': 'charging_mode',
        'id': 'id'
    }

    def __init__(self, size=None, share_type=None, charging_mode=None, id=None):
        r"""BandwidthResult

        The model defined in huaweicloud sdk

        :param size: 带宽（Mbit/s）。
        :type size: int
        :param share_type: 带宽的共享类型。共享类型枚举：PER，表示独享。目前只支持独享。
        :type share_type: str
        :param charging_mode: 带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。
        :type charging_mode: str
        :param id: 带宽ID，创建WHOLE类型带宽的弹性IP时指定的共享带宽。
        :type id: str
        """
        
        

        self._size = None
        self._share_type = None
        self._charging_mode = None
        self._id = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if share_type is not None:
            self.share_type = share_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if id is not None:
            self.id = id

    @property
    def size(self):
        r"""Gets the size of this BandwidthResult.

        带宽（Mbit/s）。

        :return: The size of this BandwidthResult.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BandwidthResult.

        带宽（Mbit/s）。

        :param size: The size of this BandwidthResult.
        :type size: int
        """
        self._size = size

    @property
    def share_type(self):
        r"""Gets the share_type of this BandwidthResult.

        带宽的共享类型。共享类型枚举：PER，表示独享。目前只支持独享。

        :return: The share_type of this BandwidthResult.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this BandwidthResult.

        带宽的共享类型。共享类型枚举：PER，表示独享。目前只支持独享。

        :param share_type: The share_type of this BandwidthResult.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this BandwidthResult.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。

        :return: The charging_mode of this BandwidthResult.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this BandwidthResult.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。

        :param charging_mode: The charging_mode of this BandwidthResult.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def id(self):
        r"""Gets the id of this BandwidthResult.

        带宽ID，创建WHOLE类型带宽的弹性IP时指定的共享带宽。

        :return: The id of this BandwidthResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandwidthResult.

        带宽ID，创建WHOLE类型带宽的弹性IP时指定的共享带宽。

        :param id: The id of this BandwidthResult.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, BandwidthResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
