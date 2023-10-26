# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkCapabilitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capability': 'list[CentralNetworkCapabilityEnum]'
    }

    attribute_map = {
        'capability': 'capability'
    }

    def __init__(self, capability=None):
        """ListCentralNetworkCapabilitiesRequest

        The model defined in huaweicloud sdk

        :param capability: 根据租户能力名查询，可查询多个类型。
        :type capability: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        """
        
        

        self._capability = None
        self.discriminator = None

        if capability is not None:
            self.capability = capability

    @property
    def capability(self):
        """Gets the capability of this ListCentralNetworkCapabilitiesRequest.

        根据租户能力名查询，可查询多个类型。

        :return: The capability of this ListCentralNetworkCapabilitiesRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this ListCentralNetworkCapabilitiesRequest.

        根据租户能力名查询，可查询多个类型。

        :param capability: The capability of this ListCentralNetworkCapabilitiesRequest.
        :type capability: list[:class:`huaweicloudsdkcc.v3.CentralNetworkCapabilityEnum`]
        """
        self._capability = capability

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
        if not isinstance(other, ListCentralNetworkCapabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
