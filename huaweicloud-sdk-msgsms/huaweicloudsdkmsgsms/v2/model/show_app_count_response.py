# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppCountResponse(SdkResponse):

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
        'used': 'int'
    }

    attribute_map = {
        'total': 'total',
        'used': 'used'
    }

    def __init__(self, total=None, used=None):
        r"""ShowAppCountResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param used: 已使用数
        :type used: int
        """
        
        super(ShowAppCountResponse, self).__init__()

        self._total = None
        self._used = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if used is not None:
            self.used = used

    @property
    def total(self):
        r"""Gets the total of this ShowAppCountResponse.

        总数

        :return: The total of this ShowAppCountResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowAppCountResponse.

        总数

        :param total: The total of this ShowAppCountResponse.
        :type total: int
        """
        self._total = total

    @property
    def used(self):
        r"""Gets the used of this ShowAppCountResponse.

        已使用数

        :return: The used of this ShowAppCountResponse.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ShowAppCountResponse.

        已使用数

        :param used: The used of this ShowAppCountResponse.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, ShowAppCountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
