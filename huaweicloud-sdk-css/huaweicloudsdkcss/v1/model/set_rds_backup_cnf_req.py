# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRDSBackupCnfReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'indices': 'str',
        'prefix': 'str',
        'period': 'str',
        'keepday': 'int',
        'enable': 'str',
        'delete_auto': 'str',
        'frequency': 'str'
    }

    attribute_map = {
        'indices': 'indices',
        'prefix': 'prefix',
        'period': 'period',
        'keepday': 'keepday',
        'enable': 'enable',
        'delete_auto': 'delete_auto',
        'frequency': 'frequency'
    }

    def __init__(self, indices=None, prefix=None, period=None, keepday=None, enable=None, delete_auto=None, frequency=None):
        r"""SetRDSBackupCnfReq

        The model defined in huaweicloud sdk

        :param indices: 需要备份的索引名。*代表所有索引。
        :type indices: str
        :param prefix: 自动创建快照的名称前缀，需要用户自己手动输入。 只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。  &gt; 当enable为true时该字段为必选字段
        :type prefix: str
        :param period: 每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。 比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。  &gt; 当enable为true时该字段为必选字段
        :type period: str
        :param keepday: 自定义设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。  &gt; 当enable为true时该字段为必选字段
        :type keepday: int
        :param enable: 是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。
        :type enable: str
        :param delete_auto: 表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。 默认为“false”，表示不会删除之前已自动创建的快照。 设置为true，表示在关闭自动创建快照策略的同时，删除所有已创建的快照。
        :type delete_auto: str
        :param frequency: 自动创建快照的执行频次。
        :type frequency: str
        """
        
        

        self._indices = None
        self._prefix = None
        self._period = None
        self._keepday = None
        self._enable = None
        self._delete_auto = None
        self._frequency = None
        self.discriminator = None

        if indices is not None:
            self.indices = indices
        if prefix is not None:
            self.prefix = prefix
        if period is not None:
            self.period = period
        if keepday is not None:
            self.keepday = keepday
        self.enable = enable
        if delete_auto is not None:
            self.delete_auto = delete_auto
        if frequency is not None:
            self.frequency = frequency

    @property
    def indices(self):
        r"""Gets the indices of this SetRDSBackupCnfReq.

        需要备份的索引名。*代表所有索引。

        :return: The indices of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        r"""Sets the indices of this SetRDSBackupCnfReq.

        需要备份的索引名。*代表所有索引。

        :param indices: The indices of this SetRDSBackupCnfReq.
        :type indices: str
        """
        self._indices = indices

    @property
    def prefix(self):
        r"""Gets the prefix of this SetRDSBackupCnfReq.

        自动创建快照的名称前缀，需要用户自己手动输入。 只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。  > 当enable为true时该字段为必选字段

        :return: The prefix of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this SetRDSBackupCnfReq.

        自动创建快照的名称前缀，需要用户自己手动输入。 只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。  > 当enable为true时该字段为必选字段

        :param prefix: The prefix of this SetRDSBackupCnfReq.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def period(self):
        r"""Gets the period of this SetRDSBackupCnfReq.

        每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。 比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。  > 当enable为true时该字段为必选字段

        :return: The period of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SetRDSBackupCnfReq.

        每天创建快照的时刻，只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。 比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。  > 当enable为true时该字段为必选字段

        :param period: The period of this SetRDSBackupCnfReq.
        :type period: str
        """
        self._period = period

    @property
    def keepday(self):
        r"""Gets the keepday of this SetRDSBackupCnfReq.

        自定义设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。  > 当enable为true时该字段为必选字段

        :return: The keepday of this SetRDSBackupCnfReq.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        r"""Sets the keepday of this SetRDSBackupCnfReq.

        自定义设置快照保留的天数，范围是1～90。系统在半点时刻会自动删除超过保留天数的快照。  > 当enable为true时该字段为必选字段

        :param keepday: The keepday of this SetRDSBackupCnfReq.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def enable(self):
        r"""Gets the enable of this SetRDSBackupCnfReq.

        是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。

        :return: The enable of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this SetRDSBackupCnfReq.

        是否开启自动创建快照策略。 - true：表示开启自动创建快照策略。 - false：表示关闭自动创建快照策略。

        :param enable: The enable of this SetRDSBackupCnfReq.
        :type enable: str
        """
        self._enable = enable

    @property
    def delete_auto(self):
        r"""Gets the delete_auto of this SetRDSBackupCnfReq.

        表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。 默认为“false”，表示不会删除之前已自动创建的快照。 设置为true，表示在关闭自动创建快照策略的同时，删除所有已创建的快照。

        :return: The delete_auto of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._delete_auto

    @delete_auto.setter
    def delete_auto(self, delete_auto):
        r"""Sets the delete_auto of this SetRDSBackupCnfReq.

        表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。 默认为“false”，表示不会删除之前已自动创建的快照。 设置为true，表示在关闭自动创建快照策略的同时，删除所有已创建的快照。

        :param delete_auto: The delete_auto of this SetRDSBackupCnfReq.
        :type delete_auto: str
        """
        self._delete_auto = delete_auto

    @property
    def frequency(self):
        r"""Gets the frequency of this SetRDSBackupCnfReq.

        自动创建快照的执行频次。

        :return: The frequency of this SetRDSBackupCnfReq.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this SetRDSBackupCnfReq.

        自动创建快照的执行频次。

        :param frequency: The frequency of this SetRDSBackupCnfReq.
        :type frequency: str
        """
        self._frequency = frequency

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
        if not isinstance(other, SetRDSBackupCnfReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
