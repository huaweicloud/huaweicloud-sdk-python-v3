# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTsvi:

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
        'enable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'enable': 'enable'
    }

    def __init__(self, id=None, enable=None):
        """UpdateTsvi

        The model defined in huaweicloud sdk

        :param id: 服务器ID
        :type id: str
        :param enable: **⚠ 预留字段，不使用，是否启用虚拟IP功能与服务器组配置保持一致。 是否启用虚拟IP功能。 开关只在租户配置允许启用虚拟IP场景有效，否则忽略传值并设置为关闭。
        :type enable: bool
        """
        
        

        self._id = None
        self._enable = None
        self.discriminator = None

        self.id = id
        self.enable = enable

    @property
    def id(self):
        """Gets the id of this UpdateTsvi.

        服务器ID

        :return: The id of this UpdateTsvi.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTsvi.

        服务器ID

        :param id: The id of this UpdateTsvi.
        :type id: str
        """
        self._id = id

    @property
    def enable(self):
        """Gets the enable of this UpdateTsvi.

        **⚠ 预留字段，不使用，是否启用虚拟IP功能与服务器组配置保持一致。 是否启用虚拟IP功能。 开关只在租户配置允许启用虚拟IP场景有效，否则忽略传值并设置为关闭。

        :return: The enable of this UpdateTsvi.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateTsvi.

        **⚠ 预留字段，不使用，是否启用虚拟IP功能与服务器组配置保持一致。 是否启用虚拟IP功能。 开关只在租户配置允许启用虚拟IP场景有效，否则忽略传值并设置为关闭。

        :param enable: The enable of this UpdateTsvi.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, UpdateTsvi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
