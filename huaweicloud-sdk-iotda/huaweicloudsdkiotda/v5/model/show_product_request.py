# coding: utf-8

import pprint
import re

import six





class ShowProductRequest:


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
        'app_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'product_id': 'product_id',
        'app_id': 'app_id'
    }

    def __init__(self, instance_id=None, product_id=None, app_id=None):
        """ShowProductRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._product_id = None
        self._app_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.product_id = product_id
        if app_id is not None:
            self.app_id = app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowProductRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ShowProductRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowProductRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ShowProductRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this ShowProductRequest.

        产品ID，用于唯一标识一个产品，在物联网平台创建产品后由平台分配获得。

        :return: The product_id of this ShowProductRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowProductRequest.

        产品ID，用于唯一标识一个产品，在物联网平台创建产品后由平台分配获得。

        :param product_id: The product_id of this ShowProductRequest.
        :type: str
        """
        self._product_id = product_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowProductRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，必须携带该参数指定要查询的产品属于哪个资源空间，否则接口会提示错误。如果用户存在多资源空间，同时又不想携带该参数，可以联系华为技术支持对用户数据做资源空间合并。

        :return: The app_id of this ShowProductRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowProductRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，必须携带该参数指定要查询的产品属于哪个资源空间，否则接口会提示错误。如果用户存在多资源空间，同时又不想携带该参数，可以联系华为技术支持对用户数据做资源空间合并。

        :param app_id: The app_id of this ShowProductRequest.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ShowProductRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
