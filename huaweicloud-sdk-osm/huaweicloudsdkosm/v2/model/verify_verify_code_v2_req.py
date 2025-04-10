# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyVerifyCodeV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verify_code': 'str',
        'contact_value': 'str',
        'contact_way': 'int',
        'area_code': 'str',
        'x_customer_id': 'str',
        'customer_id': 'str'
    }

    attribute_map = {
        'verify_code': 'verify_code',
        'contact_value': 'contact_value',
        'contact_way': 'contact_way',
        'area_code': 'area_code',
        'x_customer_id': 'x_customer_id',
        'customer_id': 'customer_id'
    }

    def __init__(self, verify_code=None, contact_value=None, contact_way=None, area_code=None, x_customer_id=None, customer_id=None):
        r"""VerifyVerifyCodeV2Req

        The model defined in huaweicloud sdk

        :param verify_code: 验证码
        :type verify_code: str
        :param contact_value: 联系方式的值
        :type contact_value: str
        :param contact_way: 联系方式的类型，0：短信；1：邮件
        :type contact_way: int
        :param area_code: 国家码
        :type area_code: str
        :param x_customer_id: 子用户id
        :type x_customer_id: str
        :param customer_id: 客户id
        :type customer_id: str
        """
        
        

        self._verify_code = None
        self._contact_value = None
        self._contact_way = None
        self._area_code = None
        self._x_customer_id = None
        self._customer_id = None
        self.discriminator = None

        self.verify_code = verify_code
        self.contact_value = contact_value
        self.contact_way = contact_way
        if area_code is not None:
            self.area_code = area_code
        if x_customer_id is not None:
            self.x_customer_id = x_customer_id
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def verify_code(self):
        r"""Gets the verify_code of this VerifyVerifyCodeV2Req.

        验证码

        :return: The verify_code of this VerifyVerifyCodeV2Req.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        r"""Sets the verify_code of this VerifyVerifyCodeV2Req.

        验证码

        :param verify_code: The verify_code of this VerifyVerifyCodeV2Req.
        :type verify_code: str
        """
        self._verify_code = verify_code

    @property
    def contact_value(self):
        r"""Gets the contact_value of this VerifyVerifyCodeV2Req.

        联系方式的值

        :return: The contact_value of this VerifyVerifyCodeV2Req.
        :rtype: str
        """
        return self._contact_value

    @contact_value.setter
    def contact_value(self, contact_value):
        r"""Sets the contact_value of this VerifyVerifyCodeV2Req.

        联系方式的值

        :param contact_value: The contact_value of this VerifyVerifyCodeV2Req.
        :type contact_value: str
        """
        self._contact_value = contact_value

    @property
    def contact_way(self):
        r"""Gets the contact_way of this VerifyVerifyCodeV2Req.

        联系方式的类型，0：短信；1：邮件

        :return: The contact_way of this VerifyVerifyCodeV2Req.
        :rtype: int
        """
        return self._contact_way

    @contact_way.setter
    def contact_way(self, contact_way):
        r"""Sets the contact_way of this VerifyVerifyCodeV2Req.

        联系方式的类型，0：短信；1：邮件

        :param contact_way: The contact_way of this VerifyVerifyCodeV2Req.
        :type contact_way: int
        """
        self._contact_way = contact_way

    @property
    def area_code(self):
        r"""Gets the area_code of this VerifyVerifyCodeV2Req.

        国家码

        :return: The area_code of this VerifyVerifyCodeV2Req.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        r"""Sets the area_code of this VerifyVerifyCodeV2Req.

        国家码

        :param area_code: The area_code of this VerifyVerifyCodeV2Req.
        :type area_code: str
        """
        self._area_code = area_code

    @property
    def x_customer_id(self):
        r"""Gets the x_customer_id of this VerifyVerifyCodeV2Req.

        子用户id

        :return: The x_customer_id of this VerifyVerifyCodeV2Req.
        :rtype: str
        """
        return self._x_customer_id

    @x_customer_id.setter
    def x_customer_id(self, x_customer_id):
        r"""Sets the x_customer_id of this VerifyVerifyCodeV2Req.

        子用户id

        :param x_customer_id: The x_customer_id of this VerifyVerifyCodeV2Req.
        :type x_customer_id: str
        """
        self._x_customer_id = x_customer_id

    @property
    def customer_id(self):
        r"""Gets the customer_id of this VerifyVerifyCodeV2Req.

        客户id

        :return: The customer_id of this VerifyVerifyCodeV2Req.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this VerifyVerifyCodeV2Req.

        客户id

        :param customer_id: The customer_id of this VerifyVerifyCodeV2Req.
        :type customer_id: str
        """
        self._customer_id = customer_id

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
        if not isinstance(other, VerifyVerifyCodeV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
