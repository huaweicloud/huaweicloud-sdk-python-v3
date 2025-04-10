# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorGroupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_type': 'str',
        'flavors': 'list[Flavor]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'group_type': 'group_type',
        'flavors': 'flavors',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, group_type=None, flavors=None, offset=None, limit=None, total=None):
        r"""FlavorGroupInfo

        The model defined in huaweicloud sdk

        :param group_type: 计算资源架构类型，目前分X86和ARM两种。
        :type group_type: str
        :param flavors: 规格详情。
        :type flavors: list[:class:`huaweicloudsdkddm.v1.Flavor`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: 计算类型规格总数。
        :type total: int
        """
        
        

        self._group_type = None
        self._flavors = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        self.group_type = group_type
        self.flavors = flavors
        self.offset = offset
        self.limit = limit
        self.total = total

    @property
    def group_type(self):
        r"""Gets the group_type of this FlavorGroupInfo.

        计算资源架构类型，目前分X86和ARM两种。

        :return: The group_type of this FlavorGroupInfo.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this FlavorGroupInfo.

        计算资源架构类型，目前分X86和ARM两种。

        :param group_type: The group_type of this FlavorGroupInfo.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def flavors(self):
        r"""Gets the flavors of this FlavorGroupInfo.

        规格详情。

        :return: The flavors of this FlavorGroupInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.Flavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this FlavorGroupInfo.

        规格详情。

        :param flavors: The flavors of this FlavorGroupInfo.
        :type flavors: list[:class:`huaweicloudsdkddm.v1.Flavor`]
        """
        self._flavors = flavors

    @property
    def offset(self):
        r"""Gets the offset of this FlavorGroupInfo.

        分页参数: 起始值。

        :return: The offset of this FlavorGroupInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this FlavorGroupInfo.

        分页参数: 起始值。

        :param offset: The offset of this FlavorGroupInfo.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this FlavorGroupInfo.

        分页参数：每页多少条。

        :return: The limit of this FlavorGroupInfo.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this FlavorGroupInfo.

        分页参数：每页多少条。

        :param limit: The limit of this FlavorGroupInfo.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this FlavorGroupInfo.

        计算类型规格总数。

        :return: The total of this FlavorGroupInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this FlavorGroupInfo.

        计算类型规格总数。

        :param total: The total of this FlavorGroupInfo.
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
        if not isinstance(other, FlavorGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
