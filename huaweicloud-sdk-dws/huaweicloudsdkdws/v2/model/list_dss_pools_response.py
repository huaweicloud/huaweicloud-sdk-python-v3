# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDssPoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pools': 'list[DssPool]',
        'count': 'int'
    }

    attribute_map = {
        'pools': 'pools',
        'count': 'count'
    }

    def __init__(self, pools=None, count=None):
        r"""ListDssPoolsResponse

        The model defined in huaweicloud sdk

        :param pools: **参数解释**： 专属分布式存储池详情列表。 **取值范围**： 不涉及。
        :type pools: list[:class:`huaweicloudsdkdws.v2.DssPool`]
        :param count: **参数解释**： 专属分布式存储池个数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListDssPoolsResponse, self).__init__()

        self._pools = None
        self._count = None
        self.discriminator = None

        if pools is not None:
            self.pools = pools
        if count is not None:
            self.count = count

    @property
    def pools(self):
        r"""Gets the pools of this ListDssPoolsResponse.

        **参数解释**： 专属分布式存储池详情列表。 **取值范围**： 不涉及。

        :return: The pools of this ListDssPoolsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DssPool`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this ListDssPoolsResponse.

        **参数解释**： 专属分布式存储池详情列表。 **取值范围**： 不涉及。

        :param pools: The pools of this ListDssPoolsResponse.
        :type pools: list[:class:`huaweicloudsdkdws.v2.DssPool`]
        """
        self._pools = pools

    @property
    def count(self):
        r"""Gets the count of this ListDssPoolsResponse.

        **参数解释**： 专属分布式存储池个数。 **取值范围**： 不涉及。

        :return: The count of this ListDssPoolsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDssPoolsResponse.

        **参数解释**： 专属分布式存储池个数。 **取值范围**： 不涉及。

        :param count: The count of this ListDssPoolsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDssPoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
