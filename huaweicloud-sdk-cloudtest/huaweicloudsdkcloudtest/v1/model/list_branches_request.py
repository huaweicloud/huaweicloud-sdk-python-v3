# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBranchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, sort_field=None, sort_type=None, offset=None, limit=None):
        """ListBranchesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序方式
        :type sort_type: str
        :param offset: 起始偏移量，表示从此偏移量开始查询， offset大于等于0，小于等于20000
        :type offset: int
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        """
        
        

        self._project_id = None
        self._sort_field = None
        self._sort_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        self.offset = offset
        self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ListBranchesRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListBranchesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListBranchesRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListBranchesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def sort_field(self):
        """Gets the sort_field of this ListBranchesRequest.

        排序字段

        :return: The sort_field of this ListBranchesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListBranchesRequest.

        排序字段

        :param sort_field: The sort_field of this ListBranchesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListBranchesRequest.

        排序方式

        :return: The sort_type of this ListBranchesRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListBranchesRequest.

        排序方式

        :param sort_type: The sort_type of this ListBranchesRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def offset(self):
        """Gets the offset of this ListBranchesRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0，小于等于20000

        :return: The offset of this ListBranchesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBranchesRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0，小于等于20000

        :param offset: The offset of this ListBranchesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBranchesRequest.

        每页显示的条目数量，最大支持200条

        :return: The limit of this ListBranchesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBranchesRequest.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this ListBranchesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListBranchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
