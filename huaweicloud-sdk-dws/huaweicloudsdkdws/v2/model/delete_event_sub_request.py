# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEventSubRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_sub_id': 'str'
    }

    attribute_map = {
        'event_sub_id': 'event_sub_id'
    }

    def __init__(self, event_sub_id=None):
        r"""DeleteEventSubRequest

        The model defined in huaweicloud sdk

        :param event_sub_id: **参数解释**： 事件订阅ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type event_sub_id: str
        """
        
        

        self._event_sub_id = None
        self.discriminator = None

        self.event_sub_id = event_sub_id

    @property
    def event_sub_id(self):
        r"""Gets the event_sub_id of this DeleteEventSubRequest.

        **参数解释**： 事件订阅ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The event_sub_id of this DeleteEventSubRequest.
        :rtype: str
        """
        return self._event_sub_id

    @event_sub_id.setter
    def event_sub_id(self, event_sub_id):
        r"""Sets the event_sub_id of this DeleteEventSubRequest.

        **参数解释**： 事件订阅ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param event_sub_id: The event_sub_id of this DeleteEventSubRequest.
        :type event_sub_id: str
        """
        self._event_sub_id = event_sub_id

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
        if not isinstance(other, DeleteEventSubRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
