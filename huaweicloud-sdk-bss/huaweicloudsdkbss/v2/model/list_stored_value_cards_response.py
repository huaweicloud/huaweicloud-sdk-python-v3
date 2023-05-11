# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoredValueCardsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'stored_value_cards': 'list[UserStoredValueCard]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'stored_value_cards': 'stored_value_cards'
    }

    def __init__(self, total_count=None, stored_value_cards=None):
        """ListStoredValueCardsResponse

        The model defined in huaweicloud sdk

        :param total_count: 符合查询条件的总条数。
        :type total_count: int
        :param stored_value_cards: 优惠券记录。 具体请参见表2。
        :type stored_value_cards: list[:class:`huaweicloudsdkbss.v2.UserStoredValueCard`]
        """
        
        super(ListStoredValueCardsResponse, self).__init__()

        self._total_count = None
        self._stored_value_cards = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if stored_value_cards is not None:
            self.stored_value_cards = stored_value_cards

    @property
    def total_count(self):
        """Gets the total_count of this ListStoredValueCardsResponse.

        符合查询条件的总条数。

        :return: The total_count of this ListStoredValueCardsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListStoredValueCardsResponse.

        符合查询条件的总条数。

        :param total_count: The total_count of this ListStoredValueCardsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def stored_value_cards(self):
        """Gets the stored_value_cards of this ListStoredValueCardsResponse.

        优惠券记录。 具体请参见表2。

        :return: The stored_value_cards of this ListStoredValueCardsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.UserStoredValueCard`]
        """
        return self._stored_value_cards

    @stored_value_cards.setter
    def stored_value_cards(self, stored_value_cards):
        """Sets the stored_value_cards of this ListStoredValueCardsResponse.

        优惠券记录。 具体请参见表2。

        :param stored_value_cards: The stored_value_cards of this ListStoredValueCardsResponse.
        :type stored_value_cards: list[:class:`huaweicloudsdkbss.v2.UserStoredValueCard`]
        """
        self._stored_value_cards = stored_value_cards

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
        if not isinstance(other, ListStoredValueCardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
