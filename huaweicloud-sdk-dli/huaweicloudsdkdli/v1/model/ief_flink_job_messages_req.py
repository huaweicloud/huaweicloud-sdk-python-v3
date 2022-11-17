# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IefFlinkJobMessagesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'state': 'State'
    }

    attribute_map = {
        'message_id': 'message_id',
        'state': 'state'
    }

    def __init__(self, message_id=None, state=None):
        """IefFlinkJobMessagesReq

        The model defined in huaweicloud sdk

        :param message_id: 消息id
        :type message_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkdli.v1.State`
        """
        
        

        self._message_id = None
        self._state = None
        self.discriminator = None

        self.message_id = message_id
        if state is not None:
            self.state = state

    @property
    def message_id(self):
        """Gets the message_id of this IefFlinkJobMessagesReq.

        消息id

        :return: The message_id of this IefFlinkJobMessagesReq.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this IefFlinkJobMessagesReq.

        消息id

        :param message_id: The message_id of this IefFlinkJobMessagesReq.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def state(self):
        """Gets the state of this IefFlinkJobMessagesReq.

        :return: The state of this IefFlinkJobMessagesReq.
        :rtype: :class:`huaweicloudsdkdli.v1.State`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IefFlinkJobMessagesReq.

        :param state: The state of this IefFlinkJobMessagesReq.
        :type state: :class:`huaweicloudsdkdli.v1.State`
        """
        self._state = state

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
        if not isinstance(other, IefFlinkJobMessagesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
