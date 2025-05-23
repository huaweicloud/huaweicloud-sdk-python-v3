# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BranchList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branches': 'list[Branch]',
        'total': 'int'
    }

    attribute_map = {
        'branches': 'branches',
        'total': 'total'
    }

    def __init__(self, branches=None, total=None):
        r"""BranchList

        The model defined in huaweicloud sdk

        :param branches: 指定仓库的分支列表
        :type branches: list[:class:`huaweicloudsdkcodehub.v3.Branch`]
        :param total: 指定仓库的分支总数
        :type total: int
        """
        
        

        self._branches = None
        self._total = None
        self.discriminator = None

        if branches is not None:
            self.branches = branches
        if total is not None:
            self.total = total

    @property
    def branches(self):
        r"""Gets the branches of this BranchList.

        指定仓库的分支列表

        :return: The branches of this BranchList.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.Branch`]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        r"""Sets the branches of this BranchList.

        指定仓库的分支列表

        :param branches: The branches of this BranchList.
        :type branches: list[:class:`huaweicloudsdkcodehub.v3.Branch`]
        """
        self._branches = branches

    @property
    def total(self):
        r"""Gets the total of this BranchList.

        指定仓库的分支总数

        :return: The total of this BranchList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BranchList.

        指定仓库的分支总数

        :param total: The total of this BranchList.
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
        if not isinstance(other, BranchList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
