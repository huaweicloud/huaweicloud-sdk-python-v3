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
        r"""DeleteResultError

        The model defined in huaweicloud sdk

        :param key: Object names in a deletion result
        :type key: str
        :param code: Error code of the failed deletion
        :type code: str
        :param message: Error message of the failed deletion
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
        r"""Gets the key of this DeleteResultError.

        Object names in a deletion result

        :return: The key of this DeleteResultError.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this DeleteResultError.

        Object names in a deletion result

        :param key: The key of this DeleteResultError.
        :type key: str
        """
        self._key = key

    @property
    def code(self):
        r"""Gets the code of this DeleteResultError.

        Error code of the failed deletion

        :return: The code of this DeleteResultError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DeleteResultError.

        Error code of the failed deletion

        :param code: The code of this DeleteResultError.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this DeleteResultError.

        Error message of the failed deletion

        :return: The message of this DeleteResultError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DeleteResultError.

        Error message of the failed deletion

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
