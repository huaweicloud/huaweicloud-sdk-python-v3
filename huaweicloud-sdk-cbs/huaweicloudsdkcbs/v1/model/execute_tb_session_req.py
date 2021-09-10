# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTbSessionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'reply': 'str',
        'type': 'int'
    }

    attribute_map = {
        'reply': 'reply',
        'type': 'type'
    }

    def __init__(self, reply=None, type=None):
        """ExecuteTbSessionReq - a model defined in huaweicloud sdk"""
        
        

        self._reply = None
        self._type = None
        self.discriminator = None

        if reply is not None:
            self.reply = reply
        self.type = type

    @property
    def reply(self):
        """Gets the reply of this ExecuteTbSessionReq.

        客户回复。

        :return: The reply of this ExecuteTbSessionReq.
        :rtype: str
        """
        return self._reply

    @reply.setter
    def reply(self, reply):
        """Sets the reply of this ExecuteTbSessionReq.

        客户回复。

        :param reply: The reply of this ExecuteTbSessionReq.
        :type: str
        """
        self._reply = reply

    @property
    def type(self):
        """Gets the type of this ExecuteTbSessionReq.

        客户回复属性，0表示通用回复，1表示客户打断， 2表示客户长时未回复。

        :return: The type of this ExecuteTbSessionReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecuteTbSessionReq.

        客户回复属性，0表示通用回复，1表示客户打断， 2表示客户长时未回复。

        :param type: The type of this ExecuteTbSessionReq.
        :type: int
        """
        self._type = type

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
        if not isinstance(other, ExecuteTbSessionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
