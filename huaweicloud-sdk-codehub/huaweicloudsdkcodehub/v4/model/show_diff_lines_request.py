# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiffLinesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'file_path': 'str',
        'commit_id': 'str',
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'file_path': 'file_path',
        'commit_id': 'commit_id',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, repository_id=None, file_path=None, commit_id=None, start=None, end=None):
        r"""ShowDiffLinesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param file_path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type file_path: str
        :param commit_id: **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。
        :type commit_id: str
        :param start: **参数解释：** 文件开始行数。
        :type start: int
        :param end: **参数解释：** 文件结束行数。
        :type end: int
        """
        
        

        self._repository_id = None
        self._file_path = None
        self._commit_id = None
        self._start = None
        self._end = None
        self.discriminator = None

        self.repository_id = repository_id
        self.file_path = file_path
        self.commit_id = commit_id
        self.start = start
        self.end = end

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowDiffLinesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowDiffLinesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowDiffLinesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowDiffLinesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowDiffLinesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The file_path of this ShowDiffLinesRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowDiffLinesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param file_path: The file_path of this ShowDiffLinesRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ShowDiffLinesRequest.

        **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。

        :return: The commit_id of this ShowDiffLinesRequest.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ShowDiffLinesRequest.

        **参数解释：** commit ID。 **取值范围：** 字符串长度不少于1，不超过40。

        :param commit_id: The commit_id of this ShowDiffLinesRequest.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def start(self):
        r"""Gets the start of this ShowDiffLinesRequest.

        **参数解释：** 文件开始行数。

        :return: The start of this ShowDiffLinesRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ShowDiffLinesRequest.

        **参数解释：** 文件开始行数。

        :param start: The start of this ShowDiffLinesRequest.
        :type start: int
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this ShowDiffLinesRequest.

        **参数解释：** 文件结束行数。

        :return: The end of this ShowDiffLinesRequest.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this ShowDiffLinesRequest.

        **参数解释：** 文件结束行数。

        :param end: The end of this ShowDiffLinesRequest.
        :type end: int
        """
        self._end = end

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
        if not isinstance(other, ShowDiffLinesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
