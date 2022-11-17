# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'event_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'event_id': 'event_id'
    }

    def __init__(self, resource_id=None, resource_name=None, event_id=None):
        """AdditionalInfo

        The model defined in huaweicloud sdk

        :param resource_id: 该条告警历史对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。
        :type resource_id: str
        :param resource_name: 该条告警历史对应的资源名称；如：ECS-Test01。
        :type resource_name: str
        :param event_id: 该条告警历史对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。
        :type event_id: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._event_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if event_id is not None:
            self.event_id = event_id

    @property
    def resource_id(self):
        """Gets the resource_id of this AdditionalInfo.

        该条告警历史对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。

        :return: The resource_id of this AdditionalInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this AdditionalInfo.

        该条告警历史对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。

        :param resource_id: The resource_id of this AdditionalInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this AdditionalInfo.

        该条告警历史对应的资源名称；如：ECS-Test01。

        :return: The resource_name of this AdditionalInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this AdditionalInfo.

        该条告警历史对应的资源名称；如：ECS-Test01。

        :param resource_name: The resource_name of this AdditionalInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_id(self):
        """Gets the event_id of this AdditionalInfo.

        该条告警历史对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。

        :return: The event_id of this AdditionalInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this AdditionalInfo.

        该条告警历史对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。

        :param event_id: The event_id of this AdditionalInfo.
        :type event_id: str
        """
        self._event_id = event_id

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
        if not isinstance(other, AdditionalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
