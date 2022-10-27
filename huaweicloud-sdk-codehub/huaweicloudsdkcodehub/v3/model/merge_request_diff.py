# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestDiff:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'base_commit_sha': 'str',
        'commits_count': 'float',
        'created_at': 'str',
        'head_commit_sha': 'str',
        'merge_request_id': 'float',
        'start_commit_sha': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'base_commit_sha': 'base_commit_sha',
        'commits_count': 'commits_count',
        'created_at': 'created_at',
        'head_commit_sha': 'head_commit_sha',
        'merge_request_id': 'merge_request_id',
        'start_commit_sha': 'start_commit_sha',
        'updated_at': 'updated_at'
    }

    def __init__(self, base_commit_sha=None, commits_count=None, created_at=None, head_commit_sha=None, merge_request_id=None, start_commit_sha=None, updated_at=None):
        """MergeRequestDiff

        The model defined in huaweicloud sdk

        :param base_commit_sha: base提交
        :type base_commit_sha: str
        :param commits_count: 提交数
        :type commits_count: float
        :param created_at: 创建时间
        :type created_at: str
        :param head_commit_sha: head提交
        :type head_commit_sha: str
        :param merge_request_id: 合并请求id
        :type merge_request_id: float
        :param start_commit_sha: start提交
        :type start_commit_sha: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._base_commit_sha = None
        self._commits_count = None
        self._created_at = None
        self._head_commit_sha = None
        self._merge_request_id = None
        self._start_commit_sha = None
        self._updated_at = None
        self.discriminator = None

        if base_commit_sha is not None:
            self.base_commit_sha = base_commit_sha
        if commits_count is not None:
            self.commits_count = commits_count
        if created_at is not None:
            self.created_at = created_at
        if head_commit_sha is not None:
            self.head_commit_sha = head_commit_sha
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if start_commit_sha is not None:
            self.start_commit_sha = start_commit_sha
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def base_commit_sha(self):
        """Gets the base_commit_sha of this MergeRequestDiff.

        base提交

        :return: The base_commit_sha of this MergeRequestDiff.
        :rtype: str
        """
        return self._base_commit_sha

    @base_commit_sha.setter
    def base_commit_sha(self, base_commit_sha):
        """Sets the base_commit_sha of this MergeRequestDiff.

        base提交

        :param base_commit_sha: The base_commit_sha of this MergeRequestDiff.
        :type base_commit_sha: str
        """
        self._base_commit_sha = base_commit_sha

    @property
    def commits_count(self):
        """Gets the commits_count of this MergeRequestDiff.

        提交数

        :return: The commits_count of this MergeRequestDiff.
        :rtype: float
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        """Sets the commits_count of this MergeRequestDiff.

        提交数

        :param commits_count: The commits_count of this MergeRequestDiff.
        :type commits_count: float
        """
        self._commits_count = commits_count

    @property
    def created_at(self):
        """Gets the created_at of this MergeRequestDiff.

        创建时间

        :return: The created_at of this MergeRequestDiff.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MergeRequestDiff.

        创建时间

        :param created_at: The created_at of this MergeRequestDiff.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def head_commit_sha(self):
        """Gets the head_commit_sha of this MergeRequestDiff.

        head提交

        :return: The head_commit_sha of this MergeRequestDiff.
        :rtype: str
        """
        return self._head_commit_sha

    @head_commit_sha.setter
    def head_commit_sha(self, head_commit_sha):
        """Sets the head_commit_sha of this MergeRequestDiff.

        head提交

        :param head_commit_sha: The head_commit_sha of this MergeRequestDiff.
        :type head_commit_sha: str
        """
        self._head_commit_sha = head_commit_sha

    @property
    def merge_request_id(self):
        """Gets the merge_request_id of this MergeRequestDiff.

        合并请求id

        :return: The merge_request_id of this MergeRequestDiff.
        :rtype: float
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        """Sets the merge_request_id of this MergeRequestDiff.

        合并请求id

        :param merge_request_id: The merge_request_id of this MergeRequestDiff.
        :type merge_request_id: float
        """
        self._merge_request_id = merge_request_id

    @property
    def start_commit_sha(self):
        """Gets the start_commit_sha of this MergeRequestDiff.

        start提交

        :return: The start_commit_sha of this MergeRequestDiff.
        :rtype: str
        """
        return self._start_commit_sha

    @start_commit_sha.setter
    def start_commit_sha(self, start_commit_sha):
        """Sets the start_commit_sha of this MergeRequestDiff.

        start提交

        :param start_commit_sha: The start_commit_sha of this MergeRequestDiff.
        :type start_commit_sha: str
        """
        self._start_commit_sha = start_commit_sha

    @property
    def updated_at(self):
        """Gets the updated_at of this MergeRequestDiff.

        更新时间

        :return: The updated_at of this MergeRequestDiff.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MergeRequestDiff.

        更新时间

        :param updated_at: The updated_at of this MergeRequestDiff.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, MergeRequestDiff):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
