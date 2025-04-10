# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimDeviceMultiplyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'count': 'int',
        'sim_cards': 'list[SimDeviceMultiplyVO]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'sim_cards': 'sim_cards'
    }

    def __init__(self, limit=None, offset=None, count=None, sim_cards=None):
        r"""ListSimDeviceMultiplyResponse

        The model defined in huaweicloud sdk

        :param limit: 每页记录数
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param count: 总数
        :type count: int
        :param sim_cards: 三网卡数据集合
        :type sim_cards: list[:class:`huaweicloudsdkgsl.v3.SimDeviceMultiplyVO`]
        """
        
        super(ListSimDeviceMultiplyResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._sim_cards = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if sim_cards is not None:
            self.sim_cards = sim_cards

    @property
    def limit(self):
        r"""Gets the limit of this ListSimDeviceMultiplyResponse.

        每页记录数

        :return: The limit of this ListSimDeviceMultiplyResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimDeviceMultiplyResponse.

        每页记录数

        :param limit: The limit of this ListSimDeviceMultiplyResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSimDeviceMultiplyResponse.

        页码

        :return: The offset of this ListSimDeviceMultiplyResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimDeviceMultiplyResponse.

        页码

        :param offset: The offset of this ListSimDeviceMultiplyResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        r"""Gets the count of this ListSimDeviceMultiplyResponse.

        总数

        :return: The count of this ListSimDeviceMultiplyResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSimDeviceMultiplyResponse.

        总数

        :param count: The count of this ListSimDeviceMultiplyResponse.
        :type count: int
        """
        self._count = count

    @property
    def sim_cards(self):
        r"""Gets the sim_cards of this ListSimDeviceMultiplyResponse.

        三网卡数据集合

        :return: The sim_cards of this ListSimDeviceMultiplyResponse.
        :rtype: list[:class:`huaweicloudsdkgsl.v3.SimDeviceMultiplyVO`]
        """
        return self._sim_cards

    @sim_cards.setter
    def sim_cards(self, sim_cards):
        r"""Sets the sim_cards of this ListSimDeviceMultiplyResponse.

        三网卡数据集合

        :param sim_cards: The sim_cards of this ListSimDeviceMultiplyResponse.
        :type sim_cards: list[:class:`huaweicloudsdkgsl.v3.SimDeviceMultiplyVO`]
        """
        self._sim_cards = sim_cards

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
        if not isinstance(other, ListSimDeviceMultiplyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
