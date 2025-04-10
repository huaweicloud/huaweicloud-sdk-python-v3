# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubCutomerInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mobile': 'str',
        'email': 'str',
        'customer_id': 'str',
        'domain_id': 'str',
        'customer_name': 'str',
        'area_code': 'str'
    }

    attribute_map = {
        'mobile': 'mobile',
        'email': 'email',
        'customer_id': 'customer_id',
        'domain_id': 'domain_id',
        'customer_name': 'customer_name',
        'area_code': 'area_code'
    }

    def __init__(self, mobile=None, email=None, customer_id=None, domain_id=None, customer_name=None, area_code=None):
        r"""SubCutomerInfoV2

        The model defined in huaweicloud sdk

        :param mobile: 手机号（匿名化）
        :type mobile: str
        :param email: 邮箱（匿名化）
        :type email: str
        :param customer_id: 客户id
        :type customer_id: str
        :param domain_id: 主账号id
        :type domain_id: str
        :param customer_name: 客户名称（匿名化）
        :type customer_name: str
        :param area_code: 国家码
        :type area_code: str
        """
        
        

        self._mobile = None
        self._email = None
        self._customer_id = None
        self._domain_id = None
        self._customer_name = None
        self._area_code = None
        self.discriminator = None

        if mobile is not None:
            self.mobile = mobile
        if email is not None:
            self.email = email
        if customer_id is not None:
            self.customer_id = customer_id
        if domain_id is not None:
            self.domain_id = domain_id
        if customer_name is not None:
            self.customer_name = customer_name
        if area_code is not None:
            self.area_code = area_code

    @property
    def mobile(self):
        r"""Gets the mobile of this SubCutomerInfoV2.

        手机号（匿名化）

        :return: The mobile of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this SubCutomerInfoV2.

        手机号（匿名化）

        :param mobile: The mobile of this SubCutomerInfoV2.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def email(self):
        r"""Gets the email of this SubCutomerInfoV2.

        邮箱（匿名化）

        :return: The email of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this SubCutomerInfoV2.

        邮箱（匿名化）

        :param email: The email of this SubCutomerInfoV2.
        :type email: str
        """
        self._email = email

    @property
    def customer_id(self):
        r"""Gets the customer_id of this SubCutomerInfoV2.

        客户id

        :return: The customer_id of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this SubCutomerInfoV2.

        客户id

        :param customer_id: The customer_id of this SubCutomerInfoV2.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SubCutomerInfoV2.

        主账号id

        :return: The domain_id of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SubCutomerInfoV2.

        主账号id

        :param domain_id: The domain_id of this SubCutomerInfoV2.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def customer_name(self):
        r"""Gets the customer_name of this SubCutomerInfoV2.

        客户名称（匿名化）

        :return: The customer_name of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        r"""Sets the customer_name of this SubCutomerInfoV2.

        客户名称（匿名化）

        :param customer_name: The customer_name of this SubCutomerInfoV2.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def area_code(self):
        r"""Gets the area_code of this SubCutomerInfoV2.

        国家码

        :return: The area_code of this SubCutomerInfoV2.
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        r"""Sets the area_code of this SubCutomerInfoV2.

        国家码

        :param area_code: The area_code of this SubCutomerInfoV2.
        :type area_code: str
        """
        self._area_code = area_code

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
        if not isinstance(other, SubCutomerInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
