# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatChoice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'message': 'MessageItem'
    }

    attribute_map = {
        'index': 'index',
        'message': 'message'
    }

    def __init__(self, index=None, message=None):
        r"""ChatChoice

        The model defined in huaweicloud sdk

        :param index: 回复的索引
        :type index: int
        :param message: 
        :type message: :class:`huaweicloudsdkmastudio.v1.MessageItem`
        """
        
        

        self._index = None
        self._message = None
        self.discriminator = None

        self.index = index
        self.message = message

    @property
    def index(self):
        r"""Gets the index of this ChatChoice.

        回复的索引

        :return: The index of this ChatChoice.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ChatChoice.

        回复的索引

        :param index: The index of this ChatChoice.
        :type index: int
        """
        self._index = index

    @property
    def message(self):
        r"""Gets the message of this ChatChoice.

        :return: The message of this ChatChoice.
        :rtype: :class:`huaweicloudsdkmastudio.v1.MessageItem`
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ChatChoice.

        :param message: The message of this ChatChoice.
        :type message: :class:`huaweicloudsdkmastudio.v1.MessageItem`
        """
        self._message = message

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
        if not isinstance(other, ChatChoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
