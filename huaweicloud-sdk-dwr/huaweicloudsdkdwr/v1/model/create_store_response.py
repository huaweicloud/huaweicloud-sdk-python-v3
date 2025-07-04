# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStoreResponse(SdkResponse):

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
        'data': 'CreateStoreData'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, data=None):
        r"""CreateStoreResponse

        The model defined in huaweicloud sdk

        :param code: 返回码
        :type code: str
        :param message: 描述信息
        :type message: str
        :param data: 
        :type data: :class:`huaweicloudsdkdwr.v1.CreateStoreData`
        """
        
        super(CreateStoreResponse, self).__init__()

        self._code = None
        self._message = None
        self._data = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def code(self):
        r"""Gets the code of this CreateStoreResponse.

        返回码

        :return: The code of this CreateStoreResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateStoreResponse.

        返回码

        :param code: The code of this CreateStoreResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this CreateStoreResponse.

        描述信息

        :return: The message of this CreateStoreResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateStoreResponse.

        描述信息

        :param message: The message of this CreateStoreResponse.
        :type message: str
        """
        self._message = message

    @property
    def data(self):
        r"""Gets the data of this CreateStoreResponse.

        :return: The data of this CreateStoreResponse.
        :rtype: :class:`huaweicloudsdkdwr.v1.CreateStoreData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreateStoreResponse.

        :param data: The data of this CreateStoreResponse.
        :type data: :class:`huaweicloudsdkdwr.v1.CreateStoreData`
        """
        self._data = data

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
        if not isinstance(other, CreateStoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
