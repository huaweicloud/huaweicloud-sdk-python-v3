# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommitResponseBodyStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'additions': 'int',
        'deletions': 'int',
        'total': 'int'
    }

    attribute_map = {
        'additions': 'additions',
        'deletions': 'deletions',
        'total': 'total'
    }

    def __init__(self, additions=None, deletions=None, total=None):
        """CreateCommitResponseBodyStats

        The model defined in huaweicloud sdk

        :param additions: 变更增加的行数
        :type additions: int
        :param deletions: 变更删除的行数
        :type deletions: int
        :param total: 变更的总行数
        :type total: int
        """
        
        

        self._additions = None
        self._deletions = None
        self._total = None
        self.discriminator = None

        if additions is not None:
            self.additions = additions
        if deletions is not None:
            self.deletions = deletions
        if total is not None:
            self.total = total

    @property
    def additions(self):
        """Gets the additions of this CreateCommitResponseBodyStats.

        变更增加的行数

        :return: The additions of this CreateCommitResponseBodyStats.
        :rtype: int
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        """Sets the additions of this CreateCommitResponseBodyStats.

        变更增加的行数

        :param additions: The additions of this CreateCommitResponseBodyStats.
        :type additions: int
        """
        self._additions = additions

    @property
    def deletions(self):
        """Gets the deletions of this CreateCommitResponseBodyStats.

        变更删除的行数

        :return: The deletions of this CreateCommitResponseBodyStats.
        :rtype: int
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        """Sets the deletions of this CreateCommitResponseBodyStats.

        变更删除的行数

        :param deletions: The deletions of this CreateCommitResponseBodyStats.
        :type deletions: int
        """
        self._deletions = deletions

    @property
    def total(self):
        """Gets the total of this CreateCommitResponseBodyStats.

        变更的总行数

        :return: The total of this CreateCommitResponseBodyStats.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CreateCommitResponseBodyStats.

        变更的总行数

        :param total: The total of this CreateCommitResponseBodyStats.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, CreateCommitResponseBodyStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
