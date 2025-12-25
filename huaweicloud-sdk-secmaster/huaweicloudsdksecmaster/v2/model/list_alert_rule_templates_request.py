# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRuleTemplatesRequest:

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
        'template_name': 'str',
        'status': 'str',
        'severity': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'template_name': 'template_name',
        'status': 'status',
        'severity': 'severity',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, project_id=None, workspace_id=None, template_name=None, status=None, severity=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListAlertRuleTemplatesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及           
        :type status: str
        :param severity: **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及                 
        :type severity: str
        :param offset: **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type offset: int
        :param limit: **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及
        :type limit: int
        :param sort_key: 按照属性排序。
        :type sort_key: str
        :param sort_dir: 排序顺序，支持 &#x60;ASC&#x60; 或 &#x60;DESC&#x60;。
        :type sort_dir: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._template_name = None
        self._status = None
        self._severity = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if template_name is not None:
            self.template_name = template_name
        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity
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
        r"""Gets the project_id of this ListAlertRuleTemplatesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAlertRuleTemplatesRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListAlertRuleTemplatesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAlertRuleTemplatesRequest.

        工作空间ID

        :return: The workspace_id of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAlertRuleTemplatesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListAlertRuleTemplatesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ListAlertRuleTemplatesRequest.

        模板名称

        :return: The template_name of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ListAlertRuleTemplatesRequest.

        模板名称

        :param template_name: The template_name of this ListAlertRuleTemplatesRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def status(self):
        r"""Gets the status of this ListAlertRuleTemplatesRequest.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及           

        :return: The status of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAlertRuleTemplatesRequest.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及           

        :param status: The status of this ListAlertRuleTemplatesRequest.
        :type status: str
        """
        self._status = status

    @property
    def severity(self):
        r"""Gets the severity of this ListAlertRuleTemplatesRequest.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及                 

        :return: The severity of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListAlertRuleTemplatesRequest.

        **参数解释**: 告警等级 - TIPS 提示 - LOW 低危 - MEDIUM 中危 - HIGH 高危 - FATAL 致命  **约束限制** 不涉及 **取值范围**: - TIPS - LOW - MEDIUM - HIGH - FATAL  **默认值** 不涉及                 

        :param severity: The severity of this ListAlertRuleTemplatesRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def offset(self):
        r"""Gets the offset of this ListAlertRuleTemplatesRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The offset of this ListAlertRuleTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlertRuleTemplatesRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param offset: The offset of this ListAlertRuleTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlertRuleTemplatesRequest.

        **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及

        :return: The limit of this ListAlertRuleTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlertRuleTemplatesRequest.

        **参数解释：** 查询数据限制 **取值范围：** 0-1000 **默认取值：** 不涉及

        :param limit: The limit of this ListAlertRuleTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAlertRuleTemplatesRequest.

        按照属性排序。

        :return: The sort_key of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAlertRuleTemplatesRequest.

        按照属性排序。

        :param sort_key: The sort_key of this ListAlertRuleTemplatesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAlertRuleTemplatesRequest.

        排序顺序，支持 `ASC` 或 `DESC`。

        :return: The sort_dir of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAlertRuleTemplatesRequest.

        排序顺序，支持 `ASC` 或 `DESC`。

        :param sort_dir: The sort_dir of this ListAlertRuleTemplatesRequest.
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
        if not isinstance(other, ListAlertRuleTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
