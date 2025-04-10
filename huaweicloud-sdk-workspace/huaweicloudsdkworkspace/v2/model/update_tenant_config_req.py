# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_config': 'FunctionConfig'
    }

    attribute_map = {
        'function_config': 'function_config'
    }

    def __init__(self, function_config=None):
        r"""UpdateTenantConfigReq

        The model defined in huaweicloud sdk

        :param function_config: 
        :type function_config: :class:`huaweicloudsdkworkspace.v2.FunctionConfig`
        """
        
        

        self._function_config = None
        self.discriminator = None

        if function_config is not None:
            self.function_config = function_config

    @property
    def function_config(self):
        r"""Gets the function_config of this UpdateTenantConfigReq.

        :return: The function_config of this UpdateTenantConfigReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FunctionConfig`
        """
        return self._function_config

    @function_config.setter
    def function_config(self, function_config):
        r"""Sets the function_config of this UpdateTenantConfigReq.

        :param function_config: The function_config of this UpdateTenantConfigReq.
        :type function_config: :class:`huaweicloudsdkworkspace.v2.FunctionConfig`
        """
        self._function_config = function_config

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
        if not isinstance(other, UpdateTenantConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
