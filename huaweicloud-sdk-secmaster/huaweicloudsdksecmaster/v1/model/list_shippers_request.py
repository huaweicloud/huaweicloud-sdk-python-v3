# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShippersRequest:

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
        'dataspace_id': 'str',
        'pipe_id': 'str',
        'shipper_name': 'str',
        'shipper_source_region': 'str',
        'shipper_source_strategy': 'str',
        'shipper_consumption_type': 'str',
        'destination_shipper_type': 'str',
        'shipper_status': 'str',
        'create_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataspace_id': 'dataspace_id',
        'pipe_id': 'pipe_id',
        'shipper_name': 'shipper_name',
        'shipper_source_region': 'shipper_source_region',
        'shipper_source_strategy': 'shipper_source_strategy',
        'shipper_consumption_type': 'shipper_consumption_type',
        'destination_shipper_type': 'destination_shipper_type',
        'shipper_status': 'shipper_status',
        'create_time': 'create_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, workspace_id=None, dataspace_id=None, pipe_id=None, shipper_name=None, shipper_source_region=None, shipper_source_strategy=None, shipper_consumption_type=None, destination_shipper_type=None, shipper_status=None, create_time=None, limit=None, offset=None):
        r"""ListShippersRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param shipper_name: 投递名称
        :type shipper_name: str
        :param shipper_source_region: 数据源区域
        :type shipper_source_region: str
        :param shipper_source_strategy: 数据源消费策略
        :type shipper_source_strategy: str
        :param shipper_consumption_type: 数据源消费类型
        :type shipper_consumption_type: str
        :param destination_shipper_type: 目的投递类型
        :type destination_shipper_type: str
        :param shipper_status: 数据投递状态
        :type shipper_status: str
        :param create_time: 创建时间
        :type create_time: str
        :param limit: 每页数量
        :type limit: int
        :param offset: 第几页
        :type offset: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._dataspace_id = None
        self._pipe_id = None
        self._shipper_name = None
        self._shipper_source_region = None
        self._shipper_source_strategy = None
        self._shipper_consumption_type = None
        self._destination_shipper_type = None
        self._shipper_status = None
        self._create_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if shipper_name is not None:
            self.shipper_name = shipper_name
        if shipper_source_region is not None:
            self.shipper_source_region = shipper_source_region
        if shipper_source_strategy is not None:
            self.shipper_source_strategy = shipper_source_strategy
        if shipper_consumption_type is not None:
            self.shipper_consumption_type = shipper_consumption_type
        if destination_shipper_type is not None:
            self.destination_shipper_type = destination_shipper_type
        if shipper_status is not None:
            self.shipper_status = shipper_status
        if create_time is not None:
            self.create_time = create_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this ListShippersRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListShippersRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListShippersRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListShippersRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListShippersRequest.

        工作空间ID

        :return: The workspace_id of this ListShippersRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListShippersRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListShippersRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ListShippersRequest.

        数据空间ID

        :return: The dataspace_id of this ListShippersRequest.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ListShippersRequest.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ListShippersRequest.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ListShippersRequest.

        管道ID

        :return: The pipe_id of this ListShippersRequest.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ListShippersRequest.

        管道ID

        :param pipe_id: The pipe_id of this ListShippersRequest.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def shipper_name(self):
        r"""Gets the shipper_name of this ListShippersRequest.

        投递名称

        :return: The shipper_name of this ListShippersRequest.
        :rtype: str
        """
        return self._shipper_name

    @shipper_name.setter
    def shipper_name(self, shipper_name):
        r"""Sets the shipper_name of this ListShippersRequest.

        投递名称

        :param shipper_name: The shipper_name of this ListShippersRequest.
        :type shipper_name: str
        """
        self._shipper_name = shipper_name

    @property
    def shipper_source_region(self):
        r"""Gets the shipper_source_region of this ListShippersRequest.

        数据源区域

        :return: The shipper_source_region of this ListShippersRequest.
        :rtype: str
        """
        return self._shipper_source_region

    @shipper_source_region.setter
    def shipper_source_region(self, shipper_source_region):
        r"""Sets the shipper_source_region of this ListShippersRequest.

        数据源区域

        :param shipper_source_region: The shipper_source_region of this ListShippersRequest.
        :type shipper_source_region: str
        """
        self._shipper_source_region = shipper_source_region

    @property
    def shipper_source_strategy(self):
        r"""Gets the shipper_source_strategy of this ListShippersRequest.

        数据源消费策略

        :return: The shipper_source_strategy of this ListShippersRequest.
        :rtype: str
        """
        return self._shipper_source_strategy

    @shipper_source_strategy.setter
    def shipper_source_strategy(self, shipper_source_strategy):
        r"""Sets the shipper_source_strategy of this ListShippersRequest.

        数据源消费策略

        :param shipper_source_strategy: The shipper_source_strategy of this ListShippersRequest.
        :type shipper_source_strategy: str
        """
        self._shipper_source_strategy = shipper_source_strategy

    @property
    def shipper_consumption_type(self):
        r"""Gets the shipper_consumption_type of this ListShippersRequest.

        数据源消费类型

        :return: The shipper_consumption_type of this ListShippersRequest.
        :rtype: str
        """
        return self._shipper_consumption_type

    @shipper_consumption_type.setter
    def shipper_consumption_type(self, shipper_consumption_type):
        r"""Sets the shipper_consumption_type of this ListShippersRequest.

        数据源消费类型

        :param shipper_consumption_type: The shipper_consumption_type of this ListShippersRequest.
        :type shipper_consumption_type: str
        """
        self._shipper_consumption_type = shipper_consumption_type

    @property
    def destination_shipper_type(self):
        r"""Gets the destination_shipper_type of this ListShippersRequest.

        目的投递类型

        :return: The destination_shipper_type of this ListShippersRequest.
        :rtype: str
        """
        return self._destination_shipper_type

    @destination_shipper_type.setter
    def destination_shipper_type(self, destination_shipper_type):
        r"""Sets the destination_shipper_type of this ListShippersRequest.

        目的投递类型

        :param destination_shipper_type: The destination_shipper_type of this ListShippersRequest.
        :type destination_shipper_type: str
        """
        self._destination_shipper_type = destination_shipper_type

    @property
    def shipper_status(self):
        r"""Gets the shipper_status of this ListShippersRequest.

        数据投递状态

        :return: The shipper_status of this ListShippersRequest.
        :rtype: str
        """
        return self._shipper_status

    @shipper_status.setter
    def shipper_status(self, shipper_status):
        r"""Sets the shipper_status of this ListShippersRequest.

        数据投递状态

        :param shipper_status: The shipper_status of this ListShippersRequest.
        :type shipper_status: str
        """
        self._shipper_status = shipper_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ListShippersRequest.

        创建时间

        :return: The create_time of this ListShippersRequest.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListShippersRequest.

        创建时间

        :param create_time: The create_time of this ListShippersRequest.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def limit(self):
        r"""Gets the limit of this ListShippersRequest.

        每页数量

        :return: The limit of this ListShippersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListShippersRequest.

        每页数量

        :param limit: The limit of this ListShippersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListShippersRequest.

        第几页

        :return: The offset of this ListShippersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListShippersRequest.

        第几页

        :param offset: The offset of this ListShippersRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListShippersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
