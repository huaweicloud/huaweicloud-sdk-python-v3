# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTypesSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, region_id=None, resource_type=None):
        r"""ResourceTypesSummary

        The model defined in huaweicloud sdk

        :param region_id: 资源所在区域名称。
        :type region_id: str
        :param resource_type: 资源类型名称。
        :type resource_type: str
        """
        
        

        self._region_id = None
        self._resource_type = None
        self.discriminator = None

        self.region_id = region_id
        self.resource_type = resource_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceTypesSummary.

        资源所在区域名称。

        :return: The region_id of this ResourceTypesSummary.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceTypesSummary.

        资源所在区域名称。

        :param region_id: The region_id of this ResourceTypesSummary.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceTypesSummary.

        资源类型名称。

        :return: The resource_type of this ResourceTypesSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceTypesSummary.

        资源类型名称。

        :param resource_type: The resource_type of this ResourceTypesSummary.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ResourceTypesSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
