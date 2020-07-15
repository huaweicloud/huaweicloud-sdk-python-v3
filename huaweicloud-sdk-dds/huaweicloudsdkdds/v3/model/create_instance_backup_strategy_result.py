# coding: utf-8

import pprint
import re

import six





class CreateInstanceBackupStrategyResult:


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
        'keep_days': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'keep_days': 'keep_days'
    }

    def __init__(self, start_time=None, keep_days=None):
        """CreateInstanceBackupStrategyResult - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._keep_days = None
        self.discriminator = None

        self.start_time = start_time
        if keep_days is not None:
            self.keep_days = keep_days

    @property
    def start_time(self):
        """Gets the start_time of this CreateInstanceBackupStrategyResult.

        备份时间段。自动备份将在该时间段内触发。 取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。   - HH取值必须比hh大1。   - mm和MM取值必须相同，且取值必须为00、15、30或45。

        :return: The start_time of this CreateInstanceBackupStrategyResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateInstanceBackupStrategyResult.

        备份时间段。自动备份将在该时间段内触发。 取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。   - HH取值必须比hh大1。   - mm和MM取值必须相同，且取值必须为00、15、30或45。

        :param start_time: The start_time of this CreateInstanceBackupStrategyResult.
        :type: str
        """
        self._start_time = start_time

    @property
    def keep_days(self):
        """Gets the keep_days of this CreateInstanceBackupStrategyResult.

        指定已生成的备份文件可以保存的天数。 取值范围：0～732。   - 取0值，表示不设置自动备份策略。   - 不传该参数，默认开启自动备份策略，备份文件默认保存7天。

        :return: The keep_days of this CreateInstanceBackupStrategyResult.
        :rtype: str
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this CreateInstanceBackupStrategyResult.

        指定已生成的备份文件可以保存的天数。 取值范围：0～732。   - 取0值，表示不设置自动备份策略。   - 不传该参数，默认开启自动备份策略，备份文件默认保存7天。

        :param keep_days: The keep_days of this CreateInstanceBackupStrategyResult.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateInstanceBackupStrategyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
