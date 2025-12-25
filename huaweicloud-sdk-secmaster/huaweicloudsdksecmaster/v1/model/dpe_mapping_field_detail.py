# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeMappingFieldDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'dataclass_id': 'str',
        'mapping_id': 'str',
        'mapper_id': 'str',
        'default_value': 'str',
        'target_key': 'str',
        'expression': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataclass_id': 'dataclass_id',
        'mapping_id': 'mapping_id',
        'mapper_id': 'mapper_id',
        'default_value': 'default_value',
        'target_key': 'target_key',
        'expression': 'expression',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, project_id=None, workspace_id=None, dataclass_id=None, mapping_id=None, mapper_id=None, default_value=None, target_key=None, expression=None, create_time=None, update_time=None):
        r"""DpeMappingFieldDetail

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param project_id: 映射id
        :type project_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param dataclass_id: 映射id
        :type dataclass_id: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param mapper_id: 映射id
        :type mapper_id: str
        :param default_value: 默认值
        :type default_value: str
        :param target_key: 目标字段
        :type target_key: str
        :param expression: 表达式
        :type expression: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._project_id = None
        self._workspace_id = None
        self._dataclass_id = None
        self._mapping_id = None
        self._mapper_id = None
        self._default_value = None
        self._target_key = None
        self._expression = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if mapper_id is not None:
            self.mapper_id = mapper_id
        if default_value is not None:
            self.default_value = default_value
        if target_key is not None:
            self.target_key = target_key
        if expression is not None:
            self.expression = expression
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this DpeMappingFieldDetail.

        映射id

        :return: The id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DpeMappingFieldDetail.

        映射id

        :param id: The id of this DpeMappingFieldDetail.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this DpeMappingFieldDetail.

        映射id

        :return: The project_id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DpeMappingFieldDetail.

        映射id

        :param project_id: The project_id of this DpeMappingFieldDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DpeMappingFieldDetail.

        映射id

        :return: The workspace_id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DpeMappingFieldDetail.

        映射id

        :param workspace_id: The workspace_id of this DpeMappingFieldDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this DpeMappingFieldDetail.

        映射id

        :return: The dataclass_id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this DpeMappingFieldDetail.

        映射id

        :param dataclass_id: The dataclass_id of this DpeMappingFieldDetail.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this DpeMappingFieldDetail.

        映射id

        :return: The mapping_id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this DpeMappingFieldDetail.

        映射id

        :param mapping_id: The mapping_id of this DpeMappingFieldDetail.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def mapper_id(self):
        r"""Gets the mapper_id of this DpeMappingFieldDetail.

        映射id

        :return: The mapper_id of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._mapper_id

    @mapper_id.setter
    def mapper_id(self, mapper_id):
        r"""Sets the mapper_id of this DpeMappingFieldDetail.

        映射id

        :param mapper_id: The mapper_id of this DpeMappingFieldDetail.
        :type mapper_id: str
        """
        self._mapper_id = mapper_id

    @property
    def default_value(self):
        r"""Gets the default_value of this DpeMappingFieldDetail.

        默认值

        :return: The default_value of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this DpeMappingFieldDetail.

        默认值

        :param default_value: The default_value of this DpeMappingFieldDetail.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def target_key(self):
        r"""Gets the target_key of this DpeMappingFieldDetail.

        目标字段

        :return: The target_key of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._target_key

    @target_key.setter
    def target_key(self, target_key):
        r"""Sets the target_key of this DpeMappingFieldDetail.

        目标字段

        :param target_key: The target_key of this DpeMappingFieldDetail.
        :type target_key: str
        """
        self._target_key = target_key

    @property
    def expression(self):
        r"""Gets the expression of this DpeMappingFieldDetail.

        表达式

        :return: The expression of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this DpeMappingFieldDetail.

        表达式

        :param expression: The expression of this DpeMappingFieldDetail.
        :type expression: str
        """
        self._expression = expression

    @property
    def create_time(self):
        r"""Gets the create_time of this DpeMappingFieldDetail.

        创建时间

        :return: The create_time of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DpeMappingFieldDetail.

        创建时间

        :param create_time: The create_time of this DpeMappingFieldDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DpeMappingFieldDetail.

        更新时间

        :return: The update_time of this DpeMappingFieldDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DpeMappingFieldDetail.

        更新时间

        :param update_time: The update_time of this DpeMappingFieldDetail.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DpeMappingFieldDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
