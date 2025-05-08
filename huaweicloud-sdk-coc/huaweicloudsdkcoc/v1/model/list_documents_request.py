# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDocumentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'str',
        'name_like': 'str',
        'creator': 'str',
        'enterprise_project_id': 'str',
        'document_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name_like': 'name_like',
        'creator': 'creator',
        'enterprise_project_id': 'enterprise_project_id',
        'document_type': 'document_type'
    }

    def __init__(self, limit=None, offset=None, name_like=None, creator=None, enterprise_project_id=None, document_type=None):
        r"""ListDocumentsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页参数：每页返回记录个数限制
        :type limit: int
        :param offset: 偏移量
        :type offset: str
        :param name_like: 作业名（模糊）
        :type name_like: str
        :param creator: 创建人
        :type creator: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param document_type: 执行的作业类型 枚举：PUBLIC/NORMAL 默认NORMAL
        :type document_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._name_like = None
        self._creator = None
        self._enterprise_project_id = None
        self._document_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name_like is not None:
            self.name_like = name_like
        if creator is not None:
            self.creator = creator
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if document_type is not None:
            self.document_type = document_type

    @property
    def limit(self):
        r"""Gets the limit of this ListDocumentsRequest.

        分页参数：每页返回记录个数限制

        :return: The limit of this ListDocumentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDocumentsRequest.

        分页参数：每页返回记录个数限制

        :param limit: The limit of this ListDocumentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDocumentsRequest.

        偏移量

        :return: The offset of this ListDocumentsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDocumentsRequest.

        偏移量

        :param offset: The offset of this ListDocumentsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def name_like(self):
        r"""Gets the name_like of this ListDocumentsRequest.

        作业名（模糊）

        :return: The name_like of this ListDocumentsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        r"""Sets the name_like of this ListDocumentsRequest.

        作业名（模糊）

        :param name_like: The name_like of this ListDocumentsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def creator(self):
        r"""Gets the creator of this ListDocumentsRequest.

        创建人

        :return: The creator of this ListDocumentsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListDocumentsRequest.

        创建人

        :param creator: The creator of this ListDocumentsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDocumentsRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListDocumentsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDocumentsRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListDocumentsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def document_type(self):
        r"""Gets the document_type of this ListDocumentsRequest.

        执行的作业类型 枚举：PUBLIC/NORMAL 默认NORMAL

        :return: The document_type of this ListDocumentsRequest.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        r"""Sets the document_type of this ListDocumentsRequest.

        执行的作业类型 枚举：PUBLIC/NORMAL 默认NORMAL

        :param document_type: The document_type of this ListDocumentsRequest.
        :type document_type: str
        """
        self._document_type = document_type

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
        if not isinstance(other, ListDocumentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
