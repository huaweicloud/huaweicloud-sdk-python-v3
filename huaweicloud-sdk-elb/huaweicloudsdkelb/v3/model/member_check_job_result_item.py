# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberCheckJobResultItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'reason': 'str',
        'severity': 'str',
        'subject': 'str',
        'job_id': 'str',
        'reason_template': 'str',
        'reason_params': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'reason': 'reason',
        'severity': 'severity',
        'subject': 'subject',
        'job_id': 'job_id',
        'reason_template': 'reason_template',
        'reason_params': 'reason_params'
    }

    def __init__(self, name=None, reason=None, severity=None, subject=None, job_id=None, reason_template=None, reason_params=None):
        r"""MemberCheckJobResultItem

        The model defined in huaweicloud sdk

        :param name: **参数解释**：检查项名称。  **取值范围**：不涉及
        :type name: str
        :param reason: **参数解释**：异常原因。  **取值范围**：不涉及
        :type reason: str
        :param severity: **参数解释**：重要级别，分为Major(严重)和Tips(提示)。  **取值范围**：不涉及
        :type severity: str
        :param subject: **参数解释**：检查类别，config表示配置检查。  **取值范围**：不涉及
        :type subject: str
        :param job_id: **参数解释**：任务ID。  **取值范围**：不涉及
        :type job_id: str
        :param reason_template: **参数解释**：异常原因模板。  **取值范围**：不涉及
        :type reason_template: str
        :param reason_params: **参数解释**：异常结果变量参数表，用于结合异常原因模板动态生成异常原因。  **取值范围**：不涉及
        :type reason_params: list[str]
        """
        
        

        self._name = None
        self._reason = None
        self._severity = None
        self._subject = None
        self._job_id = None
        self._reason_template = None
        self._reason_params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason
        if severity is not None:
            self.severity = severity
        if subject is not None:
            self.subject = subject
        if job_id is not None:
            self.job_id = job_id
        if reason_template is not None:
            self.reason_template = reason_template
        if reason_params is not None:
            self.reason_params = reason_params

    @property
    def name(self):
        r"""Gets the name of this MemberCheckJobResultItem.

        **参数解释**：检查项名称。  **取值范围**：不涉及

        :return: The name of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MemberCheckJobResultItem.

        **参数解释**：检查项名称。  **取值范围**：不涉及

        :param name: The name of this MemberCheckJobResultItem.
        :type name: str
        """
        self._name = name

    @property
    def reason(self):
        r"""Gets the reason of this MemberCheckJobResultItem.

        **参数解释**：异常原因。  **取值范围**：不涉及

        :return: The reason of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this MemberCheckJobResultItem.

        **参数解释**：异常原因。  **取值范围**：不涉及

        :param reason: The reason of this MemberCheckJobResultItem.
        :type reason: str
        """
        self._reason = reason

    @property
    def severity(self):
        r"""Gets the severity of this MemberCheckJobResultItem.

        **参数解释**：重要级别，分为Major(严重)和Tips(提示)。  **取值范围**：不涉及

        :return: The severity of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this MemberCheckJobResultItem.

        **参数解释**：重要级别，分为Major(严重)和Tips(提示)。  **取值范围**：不涉及

        :param severity: The severity of this MemberCheckJobResultItem.
        :type severity: str
        """
        self._severity = severity

    @property
    def subject(self):
        r"""Gets the subject of this MemberCheckJobResultItem.

        **参数解释**：检查类别，config表示配置检查。  **取值范围**：不涉及

        :return: The subject of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this MemberCheckJobResultItem.

        **参数解释**：检查类别，config表示配置检查。  **取值范围**：不涉及

        :param subject: The subject of this MemberCheckJobResultItem.
        :type subject: str
        """
        self._subject = subject

    @property
    def job_id(self):
        r"""Gets the job_id of this MemberCheckJobResultItem.

        **参数解释**：任务ID。  **取值范围**：不涉及

        :return: The job_id of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this MemberCheckJobResultItem.

        **参数解释**：任务ID。  **取值范围**：不涉及

        :param job_id: The job_id of this MemberCheckJobResultItem.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def reason_template(self):
        r"""Gets the reason_template of this MemberCheckJobResultItem.

        **参数解释**：异常原因模板。  **取值范围**：不涉及

        :return: The reason_template of this MemberCheckJobResultItem.
        :rtype: str
        """
        return self._reason_template

    @reason_template.setter
    def reason_template(self, reason_template):
        r"""Sets the reason_template of this MemberCheckJobResultItem.

        **参数解释**：异常原因模板。  **取值范围**：不涉及

        :param reason_template: The reason_template of this MemberCheckJobResultItem.
        :type reason_template: str
        """
        self._reason_template = reason_template

    @property
    def reason_params(self):
        r"""Gets the reason_params of this MemberCheckJobResultItem.

        **参数解释**：异常结果变量参数表，用于结合异常原因模板动态生成异常原因。  **取值范围**：不涉及

        :return: The reason_params of this MemberCheckJobResultItem.
        :rtype: list[str]
        """
        return self._reason_params

    @reason_params.setter
    def reason_params(self, reason_params):
        r"""Sets the reason_params of this MemberCheckJobResultItem.

        **参数解释**：异常结果变量参数表，用于结合异常原因模板动态生成异常原因。  **取值范围**：不涉及

        :param reason_params: The reason_params of this MemberCheckJobResultItem.
        :type reason_params: list[str]
        """
        self._reason_params = reason_params

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
        if not isinstance(other, MemberCheckJobResultItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
