# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestListDtoUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_merge': 'bool'
    }

    attribute_map = {
        'can_merge': 'can_merge'
    }

    def __init__(self, can_merge=None):
        r"""MergeRequestListDtoUser

        The model defined in huaweicloud sdk

        :param can_merge: 当前用户是否可合入
        :type can_merge: bool
        """
        
        

        self._can_merge = None
        self.discriminator = None

        if can_merge is not None:
            self.can_merge = can_merge

    @property
    def can_merge(self):
        r"""Gets the can_merge of this MergeRequestListDtoUser.

        当前用户是否可合入

        :return: The can_merge of this MergeRequestListDtoUser.
        :rtype: bool
        """
        return self._can_merge

    @can_merge.setter
    def can_merge(self, can_merge):
        r"""Sets the can_merge of this MergeRequestListDtoUser.

        当前用户是否可合入

        :param can_merge: The can_merge of this MergeRequestListDtoUser.
        :type can_merge: bool
        """
        self._can_merge = can_merge

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
        if not isinstance(other, MergeRequestListDtoUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
