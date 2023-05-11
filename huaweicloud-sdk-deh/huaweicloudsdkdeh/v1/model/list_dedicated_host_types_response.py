# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedHostTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_host_types': 'list[RespHostType]'
    }

    attribute_map = {
        'dedicated_host_types': 'dedicated_host_types'
    }

    def __init__(self, dedicated_host_types=None):
        """ListDedicatedHostTypesResponse

        The model defined in huaweicloud sdk

        :param dedicated_host_types: 可用的专属主机类型。
        :type dedicated_host_types: list[:class:`huaweicloudsdkdeh.v1.RespHostType`]
        """
        
        super(ListDedicatedHostTypesResponse, self).__init__()

        self._dedicated_host_types = None
        self.discriminator = None

        if dedicated_host_types is not None:
            self.dedicated_host_types = dedicated_host_types

    @property
    def dedicated_host_types(self):
        """Gets the dedicated_host_types of this ListDedicatedHostTypesResponse.

        可用的专属主机类型。

        :return: The dedicated_host_types of this ListDedicatedHostTypesResponse.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.RespHostType`]
        """
        return self._dedicated_host_types

    @dedicated_host_types.setter
    def dedicated_host_types(self, dedicated_host_types):
        """Sets the dedicated_host_types of this ListDedicatedHostTypesResponse.

        可用的专属主机类型。

        :param dedicated_host_types: The dedicated_host_types of this ListDedicatedHostTypesResponse.
        :type dedicated_host_types: list[:class:`huaweicloudsdkdeh.v1.RespHostType`]
        """
        self._dedicated_host_types = dedicated_host_types

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
        if not isinstance(other, ListDedicatedHostTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
