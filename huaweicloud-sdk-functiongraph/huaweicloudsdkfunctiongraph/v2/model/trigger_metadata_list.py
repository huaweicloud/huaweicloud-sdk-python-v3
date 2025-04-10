# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerMetadataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_name': 'str',
        'trigger_type': 'str',
        'event_type': 'str',
        'event_data': 'str'
    }

    attribute_map = {
        'trigger_name': 'trigger_name',
        'trigger_type': 'trigger_type',
        'event_type': 'event_type',
        'event_data': 'event_data'
    }

    def __init__(self, trigger_name=None, trigger_type=None, event_type=None, event_data=None):
        r"""TriggerMetadataList

        The model defined in huaweicloud sdk

        :param trigger_name: 触发名称
        :type trigger_name: str
        :param trigger_type: 触发器类型
        :type trigger_type: str
        :param event_type: 事件类型
        :type event_type: str
        :param event_data: 事件数据
        :type event_data: str
        """
        
        

        self._trigger_name = None
        self._trigger_type = None
        self._event_type = None
        self._event_data = None
        self.discriminator = None

        if trigger_name is not None:
            self.trigger_name = trigger_name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if event_type is not None:
            self.event_type = event_type
        if event_data is not None:
            self.event_data = event_data

    @property
    def trigger_name(self):
        r"""Gets the trigger_name of this TriggerMetadataList.

        触发名称

        :return: The trigger_name of this TriggerMetadataList.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        r"""Sets the trigger_name of this TriggerMetadataList.

        触发名称

        :param trigger_name: The trigger_name of this TriggerMetadataList.
        :type trigger_name: str
        """
        self._trigger_name = trigger_name

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this TriggerMetadataList.

        触发器类型

        :return: The trigger_type of this TriggerMetadataList.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this TriggerMetadataList.

        触发器类型

        :param trigger_type: The trigger_type of this TriggerMetadataList.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def event_type(self):
        r"""Gets the event_type of this TriggerMetadataList.

        事件类型

        :return: The event_type of this TriggerMetadataList.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this TriggerMetadataList.

        事件类型

        :param event_type: The event_type of this TriggerMetadataList.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_data(self):
        r"""Gets the event_data of this TriggerMetadataList.

        事件数据

        :return: The event_data of this TriggerMetadataList.
        :rtype: str
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        r"""Sets the event_data of this TriggerMetadataList.

        事件数据

        :param event_data: The event_data of this TriggerMetadataList.
        :type event_data: str
        """
        self._event_data = event_data

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
        if not isinstance(other, TriggerMetadataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
