# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBuildJobScm:

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
        'url': 'str',
        'repo_id': 'str',
        'web_url': 'str',
        'scm_type': 'str',
        'is_auto_build': 'bool',
        'build_type': 'str',
        'depth': 'str',
        'end_point_id': 'str',
        'source': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'url': 'url',
        'repo_id': 'repo_id',
        'web_url': 'web_url',
        'scm_type': 'scm_type',
        'is_auto_build': 'is_auto_build',
        'build_type': 'build_type',
        'depth': 'depth',
        'end_point_id': 'end_point_id',
        'source': 'source'
    }

    def __init__(self, branch=None, url=None, repo_id=None, web_url=None, scm_type=None, is_auto_build=None, build_type=None, depth=None, end_point_id=None, source=None):
        """CreateBuildJobScm

        The model defined in huaweicloud sdk

        :param branch: 代码分支
        :type branch: str
        :param url: 代码仓地址
        :type url: str
        :param repo_id: repo的id
        :type repo_id: str
        :param web_url: 代码仓http地址
        :type web_url: str
        :param scm_type: 仓库类别，codehub还是github等等
        :type scm_type: str
        :param is_auto_build: 是否自动构建
        :type is_auto_build: bool
        :param build_type: 构建类别
        :type build_type: str
        :param depth: 克隆深度
        :type depth: str
        :param end_point_id: endpointId
        :type end_point_id: str
        :param source: source
        :type source: str
        """
        
        

        self._branch = None
        self._url = None
        self._repo_id = None
        self._web_url = None
        self._scm_type = None
        self._is_auto_build = None
        self._build_type = None
        self._depth = None
        self._end_point_id = None
        self._source = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        self.url = url
        if repo_id is not None:
            self.repo_id = repo_id
        if web_url is not None:
            self.web_url = web_url
        self.scm_type = scm_type
        if is_auto_build is not None:
            self.is_auto_build = is_auto_build
        if build_type is not None:
            self.build_type = build_type
        if depth is not None:
            self.depth = depth
        if end_point_id is not None:
            self.end_point_id = end_point_id
        if source is not None:
            self.source = source

    @property
    def branch(self):
        """Gets the branch of this CreateBuildJobScm.

        代码分支

        :return: The branch of this CreateBuildJobScm.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this CreateBuildJobScm.

        代码分支

        :param branch: The branch of this CreateBuildJobScm.
        :type branch: str
        """
        self._branch = branch

    @property
    def url(self):
        """Gets the url of this CreateBuildJobScm.

        代码仓地址

        :return: The url of this CreateBuildJobScm.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateBuildJobScm.

        代码仓地址

        :param url: The url of this CreateBuildJobScm.
        :type url: str
        """
        self._url = url

    @property
    def repo_id(self):
        """Gets the repo_id of this CreateBuildJobScm.

        repo的id

        :return: The repo_id of this CreateBuildJobScm.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this CreateBuildJobScm.

        repo的id

        :param repo_id: The repo_id of this CreateBuildJobScm.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def web_url(self):
        """Gets the web_url of this CreateBuildJobScm.

        代码仓http地址

        :return: The web_url of this CreateBuildJobScm.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this CreateBuildJobScm.

        代码仓http地址

        :param web_url: The web_url of this CreateBuildJobScm.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def scm_type(self):
        """Gets the scm_type of this CreateBuildJobScm.

        仓库类别，codehub还是github等等

        :return: The scm_type of this CreateBuildJobScm.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        """Sets the scm_type of this CreateBuildJobScm.

        仓库类别，codehub还是github等等

        :param scm_type: The scm_type of this CreateBuildJobScm.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def is_auto_build(self):
        """Gets the is_auto_build of this CreateBuildJobScm.

        是否自动构建

        :return: The is_auto_build of this CreateBuildJobScm.
        :rtype: bool
        """
        return self._is_auto_build

    @is_auto_build.setter
    def is_auto_build(self, is_auto_build):
        """Sets the is_auto_build of this CreateBuildJobScm.

        是否自动构建

        :param is_auto_build: The is_auto_build of this CreateBuildJobScm.
        :type is_auto_build: bool
        """
        self._is_auto_build = is_auto_build

    @property
    def build_type(self):
        """Gets the build_type of this CreateBuildJobScm.

        构建类别

        :return: The build_type of this CreateBuildJobScm.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this CreateBuildJobScm.

        构建类别

        :param build_type: The build_type of this CreateBuildJobScm.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def depth(self):
        """Gets the depth of this CreateBuildJobScm.

        克隆深度

        :return: The depth of this CreateBuildJobScm.
        :rtype: str
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this CreateBuildJobScm.

        克隆深度

        :param depth: The depth of this CreateBuildJobScm.
        :type depth: str
        """
        self._depth = depth

    @property
    def end_point_id(self):
        """Gets the end_point_id of this CreateBuildJobScm.

        endpointId

        :return: The end_point_id of this CreateBuildJobScm.
        :rtype: str
        """
        return self._end_point_id

    @end_point_id.setter
    def end_point_id(self, end_point_id):
        """Sets the end_point_id of this CreateBuildJobScm.

        endpointId

        :param end_point_id: The end_point_id of this CreateBuildJobScm.
        :type end_point_id: str
        """
        self._end_point_id = end_point_id

    @property
    def source(self):
        """Gets the source of this CreateBuildJobScm.

        source

        :return: The source of this CreateBuildJobScm.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateBuildJobScm.

        source

        :param source: The source of this CreateBuildJobScm.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, CreateBuildJobScm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
