# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLayoutWizardsRequest:

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
        'layout_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'layout_id': 'layout_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_id=None, workspace_id=None, layout_id=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListLayoutWizardsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param offset: 分页
        :type offset: int
        :param limit: **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type limit: int
        :param sort_key: **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time
        :type sort_key: str
        :param sort_dir: **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC
        :type sort_dir: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._layout_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.layout_id = layout_id
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
        r"""Gets the project_id of this ListLayoutWizardsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListLayoutWizardsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListLayoutWizardsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListLayoutWizardsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListLayoutWizardsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this ListLayoutWizardsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListLayoutWizardsRequest.

        **参数解释：** 工作空间id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this ListLayoutWizardsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def layout_id(self):
        r"""Gets the layout_id of this ListLayoutWizardsRequest.

        布局ID

        :return: The layout_id of this ListLayoutWizardsRequest.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this ListLayoutWizardsRequest.

        布局ID

        :param layout_id: The layout_id of this ListLayoutWizardsRequest.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def offset(self):
        r"""Gets the offset of this ListLayoutWizardsRequest.

        分页

        :return: The offset of this ListLayoutWizardsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLayoutWizardsRequest.

        分页

        :param offset: The offset of this ListLayoutWizardsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLayoutWizardsRequest.

        **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The limit of this ListLayoutWizardsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLayoutWizardsRequest.

        **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param limit: The limit of this ListLayoutWizardsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListLayoutWizardsRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :return: The sort_key of this ListLayoutWizardsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListLayoutWizardsRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :param sort_key: The sort_key of this ListLayoutWizardsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListLayoutWizardsRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :return: The sort_dir of this ListLayoutWizardsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListLayoutWizardsRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :param sort_dir: The sort_dir of this ListLayoutWizardsRequest.
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
        if not isinstance(other, ListLayoutWizardsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
