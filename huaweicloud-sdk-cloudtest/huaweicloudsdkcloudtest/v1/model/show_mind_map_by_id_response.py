# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMindMapByIdResponse(SdkResponse):

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
        'data': 'MindmapObject',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'message': 'message'
    }

    def __init__(self, code=None, data=None, message=None):
        r"""ShowMindMapByIdResponse

        The model defined in huaweicloud sdk

        :param code: 
        :type code: str
        :param data: 
        :type data: :class:`huaweicloudsdkcloudtest.v1.MindmapObject`
        :param message: 
        :type message: str
        """
        
        super(ShowMindMapByIdResponse, self).__init__()

        self._code = None
        self._data = None
        self._message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if message is not None:
            self.message = message

    @property
    def code(self):
        r"""Gets the code of this ShowMindMapByIdResponse.

        :return: The code of this ShowMindMapByIdResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowMindMapByIdResponse.

        :param code: The code of this ShowMindMapByIdResponse.
        :type code: str
        """
        self._code = code

    @property
    def data(self):
        r"""Gets the data of this ShowMindMapByIdResponse.

        :return: The data of this ShowMindMapByIdResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.MindmapObject`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowMindMapByIdResponse.

        :param data: The data of this ShowMindMapByIdResponse.
        :type data: :class:`huaweicloudsdkcloudtest.v1.MindmapObject`
        """
        self._data = data

    @property
    def message(self):
        r"""Gets the message of this ShowMindMapByIdResponse.

        :return: The message of this ShowMindMapByIdResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowMindMapByIdResponse.

        :param message: The message of this ShowMindMapByIdResponse.
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
        if not isinstance(other, ShowMindMapByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
