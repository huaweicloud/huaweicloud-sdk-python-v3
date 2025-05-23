# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteActiveAlarmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[Event]'
    }

    attribute_map = {
        'events': 'events'
    }

    def __init__(self, events=None):
        r"""DeleteActiveAlarmsRequestBody

        The model defined in huaweicloud sdk

        :param events: 主题信息
        :type events: list[:class:`huaweicloudsdklts.v2.Event`]
        """
        
        

        self._events = None
        self.discriminator = None

        self.events = events

    @property
    def events(self):
        r"""Gets the events of this DeleteActiveAlarmsRequestBody.

        主题信息

        :return: The events of this DeleteActiveAlarmsRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.Event`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this DeleteActiveAlarmsRequestBody.

        主题信息

        :param events: The events of this DeleteActiveAlarmsRequestBody.
        :type events: list[:class:`huaweicloudsdklts.v2.Event`]
        """
        self._events = events

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
        if not isinstance(other, DeleteActiveAlarmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
