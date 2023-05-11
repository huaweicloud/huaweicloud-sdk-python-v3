# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_templates': 'ProductTemplatesCalculation',
        'products': 'ProductsCalculation',
        'devices': 'DevicesCalculation'
    }

    attribute_map = {
        'product_templates': 'product_templates',
        'products': 'products',
        'devices': 'devices'
    }

    def __init__(self, product_templates=None, products=None, devices=None):
        """CountDevicesResponse

        The model defined in huaweicloud sdk

        :param product_templates: 
        :type product_templates: :class:`huaweicloudsdkroma.v2.ProductTemplatesCalculation`
        :param products: 
        :type products: :class:`huaweicloudsdkroma.v2.ProductsCalculation`
        :param devices: 
        :type devices: :class:`huaweicloudsdkroma.v2.DevicesCalculation`
        """
        
        super(CountDevicesResponse, self).__init__()

        self._product_templates = None
        self._products = None
        self._devices = None
        self.discriminator = None

        if product_templates is not None:
            self.product_templates = product_templates
        if products is not None:
            self.products = products
        if devices is not None:
            self.devices = devices

    @property
    def product_templates(self):
        """Gets the product_templates of this CountDevicesResponse.

        :return: The product_templates of this CountDevicesResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.ProductTemplatesCalculation`
        """
        return self._product_templates

    @product_templates.setter
    def product_templates(self, product_templates):
        """Sets the product_templates of this CountDevicesResponse.

        :param product_templates: The product_templates of this CountDevicesResponse.
        :type product_templates: :class:`huaweicloudsdkroma.v2.ProductTemplatesCalculation`
        """
        self._product_templates = product_templates

    @property
    def products(self):
        """Gets the products of this CountDevicesResponse.

        :return: The products of this CountDevicesResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.ProductsCalculation`
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this CountDevicesResponse.

        :param products: The products of this CountDevicesResponse.
        :type products: :class:`huaweicloudsdkroma.v2.ProductsCalculation`
        """
        self._products = products

    @property
    def devices(self):
        """Gets the devices of this CountDevicesResponse.

        :return: The devices of this CountDevicesResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.DevicesCalculation`
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this CountDevicesResponse.

        :param devices: The devices of this CountDevicesResponse.
        :type devices: :class:`huaweicloudsdkroma.v2.DevicesCalculation`
        """
        self._devices = devices

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
        if not isinstance(other, CountDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
