# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildInfoRecordCommitInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit_id': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'commit_id': 'commit_id',
        'created_at': 'created_at'
    }

    def __init__(self, commit_id=None, created_at=None):
        r"""BuildInfoRecordCommitInfo

        The model defined in huaweicloud sdk

        :param commit_id: 代码提交的commit id
        :type commit_id: str
        :param created_at: 提交时间
        :type created_at: str
        """
        
        

        self._commit_id = None
        self._created_at = None
        self.discriminator = None

        if commit_id is not None:
            self.commit_id = commit_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def commit_id(self):
        r"""Gets the commit_id of this BuildInfoRecordCommitInfo.

        代码提交的commit id

        :return: The commit_id of this BuildInfoRecordCommitInfo.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this BuildInfoRecordCommitInfo.

        代码提交的commit id

        :param commit_id: The commit_id of this BuildInfoRecordCommitInfo.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def created_at(self):
        r"""Gets the created_at of this BuildInfoRecordCommitInfo.

        提交时间

        :return: The created_at of this BuildInfoRecordCommitInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BuildInfoRecordCommitInfo.

        提交时间

        :param created_at: The created_at of this BuildInfoRecordCommitInfo.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, BuildInfoRecordCommitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
