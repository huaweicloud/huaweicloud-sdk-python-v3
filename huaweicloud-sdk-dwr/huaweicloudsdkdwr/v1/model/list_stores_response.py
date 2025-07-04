# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoresResponse(SdkResponse):

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
        'data': 'list[DescribeStoreData]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, code=None, message=None, data=None):
        r"""ListStoresResponse

        The model defined in huaweicloud sdk

        :param code: 返回码
        :type code: str
        :param message: 描述信息
        :type message: str
        :param data: 响应数据
        :type data: list[:class:`huaweicloudsdkdwr.v1.DescribeStoreData`]
        """
        
        super(ListStoresResponse, self).__init__()

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
        r"""Gets the code of this ListStoresResponse.

        返回码

        :return: The code of this ListStoresResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListStoresResponse.

        返回码

        :param code: The code of this ListStoresResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ListStoresResponse.

        描述信息

        :return: The message of this ListStoresResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListStoresResponse.

        描述信息

        :param message: The message of this ListStoresResponse.
        :type message: str
        """
        self._message = message

    @property
    def data(self):
        r"""Gets the data of this ListStoresResponse.

        响应数据

        :return: The data of this ListStoresResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.DescribeStoreData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListStoresResponse.

        响应数据

        :param data: The data of this ListStoresResponse.
        :type data: list[:class:`huaweicloudsdkdwr.v1.DescribeStoreData`]
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
        if not isinstance(other, ListStoresResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
