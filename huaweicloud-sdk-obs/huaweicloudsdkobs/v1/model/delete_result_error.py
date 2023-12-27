# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResultError:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteResultError"

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'key': 'Key',
        'code': 'Code',
        'message': 'Message'
    }

    def __init__(self, key=None, code=None, message=None):
        """DeleteResultError

        The model defined in huaweicloud sdk

        :param key: 每个删除结果的对象名。 
        :type key: str
        :param code: 删除失败结果的错误码。 
        :type code: str
        :param message: 删除失败结果的错误消息。 
        :type message: str
        """
        
        

        self._key = None
        self._code = None
        self._message = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message

    @property
    def key(self):
        """Gets the key of this DeleteResultError.

        每个删除结果的对象名。 

        :return: The key of this DeleteResultError.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteResultError.

        每个删除结果的对象名。 

        :param key: The key of this DeleteResultError.
        :type key: str
        """
        self._key = key

    @property
    def code(self):
        """Gets the code of this DeleteResultError.

        删除失败结果的错误码。 

        :return: The code of this DeleteResultError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DeleteResultError.

        删除失败结果的错误码。 

        :param code: The code of this DeleteResultError.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this DeleteResultError.

        删除失败结果的错误消息。 

        :return: The message of this DeleteResultError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeleteResultError.

        删除失败结果的错误消息。 

        :param message: The message of this DeleteResultError.
        :type message: str
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
        if not isinstance(other, DeleteResultError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
