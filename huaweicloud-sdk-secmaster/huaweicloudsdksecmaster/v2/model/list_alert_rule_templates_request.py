# coding: utf-8

import six

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
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'severity': 'list[str]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'severity': 'severity'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, severity=None):
        r"""ListAlertRuleTemplatesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目 ID。Project ID.
        :type project_id: str
        :param workspace_id: 工作空间 ID。Workspace ID.
        :type workspace_id: str
        :param offset: 偏移量。Offset.
        :type offset: int
        :param limit: 条数。Limit.
        :type limit: int
        :param sort_key: 排序字段。Sort key
        :type sort_key: str
        :param sort_dir: 排序顺序，顺序、逆序。Sort direction, asc, desc。
        :type sort_dir: str
        :param severity: 严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: list[str]
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
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
        if severity is not None:
            self.severity = severity

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAlertRuleTemplatesRequest.

        项目 ID。Project ID.

        :return: The project_id of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAlertRuleTemplatesRequest.

        项目 ID。Project ID.

        :param project_id: The project_id of this ListAlertRuleTemplatesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAlertRuleTemplatesRequest.

        工作空间 ID。Workspace ID.

        :return: The workspace_id of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAlertRuleTemplatesRequest.

        工作空间 ID。Workspace ID.

        :param workspace_id: The workspace_id of this ListAlertRuleTemplatesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAlertRuleTemplatesRequest.

        偏移量。Offset.

        :return: The offset of this ListAlertRuleTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlertRuleTemplatesRequest.

        偏移量。Offset.

        :param offset: The offset of this ListAlertRuleTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlertRuleTemplatesRequest.

        条数。Limit.

        :return: The limit of this ListAlertRuleTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlertRuleTemplatesRequest.

        条数。Limit.

        :param limit: The limit of this ListAlertRuleTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAlertRuleTemplatesRequest.

        排序字段。Sort key

        :return: The sort_key of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAlertRuleTemplatesRequest.

        排序字段。Sort key

        :param sort_key: The sort_key of this ListAlertRuleTemplatesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAlertRuleTemplatesRequest.

        排序顺序，顺序、逆序。Sort direction, asc, desc。

        :return: The sort_dir of this ListAlertRuleTemplatesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAlertRuleTemplatesRequest.

        排序顺序，顺序、逆序。Sort direction, asc, desc。

        :param sort_dir: The sort_dir of this ListAlertRuleTemplatesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def severity(self):
        r"""Gets the severity of this ListAlertRuleTemplatesRequest.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this ListAlertRuleTemplatesRequest.
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListAlertRuleTemplatesRequest.

        严重程度，提示、低危、中危、高危、致命。Severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this ListAlertRuleTemplatesRequest.
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
        if not isinstance(other, ListAlertRuleTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
