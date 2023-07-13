# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDirectoryTreeRequest:

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
        'category': 'str',
        'directory_id': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'category': 'category',
        'directory_id': 'directory_id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, category=None, directory_id=None, name=None, offset=None, limit=None):
        """ShowDirectoryTreeRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param category: 查询的目录节点类型.
        :type category: str
        :param directory_id: 目录编号.
        :type directory_id: str
        :param name: 目标元素名称.
        :type name: str
        :param offset: 查询偏移量.
        :type offset: int
        :param limit: 每页显示的条目数量.
        :type limit: int
        """
        
        

        self._workspace = None
        self._category = None
        self._directory_id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if category is not None:
            self.category = category
        if directory_id is not None:
            self.directory_id = directory_id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        """Gets the workspace of this ShowDirectoryTreeRequest.

        工作空间id

        :return: The workspace of this ShowDirectoryTreeRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowDirectoryTreeRequest.

        工作空间id

        :param workspace: The workspace of this ShowDirectoryTreeRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def category(self):
        """Gets the category of this ShowDirectoryTreeRequest.

        查询的目录节点类型.

        :return: The category of this ShowDirectoryTreeRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowDirectoryTreeRequest.

        查询的目录节点类型.

        :param category: The category of this ShowDirectoryTreeRequest.
        :type category: str
        """
        self._category = category

    @property
    def directory_id(self):
        """Gets the directory_id of this ShowDirectoryTreeRequest.

        目录编号.

        :return: The directory_id of this ShowDirectoryTreeRequest.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this ShowDirectoryTreeRequest.

        目录编号.

        :param directory_id: The directory_id of this ShowDirectoryTreeRequest.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def name(self):
        """Gets the name of this ShowDirectoryTreeRequest.

        目标元素名称.

        :return: The name of this ShowDirectoryTreeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDirectoryTreeRequest.

        目标元素名称.

        :param name: The name of this ShowDirectoryTreeRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ShowDirectoryTreeRequest.

        查询偏移量.

        :return: The offset of this ShowDirectoryTreeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowDirectoryTreeRequest.

        查询偏移量.

        :param offset: The offset of this ShowDirectoryTreeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowDirectoryTreeRequest.

        每页显示的条目数量.

        :return: The limit of this ShowDirectoryTreeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowDirectoryTreeRequest.

        每页显示的条目数量.

        :param limit: The limit of this ShowDirectoryTreeRequest.
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
        if not isinstance(other, ShowDirectoryTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
