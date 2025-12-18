# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageProductDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_name': 'str',
        'resource_spec_code': 'str',
        'period_type': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'product_name': 'product_name',
        'resource_spec_code': 'resource_spec_code',
        'period_type': 'period_type',
        'instance_type': 'instance_type'
    }

    def __init__(self, product_name=None, resource_spec_code=None, period_type=None, instance_type=None):
        r"""PackageProductDetail

        The model defined in huaweicloud sdk

        :param product_name: 套餐包名称。
        :type product_name: str
        :param resource_spec_code: 套餐包规格。
        :type resource_spec_code: str
        :param period_type: 周期类型，如month（表示月包）、year（表示年包）。
        :type period_type: str
        :param instance_type: 实例类型，如general-computing。
        :type instance_type: str
        """
        
        

        self._product_name = None
        self._resource_spec_code = None
        self._period_type = None
        self._instance_type = None
        self.discriminator = None

        self.product_name = product_name
        self.resource_spec_code = resource_spec_code
        self.period_type = period_type
        self.instance_type = instance_type

    @property
    def product_name(self):
        r"""Gets the product_name of this PackageProductDetail.

        套餐包名称。

        :return: The product_name of this PackageProductDetail.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this PackageProductDetail.

        套餐包名称。

        :param product_name: The product_name of this PackageProductDetail.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this PackageProductDetail.

        套餐包规格。

        :return: The resource_spec_code of this PackageProductDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this PackageProductDetail.

        套餐包规格。

        :param resource_spec_code: The resource_spec_code of this PackageProductDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def period_type(self):
        r"""Gets the period_type of this PackageProductDetail.

        周期类型，如month（表示月包）、year（表示年包）。

        :return: The period_type of this PackageProductDetail.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PackageProductDetail.

        周期类型，如month（表示月包）、year（表示年包）。

        :param period_type: The period_type of this PackageProductDetail.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def instance_type(self):
        r"""Gets the instance_type of this PackageProductDetail.

        实例类型，如general-computing。

        :return: The instance_type of this PackageProductDetail.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this PackageProductDetail.

        实例类型，如general-computing。

        :param instance_type: The instance_type of this PackageProductDetail.
        :type instance_type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, PackageProductDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
