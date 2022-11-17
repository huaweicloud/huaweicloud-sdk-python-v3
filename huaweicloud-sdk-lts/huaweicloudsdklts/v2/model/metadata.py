# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'event_id': 'str',
        'event_severity': 'str',
        'event_name': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'resource_provider': 'str',
        'lts_alarm_type': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'event_id': 'event_id',
        'event_severity': 'event_severity',
        'event_name': 'event_name',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'resource_provider': 'resource_provider',
        'lts_alarm_type': 'lts_alarm_type'
    }

    def __init__(self, event_type=None, event_id=None, event_severity=None, event_name=None, resource_type=None, resource_id=None, resource_provider=None, lts_alarm_type=None):
        """Metadata

        The model defined in huaweicloud sdk

        :param event_type: 告警类型
        :type event_type: str
        :param event_id: 告警id
        :type event_id: str
        :param event_severity: 告警级别
        :type event_severity: str
        :param event_name: 告警名称
        :type event_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_id: 日志组/流名称
        :type resource_id: str
        :param resource_provider: 告警源
        :type resource_provider: str
        :param lts_alarm_type: 告警规则类型(SQL/关键词)
        :type lts_alarm_type: str
        """
        
        

        self._event_type = None
        self._event_id = None
        self._event_severity = None
        self._event_name = None
        self._resource_type = None
        self._resource_id = None
        self._resource_provider = None
        self._lts_alarm_type = None
        self.discriminator = None

        self.event_type = event_type
        self.event_id = event_id
        self.event_severity = event_severity
        self.event_name = event_name
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.resource_provider = resource_provider
        self.lts_alarm_type = lts_alarm_type

    @property
    def event_type(self):
        """Gets the event_type of this Metadata.

        告警类型

        :return: The event_type of this Metadata.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Metadata.

        告警类型

        :param event_type: The event_type of this Metadata.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_id(self):
        """Gets the event_id of this Metadata.

        告警id

        :return: The event_id of this Metadata.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Metadata.

        告警id

        :param event_id: The event_id of this Metadata.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_severity(self):
        """Gets the event_severity of this Metadata.

        告警级别

        :return: The event_severity of this Metadata.
        :rtype: str
        """
        return self._event_severity

    @event_severity.setter
    def event_severity(self, event_severity):
        """Sets the event_severity of this Metadata.

        告警级别

        :param event_severity: The event_severity of this Metadata.
        :type event_severity: str
        """
        self._event_severity = event_severity

    @property
    def event_name(self):
        """Gets the event_name of this Metadata.

        告警名称

        :return: The event_name of this Metadata.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Metadata.

        告警名称

        :param event_name: The event_name of this Metadata.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def resource_type(self):
        """Gets the resource_type of this Metadata.

        资源类型

        :return: The resource_type of this Metadata.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Metadata.

        资源类型

        :param resource_type: The resource_type of this Metadata.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this Metadata.

        日志组/流名称

        :return: The resource_id of this Metadata.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Metadata.

        日志组/流名称

        :param resource_id: The resource_id of this Metadata.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_provider(self):
        """Gets the resource_provider of this Metadata.

        告警源

        :return: The resource_provider of this Metadata.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        """Sets the resource_provider of this Metadata.

        告警源

        :param resource_provider: The resource_provider of this Metadata.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def lts_alarm_type(self):
        """Gets the lts_alarm_type of this Metadata.

        告警规则类型(SQL/关键词)

        :return: The lts_alarm_type of this Metadata.
        :rtype: str
        """
        return self._lts_alarm_type

    @lts_alarm_type.setter
    def lts_alarm_type(self, lts_alarm_type):
        """Sets the lts_alarm_type of this Metadata.

        告警规则类型(SQL/关键词)

        :param lts_alarm_type: The lts_alarm_type of this Metadata.
        :type lts_alarm_type: str
        """
        self._lts_alarm_type = lts_alarm_type

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
