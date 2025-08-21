# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReadmeFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blob_id': 'str',
        'content': 'str',
        'encoding': 'object',
        'file_name': 'str',
        'file_path': 'str',
        'file_type': 'str',
        'size': 'int',
        'x_total': 'str'
    }

    attribute_map = {
        'blob_id': 'blob_id',
        'content': 'content',
        'encoding': 'encoding',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'size': 'size',
        'x_total': 'X-Total'
    }

    def __init__(self, blob_id=None, content=None, encoding=None, file_name=None, file_path=None, file_type=None, size=None, x_total=None):
        r"""ShowReadmeFileResponse

        The model defined in huaweicloud sdk

        :param blob_id: **参数解释：** bolb文件ID。 **约束限制：** 不涉及。
        :type blob_id: str
        :param content: **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。
        :type content: str
        :param encoding: **参数解释：** 文件编码方式。 **约束限制：** - base64。
        :type encoding: object
        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_type: 文件类型
        :type file_type: str
        :param size: **参数解释：** 文件字节大小。 **约束限制：** 不涉及。
        :type size: int
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowReadmeFileResponse, self).__init__()

        self._blob_id = None
        self._content = None
        self._encoding = None
        self._file_name = None
        self._file_path = None
        self._file_type = None
        self._size = None
        self._x_total = None
        self.discriminator = None

        if blob_id is not None:
            self.blob_id = blob_id
        if content is not None:
            self.content = content
        if encoding is not None:
            self.encoding = encoding
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if size is not None:
            self.size = size
        if x_total is not None:
            self.x_total = x_total

    @property
    def blob_id(self):
        r"""Gets the blob_id of this ShowReadmeFileResponse.

        **参数解释：** bolb文件ID。 **约束限制：** 不涉及。

        :return: The blob_id of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        r"""Sets the blob_id of this ShowReadmeFileResponse.

        **参数解释：** bolb文件ID。 **约束限制：** 不涉及。

        :param blob_id: The blob_id of this ShowReadmeFileResponse.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def content(self):
        r"""Gets the content of this ShowReadmeFileResponse.

        **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。

        :return: The content of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowReadmeFileResponse.

        **参数解释：** 经过base64编码后的文件内容。 **约束限制：** 不涉及。

        :param content: The content of this ShowReadmeFileResponse.
        :type content: str
        """
        self._content = content

    @property
    def encoding(self):
        r"""Gets the encoding of this ShowReadmeFileResponse.

        **参数解释：** 文件编码方式。 **约束限制：** - base64。

        :return: The encoding of this ShowReadmeFileResponse.
        :rtype: object
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this ShowReadmeFileResponse.

        **参数解释：** 文件编码方式。 **约束限制：** - base64。

        :param encoding: The encoding of this ShowReadmeFileResponse.
        :type encoding: object
        """
        self._encoding = encoding

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowReadmeFileResponse.

        文件名称

        :return: The file_name of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowReadmeFileResponse.

        文件名称

        :param file_name: The file_name of this ShowReadmeFileResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowReadmeFileResponse.

        文件路径

        :return: The file_path of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowReadmeFileResponse.

        文件路径

        :param file_path: The file_path of this ShowReadmeFileResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this ShowReadmeFileResponse.

        文件类型

        :return: The file_type of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ShowReadmeFileResponse.

        文件类型

        :param file_type: The file_type of this ShowReadmeFileResponse.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def size(self):
        r"""Gets the size of this ShowReadmeFileResponse.

        **参数解释：** 文件字节大小。 **约束限制：** 不涉及。

        :return: The size of this ShowReadmeFileResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowReadmeFileResponse.

        **参数解释：** 文件字节大小。 **约束限制：** 不涉及。

        :param size: The size of this ShowReadmeFileResponse.
        :type size: int
        """
        self._size = size

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowReadmeFileResponse.

        :return: The x_total of this ShowReadmeFileResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowReadmeFileResponse.

        :param x_total: The x_total of this ShowReadmeFileResponse.
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
        if not isinstance(other, ShowReadmeFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
