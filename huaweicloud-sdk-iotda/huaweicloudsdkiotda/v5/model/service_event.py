# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceEvent:

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
        'paras': 'list[ServiceCommandPara]'
    }

    attribute_map = {
        'event_type': 'event_type',
        'paras': 'paras'
    }

    def __init__(self, event_type=None, paras=None):
        """ServiceEvent

        The model defined in huaweicloud sdk

        :param event_type: **参数说明**：设备事件类型。注：设备服务内不允许重复。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type event_type: str
        :param paras: **参数说明**：设备事件的参数列表。
        :type paras: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        """
        
        

        self._event_type = None
        self._paras = None
        self.discriminator = None

        self.event_type = event_type
        if paras is not None:
            self.paras = paras

    @property
    def event_type(self):
        """Gets the event_type of this ServiceEvent.

        **参数说明**：设备事件类型。注：设备服务内不允许重复。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The event_type of this ServiceEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ServiceEvent.

        **参数说明**：设备事件类型。注：设备服务内不允许重复。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param event_type: The event_type of this ServiceEvent.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def paras(self):
        """Gets the paras of this ServiceEvent.

        **参数说明**：设备事件的参数列表。

        :return: The paras of this ServiceEvent.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this ServiceEvent.

        **参数说明**：设备事件的参数列表。

        :param paras: The paras of this ServiceEvent.
        :type paras: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        """
        self._paras = paras

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
        if not isinstance(other, ServiceEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
