# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'alarm_configs': 'list[AlarmConfigResponse]'
    }

    attribute_map = {
        'count': 'count',
        'alarm_configs': 'alarm_configs'
    }

    def __init__(self, count=None, alarm_configs=None):
        """ListAlarmConfigsResponse

        The model defined in huaweicloud sdk

        :param count: 告警配置总数
        :type count: int
        :param alarm_configs: 告警配置列表
        :type alarm_configs: list[:class:`huaweicloudsdkdws.v2.AlarmConfigResponse`]
        """
        
        super(ListAlarmConfigsResponse, self).__init__()

        self._count = None
        self._alarm_configs = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if alarm_configs is not None:
            self.alarm_configs = alarm_configs

    @property
    def count(self):
        """Gets the count of this ListAlarmConfigsResponse.

        告警配置总数

        :return: The count of this ListAlarmConfigsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAlarmConfigsResponse.

        告警配置总数

        :param count: The count of this ListAlarmConfigsResponse.
        :type count: int
        """
        self._count = count

    @property
    def alarm_configs(self):
        """Gets the alarm_configs of this ListAlarmConfigsResponse.

        告警配置列表

        :return: The alarm_configs of this ListAlarmConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.AlarmConfigResponse`]
        """
        return self._alarm_configs

    @alarm_configs.setter
    def alarm_configs(self, alarm_configs):
        """Sets the alarm_configs of this ListAlarmConfigsResponse.

        告警配置列表

        :param alarm_configs: The alarm_configs of this ListAlarmConfigsResponse.
        :type alarm_configs: list[:class:`huaweicloudsdkdws.v2.AlarmConfigResponse`]
        """
        self._alarm_configs = alarm_configs

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
        if not isinstance(other, ListAlarmConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
