# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'encoding': 'str',
        'content': 'str',
        'blob_id': 'str',
        'x_total': 'str'
    }

    attribute_map = {
        'size': 'size',
        'encoding': 'encoding',
        'content': 'content',
        'blob_id': 'blob_id',
        'x_total': 'X-Total'
    }

    def __init__(self, size=None, encoding=None, content=None, blob_id=None, x_total=None):
        r"""ShowBlobsResponse

        The model defined in huaweicloud sdk

        :param size: **参数解释：** 文件字节大小。 **约束限制：** 不涉及。
        :type size: int
        :param encoding: **参数解释：** 文件编码方式。 **约束限制：** - base64。
        :type encoding: str
        :param content: **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。
        :type content: str
        :param blob_id: **参数解释：** bolb文件ID。 **约束限制：** 不涉及。
        :type blob_id: str
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowBlobsResponse, self).__init__()

        self._size = None
        self._encoding = None
        self._content = None
        self._blob_id = None
        self._x_total = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if encoding is not None:
            self.encoding = encoding
        if content is not None:
            self.content = content
        if blob_id is not None:
            self.blob_id = blob_id
        if x_total is not None:
            self.x_total = x_total

    @property
    def size(self):
        r"""Gets the size of this ShowBlobsResponse.

        **参数解释：** 文件字节大小。 **约束限制：** 不涉及。

        :return: The size of this ShowBlobsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowBlobsResponse.

        **参数解释：** 文件字节大小。 **约束限制：** 不涉及。

        :param size: The size of this ShowBlobsResponse.
        :type size: int
        """
        self._size = size

    @property
    def encoding(self):
        r"""Gets the encoding of this ShowBlobsResponse.

        **参数解释：** 文件编码方式。 **约束限制：** - base64。

        :return: The encoding of this ShowBlobsResponse.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this ShowBlobsResponse.

        **参数解释：** 文件编码方式。 **约束限制：** - base64。

        :param encoding: The encoding of this ShowBlobsResponse.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def content(self):
        r"""Gets the content of this ShowBlobsResponse.

        **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。

        :return: The content of this ShowBlobsResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowBlobsResponse.

        **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。

        :param content: The content of this ShowBlobsResponse.
        :type content: str
        """
        self._content = content

    @property
    def blob_id(self):
        r"""Gets the blob_id of this ShowBlobsResponse.

        **参数解释：** bolb文件ID。 **约束限制：** 不涉及。

        :return: The blob_id of this ShowBlobsResponse.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this ShowBlobsResponse.

        **参数解释：** bolb文件ID。 **约束限制：** 不涉及。

        :param blob_id: The blob_id of this ShowBlobsResponse.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowBlobsResponse.

        :return: The x_total of this ShowBlobsResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowBlobsResponse.

        :param x_total: The x_total of this ShowBlobsResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowBlobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
