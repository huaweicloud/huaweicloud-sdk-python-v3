# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueAssociatedCommitsRequest:

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
        'issue_id': 'int',
        'type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_id': 'issue_id',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, issue_id=None, type=None, limit=None, offset=None):
        """ListIssueAssociatedCommitsRequest

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param issue_id: 工作项ID
        :type issue_id: int
        :param type: 查询类型：commit（提交记录） || branch（分支记录）
        :type type: str
        :param limit: 每页数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._project_id = None
        self._issue_id = None
        self._type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        self.issue_id = issue_id
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def project_id(self):
        """Gets the project_id of this ListIssueAssociatedCommitsRequest.

        devcloud项目的32位id

        :return: The project_id of this ListIssueAssociatedCommitsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListIssueAssociatedCommitsRequest.

        devcloud项目的32位id

        :param project_id: The project_id of this ListIssueAssociatedCommitsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_id(self):
        """Gets the issue_id of this ListIssueAssociatedCommitsRequest.

        工作项ID

        :return: The issue_id of this ListIssueAssociatedCommitsRequest.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this ListIssueAssociatedCommitsRequest.

        工作项ID

        :param issue_id: The issue_id of this ListIssueAssociatedCommitsRequest.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def type(self):
        """Gets the type of this ListIssueAssociatedCommitsRequest.

        查询类型：commit（提交记录） || branch（分支记录）

        :return: The type of this ListIssueAssociatedCommitsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListIssueAssociatedCommitsRequest.

        查询类型：commit（提交记录） || branch（分支记录）

        :param type: The type of this ListIssueAssociatedCommitsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListIssueAssociatedCommitsRequest.

        每页数量

        :return: The limit of this ListIssueAssociatedCommitsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssueAssociatedCommitsRequest.

        每页数量

        :param limit: The limit of this ListIssueAssociatedCommitsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListIssueAssociatedCommitsRequest.

        偏移量

        :return: The offset of this ListIssueAssociatedCommitsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIssueAssociatedCommitsRequest.

        偏移量

        :param offset: The offset of this ListIssueAssociatedCommitsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListIssueAssociatedCommitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
