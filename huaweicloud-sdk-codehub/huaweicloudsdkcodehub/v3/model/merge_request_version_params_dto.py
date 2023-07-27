# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestVersionParamsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'diff_id': 'int',
        'start_sha': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'diff_id': 'diff_id',
        'start_sha': 'start_sha',
        'commit_id': 'commit_id'
    }

    def __init__(self, diff_id=None, start_sha=None, commit_id=None):
        """MergeRequestVersionParamsDto

        The model defined in huaweicloud sdk

        :param diff_id: MR最新变更id
        :type diff_id: int
        :param start_sha: 目标分支最新提交
        :type start_sha: str
        :param commit_id: 源分支最新提交
        :type commit_id: str
        """
        
        

        self._diff_id = None
        self._start_sha = None
        self._commit_id = None
        self.discriminator = None

        if diff_id is not None:
            self.diff_id = diff_id
        if start_sha is not None:
            self.start_sha = start_sha
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def diff_id(self):
        """Gets the diff_id of this MergeRequestVersionParamsDto.

        MR最新变更id

        :return: The diff_id of this MergeRequestVersionParamsDto.
        :rtype: int
        """
        return self._diff_id

    @diff_id.setter
    def diff_id(self, diff_id):
        """Sets the diff_id of this MergeRequestVersionParamsDto.

        MR最新变更id

        :param diff_id: The diff_id of this MergeRequestVersionParamsDto.
        :type diff_id: int
        """
        self._diff_id = diff_id

    @property
    def start_sha(self):
        """Gets the start_sha of this MergeRequestVersionParamsDto.

        目标分支最新提交

        :return: The start_sha of this MergeRequestVersionParamsDto.
        :rtype: str
        """
        return self._start_sha

    @start_sha.setter
    def start_sha(self, start_sha):
        """Sets the start_sha of this MergeRequestVersionParamsDto.

        目标分支最新提交

        :param start_sha: The start_sha of this MergeRequestVersionParamsDto.
        :type start_sha: str
        """
        self._start_sha = start_sha

    @property
    def commit_id(self):
        """Gets the commit_id of this MergeRequestVersionParamsDto.

        源分支最新提交

        :return: The commit_id of this MergeRequestVersionParamsDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this MergeRequestVersionParamsDto.

        源分支最新提交

        :param commit_id: The commit_id of this MergeRequestVersionParamsDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

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
        if not isinstance(other, MergeRequestVersionParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
