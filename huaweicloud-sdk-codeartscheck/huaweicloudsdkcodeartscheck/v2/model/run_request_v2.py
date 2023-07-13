# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunRequestV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'access_token': 'str',
        'git_url': 'str',
        'git_branch': 'str'
    }

    attribute_map = {
        'username': 'username',
        'access_token': 'access_token',
        'git_url': 'git_url',
        'git_branch': 'git_branch'
    }

    def __init__(self, username=None, access_token=None, git_url=None, git_branch=None):
        """RunRequestV2

        The model defined in huaweicloud sdk

        :param username: 该任务对应临时仓库有权限的用户名
        :type username: str
        :param access_token: 该任务对应临时仓库有权限的用户token
        :type access_token: str
        :param git_url: 该任务对应的临时仓库地址
        :type git_url: str
        :param git_branch: 该任务对应的临时仓库分支
        :type git_branch: str
        """
        
        

        self._username = None
        self._access_token = None
        self._git_url = None
        self._git_branch = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if access_token is not None:
            self.access_token = access_token
        if git_url is not None:
            self.git_url = git_url
        if git_branch is not None:
            self.git_branch = git_branch

    @property
    def username(self):
        """Gets the username of this RunRequestV2.

        该任务对应临时仓库有权限的用户名

        :return: The username of this RunRequestV2.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RunRequestV2.

        该任务对应临时仓库有权限的用户名

        :param username: The username of this RunRequestV2.
        :type username: str
        """
        self._username = username

    @property
    def access_token(self):
        """Gets the access_token of this RunRequestV2.

        该任务对应临时仓库有权限的用户token

        :return: The access_token of this RunRequestV2.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RunRequestV2.

        该任务对应临时仓库有权限的用户token

        :param access_token: The access_token of this RunRequestV2.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def git_url(self):
        """Gets the git_url of this RunRequestV2.

        该任务对应的临时仓库地址

        :return: The git_url of this RunRequestV2.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this RunRequestV2.

        该任务对应的临时仓库地址

        :param git_url: The git_url of this RunRequestV2.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        """Gets the git_branch of this RunRequestV2.

        该任务对应的临时仓库分支

        :return: The git_branch of this RunRequestV2.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """Sets the git_branch of this RunRequestV2.

        该任务对应的临时仓库分支

        :param git_branch: The git_branch of this RunRequestV2.
        :type git_branch: str
        """
        self._git_branch = git_branch

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
        if not isinstance(other, RunRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
