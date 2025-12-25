# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDpeMapperRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mapping_id': 'str',
        'workspace_id': 'str',
        'project_id': 'str',
        'dataclass_id': 'str',
        'datasource_instance_id': 'str',
        'status': 'str',
        'name': 'str',
        'has_preprocess_rule': 'bool',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'mapping_id': 'mapping_id',
        'workspace_id': 'workspace_id',
        'project_id': 'project_id',
        'dataclass_id': 'dataclass_id',
        'datasource_instance_id': 'datasource_instance_id',
        'status': 'status',
        'name': 'name',
        'has_preprocess_rule': 'has_preprocess_rule',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, mapping_id=None, workspace_id=None, project_id=None, dataclass_id=None, datasource_instance_id=None, status=None, name=None, has_preprocess_rule=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""QueryDpeMapperRequestBody

        The model defined in huaweicloud sdk

        :param mapping_id: 映射id
        :type mapping_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param project_id: 映射id
        :type project_id: str
        :param dataclass_id: 映射id
        :type dataclass_id: str
        :param datasource_instance_id: 映射id
        :type datasource_instance_id: str
        :param status: 状态(enabled，disabled)
        :type status: str
        :param name: 名称
        :type name: str
        :param has_preprocess_rule: 是否配置预处理规则
        :type has_preprocess_rule: bool
        :param start_time: 开始时间
        :type start_time: datetime
        :param end_time: 结束时间
        :type end_time: datetime
        :param offset: **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释**: 当前页码 **约束限制**: 不涉及
        :type limit: int
        """
        
        

        self._mapping_id = None
        self._workspace_id = None
        self._project_id = None
        self._dataclass_id = None
        self._datasource_instance_id = None
        self._status = None
        self._name = None
        self._has_preprocess_rule = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.mapping_id = mapping_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if project_id is not None:
            self.project_id = project_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if datasource_instance_id is not None:
            self.datasource_instance_id = datasource_instance_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if has_preprocess_rule is not None:
            self.has_preprocess_rule = has_preprocess_rule
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this QueryDpeMapperRequestBody.

        映射id

        :return: The mapping_id of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this QueryDpeMapperRequestBody.

        映射id

        :param mapping_id: The mapping_id of this QueryDpeMapperRequestBody.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this QueryDpeMapperRequestBody.

        映射id

        :return: The workspace_id of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this QueryDpeMapperRequestBody.

        映射id

        :param workspace_id: The workspace_id of this QueryDpeMapperRequestBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def project_id(self):
        r"""Gets the project_id of this QueryDpeMapperRequestBody.

        映射id

        :return: The project_id of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this QueryDpeMapperRequestBody.

        映射id

        :param project_id: The project_id of this QueryDpeMapperRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this QueryDpeMapperRequestBody.

        映射id

        :return: The dataclass_id of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this QueryDpeMapperRequestBody.

        映射id

        :param dataclass_id: The dataclass_id of this QueryDpeMapperRequestBody.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def datasource_instance_id(self):
        r"""Gets the datasource_instance_id of this QueryDpeMapperRequestBody.

        映射id

        :return: The datasource_instance_id of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._datasource_instance_id

    @datasource_instance_id.setter
    def datasource_instance_id(self, datasource_instance_id):
        r"""Sets the datasource_instance_id of this QueryDpeMapperRequestBody.

        映射id

        :param datasource_instance_id: The datasource_instance_id of this QueryDpeMapperRequestBody.
        :type datasource_instance_id: str
        """
        self._datasource_instance_id = datasource_instance_id

    @property
    def status(self):
        r"""Gets the status of this QueryDpeMapperRequestBody.

        状态(enabled，disabled)

        :return: The status of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryDpeMapperRequestBody.

        状态(enabled，disabled)

        :param status: The status of this QueryDpeMapperRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this QueryDpeMapperRequestBody.

        名称

        :return: The name of this QueryDpeMapperRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryDpeMapperRequestBody.

        名称

        :param name: The name of this QueryDpeMapperRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def has_preprocess_rule(self):
        r"""Gets the has_preprocess_rule of this QueryDpeMapperRequestBody.

        是否配置预处理规则

        :return: The has_preprocess_rule of this QueryDpeMapperRequestBody.
        :rtype: bool
        """
        return self._has_preprocess_rule

    @has_preprocess_rule.setter
    def has_preprocess_rule(self, has_preprocess_rule):
        r"""Sets the has_preprocess_rule of this QueryDpeMapperRequestBody.

        是否配置预处理规则

        :param has_preprocess_rule: The has_preprocess_rule of this QueryDpeMapperRequestBody.
        :type has_preprocess_rule: bool
        """
        self._has_preprocess_rule = has_preprocess_rule

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryDpeMapperRequestBody.

        开始时间

        :return: The start_time of this QueryDpeMapperRequestBody.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryDpeMapperRequestBody.

        开始时间

        :param start_time: The start_time of this QueryDpeMapperRequestBody.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryDpeMapperRequestBody.

        结束时间

        :return: The end_time of this QueryDpeMapperRequestBody.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryDpeMapperRequestBody.

        结束时间

        :param end_time: The end_time of this QueryDpeMapperRequestBody.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this QueryDpeMapperRequestBody.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this QueryDpeMapperRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryDpeMapperRequestBody.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this QueryDpeMapperRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this QueryDpeMapperRequestBody.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :return: The limit of this QueryDpeMapperRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryDpeMapperRequestBody.

        **参数解释**: 当前页码 **约束限制**: 不涉及

        :param limit: The limit of this QueryDpeMapperRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, QueryDpeMapperRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
