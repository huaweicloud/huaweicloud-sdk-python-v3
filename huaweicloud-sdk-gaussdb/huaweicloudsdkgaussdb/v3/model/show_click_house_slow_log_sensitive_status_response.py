# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClickHouseSlowLogSensitiveStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_slow_log_switch': 'str'
    }

    attribute_map = {
        'open_slow_log_switch': 'open_slow_log_switch'
    }

    def __init__(self, open_slow_log_switch=None):
        """ShowClickHouseSlowLogSensitiveStatusResponse

        The model defined in huaweicloud sdk

        :param open_slow_log_switch: 慢日志脱敏开关。
        :type open_slow_log_switch: str
        """
        
        super(ShowClickHouseSlowLogSensitiveStatusResponse, self).__init__()

        self._open_slow_log_switch = None
        self.discriminator = None

        if open_slow_log_switch is not None:
            self.open_slow_log_switch = open_slow_log_switch

    @property
    def open_slow_log_switch(self):
        """Gets the open_slow_log_switch of this ShowClickHouseSlowLogSensitiveStatusResponse.

        慢日志脱敏开关。

        :return: The open_slow_log_switch of this ShowClickHouseSlowLogSensitiveStatusResponse.
        :rtype: str
        """
        return self._open_slow_log_switch

    @open_slow_log_switch.setter
    def open_slow_log_switch(self, open_slow_log_switch):
        """Sets the open_slow_log_switch of this ShowClickHouseSlowLogSensitiveStatusResponse.

        慢日志脱敏开关。

        :param open_slow_log_switch: The open_slow_log_switch of this ShowClickHouseSlowLogSensitiveStatusResponse.
        :type open_slow_log_switch: str
        """
        self._open_slow_log_switch = open_slow_log_switch

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
        if not isinstance(other, ShowClickHouseSlowLogSensitiveStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
