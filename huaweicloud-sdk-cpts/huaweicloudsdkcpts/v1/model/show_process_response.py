# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProcessResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'json': 'UploadProcessJson',
        'extend': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'json': 'json',
        'extend': 'extend'
    }

    def __init__(self, code=None, message=None, json=None, extend=None):
        """ShowProcessResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param message: message
        :type message: str
        :param json: 
        :type json: :class:`huaweicloudsdkcpts.v1.UploadProcessJson`
        :param extend: extend
        :type extend: str
        """
        
        super(ShowProcessResponse, self).__init__()

        self._code = None
        self._message = None
        self._json = None
        self._extend = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if json is not None:
            self.json = json
        if extend is not None:
            self.extend = extend

    @property
    def code(self):
        """Gets the code of this ShowProcessResponse.

        code

        :return: The code of this ShowProcessResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowProcessResponse.

        code

        :param code: The code of this ShowProcessResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowProcessResponse.

        message

        :return: The message of this ShowProcessResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowProcessResponse.

        message

        :param message: The message of this ShowProcessResponse.
        :type message: str
        """
        self._message = message

    @property
    def json(self):
        """Gets the json of this ShowProcessResponse.

        :return: The json of this ShowProcessResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.UploadProcessJson`
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this ShowProcessResponse.

        :param json: The json of this ShowProcessResponse.
        :type json: :class:`huaweicloudsdkcpts.v1.UploadProcessJson`
        """
        self._json = json

    @property
    def extend(self):
        """Gets the extend of this ShowProcessResponse.

        extend

        :return: The extend of this ShowProcessResponse.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowProcessResponse.

        extend

        :param extend: The extend of this ShowProcessResponse.
        :type extend: str
        """
        self._extend = extend

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
        if not isinstance(other, ShowProcessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
