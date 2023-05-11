# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRulesRequest:

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
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'pipe_id': 'str',
        'rule_name': 'str',
        'rule_id': 'str',
        'status': 'list[str]',
        'severity': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'pipe_id': 'pipe_id',
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'status': 'status',
        'severity': 'severity'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, pipe_id=None, rule_name=None, rule_id=None, status=None, severity=None):
        """ListAlertRulesRequest

        The model defined in huaweicloud sdk

        :param project_id: project_id
        :type project_id: str
        :param workspace_id: workspace_id
        :type workspace_id: str
        :param offset: offset
        :type offset: int
        :param limit: limit
        :type limit: int
        :param sort_key: sort_key
        :type sort_key: str
        :param sort_dir: sort_dir. asc, desc
        :type sort_dir: str
        :param pipe_id: pipe_id
        :type pipe_id: str
        :param rule_name: rule_name
        :type rule_name: str
        :param rule_id: rule_id
        :type rule_id: str
        :param status: status. ENABLED, DISABLED
        :type status: list[str]
        :param severity: severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: list[str]
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._pipe_id = None
        self._rule_name = None
        self._rule_id = None
        self._status = None
        self._severity = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.offset = offset
        self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_id is not None:
            self.rule_id = rule_id
        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity

    @property
    def project_id(self):
        """Gets the project_id of this ListAlertRulesRequest.

        project_id

        :return: The project_id of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListAlertRulesRequest.

        project_id

        :param project_id: The project_id of this ListAlertRulesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListAlertRulesRequest.

        workspace_id

        :return: The workspace_id of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListAlertRulesRequest.

        workspace_id

        :param workspace_id: The workspace_id of this ListAlertRulesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        """Gets the offset of this ListAlertRulesRequest.

        offset

        :return: The offset of this ListAlertRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlertRulesRequest.

        offset

        :param offset: The offset of this ListAlertRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlertRulesRequest.

        limit

        :return: The limit of this ListAlertRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlertRulesRequest.

        limit

        :param limit: The limit of this ListAlertRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAlertRulesRequest.

        sort_key

        :return: The sort_key of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAlertRulesRequest.

        sort_key

        :param sort_key: The sort_key of this ListAlertRulesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAlertRulesRequest.

        sort_dir. asc, desc

        :return: The sort_dir of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAlertRulesRequest.

        sort_dir. asc, desc

        :param sort_dir: The sort_dir of this ListAlertRulesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def pipe_id(self):
        """Gets the pipe_id of this ListAlertRulesRequest.

        pipe_id

        :return: The pipe_id of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        """Sets the pipe_id of this ListAlertRulesRequest.

        pipe_id

        :param pipe_id: The pipe_id of this ListAlertRulesRequest.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ListAlertRulesRequest.

        rule_name

        :return: The rule_name of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListAlertRulesRequest.

        rule_name

        :param rule_name: The rule_name of this ListAlertRulesRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        """Gets the rule_id of this ListAlertRulesRequest.

        rule_id

        :return: The rule_id of this ListAlertRulesRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ListAlertRulesRequest.

        rule_id

        :param rule_id: The rule_id of this ListAlertRulesRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def status(self):
        """Gets the status of this ListAlertRulesRequest.

        status. ENABLED, DISABLED

        :return: The status of this ListAlertRulesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAlertRulesRequest.

        status. ENABLED, DISABLED

        :param status: The status of this ListAlertRulesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def severity(self):
        """Gets the severity of this ListAlertRulesRequest.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this ListAlertRulesRequest.
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ListAlertRulesRequest.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this ListAlertRulesRequest.
        :type severity: list[str]
        """
        self._severity = severity

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
        if not isinstance(other, ListAlertRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
