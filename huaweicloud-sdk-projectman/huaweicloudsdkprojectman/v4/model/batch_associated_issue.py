# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssociatedIssue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_issue_id': 'int',
        'subject': 'str',
        'issue_id': 'int',
        'project': 'SimpleProject',
        'user': 'SimpleUser',
        'status': 'StatusVo'
    }

    attribute_map = {
        'source_issue_id': 'source_issue_id',
        'subject': 'subject',
        'issue_id': 'issue_id',
        'project': 'project',
        'user': 'user',
        'status': 'status'
    }

    def __init__(self, source_issue_id=None, subject=None, issue_id=None, project=None, user=None, status=None):
        r"""BatchAssociatedIssue

        The model defined in huaweicloud sdk

        :param source_issue_id: 关联工作项ID
        :type source_issue_id: int
        :param subject: 工作项标题
        :type subject: str
        :param issue_id: 工作项ID
        :type issue_id: int
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        :param user: 
        :type user: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        
        

        self._source_issue_id = None
        self._subject = None
        self._issue_id = None
        self._project = None
        self._user = None
        self._status = None
        self.discriminator = None

        if source_issue_id is not None:
            self.source_issue_id = source_issue_id
        if subject is not None:
            self.subject = subject
        if issue_id is not None:
            self.issue_id = issue_id
        if project is not None:
            self.project = project
        if user is not None:
            self.user = user
        if status is not None:
            self.status = status

    @property
    def source_issue_id(self):
        r"""Gets the source_issue_id of this BatchAssociatedIssue.

        关联工作项ID

        :return: The source_issue_id of this BatchAssociatedIssue.
        :rtype: int
        """
        return self._source_issue_id

    @source_issue_id.setter
    def source_issue_id(self, source_issue_id):
        r"""Sets the source_issue_id of this BatchAssociatedIssue.

        关联工作项ID

        :param source_issue_id: The source_issue_id of this BatchAssociatedIssue.
        :type source_issue_id: int
        """
        self._source_issue_id = source_issue_id

    @property
    def subject(self):
        r"""Gets the subject of this BatchAssociatedIssue.

        工作项标题

        :return: The subject of this BatchAssociatedIssue.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this BatchAssociatedIssue.

        工作项标题

        :param subject: The subject of this BatchAssociatedIssue.
        :type subject: str
        """
        self._subject = subject

    @property
    def issue_id(self):
        r"""Gets the issue_id of this BatchAssociatedIssue.

        工作项ID

        :return: The issue_id of this BatchAssociatedIssue.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this BatchAssociatedIssue.

        工作项ID

        :param issue_id: The issue_id of this BatchAssociatedIssue.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def project(self):
        r"""Gets the project of this BatchAssociatedIssue.

        :return: The project of this BatchAssociatedIssue.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this BatchAssociatedIssue.

        :param project: The project of this BatchAssociatedIssue.
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        self._project = project

    @property
    def user(self):
        r"""Gets the user of this BatchAssociatedIssue.

        :return: The user of this BatchAssociatedIssue.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this BatchAssociatedIssue.

        :param user: The user of this BatchAssociatedIssue.
        :type user: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._user = user

    @property
    def status(self):
        r"""Gets the status of this BatchAssociatedIssue.

        :return: The status of this BatchAssociatedIssue.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchAssociatedIssue.

        :param status: The status of this BatchAssociatedIssue.
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        self._status = status

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
        if not isinstance(other, BatchAssociatedIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
