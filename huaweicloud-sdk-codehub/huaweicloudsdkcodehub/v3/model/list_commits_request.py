# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommitsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'int',
        'ref_name': 'str',
        'since': 'str',
        'until': 'str',
        'path': 'str',
        'all': 'bool',
        'with_stats': 'bool',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'ref_name': 'ref_name',
        'since': 'since',
        'until': 'until',
        'path': 'path',
        'all': 'all',
        'with_stats': 'with_stats',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, repo_id=None, ref_name=None, since=None, until=None, path=None, all=None, with_stats=None, page=None, per_page=None):
        """ListCommitsRequest

        The model defined in huaweicloud sdk

        :param repo_id: 仓库短id
        :type repo_id: int
        :param ref_name: 仓库的branch名或tag名，如果为空则查询默认分支
        :type ref_name: str
        :param since: 在此日期之后或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ
        :type since: str
        :param until: 在此日期之前或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ
        :type until: str
        :param path: 文件路径
        :type path: str
        :param all: 是否检索仓库中每个提交
        :type all: bool
        :param with_stats: 有关每个提交的统计信息是否添加到响应中
        :type with_stats: bool
        :param page: 页码
        :type page: int
        :param per_page: 每页条目数
        :type per_page: int
        """
        
        

        self._repo_id = None
        self._ref_name = None
        self._since = None
        self._until = None
        self._path = None
        self._all = None
        self._with_stats = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        self.repo_id = repo_id
        if ref_name is not None:
            self.ref_name = ref_name
        if since is not None:
            self.since = since
        if until is not None:
            self.until = until
        if path is not None:
            self.path = path
        if all is not None:
            self.all = all
        if with_stats is not None:
            self.with_stats = with_stats
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def repo_id(self):
        """Gets the repo_id of this ListCommitsRequest.

        仓库短id

        :return: The repo_id of this ListCommitsRequest.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this ListCommitsRequest.

        仓库短id

        :param repo_id: The repo_id of this ListCommitsRequest.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def ref_name(self):
        """Gets the ref_name of this ListCommitsRequest.

        仓库的branch名或tag名，如果为空则查询默认分支

        :return: The ref_name of this ListCommitsRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this ListCommitsRequest.

        仓库的branch名或tag名，如果为空则查询默认分支

        :param ref_name: The ref_name of this ListCommitsRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def since(self):
        """Gets the since of this ListCommitsRequest.

        在此日期之后或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ

        :return: The since of this ListCommitsRequest.
        :rtype: str
        """
        return self._since

    @since.setter
    def since(self, since):
        """Sets the since of this ListCommitsRequest.

        在此日期之后或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ

        :param since: The since of this ListCommitsRequest.
        :type since: str
        """
        self._since = since

    @property
    def until(self):
        """Gets the until of this ListCommitsRequest.

        在此日期之前或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ

        :return: The until of this ListCommitsRequest.
        :rtype: str
        """
        return self._until

    @until.setter
    def until(self, until):
        """Sets the until of this ListCommitsRequest.

        在此日期之前或当天提交，格式 YYYY-MM-DDTHH:MM:SSZ

        :param until: The until of this ListCommitsRequest.
        :type until: str
        """
        self._until = until

    @property
    def path(self):
        """Gets the path of this ListCommitsRequest.

        文件路径

        :return: The path of this ListCommitsRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListCommitsRequest.

        文件路径

        :param path: The path of this ListCommitsRequest.
        :type path: str
        """
        self._path = path

    @property
    def all(self):
        """Gets the all of this ListCommitsRequest.

        是否检索仓库中每个提交

        :return: The all of this ListCommitsRequest.
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this ListCommitsRequest.

        是否检索仓库中每个提交

        :param all: The all of this ListCommitsRequest.
        :type all: bool
        """
        self._all = all

    @property
    def with_stats(self):
        """Gets the with_stats of this ListCommitsRequest.

        有关每个提交的统计信息是否添加到响应中

        :return: The with_stats of this ListCommitsRequest.
        :rtype: bool
        """
        return self._with_stats

    @with_stats.setter
    def with_stats(self, with_stats):
        """Sets the with_stats of this ListCommitsRequest.

        有关每个提交的统计信息是否添加到响应中

        :param with_stats: The with_stats of this ListCommitsRequest.
        :type with_stats: bool
        """
        self._with_stats = with_stats

    @property
    def page(self):
        """Gets the page of this ListCommitsRequest.

        页码

        :return: The page of this ListCommitsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCommitsRequest.

        页码

        :param page: The page of this ListCommitsRequest.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this ListCommitsRequest.

        每页条目数

        :return: The per_page of this ListCommitsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListCommitsRequest.

        每页条目数

        :param per_page: The per_page of this ListCommitsRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ListCommitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
