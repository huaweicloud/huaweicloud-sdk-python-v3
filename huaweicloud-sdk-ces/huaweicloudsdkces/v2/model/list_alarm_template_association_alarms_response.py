# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplateAssociationAlarmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarms': 'list[ListAssociationAlarmsResponseAlarms]',
        'count': 'int'
    }

    attribute_map = {
        'alarms': 'alarms',
        'count': 'count'
    }

    def __init__(self, alarms=None, count=None):
        r"""ListAlarmTemplateAssociationAlarmsResponse

        The model defined in huaweicloud sdk

        :param alarms: 告警规则列表
        :type alarms: list[:class:`huaweicloudsdkces.v2.ListAssociationAlarmsResponseAlarms`]
        :param count: 告警规则列表总数
        :type count: int
        """
        
        super(ListAlarmTemplateAssociationAlarmsResponse, self).__init__()

        self._alarms = None
        self._count = None
        self.discriminator = None

        if alarms is not None:
            self.alarms = alarms
        if count is not None:
            self.count = count

    @property
    def alarms(self):
        r"""Gets the alarms of this ListAlarmTemplateAssociationAlarmsResponse.

        告警规则列表

        :return: The alarms of this ListAlarmTemplateAssociationAlarmsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.ListAssociationAlarmsResponseAlarms`]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        r"""Sets the alarms of this ListAlarmTemplateAssociationAlarmsResponse.

        告警规则列表

        :param alarms: The alarms of this ListAlarmTemplateAssociationAlarmsResponse.
        :type alarms: list[:class:`huaweicloudsdkces.v2.ListAssociationAlarmsResponseAlarms`]
        """
        self._alarms = alarms

    @property
    def count(self):
        r"""Gets the count of this ListAlarmTemplateAssociationAlarmsResponse.

        告警规则列表总数

        :return: The count of this ListAlarmTemplateAssociationAlarmsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlarmTemplateAssociationAlarmsResponse.

        告警规则列表总数

        :param count: The count of this ListAlarmTemplateAssociationAlarmsResponse.
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
        if not isinstance(other, ListAlarmTemplateAssociationAlarmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
