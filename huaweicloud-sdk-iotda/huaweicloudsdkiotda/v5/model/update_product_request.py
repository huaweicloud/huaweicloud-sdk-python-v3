# coding: utf-8

import pprint
import re

import six





class UpdateProductRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'product_id': 'str',
        'body': 'UpdateProduct'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'product_id': 'product_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, product_id=None, body=None):
        """UpdateProductRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._product_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.product_id = product_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateProductRequest.


        :return: The instance_id of this UpdateProductRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateProductRequest.


        :param instance_id: The instance_id of this UpdateProductRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this UpdateProductRequest.


        :return: The product_id of this UpdateProductRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this UpdateProductRequest.


        :param product_id: The product_id of this UpdateProductRequest.
        :type: str
        """
        self._product_id = product_id

    @property
    def body(self):
        """Gets the body of this UpdateProductRequest.


        :return: The body of this UpdateProductRequest.
        :rtype: UpdateProduct
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateProductRequest.


        :param body: The body of this UpdateProductRequest.
        :type: UpdateProduct
        """
        self._body = body

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateProductRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
