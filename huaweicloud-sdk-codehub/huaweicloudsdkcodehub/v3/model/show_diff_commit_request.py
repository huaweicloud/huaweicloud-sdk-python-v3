# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiffCommitRequest:

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
        'sha': 'str'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'sha': 'sha'
    }

    def __init__(self, repo_id=None, sha=None):
        """ShowDiffCommitRequest

        The model defined in huaweicloud sdk

        :param repo_id: 仓库短id
        :type repo_id: int
        :param sha: commit id，仓库的branch名或tag名
        :type sha: str
        """
        
        

        self._repo_id = None
        self._sha = None
        self.discriminator = None

        self.repo_id = repo_id
        self.sha = sha

    @property
    def repo_id(self):
        """Gets the repo_id of this ShowDiffCommitRequest.

        仓库短id

        :return: The repo_id of this ShowDiffCommitRequest.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this ShowDiffCommitRequest.

        仓库短id

        :param repo_id: The repo_id of this ShowDiffCommitRequest.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def sha(self):
        """Gets the sha of this ShowDiffCommitRequest.

        commit id，仓库的branch名或tag名

        :return: The sha of this ShowDiffCommitRequest.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ShowDiffCommitRequest.

        commit id，仓库的branch名或tag名

        :param sha: The sha of this ShowDiffCommitRequest.
        :type sha: str
        """
        self._sha = sha

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
        if not isinstance(other, ShowDiffCommitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
