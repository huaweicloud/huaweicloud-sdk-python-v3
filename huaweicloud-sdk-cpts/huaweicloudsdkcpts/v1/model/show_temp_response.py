# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTempResponse(SdkResponse):

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
        'temp_info': 'TempInfo'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'temp_info': 'temp_info'
    }

    def __init__(self, code=None, message=None, temp_info=None):
        r"""ShowTempResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param temp_info: 
        :type temp_info: :class:`huaweicloudsdkcpts.v1.TempInfo`
        """
        
        super(ShowTempResponse, self).__init__()

        self._code = None
        self._message = None
        self._temp_info = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if temp_info is not None:
            self.temp_info = temp_info

    @property
    def code(self):
        r"""Gets the code of this ShowTempResponse.

        响应码

        :return: The code of this ShowTempResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowTempResponse.

        响应码

        :param code: The code of this ShowTempResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ShowTempResponse.

        响应消息

        :return: The message of this ShowTempResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTempResponse.

        响应消息

        :param message: The message of this ShowTempResponse.
        :type message: str
        """
        self._message = message

    @property
    def temp_info(self):
        r"""Gets the temp_info of this ShowTempResponse.

        :return: The temp_info of this ShowTempResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.TempInfo`
        """
        return self._temp_info

    @temp_info.setter
    def temp_info(self, temp_info):
        r"""Sets the temp_info of this ShowTempResponse.

        :param temp_info: The temp_info of this ShowTempResponse.
        :type temp_info: :class:`huaweicloudsdkcpts.v1.TempInfo`
        """
        self._temp_info = temp_info

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
        if not isinstance(other, ShowTempResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
