# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCategoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'accept': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'accept': 'accept'
    }

    def __init__(self, workspace=None, limit=None, offset=None, accept=None):
        r"""ListCategoryRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: 分页时每页的条数,最大值为100
        :type limit: int
        :param offset: 分页偏移量
        :type offset: int
        :param accept: application/json
        :type accept: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._accept = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.accept = accept

    @property
    def workspace(self):
        r"""Gets the workspace of this ListCategoryRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListCategoryRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListCategoryRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListCategoryRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListCategoryRequest.

        分页时每页的条数,最大值为100

        :return: The limit of this ListCategoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCategoryRequest.

        分页时每页的条数,最大值为100

        :param limit: The limit of this ListCategoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCategoryRequest.

        分页偏移量

        :return: The offset of this ListCategoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCategoryRequest.

        分页偏移量

        :param offset: The offset of this ListCategoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def accept(self):
        r"""Gets the accept of this ListCategoryRequest.

        application/json

        :return: The accept of this ListCategoryRequest.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        r"""Sets the accept of this ListCategoryRequest.

        application/json

        :param accept: The accept of this ListCategoryRequest.
        :type accept: str
        """
        self._accept = accept

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
        if not isinstance(other, ListCategoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
