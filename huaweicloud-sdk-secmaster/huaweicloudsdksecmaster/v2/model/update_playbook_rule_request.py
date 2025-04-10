# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePlaybookRuleRequest:

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
        'version_id': 'str',
        'rule_id': 'str',
        'body': 'ModifyRuleInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'version_id': 'version_id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, version_id=None, rule_id=None, body=None):
        r"""UpdatePlaybookRuleRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param version_id: 剧本版本ID
        :type version_id: str
        :param rule_id: 剧本规则ID
        :type rule_id: str
        :param body: Body of the UpdatePlaybookRuleRequest
        :type body: :class:`huaweicloudsdksecmaster.v2.ModifyRuleInfo`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._version_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.version_id = version_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdatePlaybookRuleRequest.

        项目ID

        :return: The project_id of this UpdatePlaybookRuleRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdatePlaybookRuleRequest.

        项目ID

        :param project_id: The project_id of this UpdatePlaybookRuleRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdatePlaybookRuleRequest.

        工作空间ID

        :return: The workspace_id of this UpdatePlaybookRuleRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdatePlaybookRuleRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdatePlaybookRuleRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdatePlaybookRuleRequest.

        剧本版本ID

        :return: The version_id of this UpdatePlaybookRuleRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdatePlaybookRuleRequest.

        剧本版本ID

        :param version_id: The version_id of this UpdatePlaybookRuleRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdatePlaybookRuleRequest.

        剧本规则ID

        :return: The rule_id of this UpdatePlaybookRuleRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdatePlaybookRuleRequest.

        剧本规则ID

        :param rule_id: The rule_id of this UpdatePlaybookRuleRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePlaybookRuleRequest.

        :return: The body of this UpdatePlaybookRuleRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v2.ModifyRuleInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePlaybookRuleRequest.

        :param body: The body of this UpdatePlaybookRuleRequest.
        :type body: :class:`huaweicloudsdksecmaster.v2.ModifyRuleInfo`
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
        if not isinstance(other, UpdatePlaybookRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
