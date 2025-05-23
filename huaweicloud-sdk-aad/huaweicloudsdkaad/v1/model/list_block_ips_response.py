# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlockIpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blocking_list': 'list[BlockListBlockingList]',
        'total': 'int'
    }

    attribute_map = {
        'blocking_list': 'blocking_list',
        'total': 'total'
    }

    def __init__(self, blocking_list=None, total=None):
        r"""ListBlockIpsResponse

        The model defined in huaweicloud sdk

        :param blocking_list: 封堵列表响应体
        :type blocking_list: list[:class:`huaweicloudsdkaad.v1.BlockListBlockingList`]
        :param total: 总数
        :type total: int
        """
        
        super(ListBlockIpsResponse, self).__init__()

        self._blocking_list = None
        self._total = None
        self.discriminator = None

        if blocking_list is not None:
            self.blocking_list = blocking_list
        if total is not None:
            self.total = total

    @property
    def blocking_list(self):
        r"""Gets the blocking_list of this ListBlockIpsResponse.

        封堵列表响应体

        :return: The blocking_list of this ListBlockIpsResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v1.BlockListBlockingList`]
        """
        return self._blocking_list

    @blocking_list.setter
    def blocking_list(self, blocking_list):
        r"""Sets the blocking_list of this ListBlockIpsResponse.

        封堵列表响应体

        :param blocking_list: The blocking_list of this ListBlockIpsResponse.
        :type blocking_list: list[:class:`huaweicloudsdkaad.v1.BlockListBlockingList`]
        """
        self._blocking_list = blocking_list

    @property
    def total(self):
        r"""Gets the total of this ListBlockIpsResponse.

        总数

        :return: The total of this ListBlockIpsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListBlockIpsResponse.

        总数

        :param total: The total of this ListBlockIpsResponse.
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
        if not isinstance(other, ListBlockIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
