# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstructionLibraryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'count': 'int',
        'data': 'list[InstructionLibraryInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'data': 'data',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, offset=None, limit=None, count=None, data=None, x_request_id=None):
        r"""ListInstructionLibraryResponse

        The model defined in huaweicloud sdk

        :param offset: 与第一条数据的偏移量
        :type offset: int
        :param limit: 页面大小
        :type limit: int
        :param count: 总数量
        :type count: int
        :param data: 指令集信息
        :type data: list[:class:`huaweicloudsdkmetastudio.v1.InstructionLibraryInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListInstructionLibraryResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._count = None
        self._data = None
        self._x_request_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count is not None:
            self.count = count
        if data is not None:
            self.data = data
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstructionLibraryResponse.

        与第一条数据的偏移量

        :return: The offset of this ListInstructionLibraryResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstructionLibraryResponse.

        与第一条数据的偏移量

        :param offset: The offset of this ListInstructionLibraryResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstructionLibraryResponse.

        页面大小

        :return: The limit of this ListInstructionLibraryResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstructionLibraryResponse.

        页面大小

        :param limit: The limit of this ListInstructionLibraryResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def count(self):
        r"""Gets the count of this ListInstructionLibraryResponse.

        总数量

        :return: The count of this ListInstructionLibraryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListInstructionLibraryResponse.

        总数量

        :param count: The count of this ListInstructionLibraryResponse.
        :type count: int
        """
        self._count = count

    @property
    def data(self):
        r"""Gets the data of this ListInstructionLibraryResponse.

        指令集信息

        :return: The data of this ListInstructionLibraryResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InstructionLibraryInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListInstructionLibraryResponse.

        指令集信息

        :param data: The data of this ListInstructionLibraryResponse.
        :type data: list[:class:`huaweicloudsdkmetastudio.v1.InstructionLibraryInfo`]
        """
        self._data = data

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListInstructionLibraryResponse.

        :return: The x_request_id of this ListInstructionLibraryResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListInstructionLibraryResponse.

        :param x_request_id: The x_request_id of this ListInstructionLibraryResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListInstructionLibraryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
