# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVolumeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, description=None, name=None):
        """UpdateVolumeOption

        The model defined in huaweicloud sdk

        :param description: 新的云硬盘的描述，name和description不能同时为null。最大支持255个字节。
        :type description: str
        :param name: 新的云硬盘的名字，name和description不能同时为null。最大支持255个字节。
        :type name: str
        """
        
        

        self._description = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this UpdateVolumeOption.

        新的云硬盘的描述，name和description不能同时为null。最大支持255个字节。

        :return: The description of this UpdateVolumeOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVolumeOption.

        新的云硬盘的描述，name和description不能同时为null。最大支持255个字节。

        :param description: The description of this UpdateVolumeOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateVolumeOption.

        新的云硬盘的名字，name和description不能同时为null。最大支持255个字节。

        :return: The name of this UpdateVolumeOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVolumeOption.

        新的云硬盘的名字，name和description不能同时为null。最大支持255个字节。

        :param name: The name of this UpdateVolumeOption.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, UpdateVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
