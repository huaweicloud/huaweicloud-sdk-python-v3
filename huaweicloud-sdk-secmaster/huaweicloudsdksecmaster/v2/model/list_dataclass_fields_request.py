# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataclassFieldsRequest:

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
        'workspace_id': 'str',
        'offset': 'float',
        'limit': 'float',
        'name': 'str',
        'is_built_in': 'bool',
        'dataclass_id': 'str',
        'field_category': 'str',
        'mapping': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'is_built_in': 'is_built_in',
        'dataclass_id': 'dataclass_id',
        'field_category': 'field_category',
        'mapping': 'mapping'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, name=None, is_built_in=None, dataclass_id=None, field_category=None, mapping=None):
        """ListDataclassFieldsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param offset: 偏移量
        :type offset: float
        :param limit: 数据量
        :type limit: float
        :param name: 名称查询
        :type name: str
        :param is_built_in: 是否内置
        :type is_built_in: bool
        :param dataclass_id: 数据类id
        :type dataclass_id: str
        :param field_category: 字段分类
        :type field_category: str
        :param mapping: 是否展示在分类映射外的其他地方
        :type mapping: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._is_built_in = None
        self._dataclass_id = None
        self._field_category = None
        self._mapping = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if is_built_in is not None:
            self.is_built_in = is_built_in
        self.dataclass_id = dataclass_id
        if field_category is not None:
            self.field_category = field_category
        if mapping is not None:
            self.mapping = mapping

    @property
    def project_id(self):
        """Gets the project_id of this ListDataclassFieldsRequest.

        项目id

        :return: The project_id of this ListDataclassFieldsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListDataclassFieldsRequest.

        项目id

        :param project_id: The project_id of this ListDataclassFieldsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListDataclassFieldsRequest.

        工作空间id

        :return: The workspace_id of this ListDataclassFieldsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListDataclassFieldsRequest.

        工作空间id

        :param workspace_id: The workspace_id of this ListDataclassFieldsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        """Gets the offset of this ListDataclassFieldsRequest.

        偏移量

        :return: The offset of this ListDataclassFieldsRequest.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataclassFieldsRequest.

        偏移量

        :param offset: The offset of this ListDataclassFieldsRequest.
        :type offset: float
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDataclassFieldsRequest.

        数据量

        :return: The limit of this ListDataclassFieldsRequest.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataclassFieldsRequest.

        数据量

        :param limit: The limit of this ListDataclassFieldsRequest.
        :type limit: float
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListDataclassFieldsRequest.

        名称查询

        :return: The name of this ListDataclassFieldsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDataclassFieldsRequest.

        名称查询

        :param name: The name of this ListDataclassFieldsRequest.
        :type name: str
        """
        self._name = name

    @property
    def is_built_in(self):
        """Gets the is_built_in of this ListDataclassFieldsRequest.

        是否内置

        :return: The is_built_in of this ListDataclassFieldsRequest.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """Sets the is_built_in of this ListDataclassFieldsRequest.

        是否内置

        :param is_built_in: The is_built_in of this ListDataclassFieldsRequest.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this ListDataclassFieldsRequest.

        数据类id

        :return: The dataclass_id of this ListDataclassFieldsRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this ListDataclassFieldsRequest.

        数据类id

        :param dataclass_id: The dataclass_id of this ListDataclassFieldsRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def field_category(self):
        """Gets the field_category of this ListDataclassFieldsRequest.

        字段分类

        :return: The field_category of this ListDataclassFieldsRequest.
        :rtype: str
        """
        return self._field_category

    @field_category.setter
    def field_category(self, field_category):
        """Sets the field_category of this ListDataclassFieldsRequest.

        字段分类

        :param field_category: The field_category of this ListDataclassFieldsRequest.
        :type field_category: str
        """
        self._field_category = field_category

    @property
    def mapping(self):
        """Gets the mapping of this ListDataclassFieldsRequest.

        是否展示在分类映射外的其他地方

        :return: The mapping of this ListDataclassFieldsRequest.
        :rtype: bool
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this ListDataclassFieldsRequest.

        是否展示在分类映射外的其他地方

        :param mapping: The mapping of this ListDataclassFieldsRequest.
        :type mapping: bool
        """
        self._mapping = mapping

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
        if not isinstance(other, ListDataclassFieldsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
