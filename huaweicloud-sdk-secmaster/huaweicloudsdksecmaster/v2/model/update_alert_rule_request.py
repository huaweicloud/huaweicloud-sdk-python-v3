# coding: utf-8

import six

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
        'rule_id': 'str',
        'body': 'UpdateAlertRuleRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, rule_id=None, body=None):
        """UpdateAlertRuleRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目 ID。Project ID.
        :type project_id: str
        :param workspace_id: 工作空间 ID。Workspace ID.
        :type workspace_id: str
        :param rule_id: 告警规则 ID。Alert rule ID.
        :type rule_id: str
        :param body: Body of the UpdateAlertRuleRequest
        :type body: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this UpdateAlertRuleRequest.

        项目 ID。Project ID.

        :return: The project_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateAlertRuleRequest.

        项目 ID。Project ID.

        :param project_id: The project_id of this UpdateAlertRuleRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UpdateAlertRuleRequest.

        工作空间 ID。Workspace ID.

        :return: The workspace_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UpdateAlertRuleRequest.

        工作空间 ID。Workspace ID.

        :param workspace_id: The workspace_id of this UpdateAlertRuleRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def rule_id(self):
        """Gets the rule_id of this UpdateAlertRuleRequest.

        告警规则 ID。Alert rule ID.

        :return: The rule_id of this UpdateAlertRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this UpdateAlertRuleRequest.

        告警规则 ID。Alert rule ID.

        :param rule_id: The rule_id of this UpdateAlertRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        """Gets the body of this UpdateAlertRuleRequest.

        :return: The body of this UpdateAlertRuleRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAlertRuleRequest.

        :param body: The body of this UpdateAlertRuleRequest.
        :type body: :class:`huaweicloudsdksecmaster.v2.UpdateAlertRuleRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateAlertRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
