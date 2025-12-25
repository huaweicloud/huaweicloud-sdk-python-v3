# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcVpcCloudResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_count': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_count': 'resource_count'
    }

    def __init__(self, resource_type=None, resource_count=None):
        r"""HwcVpcCloudResource

        The model defined in huaweicloud sdk

        :param resource_type: 资产类型
        :type resource_type: str
        :param resource_count: 资产数量
        :type resource_count: int
        """
        
        

        self._resource_type = None
        self._resource_count = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_count is not None:
            self.resource_count = resource_count

    @property
    def resource_type(self):
        r"""Gets the resource_type of this HwcVpcCloudResource.

        资产类型

        :return: The resource_type of this HwcVpcCloudResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this HwcVpcCloudResource.

        资产类型

        :param resource_type: The resource_type of this HwcVpcCloudResource.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_count(self):
        r"""Gets the resource_count of this HwcVpcCloudResource.

        资产数量

        :return: The resource_count of this HwcVpcCloudResource.
        :rtype: int
        """
        return self._resource_count

    @resource_count.setter
    def resource_count(self, resource_count):
        r"""Sets the resource_count of this HwcVpcCloudResource.

        资产数量

        :param resource_count: The resource_count of this HwcVpcCloudResource.
        :type resource_count: int
        """
        self._resource_count = resource_count

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcVpcCloudResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
