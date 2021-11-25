# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiGroupInfoPage:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'groups': 'list[ApiGroupInfoPage]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'groups': 'groups'
    }

    def __init__(self, size=None, total=None, groups=None):
        """ApiGroupInfoPage - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._total = None
        self._groups = None
        self.discriminator = None

        self.size = size
        self.total = total
        if groups is not None:
            self.groups = groups

    @property
    def size(self):
        """Gets the size of this ApiGroupInfoPage.

        本次返回的列表长度

        :return: The size of this ApiGroupInfoPage.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ApiGroupInfoPage.

        本次返回的列表长度

        :param size: The size of this ApiGroupInfoPage.
        :type: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ApiGroupInfoPage.

        满足条件的记录数

        :return: The total of this ApiGroupInfoPage.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ApiGroupInfoPage.

        满足条件的记录数

        :param total: The total of this ApiGroupInfoPage.
        :type: int
        """
        self._total = total

    @property
    def groups(self):
        """Gets the groups of this ApiGroupInfoPage.

        分组列表

        :return: The groups of this ApiGroupInfoPage.
        :rtype: list[ApiGroupInfoPage]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ApiGroupInfoPage.

        分组列表

        :param groups: The groups of this ApiGroupInfoPage.
        :type: list[ApiGroupInfoPage]
        """
        self._groups = groups

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
        if not isinstance(other, ApiGroupInfoPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other