# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNeedVerifyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'contact_value': 'str',
        'contact_way': 'int',
        'area_code': 'str',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'contact_value': 'contact_value',
        'contact_way': 'contact_way',
        'area_code': 'area_code',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, contact_value=None, contact_way=None, area_code=None, x_site=None, x_language=None, x_time_zone=None):
        """CheckNeedVerifyRequest

        The model defined in huaweicloud sdk

        :param contact_value: 联系方式值
        :type contact_value: str
        :param contact_way: 联系方式类型
        :type contact_way: int
        :param area_code: 国家码
        :type area_code: str
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._contact_value = None
        self._contact_way = None
        self._area_code = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        self.contact_value = contact_value
        self.contact_way = contact_way
        if area_code is not None:
            self.area_code = area_code
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def contact_value(self):
        """Gets the contact_value of this CheckNeedVerifyRequest.

        联系方式值

        :return: The contact_value of this CheckNeedVerifyRequest.
        :rtype: str
        """
        return self._contact_value

    @contact_value.setter
    def contact_value(self, contact_value):
        """Sets the contact_value of this CheckNeedVerifyRequest.

        联系方式值

        :param contact_value: The contact_value of this CheckNeedVerifyRequest.
        :type contact_value: str
        """
        self._contact_value = contact_value

    @property
    def contact_way(self):
        """Gets the contact_way of this CheckNeedVerifyRequest.

        联系方式类型

        :return: The contact_way of this CheckNeedVerifyRequest.
        :rtype: int
        """
        return self._contact_way

    @contact_way.setter
    def contact_way(self, contact_way):
        """Sets the contact_way of this CheckNeedVerifyRequest.

        联系方式类型

        :param contact_way: The contact_way of this CheckNeedVerifyRequest.
        :type contact_way: int
        """
        self._contact_way = contact_way

    @property
    def area_code(self):
        """Gets the area_code of this CheckNeedVerifyRequest.

        国家码

        :return: The area_code of this CheckNeedVerifyRequest.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this CheckNeedVerifyRequest.

        国家码

        :param area_code: The area_code of this CheckNeedVerifyRequest.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def x_site(self):
        """Gets the x_site of this CheckNeedVerifyRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this CheckNeedVerifyRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this CheckNeedVerifyRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this CheckNeedVerifyRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this CheckNeedVerifyRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this CheckNeedVerifyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CheckNeedVerifyRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this CheckNeedVerifyRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this CheckNeedVerifyRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this CheckNeedVerifyRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this CheckNeedVerifyRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this CheckNeedVerifyRequest.
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
        if not isinstance(other, CheckNeedVerifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
