# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupStrategyForItemResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'keep_days': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'keep_days': 'keep_days'
    }

    def __init__(self, start_time=None, keep_days=None):
        """BackupStrategyForItemResponse

        The model defined in huaweicloud sdk

        :param start_time: 备份时间段。自动备份将在该时间段内触发。当前时间指UTC时间。
        :type start_time: str
        :param keep_days: 已生成备份文件可以保存的天数。取值范围：0~732。
        :type keep_days: int
        """
        
        

        self._start_time = None
        self._keep_days = None
        self.discriminator = None

        self.start_time = start_time
        self.keep_days = keep_days

    @property
    def start_time(self):
        """Gets the start_time of this BackupStrategyForItemResponse.

        备份时间段。自动备份将在该时间段内触发。当前时间指UTC时间。

        :return: The start_time of this BackupStrategyForItemResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BackupStrategyForItemResponse.

        备份时间段。自动备份将在该时间段内触发。当前时间指UTC时间。

        :param start_time: The start_time of this BackupStrategyForItemResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def keep_days(self):
        """Gets the keep_days of this BackupStrategyForItemResponse.

        已生成备份文件可以保存的天数。取值范围：0~732。

        :return: The keep_days of this BackupStrategyForItemResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this BackupStrategyForItemResponse.

        已生成备份文件可以保存的天数。取值范围：0~732。

        :param keep_days: The keep_days of this BackupStrategyForItemResponse.
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
        if not isinstance(other, BackupStrategyForItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
