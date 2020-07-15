# coding: utf-8

import pprint
import re

import six





class Bandwidth:


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
        """Bandwidth - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._share_type = None
        self._charging_mode = None
        self._id = None
        self.discriminator = None

        self.size = size
        if share_type is not None:
            self.share_type = share_type
        self.charging_mode = charging_mode
        if id is not None:
            self.id = id

    @property
    def size(self):
        """Gets the size of this Bandwidth.

        带宽（Mbit/s），取值范围为[1,300]。

        :return: The size of this Bandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Bandwidth.

        带宽（Mbit/s），取值范围为[1,300]。

        :param size: The size of this Bandwidth.
        :type: int
        """
        self._size = size

    @property
    def share_type(self):
        """Gets the share_type of this Bandwidth.

        带宽的共享类型。共享类型枚举：PER：独享型。WHOLE：共享型。

        :return: The share_type of this Bandwidth.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this Bandwidth.

        带宽的共享类型。共享类型枚举：PER：独享型。WHOLE：共享型。

        :param share_type: The share_type of this Bandwidth.
        :type: str
        """
        self._share_type = share_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this Bandwidth.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。字段为其它值，会导致创建云服务器失败。如果share_type是PER，该参数为必选项。如果share_type是WHOLE，会忽略该参数。

        :return: The charging_mode of this Bandwidth.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this Bandwidth.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。字段为其它值，会导致创建云服务器失败。如果share_type是PER，该参数为必选项。如果share_type是WHOLE，会忽略该参数。

        :param charging_mode: The charging_mode of this Bandwidth.
        :type: str
        """
        self._charging_mode = charging_mode

    @property
    def id(self):
        """Gets the id of this Bandwidth.

        带宽ID，使用共享型带宽时，可以选择之前创建的共享带宽来创建弹性IP。如果share_type是PER，会忽略该参数。如果share_type是WHOLE，该参数为必选项。

        :return: The id of this Bandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bandwidth.

        带宽ID，使用共享型带宽时，可以选择之前创建的共享带宽来创建弹性IP。如果share_type是PER，会忽略该参数。如果share_type是WHOLE，该参数为必选项。

        :param id: The id of this Bandwidth.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
