# coding: utf-8

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
        r"""AdditionalInfo

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释**： 该条告警记录对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。 **取值范围**： 字符串长度最大为128。 
        :type resource_id: str
        :param resource_name: **参数解释**： 该条告警记录对应的资源名称；如：ECS-Test01。 **取值范围**： 字符串长度最大为128。 
        :type resource_name: str
        :param event_id: **参数解释**： 该条告警记录对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。 **取值范围**： 字符串长度为24。 
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
        r"""Gets the resource_id of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。 **取值范围**： 字符串长度最大为128。 

        :return: The resource_id of this AdditionalInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的资源ID；如：22d98f6c-16d2-4c2d-b424-50e79d82838f。 **取值范围**： 字符串长度最大为128。 

        :param resource_id: The resource_id of this AdditionalInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的资源名称；如：ECS-Test01。 **取值范围**： 字符串长度最大为128。 

        :return: The resource_name of this AdditionalInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的资源名称；如：ECS-Test01。 **取值范围**： 字符串长度最大为128。 

        :param resource_name: The resource_name of this AdditionalInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_id(self):
        r"""Gets the event_id of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。 **取值范围**： 字符串长度为24。 

        :return: The event_id of this AdditionalInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this AdditionalInfo.

        **参数解释**： 该条告警记录对应的事件监控ID，资源所产生的事件；如：ev16031292300990kKN8p17J。 **取值范围**： 字符串长度为24。 

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
