# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectorChannelsRequest:

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
        'title': 'str',
        'connection_module_id': 'str',
        'parser_id': 'str',
        'group_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'title': 'title',
        'connection_module_id': 'connection_module_id',
        'parser_id': 'parser_id',
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_id=None, workspace_id=None, title=None, connection_module_id=None, parser_id=None, group_id=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListCollectorChannelsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param title: 相关标题
        :type title: str
        :param connection_module_id: 链接模块ID
        :type connection_module_id: str
        :param parser_id: 解析器ID
        :type parser_id: str
        :param group_id: 组ID
        :type group_id: str
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
        self._title = None
        self._connection_module_id = None
        self._parser_id = None
        self._group_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if title is not None:
            self.title = title
        if connection_module_id is not None:
            self.connection_module_id = connection_module_id
        if parser_id is not None:
            self.parser_id = parser_id
        if group_id is not None:
            self.group_id = group_id
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
        r"""Gets the project_id of this ListCollectorChannelsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListCollectorChannelsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListCollectorChannelsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListCollectorChannelsRequest.

        工作空间ID

        :return: The workspace_id of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListCollectorChannelsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListCollectorChannelsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def title(self):
        r"""Gets the title of this ListCollectorChannelsRequest.

        相关标题

        :return: The title of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListCollectorChannelsRequest.

        相关标题

        :param title: The title of this ListCollectorChannelsRequest.
        :type title: str
        """
        self._title = title

    @property
    def connection_module_id(self):
        r"""Gets the connection_module_id of this ListCollectorChannelsRequest.

        链接模块ID

        :return: The connection_module_id of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._connection_module_id

    @connection_module_id.setter
    def connection_module_id(self, connection_module_id):
        r"""Sets the connection_module_id of this ListCollectorChannelsRequest.

        链接模块ID

        :param connection_module_id: The connection_module_id of this ListCollectorChannelsRequest.
        :type connection_module_id: str
        """
        self._connection_module_id = connection_module_id

    @property
    def parser_id(self):
        r"""Gets the parser_id of this ListCollectorChannelsRequest.

        解析器ID

        :return: The parser_id of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this ListCollectorChannelsRequest.

        解析器ID

        :param parser_id: The parser_id of this ListCollectorChannelsRequest.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ListCollectorChannelsRequest.

        组ID

        :return: The group_id of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListCollectorChannelsRequest.

        组ID

        :param group_id: The group_id of this ListCollectorChannelsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCollectorChannelsRequest.

        第几页

        :return: The offset of this ListCollectorChannelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCollectorChannelsRequest.

        第几页

        :param offset: The offset of this ListCollectorChannelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCollectorChannelsRequest.

        每页数量

        :return: The limit of this ListCollectorChannelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCollectorChannelsRequest.

        每页数量

        :param limit: The limit of this ListCollectorChannelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCollectorChannelsRequest.

        排序字段

        :return: The sort_key of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCollectorChannelsRequest.

        排序字段

        :param sort_key: The sort_key of this ListCollectorChannelsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCollectorChannelsRequest.

        **参数解释**: 目录排序 - asc 升序排列 - desc 降序排列  **约束限制** 不涉及 **取值范围**: - asc - desc  **默认值** 不涉及

        :return: The sort_dir of this ListCollectorChannelsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCollectorChannelsRequest.

        **参数解释**: 目录排序 - asc 升序排列 - desc 降序排列  **约束限制** 不涉及 **取值范围**: - asc - desc  **默认值** 不涉及

        :param sort_dir: The sort_dir of this ListCollectorChannelsRequest.
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
        if not isinstance(other, ListCollectorChannelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
