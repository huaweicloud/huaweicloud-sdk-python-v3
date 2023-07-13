# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProductsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hourly': 'list[ListProductsRespHourly]',
        'monthly': 'list[ListProductsRespHourly]'
    }

    attribute_map = {
        'hourly': 'Hourly',
        'monthly': 'Monthly'
    }

    def __init__(self, hourly=None, monthly=None):
        """ListProductsResponse

        The model defined in huaweicloud sdk

        :param hourly: 表示按需付费的产品列表。
        :type hourly: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        :param monthly: 表示包年包月的产品列表。当前暂不支持通过API创建包年包月的Kafka实例。
        :type monthly: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        """
        
        super(ListProductsResponse, self).__init__()

        self._hourly = None
        self._monthly = None
        self.discriminator = None

        if hourly is not None:
            self.hourly = hourly
        if monthly is not None:
            self.monthly = monthly

    @property
    def hourly(self):
        """Gets the hourly of this ListProductsResponse.

        表示按需付费的产品列表。

        :return: The hourly of this ListProductsResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        """
        return self._hourly

    @hourly.setter
    def hourly(self, hourly):
        """Sets the hourly of this ListProductsResponse.

        表示按需付费的产品列表。

        :param hourly: The hourly of this ListProductsResponse.
        :type hourly: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        """
        self._hourly = hourly

    @property
    def monthly(self):
        """Gets the monthly of this ListProductsResponse.

        表示包年包月的产品列表。当前暂不支持通过API创建包年包月的Kafka实例。

        :return: The monthly of this ListProductsResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        """
        return self._monthly

    @monthly.setter
    def monthly(self, monthly):
        """Sets the monthly of this ListProductsResponse.

        表示包年包月的产品列表。当前暂不支持通过API创建包年包月的Kafka实例。

        :param monthly: The monthly of this ListProductsResponse.
        :type monthly: list[:class:`huaweicloudsdkkafka.v2.ListProductsRespHourly`]
        """
        self._monthly = monthly

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
        if not isinstance(other, ListProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
