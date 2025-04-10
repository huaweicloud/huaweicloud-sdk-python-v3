# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafAttackEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'list': 'list[ListWafAttackEventlist]'
    }

    attribute_map = {
        'total': 'total',
        'list': 'list'
    }

    def __init__(self, total=None, list=None):
        r"""ListWafAttackEventResponse

        The model defined in huaweicloud sdk

        :param total: total
        :type total: int
        :param list: list
        :type list: list[:class:`huaweicloudsdkaad.v2.ListWafAttackEventlist`]
        """
        
        super(ListWafAttackEventResponse, self).__init__()

        self._total = None
        self._list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if list is not None:
            self.list = list

    @property
    def total(self):
        r"""Gets the total of this ListWafAttackEventResponse.

        total

        :return: The total of this ListWafAttackEventResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWafAttackEventResponse.

        total

        :param total: The total of this ListWafAttackEventResponse.
        :type total: int
        """
        self._total = total

    @property
    def list(self):
        r"""Gets the list of this ListWafAttackEventResponse.

        list

        :return: The list of this ListWafAttackEventResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.ListWafAttackEventlist`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ListWafAttackEventResponse.

        list

        :param list: The list of this ListWafAttackEventResponse.
        :type list: list[:class:`huaweicloudsdkaad.v2.ListWafAttackEventlist`]
        """
        self._list = list

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
        if not isinstance(other, ListWafAttackEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
