# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafWhiteIpRuleResponse(SdkResponse):

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
        'black': 'list[BlackWhiteListRule]',
        'white': 'list[BlackWhiteListRule]'
    }

    attribute_map = {
        'total': 'total',
        'black': 'black',
        'white': 'white'
    }

    def __init__(self, total=None, black=None, white=None):
        r"""ListWafWhiteIpRuleResponse

        The model defined in huaweicloud sdk

        :param total: total
        :type total: int
        :param black: black
        :type black: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        :param white: white
        :type white: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        """
        
        super(ListWafWhiteIpRuleResponse, self).__init__()

        self._total = None
        self._black = None
        self._white = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if black is not None:
            self.black = black
        if white is not None:
            self.white = white

    @property
    def total(self):
        r"""Gets the total of this ListWafWhiteIpRuleResponse.

        total

        :return: The total of this ListWafWhiteIpRuleResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWafWhiteIpRuleResponse.

        total

        :param total: The total of this ListWafWhiteIpRuleResponse.
        :type total: int
        """
        self._total = total

    @property
    def black(self):
        r"""Gets the black of this ListWafWhiteIpRuleResponse.

        black

        :return: The black of this ListWafWhiteIpRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        """
        return self._black

    @black.setter
    def black(self, black):
        r"""Sets the black of this ListWafWhiteIpRuleResponse.

        black

        :param black: The black of this ListWafWhiteIpRuleResponse.
        :type black: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        """
        self._black = black

    @property
    def white(self):
        r"""Gets the white of this ListWafWhiteIpRuleResponse.

        white

        :return: The white of this ListWafWhiteIpRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this ListWafWhiteIpRuleResponse.

        white

        :param white: The white of this ListWafWhiteIpRuleResponse.
        :type white: list[:class:`huaweicloudsdkaad.v2.BlackWhiteListRule`]
        """
        self._white = white

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
        if not isinstance(other, ListWafWhiteIpRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
