# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVaultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vaults': 'list[Vault]',
        'count': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'vaults': 'vaults',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, vaults=None, count=None, limit=None, offset=None):
        r"""ListVaultResponse

        The model defined in huaweicloud sdk

        :param vaults: 存储库实例列表
        :type vaults: list[:class:`huaweicloudsdkcbr.v1.Vault`]
        :param count: 存储库个数
        :type count: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        """
        
        super(ListVaultResponse, self).__init__()

        self._vaults = None
        self._count = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if vaults is not None:
            self.vaults = vaults
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def vaults(self):
        r"""Gets the vaults of this ListVaultResponse.

        存储库实例列表

        :return: The vaults of this ListVaultResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Vault`]
        """
        return self._vaults

    @vaults.setter
    def vaults(self, vaults):
        r"""Sets the vaults of this ListVaultResponse.

        存储库实例列表

        :param vaults: The vaults of this ListVaultResponse.
        :type vaults: list[:class:`huaweicloudsdkcbr.v1.Vault`]
        """
        self._vaults = vaults

    @property
    def count(self):
        r"""Gets the count of this ListVaultResponse.

        存储库个数

        :return: The count of this ListVaultResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListVaultResponse.

        存储库个数

        :param count: The count of this ListVaultResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ListVaultResponse.

        每页显示的条目数量

        :return: The limit of this ListVaultResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVaultResponse.

        每页显示的条目数量

        :param limit: The limit of this ListVaultResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVaultResponse.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListVaultResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVaultResponse.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListVaultResponse.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListVaultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
