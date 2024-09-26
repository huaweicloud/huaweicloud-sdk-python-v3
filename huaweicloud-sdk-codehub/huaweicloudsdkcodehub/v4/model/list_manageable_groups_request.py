# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListManageableGroupsRequest:

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
        'scope': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'scope': 'scope',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, scope=None, offset=None, limit=None):
        """ListManageableGroupsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param scope: 创建资源类型，group 代码组，repository仓库
        :type scope: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 返回数量
        :type limit: int
        """
        
        

        self._project_id = None
        self._scope = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if scope is not None:
            self.scope = scope
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ListManageableGroupsRequest.

        项目id

        :return: The project_id of this ListManageableGroupsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListManageableGroupsRequest.

        项目id

        :param project_id: The project_id of this ListManageableGroupsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def scope(self):
        """Gets the scope of this ListManageableGroupsRequest.

        创建资源类型，group 代码组，repository仓库

        :return: The scope of this ListManageableGroupsRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ListManageableGroupsRequest.

        创建资源类型，group 代码组，repository仓库

        :param scope: The scope of this ListManageableGroupsRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def offset(self):
        """Gets the offset of this ListManageableGroupsRequest.

        偏移量

        :return: The offset of this ListManageableGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListManageableGroupsRequest.

        偏移量

        :param offset: The offset of this ListManageableGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListManageableGroupsRequest.

        返回数量

        :return: The limit of this ListManageableGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListManageableGroupsRequest.

        返回数量

        :param limit: The limit of this ListManageableGroupsRequest.
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
        if not isinstance(other, ListManageableGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
