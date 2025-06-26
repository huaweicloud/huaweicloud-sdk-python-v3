# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceConfigurationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'anonymous_access': 'bool'
    }

    attribute_map = {
        'anonymous_access': 'anonymous_access'
    }

    def __init__(self, anonymous_access=None):
        r"""UpdateInstanceConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param anonymous_access: 是否开启匿名登录
        :type anonymous_access: bool
        """
        
        

        self._anonymous_access = None
        self.discriminator = None

        self.anonymous_access = anonymous_access

    @property
    def anonymous_access(self):
        r"""Gets the anonymous_access of this UpdateInstanceConfigurationRequestBody.

        是否开启匿名登录

        :return: The anonymous_access of this UpdateInstanceConfigurationRequestBody.
        :rtype: bool
        """
        return self._anonymous_access

    @anonymous_access.setter
    def anonymous_access(self, anonymous_access):
        r"""Sets the anonymous_access of this UpdateInstanceConfigurationRequestBody.

        是否开启匿名登录

        :param anonymous_access: The anonymous_access of this UpdateInstanceConfigurationRequestBody.
        :type anonymous_access: bool
        """
        self._anonymous_access = anonymous_access

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
        if not isinstance(other, UpdateInstanceConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
