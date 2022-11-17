# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHasVerifiedContactsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contact_way': 'int',
        'customer_id': 'str',
        'sub_customer_id': 'str',
        'expired_time': 'str',
        'verified_id': 'str',
        'contact_value': 'str',
        'area_code': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str'
    }

    attribute_map = {
        'contact_way': 'contact_way',
        'customer_id': 'customer_id',
        'sub_customer_id': 'sub_customer_id',
        'expired_time': 'expired_time',
        'verified_id': 'verified_id',
        'contact_value': 'contact_value',
        'area_code': 'area_code',
        'offset': 'offset',
        'limit': 'limit',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone'
    }

    def __init__(self, contact_way=None, customer_id=None, sub_customer_id=None, expired_time=None, verified_id=None, contact_value=None, area_code=None, offset=None, limit=None, x_site=None, x_language=None, x_time_zone=None):
        """ListHasVerifiedContactsRequest

        The model defined in huaweicloud sdk

        :param contact_way: 联系方式类型
        :type contact_way: int
        :param customer_id: 客户id
        :type customer_id: str
        :param sub_customer_id: 子用户id
        :type sub_customer_id: str
        :param expired_time: 过期时间
        :type expired_time: str
        :param verified_id: 验证序列号
        :type verified_id: str
        :param contact_value: 联系方式的值
        :type contact_value: str
        :param area_code: 国家码
        :type area_code: str
        :param offset: 查询偏移量
        :type offset: int
        :param limit: 查询数量
        :type limit: int
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        """
        
        

        self._contact_way = None
        self._customer_id = None
        self._sub_customer_id = None
        self._expired_time = None
        self._verified_id = None
        self._contact_value = None
        self._area_code = None
        self._offset = None
        self._limit = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self.discriminator = None

        if contact_way is not None:
            self.contact_way = contact_way
        if customer_id is not None:
            self.customer_id = customer_id
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
        if expired_time is not None:
            self.expired_time = expired_time
        if verified_id is not None:
            self.verified_id = verified_id
        if contact_value is not None:
            self.contact_value = contact_value
        if area_code is not None:
            self.area_code = area_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone

    @property
    def contact_way(self):
        """Gets the contact_way of this ListHasVerifiedContactsRequest.

        联系方式类型

        :return: The contact_way of this ListHasVerifiedContactsRequest.
        :rtype: int
        """
        return self._contact_way

    @contact_way.setter
    def contact_way(self, contact_way):
        """Sets the contact_way of this ListHasVerifiedContactsRequest.

        联系方式类型

        :param contact_way: The contact_way of this ListHasVerifiedContactsRequest.
        :type contact_way: int
        """
        self._contact_way = contact_way

    @property
    def customer_id(self):
        """Gets the customer_id of this ListHasVerifiedContactsRequest.

        客户id

        :return: The customer_id of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListHasVerifiedContactsRequest.

        客户id

        :param customer_id: The customer_id of this ListHasVerifiedContactsRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListHasVerifiedContactsRequest.

        子用户id

        :return: The sub_customer_id of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListHasVerifiedContactsRequest.

        子用户id

        :param sub_customer_id: The sub_customer_id of this ListHasVerifiedContactsRequest.
        :type sub_customer_id: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def expired_time(self):
        """Gets the expired_time of this ListHasVerifiedContactsRequest.

        过期时间

        :return: The expired_time of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this ListHasVerifiedContactsRequest.

        过期时间

        :param expired_time: The expired_time of this ListHasVerifiedContactsRequest.
        :type expired_time: str
        """
        self._expired_time = expired_time

    @property
    def verified_id(self):
        """Gets the verified_id of this ListHasVerifiedContactsRequest.

        验证序列号

        :return: The verified_id of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._verified_id

    @verified_id.setter
    def verified_id(self, verified_id):
        """Sets the verified_id of this ListHasVerifiedContactsRequest.

        验证序列号

        :param verified_id: The verified_id of this ListHasVerifiedContactsRequest.
        :type verified_id: str
        """
        self._verified_id = verified_id

    @property
    def contact_value(self):
        """Gets the contact_value of this ListHasVerifiedContactsRequest.

        联系方式的值

        :return: The contact_value of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._contact_value

    @contact_value.setter
    def contact_value(self, contact_value):
        """Sets the contact_value of this ListHasVerifiedContactsRequest.

        联系方式的值

        :param contact_value: The contact_value of this ListHasVerifiedContactsRequest.
        :type contact_value: str
        """
        self._contact_value = contact_value

    @property
    def area_code(self):
        """Gets the area_code of this ListHasVerifiedContactsRequest.

        国家码

        :return: The area_code of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this ListHasVerifiedContactsRequest.

        国家码

        :param area_code: The area_code of this ListHasVerifiedContactsRequest.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def offset(self):
        """Gets the offset of this ListHasVerifiedContactsRequest.

        查询偏移量

        :return: The offset of this ListHasVerifiedContactsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHasVerifiedContactsRequest.

        查询偏移量

        :param offset: The offset of this ListHasVerifiedContactsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHasVerifiedContactsRequest.

        查询数量

        :return: The limit of this ListHasVerifiedContactsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHasVerifiedContactsRequest.

        查询数量

        :param limit: The limit of this ListHasVerifiedContactsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_site(self):
        """Gets the x_site of this ListHasVerifiedContactsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this ListHasVerifiedContactsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this ListHasVerifiedContactsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this ListHasVerifiedContactsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this ListHasVerifiedContactsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListHasVerifiedContactsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this ListHasVerifiedContactsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        """Gets the x_time_zone of this ListHasVerifiedContactsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this ListHasVerifiedContactsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        """Sets the x_time_zone of this ListHasVerifiedContactsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this ListHasVerifiedContactsRequest.
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
        if not isinstance(other, ListHasVerifiedContactsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
