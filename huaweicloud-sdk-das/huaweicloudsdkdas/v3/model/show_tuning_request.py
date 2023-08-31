# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTuningRequest:

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
        'connection_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'connection_id': 'connection_id',
        'x_language': 'X-Language'
    }

    def __init__(self, message_id=None, connection_id=None, x_language=None):
        """ShowTuningRequest

        The model defined in huaweicloud sdk

        :param message_id: 诊断messageId
        :type message_id: str
        :param connection_id: 连接Id
        :type connection_id: str
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._message_id = None
        self._connection_id = None
        self._x_language = None
        self.discriminator = None

        self.message_id = message_id
        self.connection_id = connection_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def message_id(self):
        """Gets the message_id of this ShowTuningRequest.

        诊断messageId

        :return: The message_id of this ShowTuningRequest.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ShowTuningRequest.

        诊断messageId

        :param message_id: The message_id of this ShowTuningRequest.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def connection_id(self):
        """Gets the connection_id of this ShowTuningRequest.

        连接Id

        :return: The connection_id of this ShowTuningRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ShowTuningRequest.

        连接Id

        :param connection_id: The connection_id of this ShowTuningRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowTuningRequest.

        语言

        :return: The x_language of this ShowTuningRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowTuningRequest.

        语言

        :param x_language: The x_language of this ShowTuningRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowTuningRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
