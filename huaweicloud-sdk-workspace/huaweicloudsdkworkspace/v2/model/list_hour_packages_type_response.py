# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHourPackagesTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hour_packages': 'list[HourPackage]',
        'total_count': 'int'
    }

    attribute_map = {
        'hour_packages': 'hour_packages',
        'total_count': 'total_count'
    }

    def __init__(self, hour_packages=None, total_count=None):
        r"""ListHourPackagesTypeResponse

        The model defined in huaweicloud sdk

        :param hour_packages: 可订购小时包类型列表。
        :type hour_packages: list[:class:`huaweicloudsdkworkspace.v2.HourPackage`]
        :param total_count: 云桌面支持的可用分区列表总数。
        :type total_count: int
        """
        
        super(ListHourPackagesTypeResponse, self).__init__()

        self._hour_packages = None
        self._total_count = None
        self.discriminator = None

        if hour_packages is not None:
            self.hour_packages = hour_packages
        if total_count is not None:
            self.total_count = total_count

    @property
    def hour_packages(self):
        r"""Gets the hour_packages of this ListHourPackagesTypeResponse.

        可订购小时包类型列表。

        :return: The hour_packages of this ListHourPackagesTypeResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.HourPackage`]
        """
        return self._hour_packages

    @hour_packages.setter
    def hour_packages(self, hour_packages):
        r"""Sets the hour_packages of this ListHourPackagesTypeResponse.

        可订购小时包类型列表。

        :param hour_packages: The hour_packages of this ListHourPackagesTypeResponse.
        :type hour_packages: list[:class:`huaweicloudsdkworkspace.v2.HourPackage`]
        """
        self._hour_packages = hour_packages

    @property
    def total_count(self):
        r"""Gets the total_count of this ListHourPackagesTypeResponse.

        云桌面支持的可用分区列表总数。

        :return: The total_count of this ListHourPackagesTypeResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListHourPackagesTypeResponse.

        云桌面支持的可用分区列表总数。

        :param total_count: The total_count of this ListHourPackagesTypeResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListHourPackagesTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
