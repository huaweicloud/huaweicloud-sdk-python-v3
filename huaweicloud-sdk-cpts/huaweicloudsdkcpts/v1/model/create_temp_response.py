# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTempResponse(SdkResponse):

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
        'temp_id': 'int',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'temp_id': 'tempId',
        'message': 'message'
    }

    def __init__(self, code=None, temp_id=None, message=None):
        """CreateTempResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param temp_id: 事务id
        :type temp_id: int
        :param message: 响应消息
        :type message: str
        """
        
        super(CreateTempResponse, self).__init__()

        self._code = None
        self._temp_id = None
        self._message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if temp_id is not None:
            self.temp_id = temp_id
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this CreateTempResponse.

        响应码

        :return: The code of this CreateTempResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateTempResponse.

        响应码

        :param code: The code of this CreateTempResponse.
        :type code: str
        """
        self._code = code

    @property
    def temp_id(self):
        """Gets the temp_id of this CreateTempResponse.

        事务id

        :return: The temp_id of this CreateTempResponse.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this CreateTempResponse.

        事务id

        :param temp_id: The temp_id of this CreateTempResponse.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def message(self):
        """Gets the message of this CreateTempResponse.

        响应消息

        :return: The message of this CreateTempResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateTempResponse.

        响应消息

        :param message: The message of this CreateTempResponse.
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
        if not isinstance(other, CreateTempResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
