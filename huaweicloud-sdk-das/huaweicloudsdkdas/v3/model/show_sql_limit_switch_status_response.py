# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlLimitSwitchStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_status': 'str'
    }

    attribute_map = {
        'switch_status': 'switch_status'
    }

    def __init__(self, switch_status=None):
        """ShowSqlLimitSwitchStatusResponse

        The model defined in huaweicloud sdk

        :param switch_status: 开关状态
        :type switch_status: str
        """
        
        super(ShowSqlLimitSwitchStatusResponse, self).__init__()

        self._switch_status = None
        self.discriminator = None

        if switch_status is not None:
            self.switch_status = switch_status

    @property
    def switch_status(self):
        """Gets the switch_status of this ShowSqlLimitSwitchStatusResponse.

        开关状态

        :return: The switch_status of this ShowSqlLimitSwitchStatusResponse.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        """Sets the switch_status of this ShowSqlLimitSwitchStatusResponse.

        开关状态

        :param switch_status: The switch_status of this ShowSqlLimitSwitchStatusResponse.
        :type switch_status: str
        """
        self._switch_status = switch_status

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
        if not isinstance(other, ShowSqlLimitSwitchStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
