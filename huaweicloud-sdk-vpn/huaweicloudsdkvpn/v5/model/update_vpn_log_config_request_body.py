# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnLogConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_config': 'UpdateVpnLogConfigRequestBodyContent'
    }

    attribute_map = {
        'log_config': 'log_config'
    }

    def __init__(self, log_config=None):
        """UpdateVpnLogConfigRequestBody

        The model defined in huaweicloud sdk

        :param log_config: 
        :type log_config: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBodyContent`
        """
        
        

        self._log_config = None
        self.discriminator = None

        self.log_config = log_config

    @property
    def log_config(self):
        """Gets the log_config of this UpdateVpnLogConfigRequestBody.

        :return: The log_config of this UpdateVpnLogConfigRequestBody.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBodyContent`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        """Sets the log_config of this UpdateVpnLogConfigRequestBody.

        :param log_config: The log_config of this UpdateVpnLogConfigRequestBody.
        :type log_config: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBodyContent`
        """
        self._log_config = log_config

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
        if not isinstance(other, UpdateVpnLogConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
