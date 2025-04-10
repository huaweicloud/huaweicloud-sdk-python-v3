# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricOrEventAlarmRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_rules': 'list[AlarmParamForV4Db]',
        'metadata': 'object',
        'count': 'int'
    }

    attribute_map = {
        'alarm_rules': 'alarm_rules',
        'metadata': 'metadata',
        'count': 'count'
    }

    def __init__(self, alarm_rules=None, metadata=None, count=None):
        r"""ListMetricOrEventAlarmRuleResponse

        The model defined in huaweicloud sdk

        :param alarm_rules: 告警规则列表。
        :type alarm_rules: list[:class:`huaweicloudsdkaom.v2.AlarmParamForV4Db`]
        :param metadata: 元数据信息。
        :type metadata: object
        :param count: 告警规则数量。
        :type count: int
        """
        
        super(ListMetricOrEventAlarmRuleResponse, self).__init__()

        self._alarm_rules = None
        self._metadata = None
        self._count = None
        self.discriminator = None

        if alarm_rules is not None:
            self.alarm_rules = alarm_rules
        if metadata is not None:
            self.metadata = metadata
        if count is not None:
            self.count = count

    @property
    def alarm_rules(self):
        r"""Gets the alarm_rules of this ListMetricOrEventAlarmRuleResponse.

        告警规则列表。

        :return: The alarm_rules of this ListMetricOrEventAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AlarmParamForV4Db`]
        """
        return self._alarm_rules

    @alarm_rules.setter
    def alarm_rules(self, alarm_rules):
        r"""Sets the alarm_rules of this ListMetricOrEventAlarmRuleResponse.

        告警规则列表。

        :param alarm_rules: The alarm_rules of this ListMetricOrEventAlarmRuleResponse.
        :type alarm_rules: list[:class:`huaweicloudsdkaom.v2.AlarmParamForV4Db`]
        """
        self._alarm_rules = alarm_rules

    @property
    def metadata(self):
        r"""Gets the metadata of this ListMetricOrEventAlarmRuleResponse.

        元数据信息。

        :return: The metadata of this ListMetricOrEventAlarmRuleResponse.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListMetricOrEventAlarmRuleResponse.

        元数据信息。

        :param metadata: The metadata of this ListMetricOrEventAlarmRuleResponse.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def count(self):
        r"""Gets the count of this ListMetricOrEventAlarmRuleResponse.

        告警规则数量。

        :return: The count of this ListMetricOrEventAlarmRuleResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListMetricOrEventAlarmRuleResponse.

        告警规则数量。

        :param count: The count of this ListMetricOrEventAlarmRuleResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListMetricOrEventAlarmRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
