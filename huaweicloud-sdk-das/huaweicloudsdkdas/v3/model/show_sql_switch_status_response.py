# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlSwitchStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'retention_days': 'int'
    }

    attribute_map = {
        'status': 'status',
        'retention_days': 'retention_days'
    }

    def __init__(self, status=None, retention_days=None):
        r"""ShowSqlSwitchStatusResponse

        The model defined in huaweicloud sdk

        :param status: 开关状态。取值： Enabled：已开启， Disabled：已关闭， Switching：开关切换中
        :type status: str
        :param retention_days: SQL数据保存天数。
        :type retention_days: int
        """
        
        super(ShowSqlSwitchStatusResponse, self).__init__()

        self._status = None
        self._retention_days = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if retention_days is not None:
            self.retention_days = retention_days

    @property
    def status(self):
        r"""Gets the status of this ShowSqlSwitchStatusResponse.

        开关状态。取值： Enabled：已开启， Disabled：已关闭， Switching：开关切换中

        :return: The status of this ShowSqlSwitchStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSqlSwitchStatusResponse.

        开关状态。取值： Enabled：已开启， Disabled：已关闭， Switching：开关切换中

        :param status: The status of this ShowSqlSwitchStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def retention_days(self):
        r"""Gets the retention_days of this ShowSqlSwitchStatusResponse.

        SQL数据保存天数。

        :return: The retention_days of this ShowSqlSwitchStatusResponse.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this ShowSqlSwitchStatusResponse.

        SQL数据保存天数。

        :param retention_days: The retention_days of this ShowSqlSwitchStatusResponse.
        :type retention_days: int
        """
        self._retention_days = retention_days

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
        if not isinstance(other, ShowSqlSwitchStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
