# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommitsByRepoIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author': 'str',
        'begin_date': 'str',
        'end_date': 'str',
        'message': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'path': 'str',
        'ref_name': 'str',
        'repository_id': 'int',
        'stat_format': 'str'
    }

    attribute_map = {
        'author': 'author',
        'begin_date': 'begin_date',
        'end_date': 'end_date',
        'message': 'message',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'path': 'path',
        'ref_name': 'ref_name',
        'repository_id': 'repository_id',
        'stat_format': 'stat_format'
    }

    def __init__(self, author=None, begin_date=None, end_date=None, message=None, page_index=None, page_size=None, path=None, ref_name=None, repository_id=None, stat_format=None):
        """ShowCommitsByRepoIdRequest

        The model defined in huaweicloud sdk

        :param author: 提交作者
        :type author: str
        :param begin_date: 起始提交日期，格式为yyyy-MM-dd
        :type begin_date: str
        :param end_date: 终止提交日期，格式为yyyy-MM-dd
        :type end_date: str
        :param message: 提交信息
        :type message: str
        :param page_index: 分页索引
        :type page_index: int
        :param page_size: 每页数据量
        :type page_size: int
        :param path: 文件路径
        :type path: str
        :param ref_name: 分支或标签名，支持SHA格式
        :type ref_name: str
        :param repository_id: 仓库主键id
        :type repository_id: int
        :param stat_format: 提交的文件变更详情信息（不包含diff）
        :type stat_format: str
        """
        
        

        self._author = None
        self._begin_date = None
        self._end_date = None
        self._message = None
        self._page_index = None
        self._page_size = None
        self._path = None
        self._ref_name = None
        self._repository_id = None
        self._stat_format = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if begin_date is not None:
            self.begin_date = begin_date
        if end_date is not None:
            self.end_date = end_date
        if message is not None:
            self.message = message
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if path is not None:
            self.path = path
        self.ref_name = ref_name
        self.repository_id = repository_id
        if stat_format is not None:
            self.stat_format = stat_format

    @property
    def author(self):
        """Gets the author of this ShowCommitsByRepoIdRequest.

        提交作者

        :return: The author of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ShowCommitsByRepoIdRequest.

        提交作者

        :param author: The author of this ShowCommitsByRepoIdRequest.
        :type author: str
        """
        self._author = author

    @property
    def begin_date(self):
        """Gets the begin_date of this ShowCommitsByRepoIdRequest.

        起始提交日期，格式为yyyy-MM-dd

        :return: The begin_date of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this ShowCommitsByRepoIdRequest.

        起始提交日期，格式为yyyy-MM-dd

        :param begin_date: The begin_date of this ShowCommitsByRepoIdRequest.
        :type begin_date: str
        """
        self._begin_date = begin_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowCommitsByRepoIdRequest.

        终止提交日期，格式为yyyy-MM-dd

        :return: The end_date of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowCommitsByRepoIdRequest.

        终止提交日期，格式为yyyy-MM-dd

        :param end_date: The end_date of this ShowCommitsByRepoIdRequest.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def message(self):
        """Gets the message of this ShowCommitsByRepoIdRequest.

        提交信息

        :return: The message of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowCommitsByRepoIdRequest.

        提交信息

        :param message: The message of this ShowCommitsByRepoIdRequest.
        :type message: str
        """
        self._message = message

    @property
    def page_index(self):
        """Gets the page_index of this ShowCommitsByRepoIdRequest.

        分页索引

        :return: The page_index of this ShowCommitsByRepoIdRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ShowCommitsByRepoIdRequest.

        分页索引

        :param page_index: The page_index of this ShowCommitsByRepoIdRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ShowCommitsByRepoIdRequest.

        每页数据量

        :return: The page_size of this ShowCommitsByRepoIdRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowCommitsByRepoIdRequest.

        每页数据量

        :param page_size: The page_size of this ShowCommitsByRepoIdRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def path(self):
        """Gets the path of this ShowCommitsByRepoIdRequest.

        文件路径

        :return: The path of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowCommitsByRepoIdRequest.

        文件路径

        :param path: The path of this ShowCommitsByRepoIdRequest.
        :type path: str
        """
        self._path = path

    @property
    def ref_name(self):
        """Gets the ref_name of this ShowCommitsByRepoIdRequest.

        分支或标签名，支持SHA格式

        :return: The ref_name of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this ShowCommitsByRepoIdRequest.

        分支或标签名，支持SHA格式

        :param ref_name: The ref_name of this ShowCommitsByRepoIdRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def repository_id(self):
        """Gets the repository_id of this ShowCommitsByRepoIdRequest.

        仓库主键id

        :return: The repository_id of this ShowCommitsByRepoIdRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this ShowCommitsByRepoIdRequest.

        仓库主键id

        :param repository_id: The repository_id of this ShowCommitsByRepoIdRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def stat_format(self):
        """Gets the stat_format of this ShowCommitsByRepoIdRequest.

        提交的文件变更详情信息（不包含diff）

        :return: The stat_format of this ShowCommitsByRepoIdRequest.
        :rtype: str
        """
        return self._stat_format

    @stat_format.setter
    def stat_format(self, stat_format):
        """Sets the stat_format of this ShowCommitsByRepoIdRequest.

        提交的文件变更详情信息（不包含diff）

        :param stat_format: The stat_format of this ShowCommitsByRepoIdRequest.
        :type stat_format: str
        """
        self._stat_format = stat_format

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
        if not isinstance(other, ShowCommitsByRepoIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
