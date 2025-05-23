# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourceUsagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resources': 'list[FreeResourceDetail]'
    }

    attribute_map = {
        'free_resources': 'free_resources'
    }

    def __init__(self, free_resources=None):
        r"""ListFreeResourceUsagesResponse

        The model defined in huaweicloud sdk

        :param free_resources: 资源套餐内的资源项信息（资源项ID级的详情），具体参见表2。
        :type free_resources: list[:class:`huaweicloudsdkbss.v2.FreeResourceDetail`]
        """
        
        super(ListFreeResourceUsagesResponse, self).__init__()

        self._free_resources = None
        self.discriminator = None

        if free_resources is not None:
            self.free_resources = free_resources

    @property
    def free_resources(self):
        r"""Gets the free_resources of this ListFreeResourceUsagesResponse.

        资源套餐内的资源项信息（资源项ID级的详情），具体参见表2。

        :return: The free_resources of this ListFreeResourceUsagesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FreeResourceDetail`]
        """
        return self._free_resources

    @free_resources.setter
    def free_resources(self, free_resources):
        r"""Sets the free_resources of this ListFreeResourceUsagesResponse.

        资源套餐内的资源项信息（资源项ID级的详情），具体参见表2。

        :param free_resources: The free_resources of this ListFreeResourceUsagesResponse.
        :type free_resources: list[:class:`huaweicloudsdkbss.v2.FreeResourceDetail`]
        """
        self._free_resources = free_resources

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
        if not isinstance(other, ListFreeResourceUsagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
