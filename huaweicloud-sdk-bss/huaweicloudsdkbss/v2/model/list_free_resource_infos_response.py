# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourceInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'free_resource_packages': 'list[FreeResourcePackageV3]',
        'total_count': 'int'
    }

    attribute_map = {
        'free_resource_packages': 'free_resource_packages',
        'total_count': 'total_count'
    }

    def __init__(self, free_resource_packages=None, total_count=None):
        """ListFreeResourceInfosResponse

        The model defined in huaweicloud sdk

        :param free_resource_packages: 资源包信息列表，具体参见表2。
        :type free_resource_packages: list[:class:`huaweicloudsdkbss.v2.FreeResourcePackageV3`]
        :param total_count: 总条数。
        :type total_count: int
        """
        
        super(ListFreeResourceInfosResponse, self).__init__()

        self._free_resource_packages = None
        self._total_count = None
        self.discriminator = None

        if free_resource_packages is not None:
            self.free_resource_packages = free_resource_packages
        if total_count is not None:
            self.total_count = total_count

    @property
    def free_resource_packages(self):
        """Gets the free_resource_packages of this ListFreeResourceInfosResponse.

        资源包信息列表，具体参见表2。

        :return: The free_resource_packages of this ListFreeResourceInfosResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FreeResourcePackageV3`]
        """
        return self._free_resource_packages

    @free_resource_packages.setter
    def free_resource_packages(self, free_resource_packages):
        """Sets the free_resource_packages of this ListFreeResourceInfosResponse.

        资源包信息列表，具体参见表2。

        :param free_resource_packages: The free_resource_packages of this ListFreeResourceInfosResponse.
        :type free_resource_packages: list[:class:`huaweicloudsdkbss.v2.FreeResourcePackageV3`]
        """
        self._free_resource_packages = free_resource_packages

    @property
    def total_count(self):
        """Gets the total_count of this ListFreeResourceInfosResponse.

        总条数。

        :return: The total_count of this ListFreeResourceInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListFreeResourceInfosResponse.

        总条数。

        :param total_count: The total_count of this ListFreeResourceInfosResponse.
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
        if not isinstance(other, ListFreeResourceInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
