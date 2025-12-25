# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertRuleRequest:

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
        'alert_rule_id': 'str',
        'body': 'UpdateAlertRuleRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'alert_rule_id': 'alert_rule_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, alert_rule_id=None, body=None):
        r"""UpdateAlertRuleRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param alert_rule_id: 告警规则 ID
        :type alert_rule_id: str
        :param body: Body of the UpdateAlertRuleRequest
        :type body: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._alert_rule_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.alert_rule_id = alert_rule_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateAlertRuleRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateAlertRuleRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this UpdateAlertRuleRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateAlertRuleRequest.

        工作空间ID

        :return: The workspace_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateAlertRuleRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateAlertRuleRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def alert_rule_id(self):
        r"""Gets the alert_rule_id of this UpdateAlertRuleRequest.

        告警规则 ID

        :return: The alert_rule_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._alert_rule_id

    @alert_rule_id.setter
    def alert_rule_id(self, alert_rule_id):
        r"""Sets the alert_rule_id of this UpdateAlertRuleRequest.

        告警规则 ID

        :param alert_rule_id: The alert_rule_id of this UpdateAlertRuleRequest.
        :type alert_rule_id: str
        """
        self._alert_rule_id = alert_rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAlertRuleRequest.

        :return: The body of this UpdateAlertRuleRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAlertRuleRequest.

        :param body: The body of this UpdateAlertRuleRequest.
        :type body: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateAlertRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
