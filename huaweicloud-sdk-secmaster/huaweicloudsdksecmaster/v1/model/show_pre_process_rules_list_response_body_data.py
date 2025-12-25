# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPreProcessRulesListResponseBodyData:

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
        'name': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'mapping_id': 'str',
        'mapper_id': 'str',
        'mapper_type_id': 'str',
        'action': 'str',
        'expression': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'mapping_id': 'mapping_id',
        'mapper_id': 'mapper_id',
        'mapper_type_id': 'mapper_type_id',
        'action': 'action',
        'expression': 'expression',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, project_id=None, workspace_id=None, mapping_id=None, mapper_id=None, mapper_type_id=None, action=None, expression=None, create_time=None, update_time=None):
        r"""ShowPreProcessRulesListResponseBodyData

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param name: 名称
        :type name: str
        :param project_id: 映射id
        :type project_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param mapper_id: 映射id
        :type mapper_id: str
        :param mapper_type_id: 映射id
        :type mapper_type_id: str
        :param action: 预处理选项: drop-丢弃
        :type action: str
        :param expression: 表达式
        :type expression: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._workspace_id = None
        self._mapping_id = None
        self._mapper_id = None
        self._mapper_type_id = None
        self._action = None
        self._expression = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if mapper_id is not None:
            self.mapper_id = mapper_id
        if mapper_type_id is not None:
            self.mapper_type_id = mapper_type_id
        if action is not None:
            self.action = action
        if expression is not None:
            self.expression = expression
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param id: The id of this ShowPreProcessRulesListResponseBodyData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPreProcessRulesListResponseBodyData.

        名称

        :return: The name of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPreProcessRulesListResponseBodyData.

        名称

        :param name: The name of this ShowPreProcessRulesListResponseBodyData.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The project_id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param project_id: The project_id of this ShowPreProcessRulesListResponseBodyData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The workspace_id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param workspace_id: The workspace_id of this ShowPreProcessRulesListResponseBodyData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The mapping_id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param mapping_id: The mapping_id of this ShowPreProcessRulesListResponseBodyData.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def mapper_id(self):
        r"""Gets the mapper_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The mapper_id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._mapper_id

    @mapper_id.setter
    def mapper_id(self, mapper_id):
        r"""Sets the mapper_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param mapper_id: The mapper_id of this ShowPreProcessRulesListResponseBodyData.
        :type mapper_id: str
        """
        self._mapper_id = mapper_id

    @property
    def mapper_type_id(self):
        r"""Gets the mapper_type_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :return: The mapper_type_id of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._mapper_type_id

    @mapper_type_id.setter
    def mapper_type_id(self, mapper_type_id):
        r"""Sets the mapper_type_id of this ShowPreProcessRulesListResponseBodyData.

        映射id

        :param mapper_type_id: The mapper_type_id of this ShowPreProcessRulesListResponseBodyData.
        :type mapper_type_id: str
        """
        self._mapper_type_id = mapper_type_id

    @property
    def action(self):
        r"""Gets the action of this ShowPreProcessRulesListResponseBodyData.

        预处理选项: drop-丢弃

        :return: The action of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowPreProcessRulesListResponseBodyData.

        预处理选项: drop-丢弃

        :param action: The action of this ShowPreProcessRulesListResponseBodyData.
        :type action: str
        """
        self._action = action

    @property
    def expression(self):
        r"""Gets the expression of this ShowPreProcessRulesListResponseBodyData.

        表达式

        :return: The expression of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this ShowPreProcessRulesListResponseBodyData.

        表达式

        :param expression: The expression of this ShowPreProcessRulesListResponseBodyData.
        :type expression: str
        """
        self._expression = expression

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPreProcessRulesListResponseBodyData.

        创建时间

        :return: The create_time of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPreProcessRulesListResponseBodyData.

        创建时间

        :param create_time: The create_time of this ShowPreProcessRulesListResponseBodyData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowPreProcessRulesListResponseBodyData.

        更新时间

        :return: The update_time of this ShowPreProcessRulesListResponseBodyData.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowPreProcessRulesListResponseBodyData.

        更新时间

        :param update_time: The update_time of this ShowPreProcessRulesListResponseBodyData.
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
        if not isinstance(other, ShowPreProcessRulesListResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
