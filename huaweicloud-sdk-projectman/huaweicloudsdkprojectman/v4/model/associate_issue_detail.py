# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateIssueDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject': 'str',
        'issue_id': 'int',
        'project': 'SimpleProject',
        'user': 'SimpleUser',
        'status': 'StatusVo'
    }

    attribute_map = {
        'subject': 'subject',
        'issue_id': 'issue_id',
        'project': 'project',
        'user': 'user',
        'status': 'status'
    }

    def __init__(self, subject=None, issue_id=None, project=None, user=None, status=None):
        """AssociateIssueDetail

        The model defined in huaweicloud sdk

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
        
        

        self._subject = None
        self._issue_id = None
        self._project = None
        self._user = None
        self._status = None
        self.discriminator = None

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
    def subject(self):
        """Gets the subject of this AssociateIssueDetail.

        工作项标题

        :return: The subject of this AssociateIssueDetail.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this AssociateIssueDetail.

        工作项标题

        :param subject: The subject of this AssociateIssueDetail.
        :type subject: str
        """
        self._subject = subject

    @property
    def issue_id(self):
        """Gets the issue_id of this AssociateIssueDetail.

        工作项ID

        :return: The issue_id of this AssociateIssueDetail.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this AssociateIssueDetail.

        工作项ID

        :param issue_id: The issue_id of this AssociateIssueDetail.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def project(self):
        """Gets the project of this AssociateIssueDetail.

        :return: The project of this AssociateIssueDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this AssociateIssueDetail.

        :param project: The project of this AssociateIssueDetail.
        :type project: :class:`huaweicloudsdkprojectman.v4.SimpleProject`
        """
        self._project = project

    @property
    def user(self):
        """Gets the user of this AssociateIssueDetail.

        :return: The user of this AssociateIssueDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AssociateIssueDetail.

        :param user: The user of this AssociateIssueDetail.
        :type user: :class:`huaweicloudsdkprojectman.v4.SimpleUser`
        """
        self._user = user

    @property
    def status(self):
        """Gets the status of this AssociateIssueDetail.

        :return: The status of this AssociateIssueDetail.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusVo`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssociateIssueDetail.

        :param status: The status of this AssociateIssueDetail.
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
        if not isinstance(other, AssociateIssueDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
