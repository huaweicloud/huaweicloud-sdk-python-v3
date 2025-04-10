# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditAlarmLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'alarm_log': 'list[AlarmLogResponseAlarmLog]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'alarm_log': 'alarm_log'
    }

    def __init__(self, total_num=None, alarm_log=None):
        r"""ListAuditAlarmLogResponse

        The model defined in huaweicloud sdk

        :param total_num: 总条数
        :type total_num: int
        :param alarm_log: 告警列表
        :type alarm_log: list[:class:`huaweicloudsdkdbss.v1.AlarmLogResponseAlarmLog`]
        """
        
        super(ListAuditAlarmLogResponse, self).__init__()

        self._total_num = None
        self._alarm_log = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if alarm_log is not None:
            self.alarm_log = alarm_log

    @property
    def total_num(self):
        r"""Gets the total_num of this ListAuditAlarmLogResponse.

        总条数

        :return: The total_num of this ListAuditAlarmLogResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListAuditAlarmLogResponse.

        总条数

        :param total_num: The total_num of this ListAuditAlarmLogResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def alarm_log(self):
        r"""Gets the alarm_log of this ListAuditAlarmLogResponse.

        告警列表

        :return: The alarm_log of this ListAuditAlarmLogResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AlarmLogResponseAlarmLog`]
        """
        return self._alarm_log

    @alarm_log.setter
    def alarm_log(self, alarm_log):
        r"""Sets the alarm_log of this ListAuditAlarmLogResponse.

        告警列表

        :param alarm_log: The alarm_log of this ListAuditAlarmLogResponse.
        :type alarm_log: list[:class:`huaweicloudsdkdbss.v1.AlarmLogResponseAlarmLog`]
        """
        self._alarm_log = alarm_log

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
        if not isinstance(other, ListAuditAlarmLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
