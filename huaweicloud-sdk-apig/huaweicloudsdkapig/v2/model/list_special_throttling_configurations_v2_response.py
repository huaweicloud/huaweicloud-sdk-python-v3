# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecialThrottlingConfigurationsV2Response(SdkResponse):

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
        'throttle_specials': 'list[ThrottleSpecialInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'throttle_specials': 'throttle_specials'
    }

    def __init__(self, size=None, total=None, throttle_specials=None):
        r"""ListSpecialThrottlingConfigurationsV2Response

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param throttle_specials: 本次查询返回的特殊配置列表
        :type throttle_specials: list[:class:`huaweicloudsdkapig.v2.ThrottleSpecialInfo`]
        """
        
        super(ListSpecialThrottlingConfigurationsV2Response, self).__init__()

        self._size = None
        self._total = None
        self._throttle_specials = None
        self.discriminator = None

        self.size = size
        self.total = total
        if throttle_specials is not None:
            self.throttle_specials = throttle_specials

    @property
    def size(self):
        r"""Gets the size of this ListSpecialThrottlingConfigurationsV2Response.

        本次返回的列表长度

        :return: The size of this ListSpecialThrottlingConfigurationsV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListSpecialThrottlingConfigurationsV2Response.

        本次返回的列表长度

        :param size: The size of this ListSpecialThrottlingConfigurationsV2Response.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListSpecialThrottlingConfigurationsV2Response.

        满足条件的记录数

        :return: The total of this ListSpecialThrottlingConfigurationsV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSpecialThrottlingConfigurationsV2Response.

        满足条件的记录数

        :param total: The total of this ListSpecialThrottlingConfigurationsV2Response.
        :type total: int
        """
        self._total = total

    @property
    def throttle_specials(self):
        r"""Gets the throttle_specials of this ListSpecialThrottlingConfigurationsV2Response.

        本次查询返回的特殊配置列表

        :return: The throttle_specials of this ListSpecialThrottlingConfigurationsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ThrottleSpecialInfo`]
        """
        return self._throttle_specials

    @throttle_specials.setter
    def throttle_specials(self, throttle_specials):
        r"""Sets the throttle_specials of this ListSpecialThrottlingConfigurationsV2Response.

        本次查询返回的特殊配置列表

        :param throttle_specials: The throttle_specials of this ListSpecialThrottlingConfigurationsV2Response.
        :type throttle_specials: list[:class:`huaweicloudsdkapig.v2.ThrottleSpecialInfo`]
        """
        self._throttle_specials = throttle_specials

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
        if not isinstance(other, ListSpecialThrottlingConfigurationsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
