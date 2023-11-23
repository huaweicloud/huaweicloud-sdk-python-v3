# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_url': 'str',
        'web_url': 'str',
        'repo_status': 'str',
        'error_msg': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'https_url': 'https_url',
        'web_url': 'web_url',
        'repo_status': 'repo_status',
        'error_msg': 'error_msg',
        'project_id': 'project_id'
    }

    def __init__(self, https_url=None, web_url=None, repo_status=None, error_msg=None, project_id=None):
        """RepoInfo

        The model defined in huaweicloud sdk

        :param https_url: http地址
        :type https_url: str
        :param web_url: 存储库链接
        :type web_url: str
        :param repo_status: 存储库状态
        :type repo_status: str
        :param error_msg: 报错信息
        :type error_msg: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._https_url = None
        self._web_url = None
        self._repo_status = None
        self._error_msg = None
        self._project_id = None
        self.discriminator = None

        if https_url is not None:
            self.https_url = https_url
        if web_url is not None:
            self.web_url = web_url
        if repo_status is not None:
            self.repo_status = repo_status
        if error_msg is not None:
            self.error_msg = error_msg
        if project_id is not None:
            self.project_id = project_id

    @property
    def https_url(self):
        """Gets the https_url of this RepoInfo.

        http地址

        :return: The https_url of this RepoInfo.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """Sets the https_url of this RepoInfo.

        http地址

        :param https_url: The https_url of this RepoInfo.
        :type https_url: str
        """
        self._https_url = https_url

    @property
    def web_url(self):
        """Gets the web_url of this RepoInfo.

        存储库链接

        :return: The web_url of this RepoInfo.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this RepoInfo.

        存储库链接

        :param web_url: The web_url of this RepoInfo.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def repo_status(self):
        """Gets the repo_status of this RepoInfo.

        存储库状态

        :return: The repo_status of this RepoInfo.
        :rtype: str
        """
        return self._repo_status

    @repo_status.setter
    def repo_status(self, repo_status):
        """Sets the repo_status of this RepoInfo.

        存储库状态

        :param repo_status: The repo_status of this RepoInfo.
        :type repo_status: str
        """
        self._repo_status = repo_status

    @property
    def error_msg(self):
        """Gets the error_msg of this RepoInfo.

        报错信息

        :return: The error_msg of this RepoInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RepoInfo.

        报错信息

        :param error_msg: The error_msg of this RepoInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def project_id(self):
        """Gets the project_id of this RepoInfo.

        项目id

        :return: The project_id of this RepoInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepoInfo.

        项目id

        :param project_id: The project_id of this RepoInfo.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, RepoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
