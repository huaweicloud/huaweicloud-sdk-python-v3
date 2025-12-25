# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectorInstancesRequest:

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
        'channel_id': 'str',
        'node_id': 'str',
        'node_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'channel_id': 'channel_id',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_id=None, workspace_id=None, channel_id=None, node_id=None, node_name=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListCollectorInstancesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param channel_id: 采集通道ID
        :type channel_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param node_name: 节点Name
        :type node_name: str
        :param offset: 第几页
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: **参数解释**: 目录排序 - asc 升序排列 - desc 降序排列  **约束限制** 不涉及 **取值范围**: - asc - desc  **默认值** 不涉及
        :type sort_dir: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._channel_id = None
        self._node_id = None
        self._node_name = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if channel_id is not None:
            self.channel_id = channel_id
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def project_id(self):
        r"""Gets the project_id of this ListCollectorInstancesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListCollectorInstancesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListCollectorInstancesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListCollectorInstancesRequest.

        工作空间ID

        :return: The workspace_id of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListCollectorInstancesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListCollectorInstancesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ListCollectorInstancesRequest.

        采集通道ID

        :return: The channel_id of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ListCollectorInstancesRequest.

        采集通道ID

        :param channel_id: The channel_id of this ListCollectorInstancesRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListCollectorInstancesRequest.

        节点ID

        :return: The node_id of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListCollectorInstancesRequest.

        节点ID

        :param node_id: The node_id of this ListCollectorInstancesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ListCollectorInstancesRequest.

        节点Name

        :return: The node_name of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ListCollectorInstancesRequest.

        节点Name

        :param node_name: The node_name of this ListCollectorInstancesRequest.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def offset(self):
        r"""Gets the offset of this ListCollectorInstancesRequest.

        第几页

        :return: The offset of this ListCollectorInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCollectorInstancesRequest.

        第几页

        :param offset: The offset of this ListCollectorInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCollectorInstancesRequest.

        每页数量

        :return: The limit of this ListCollectorInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCollectorInstancesRequest.

        每页数量

        :param limit: The limit of this ListCollectorInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCollectorInstancesRequest.

        排序字段

        :return: The sort_key of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCollectorInstancesRequest.

        排序字段

        :param sort_key: The sort_key of this ListCollectorInstancesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCollectorInstancesRequest.

        **参数解释**: 目录排序 - asc 升序排列 - desc 降序排列  **约束限制** 不涉及 **取值范围**: - asc - desc  **默认值** 不涉及

        :return: The sort_dir of this ListCollectorInstancesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCollectorInstancesRequest.

        **参数解释**: 目录排序 - asc 升序排列 - desc 降序排列  **约束限制** 不涉及 **取值范围**: - asc - desc  **默认值** 不涉及

        :param sort_dir: The sort_dir of this ListCollectorInstancesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListCollectorInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
