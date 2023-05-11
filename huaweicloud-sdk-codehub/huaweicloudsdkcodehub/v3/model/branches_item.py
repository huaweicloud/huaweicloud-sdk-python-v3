# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BranchesItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit': 'CommitV2',
        'diverging_commit_counts': 'DivergingCommitCounts',
        'name': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'diverging_commit_counts': 'diverging_commit_counts',
        'name': 'name'
    }

    def __init__(self, commit=None, diverging_commit_counts=None, name=None):
        """BranchesItem

        The model defined in huaweicloud sdk

        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitV2`
        :param diverging_commit_counts: 
        :type diverging_commit_counts: :class:`huaweicloudsdkcodehub.v3.DivergingCommitCounts`
        :param name: 分支名
        :type name: str
        """
        
        

        self._commit = None
        self._diverging_commit_counts = None
        self._name = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if diverging_commit_counts is not None:
            self.diverging_commit_counts = diverging_commit_counts
        if name is not None:
            self.name = name

    @property
    def commit(self):
        """Gets the commit of this BranchesItem.

        :return: The commit of this BranchesItem.
        :rtype: :class:`huaweicloudsdkcodehub.v3.CommitV2`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this BranchesItem.

        :param commit: The commit of this BranchesItem.
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitV2`
        """
        self._commit = commit

    @property
    def diverging_commit_counts(self):
        """Gets the diverging_commit_counts of this BranchesItem.

        :return: The diverging_commit_counts of this BranchesItem.
        :rtype: :class:`huaweicloudsdkcodehub.v3.DivergingCommitCounts`
        """
        return self._diverging_commit_counts

    @diverging_commit_counts.setter
    def diverging_commit_counts(self, diverging_commit_counts):
        """Sets the diverging_commit_counts of this BranchesItem.

        :param diverging_commit_counts: The diverging_commit_counts of this BranchesItem.
        :type diverging_commit_counts: :class:`huaweicloudsdkcodehub.v3.DivergingCommitCounts`
        """
        self._diverging_commit_counts = diverging_commit_counts

    @property
    def name(self):
        """Gets the name of this BranchesItem.

        分支名

        :return: The name of this BranchesItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchesItem.

        分支名

        :param name: The name of this BranchesItem.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, BranchesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
