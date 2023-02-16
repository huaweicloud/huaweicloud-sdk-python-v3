# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowThemeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_service_key': 'str',
        'x_site': 'str',
        'x_language': 'str',
        'product_type_id': 'str',
        'product_type_name': 'str',
        'product_type_short_name': 'str'
    }

    attribute_map = {
        'x_service_key': 'x-service-key',
        'x_site': 'x-site',
        'x_language': 'x-language',
        'product_type_id': 'product_type_id',
        'product_type_name': 'product_type_name',
        'product_type_short_name': 'product_type_short_name'
    }

    def __init__(self, x_service_key=None, x_site=None, x_language=None, product_type_id=None, product_type_name=None, product_type_short_name=None):
        """ShowThemeRequest

        The model defined in huaweicloud sdk

        :param x_service_key: 调用智能客服服务标志。
        :type x_service_key: str
        :param x_site: 站点标记，0-中国站  1-国际站
        :type x_site: str
        :param x_language: 区域语言简写，en-us  zh-cn
        :type x_language: str
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        :param product_type_name: 产品类型名称
        :type product_type_name: str
        :param product_type_short_name: 产品类型缩写
        :type product_type_short_name: str
        """
        
        

        self._x_service_key = None
        self._x_site = None
        self._x_language = None
        self._product_type_id = None
        self._product_type_name = None
        self._product_type_short_name = None
        self.discriminator = None

        self.x_service_key = x_service_key
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if product_type_id is not None:
            self.product_type_id = product_type_id
        if product_type_name is not None:
            self.product_type_name = product_type_name
        if product_type_short_name is not None:
            self.product_type_short_name = product_type_short_name

    @property
    def x_service_key(self):
        """Gets the x_service_key of this ShowThemeRequest.

        调用智能客服服务标志。

        :return: The x_service_key of this ShowThemeRequest.
        :rtype: str
        """
        return self._x_service_key

    @x_service_key.setter
    def x_service_key(self, x_service_key):
        """Sets the x_service_key of this ShowThemeRequest.

        调用智能客服服务标志。

        :param x_service_key: The x_service_key of this ShowThemeRequest.
        :type x_service_key: str
        """
        self._x_service_key = x_service_key

    @property
    def x_site(self):
        """Gets the x_site of this ShowThemeRequest.

        站点标记，0-中国站  1-国际站

        :return: The x_site of this ShowThemeRequest.
        :rtype: str
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ShowThemeRequest.

        站点标记，0-中国站  1-国际站

        :param x_site: The x_site of this ShowThemeRequest.
        :type x_site: str
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ShowThemeRequest.

        区域语言简写，en-us  zh-cn

        :return: The x_language of this ShowThemeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowThemeRequest.

        区域语言简写，en-us  zh-cn

        :param x_language: The x_language of this ShowThemeRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def product_type_id(self):
        """Gets the product_type_id of this ShowThemeRequest.

        产品类型Id

        :return: The product_type_id of this ShowThemeRequest.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this ShowThemeRequest.

        产品类型Id

        :param product_type_id: The product_type_id of this ShowThemeRequest.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

    @property
    def product_type_name(self):
        """Gets the product_type_name of this ShowThemeRequest.

        产品类型名称

        :return: The product_type_name of this ShowThemeRequest.
        :rtype: str
        """
        return self._product_type_name

    @product_type_name.setter
    def product_type_name(self, product_type_name):
        """Sets the product_type_name of this ShowThemeRequest.

        产品类型名称

        :param product_type_name: The product_type_name of this ShowThemeRequest.
        :type product_type_name: str
        """
        self._product_type_name = product_type_name

    @property
    def product_type_short_name(self):
        """Gets the product_type_short_name of this ShowThemeRequest.

        产品类型缩写

        :return: The product_type_short_name of this ShowThemeRequest.
        :rtype: str
        """
        return self._product_type_short_name

    @product_type_short_name.setter
    def product_type_short_name(self, product_type_short_name):
        """Sets the product_type_short_name of this ShowThemeRequest.

        产品类型缩写

        :param product_type_short_name: The product_type_short_name of this ShowThemeRequest.
        :type product_type_short_name: str
        """
        self._product_type_short_name = product_type_short_name

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
        if not isinstance(other, ShowThemeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
