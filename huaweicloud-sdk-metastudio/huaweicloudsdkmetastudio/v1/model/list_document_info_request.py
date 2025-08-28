# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDocumentInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'knowledge_library_id': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'knowledge_library_id': 'knowledge_library_id',
        'file_name': 'file_name'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, knowledge_library_id=None, file_name=None):
        r"""ListDocumentInfoRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param knowledge_library_id: 知识库ID
        :type knowledge_library_id: str
        :param file_name: 文档名称
        :type file_name: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._knowledge_library_id = None
        self._file_name = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.knowledge_library_id = knowledge_library_id
        if file_name is not None:
            self.file_name = file_name

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListDocumentInfoRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListDocumentInfoRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListDocumentInfoRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListDocumentInfoRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDocumentInfoRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListDocumentInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDocumentInfoRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListDocumentInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDocumentInfoRequest.

        每页显示的条目数量。

        :return: The limit of this ListDocumentInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDocumentInfoRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListDocumentInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this ListDocumentInfoRequest.

        知识库ID

        :return: The knowledge_library_id of this ListDocumentInfoRequest.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this ListDocumentInfoRequest.

        知识库ID

        :param knowledge_library_id: The knowledge_library_id of this ListDocumentInfoRequest.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ListDocumentInfoRequest.

        文档名称

        :return: The file_name of this ListDocumentInfoRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListDocumentInfoRequest.

        文档名称

        :param file_name: The file_name of this ListDocumentInfoRequest.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, ListDocumentInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
