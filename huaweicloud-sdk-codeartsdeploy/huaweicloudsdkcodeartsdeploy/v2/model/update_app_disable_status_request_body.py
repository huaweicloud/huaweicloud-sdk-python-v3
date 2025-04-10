# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppDisableStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_disable': 'bool'
    }

    attribute_map = {
        'is_disable': 'is_disable'
    }

    def __init__(self, is_disable=None):
        r"""UpdateAppDisableStatusRequestBody

        The model defined in huaweicloud sdk

        :param is_disable: 是否禁用， true禁用， false取消禁用
        :type is_disable: bool
        """
        
        

        self._is_disable = None
        self.discriminator = None

        self.is_disable = is_disable

    @property
    def is_disable(self):
        r"""Gets the is_disable of this UpdateAppDisableStatusRequestBody.

        是否禁用， true禁用， false取消禁用

        :return: The is_disable of this UpdateAppDisableStatusRequestBody.
        :rtype: bool
        """
        return self._is_disable

    @is_disable.setter
    def is_disable(self, is_disable):
        r"""Sets the is_disable of this UpdateAppDisableStatusRequestBody.

        是否禁用， true禁用， false取消禁用

        :param is_disable: The is_disable of this UpdateAppDisableStatusRequestBody.
        :type is_disable: bool
        """
        self._is_disable = is_disable

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
        if not isinstance(other, UpdateAppDisableStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
