# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReverseProtectionGroupRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority_station': 'str'
    }

    attribute_map = {
        'priority_station': 'priority_station'
    }

    def __init__(self, priority_station=None):
        """ReverseProtectionGroupRequestParams

        The model defined in huaweicloud sdk

        :param priority_station: 切换方向。target：表示从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点。source：表示从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。
        :type priority_station: str
        """
        
        

        self._priority_station = None
        self.discriminator = None

        self.priority_station = priority_station

    @property
    def priority_station(self):
        """Gets the priority_station of this ReverseProtectionGroupRequestParams.

        切换方向。target：表示从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点。source：表示从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。

        :return: The priority_station of this ReverseProtectionGroupRequestParams.
        :rtype: str
        """
        return self._priority_station

    @priority_station.setter
    def priority_station(self, priority_station):
        """Sets the priority_station of this ReverseProtectionGroupRequestParams.

        切换方向。target：表示从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点。source：表示从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。

        :param priority_station: The priority_station of this ReverseProtectionGroupRequestParams.
        :type priority_station: str
        """
        self._priority_station = priority_station

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
        if not isinstance(other, ReverseProtectionGroupRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
