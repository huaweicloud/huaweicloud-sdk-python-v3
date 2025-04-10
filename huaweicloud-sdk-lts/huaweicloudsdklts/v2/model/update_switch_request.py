# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSwitchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_converge_switch': 'str'
    }

    attribute_map = {
        'log_converge_switch': 'log_converge_switch'
    }

    def __init__(self, log_converge_switch=None):
        r"""UpdateSwitchRequest

        The model defined in huaweicloud sdk

        :param log_converge_switch: 开关参数
        :type log_converge_switch: str
        """
        
        

        self._log_converge_switch = None
        self.discriminator = None

        self.log_converge_switch = log_converge_switch

    @property
    def log_converge_switch(self):
        r"""Gets the log_converge_switch of this UpdateSwitchRequest.

        开关参数

        :return: The log_converge_switch of this UpdateSwitchRequest.
        :rtype: str
        """
        return self._log_converge_switch

    @log_converge_switch.setter
    def log_converge_switch(self, log_converge_switch):
        r"""Sets the log_converge_switch of this UpdateSwitchRequest.

        开关参数

        :param log_converge_switch: The log_converge_switch of this UpdateSwitchRequest.
        :type log_converge_switch: str
        """
        self._log_converge_switch = log_converge_switch

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
        if not isinstance(other, UpdateSwitchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
