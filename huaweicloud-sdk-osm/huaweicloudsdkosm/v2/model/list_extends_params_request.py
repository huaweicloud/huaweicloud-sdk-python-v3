# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExtendsParamsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_type_id': 'str',
        'incident_sub_type_id': 'str',
        'product_category_id': 'str',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'business_type_id': 'business_type_id',
        'incident_sub_type_id': 'incident_sub_type_id',
        'product_category_id': 'product_category_id',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, business_type_id=None, incident_sub_type_id=None, product_category_id=None, x_site=None, x_language=None, x_time_zone=None):
        """ListExtendsParamsRequest

        The model defined in huaweicloud sdk

        :param business_type_id: 业务类型id
        :type business_type_id: str
        :param incident_sub_type_id: 工单子类型id
        :type incident_sub_type_id: str
        :param product_category_id: 产品类型id
        :type product_category_id: str
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._business_type_id = None
        self._incident_sub_type_id = None
        self._product_category_id = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.business_type_id = business_type_id
        if incident_sub_type_id is not None:
            self.incident_sub_type_id = incident_sub_type_id
        if product_category_id is not None:
            self.product_category_id = product_category_id
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def business_type_id(self):
        """Gets the business_type_id of this ListExtendsParamsRequest.

        业务类型id

        :return: The business_type_id of this ListExtendsParamsRequest.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this ListExtendsParamsRequest.

        业务类型id

        :param business_type_id: The business_type_id of this ListExtendsParamsRequest.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def incident_sub_type_id(self):
        """Gets the incident_sub_type_id of this ListExtendsParamsRequest.

        工单子类型id

        :return: The incident_sub_type_id of this ListExtendsParamsRequest.
        :rtype: str
        """
        return self._incident_sub_type_id

    @incident_sub_type_id.setter
    def incident_sub_type_id(self, incident_sub_type_id):
        """Sets the incident_sub_type_id of this ListExtendsParamsRequest.

        工单子类型id

        :param incident_sub_type_id: The incident_sub_type_id of this ListExtendsParamsRequest.
        :type incident_sub_type_id: str
        """
        self._incident_sub_type_id = incident_sub_type_id

    @property
    def product_category_id(self):
        """Gets the product_category_id of this ListExtendsParamsRequest.

        产品类型id

        :return: The product_category_id of this ListExtendsParamsRequest.
        :rtype: str
        """
        return self._product_category_id

    @product_category_id.setter
    def product_category_id(self, product_category_id):
        """Sets the product_category_id of this ListExtendsParamsRequest.

        产品类型id

        :param product_category_id: The product_category_id of this ListExtendsParamsRequest.
        :type product_category_id: str
        """
        self._product_category_id = product_category_id

    @property
    def x_site(self):
        """Gets the x_site of this ListExtendsParamsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListExtendsParamsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListExtendsParamsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListExtendsParamsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListExtendsParamsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListExtendsParamsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListExtendsParamsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListExtendsParamsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListExtendsParamsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListExtendsParamsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListExtendsParamsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListExtendsParamsRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

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
        if not isinstance(other, ListExtendsParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
