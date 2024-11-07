# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthPackageLevelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'str',
        'name': 'str'
    }

    attribute_map = {
        'level': 'level',
        'name': 'name'
    }

    def __init__(self, level=None, name=None):
        """ListBandwidthPackageLevelsRequest

        The model defined in huaweicloud sdk

        :param level: 根据带宽包等级进行查询
        :type level: str
        :param name: 根据名称进行模糊查询
        :type name: str
        """
        
        

        self._level = None
        self._name = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if name is not None:
            self.name = name

    @property
    def level(self):
        """Gets the level of this ListBandwidthPackageLevelsRequest.

        根据带宽包等级进行查询

        :return: The level of this ListBandwidthPackageLevelsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ListBandwidthPackageLevelsRequest.

        根据带宽包等级进行查询

        :param level: The level of this ListBandwidthPackageLevelsRequest.
        :type level: str
        """
        self._level = level

    @property
    def name(self):
        """Gets the name of this ListBandwidthPackageLevelsRequest.

        根据名称进行模糊查询

        :return: The name of this ListBandwidthPackageLevelsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBandwidthPackageLevelsRequest.

        根据名称进行模糊查询

        :param name: The name of this ListBandwidthPackageLevelsRequest.
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
        if not isinstance(other, ListBandwidthPackageLevelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
