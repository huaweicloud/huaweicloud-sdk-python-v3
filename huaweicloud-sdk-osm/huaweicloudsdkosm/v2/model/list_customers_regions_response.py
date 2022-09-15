# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomersRegionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'region_infos': 'list[Region]'
    }

    attribute_map = {
        'count': 'count',
        'region_infos': 'region_infos'
    }

    def __init__(self, count=None, region_infos=None):
        """ListCustomersRegionsResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param region_infos: 区域信息
        :type region_infos: list[:class:`huaweicloudsdkosm.v2.Region`]
        """
        
        super(ListCustomersRegionsResponse, self).__init__()

        self._count = None
        self._region_infos = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if region_infos is not None:
            self.region_infos = region_infos

    @property
    def count(self):
        """Gets the count of this ListCustomersRegionsResponse.

        总数

        :return: The count of this ListCustomersRegionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCustomersRegionsResponse.

        总数

        :param count: The count of this ListCustomersRegionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def region_infos(self):
        """Gets the region_infos of this ListCustomersRegionsResponse.

        区域信息

        :return: The region_infos of this ListCustomersRegionsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.Region`]
        """
        return self._region_infos

    @region_infos.setter
    def region_infos(self, region_infos):
        """Sets the region_infos of this ListCustomersRegionsResponse.

        区域信息

        :param region_infos: The region_infos of this ListCustomersRegionsResponse.
        :type region_infos: list[:class:`huaweicloudsdkosm.v2.Region`]
        """
        self._region_infos = region_infos

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
        if not isinstance(other, ListCustomersRegionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
