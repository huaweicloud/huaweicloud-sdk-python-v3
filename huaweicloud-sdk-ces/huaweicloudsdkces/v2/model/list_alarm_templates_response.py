# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_templates': 'list[AlarmTemplates]',
        'count': 'int'
    }

    attribute_map = {
        'alarm_templates': 'alarm_templates',
        'count': 'count'
    }

    def __init__(self, alarm_templates=None, count=None):
        """ListAlarmTemplatesResponse

        The model defined in huaweicloud sdk

        :param alarm_templates: 告警模板列表
        :type alarm_templates: list[:class:`huaweicloudsdkces.v2.AlarmTemplates`]
        :param count: 告警模板记录总数
        :type count: int
        """
        
        super(ListAlarmTemplatesResponse, self).__init__()

        self._alarm_templates = None
        self._count = None
        self.discriminator = None

        if alarm_templates is not None:
            self.alarm_templates = alarm_templates
        if count is not None:
            self.count = count

    @property
    def alarm_templates(self):
        """Gets the alarm_templates of this ListAlarmTemplatesResponse.

        告警模板列表

        :return: The alarm_templates of this ListAlarmTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.AlarmTemplates`]
        """
        return self._alarm_templates

    @alarm_templates.setter
    def alarm_templates(self, alarm_templates):
        """Sets the alarm_templates of this ListAlarmTemplatesResponse.

        告警模板列表

        :param alarm_templates: The alarm_templates of this ListAlarmTemplatesResponse.
        :type alarm_templates: list[:class:`huaweicloudsdkces.v2.AlarmTemplates`]
        """
        self._alarm_templates = alarm_templates

    @property
    def count(self):
        """Gets the count of this ListAlarmTemplatesResponse.

        告警模板记录总数

        :return: The count of this ListAlarmTemplatesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAlarmTemplatesResponse.

        告警模板记录总数

        :param count: The count of this ListAlarmTemplatesResponse.
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
        if not isinstance(other, ListAlarmTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
