# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavors': 'list[AvailableFlavorInfoResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'flavors': 'flavors',
        'total_count': 'total_count'
    }

    def __init__(self, flavors=None, total_count=None):
        """ListAvailableFlavorsResponse

        The model defined in huaweicloud sdk

        :param flavors: 实例可变更规格信息列表。
        :type flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AvailableFlavorInfoResult`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListAvailableFlavorsResponse, self).__init__()

        self._flavors = None
        self._total_count = None
        self.discriminator = None

        if flavors is not None:
            self.flavors = flavors
        if total_count is not None:
            self.total_count = total_count

    @property
    def flavors(self):
        """Gets the flavors of this ListAvailableFlavorsResponse.

        实例可变更规格信息列表。

        :return: The flavors of this ListAvailableFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AvailableFlavorInfoResult`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        """Sets the flavors of this ListAvailableFlavorsResponse.

        实例可变更规格信息列表。

        :param flavors: The flavors of this ListAvailableFlavorsResponse.
        :type flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.AvailableFlavorInfoResult`]
        """
        self._flavors = flavors

    @property
    def total_count(self):
        """Gets the total_count of this ListAvailableFlavorsResponse.

        总记录数。

        :return: The total_count of this ListAvailableFlavorsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListAvailableFlavorsResponse.

        总记录数。

        :param total_count: The total_count of this ListAvailableFlavorsResponse.
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
        if not isinstance(other, ListAvailableFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
