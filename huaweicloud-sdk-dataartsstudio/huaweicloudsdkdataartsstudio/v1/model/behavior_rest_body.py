# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BehaviorRestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event': 'str',
        'params': 'list[EventParam]'
    }

    attribute_map = {
        'event': 'event',
        'params': 'params'
    }

    def __init__(self, event=None, params=None):
        """BehaviorRestBody

        The model defined in huaweicloud sdk

        :param event: 
        :type event: str
        :param params: 
        :type params: list[:class:`huaweicloudsdkdataartsstudio.v1.EventParam`]
        """
        
        

        self._event = None
        self._params = None
        self.discriminator = None

        self.event = event
        self.params = params

    @property
    def event(self):
        """Gets the event of this BehaviorRestBody.

        :return: The event of this BehaviorRestBody.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this BehaviorRestBody.

        :param event: The event of this BehaviorRestBody.
        :type event: str
        """
        self._event = event

    @property
    def params(self):
        """Gets the params of this BehaviorRestBody.

        :return: The params of this BehaviorRestBody.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.EventParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this BehaviorRestBody.

        :param params: The params of this BehaviorRestBody.
        :type params: list[:class:`huaweicloudsdkdataartsstudio.v1.EventParam`]
        """
        self._params = params

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
        if not isinstance(other, BehaviorRestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
