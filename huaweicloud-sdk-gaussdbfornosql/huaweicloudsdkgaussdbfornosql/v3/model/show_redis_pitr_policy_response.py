# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRedisPitrPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'interval': 'int',
        'keep_days': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'interval': 'interval',
        'keep_days': 'keep_days'
    }

    def __init__(self, enabled=None, interval=None, keep_days=None):
        r"""ShowRedisPitrPolicyResponse

        The model defined in huaweicloud sdk

        :param enabled: 标识Redis实例是否开启指定时间点恢复。 “true”，表示实例开启Redis指定时间点恢复功能。 “false”，表示实例不启用Redis指定时间点恢复功能。
        :type enabled: bool
        :param interval: 数据备份的时间间隔，该数据备份控制redis实例可恢复时间点的间隔，仅在开启时返回。
        :type interval: int
        :param keep_days: 指定已生成的备份文件可以保存的天数，仅在开启时返回。
        :type keep_days: int
        """
        
        super(ShowRedisPitrPolicyResponse, self).__init__()

        self._enabled = None
        self._interval = None
        self._keep_days = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if interval is not None:
            self.interval = interval
        if keep_days is not None:
            self.keep_days = keep_days

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowRedisPitrPolicyResponse.

        标识Redis实例是否开启指定时间点恢复。 “true”，表示实例开启Redis指定时间点恢复功能。 “false”，表示实例不启用Redis指定时间点恢复功能。

        :return: The enabled of this ShowRedisPitrPolicyResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowRedisPitrPolicyResponse.

        标识Redis实例是否开启指定时间点恢复。 “true”，表示实例开启Redis指定时间点恢复功能。 “false”，表示实例不启用Redis指定时间点恢复功能。

        :param enabled: The enabled of this ShowRedisPitrPolicyResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def interval(self):
        r"""Gets the interval of this ShowRedisPitrPolicyResponse.

        数据备份的时间间隔，该数据备份控制redis实例可恢复时间点的间隔，仅在开启时返回。

        :return: The interval of this ShowRedisPitrPolicyResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowRedisPitrPolicyResponse.

        数据备份的时间间隔，该数据备份控制redis实例可恢复时间点的间隔，仅在开启时返回。

        :param interval: The interval of this ShowRedisPitrPolicyResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def keep_days(self):
        r"""Gets the keep_days of this ShowRedisPitrPolicyResponse.

        指定已生成的备份文件可以保存的天数，仅在开启时返回。

        :return: The keep_days of this ShowRedisPitrPolicyResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this ShowRedisPitrPolicyResponse.

        指定已生成的备份文件可以保存的天数，仅在开启时返回。

        :param keep_days: The keep_days of this ShowRedisPitrPolicyResponse.
        :type keep_days: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, ShowRedisPitrPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
