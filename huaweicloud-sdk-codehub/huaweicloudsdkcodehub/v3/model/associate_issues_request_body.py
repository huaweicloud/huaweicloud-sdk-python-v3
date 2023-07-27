# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateIssuesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'str',
        'project_id': 'str',
        'related_id': 'list[str]',
        'repo_id': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'project_id': 'project_id',
        'related_id': 'related_id',
        'repo_id': 'repo_id'
    }

    def __init__(self, branch=None, project_id=None, related_id=None, repo_id=None):
        """AssociateIssuesRequestBody

        The model defined in huaweicloud sdk

        :param branch: 分支名
        :type branch: str
        :param project_id: 项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。
        :type project_id: str
        :param related_id: 工作项集合
        :type related_id: list[str]
        :param repo_id: 仓库id
        :type repo_id: str
        """
        
        

        self._branch = None
        self._project_id = None
        self._related_id = None
        self._repo_id = None
        self.discriminator = None

        self.branch = branch
        self.project_id = project_id
        self.related_id = related_id
        self.repo_id = repo_id

    @property
    def branch(self):
        """Gets the branch of this AssociateIssuesRequestBody.

        分支名

        :return: The branch of this AssociateIssuesRequestBody.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this AssociateIssuesRequestBody.

        分支名

        :param branch: The branch of this AssociateIssuesRequestBody.
        :type branch: str
        """
        self._branch = branch

    @property
    def project_id(self):
        """Gets the project_id of this AssociateIssuesRequestBody.

        项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。

        :return: The project_id of this AssociateIssuesRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssociateIssuesRequestBody.

        项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。

        :param project_id: The project_id of this AssociateIssuesRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def related_id(self):
        """Gets the related_id of this AssociateIssuesRequestBody.

        工作项集合

        :return: The related_id of this AssociateIssuesRequestBody.
        :rtype: list[str]
        """
        return self._related_id

    @related_id.setter
    def related_id(self, related_id):
        """Sets the related_id of this AssociateIssuesRequestBody.

        工作项集合

        :param related_id: The related_id of this AssociateIssuesRequestBody.
        :type related_id: list[str]
        """
        self._related_id = related_id

    @property
    def repo_id(self):
        """Gets the repo_id of this AssociateIssuesRequestBody.

        仓库id

        :return: The repo_id of this AssociateIssuesRequestBody.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this AssociateIssuesRequestBody.

        仓库id

        :param repo_id: The repo_id of this AssociateIssuesRequestBody.
        :type repo_id: str
        """
        self._repo_id = repo_id

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
        if not isinstance(other, AssociateIssuesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
