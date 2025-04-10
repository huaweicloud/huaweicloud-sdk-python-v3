# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpdateBackupEnhancePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str',
        'manual_backup_retention_days': 'str',
        'frequency': 'str',
        'policies': 'list[Policy]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'manual_backup_retention_days': 'manual_backup_retention_days',
        'frequency': 'frequency',
        'policies': 'policies'
    }

    def __init__(self, begin_time=None, end_time=None, manual_backup_retention_days=None, frequency=None, policies=None):
        r"""ListUpdateBackupEnhancePolicyResponse

        The model defined in huaweicloud sdk

        :param begin_time: 备份时间段开始时间
        :type begin_time: str
        :param end_time: 备份时间段结束时间
        :type end_time: str
        :param manual_backup_retention_days: 手动备份保留时长
        :type manual_backup_retention_days: str
        :param frequency: 高频备份的频率
        :type frequency: str
        :param policies: 备份策略集
        :type policies: list[:class:`huaweicloudsdkrds.v3.Policy`]
        """
        
        super(ListUpdateBackupEnhancePolicyResponse, self).__init__()

        self._begin_time = None
        self._end_time = None
        self._manual_backup_retention_days = None
        self._frequency = None
        self._policies = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if manual_backup_retention_days is not None:
            self.manual_backup_retention_days = manual_backup_retention_days
        if frequency is not None:
            self.frequency = frequency
        if policies is not None:
            self.policies = policies

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListUpdateBackupEnhancePolicyResponse.

        备份时间段开始时间

        :return: The begin_time of this ListUpdateBackupEnhancePolicyResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListUpdateBackupEnhancePolicyResponse.

        备份时间段开始时间

        :param begin_time: The begin_time of this ListUpdateBackupEnhancePolicyResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListUpdateBackupEnhancePolicyResponse.

        备份时间段结束时间

        :return: The end_time of this ListUpdateBackupEnhancePolicyResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListUpdateBackupEnhancePolicyResponse.

        备份时间段结束时间

        :param end_time: The end_time of this ListUpdateBackupEnhancePolicyResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def manual_backup_retention_days(self):
        r"""Gets the manual_backup_retention_days of this ListUpdateBackupEnhancePolicyResponse.

        手动备份保留时长

        :return: The manual_backup_retention_days of this ListUpdateBackupEnhancePolicyResponse.
        :rtype: str
        """
        return self._manual_backup_retention_days

    @manual_backup_retention_days.setter
    def manual_backup_retention_days(self, manual_backup_retention_days):
        r"""Sets the manual_backup_retention_days of this ListUpdateBackupEnhancePolicyResponse.

        手动备份保留时长

        :param manual_backup_retention_days: The manual_backup_retention_days of this ListUpdateBackupEnhancePolicyResponse.
        :type manual_backup_retention_days: str
        """
        self._manual_backup_retention_days = manual_backup_retention_days

    @property
    def frequency(self):
        r"""Gets the frequency of this ListUpdateBackupEnhancePolicyResponse.

        高频备份的频率

        :return: The frequency of this ListUpdateBackupEnhancePolicyResponse.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this ListUpdateBackupEnhancePolicyResponse.

        高频备份的频率

        :param frequency: The frequency of this ListUpdateBackupEnhancePolicyResponse.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def policies(self):
        r"""Gets the policies of this ListUpdateBackupEnhancePolicyResponse.

        备份策略集

        :return: The policies of this ListUpdateBackupEnhancePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListUpdateBackupEnhancePolicyResponse.

        备份策略集

        :param policies: The policies of this ListUpdateBackupEnhancePolicyResponse.
        :type policies: list[:class:`huaweicloudsdkrds.v3.Policy`]
        """
        self._policies = policies

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
        if not isinstance(other, ListUpdateBackupEnhancePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
