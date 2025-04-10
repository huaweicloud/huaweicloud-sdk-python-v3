# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str',
        'x_phone_verifiedid': 'str',
        'x_email_verifiedid': 'str',
        'body': 'CreateOrderIncidentV2Req'
    }

    attribute_map = {
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone',
        'x_phone_verifiedid': 'x-phone-verifiedid',
        'x_email_verifiedid': 'x-email-verifiedid',
        'body': 'body'
    }

    def __init__(self, x_site=None, x_language=None, x_time_zone=None, x_phone_verifiedid=None, x_email_verifiedid=None, body=None):
        r"""CreateCasesRequest

        The model defined in huaweicloud sdk

        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        :param x_phone_verifiedid: 手机验证序列号id，如果是非注册联系方式则必填，通过\&quot;查询已验证的列表\&quot;接口查询获取
        :type x_phone_verifiedid: str
        :param x_email_verifiedid: 邮件验证序列号id，如果是非注册联系方式则必填，通过\&quot;查询已验证的列表\&quot;接口查询获取
        :type x_email_verifiedid: str
        :param body: Body of the CreateCasesRequest
        :type body: :class:`huaweicloudsdkosm.v2.CreateOrderIncidentV2Req`
        """
        
        

        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self._x_phone_verifiedid = None
        self._x_email_verifiedid = None
        self._body = None
        self.discriminator = None

        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone
        if x_phone_verifiedid is not None:
            self.x_phone_verifiedid = x_phone_verifiedid
        if x_email_verifiedid is not None:
            self.x_email_verifiedid = x_email_verifiedid
        if body is not None:
            self.body = body

    @property
    def x_site(self):
        r"""Gets the x_site of this CreateCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this CreateCasesRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        r"""Sets the x_site of this CreateCasesRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this CreateCasesRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this CreateCasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateCasesRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this CreateCasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        r"""Gets the x_time_zone of this CreateCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this CreateCasesRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        r"""Sets the x_time_zone of this CreateCasesRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this CreateCasesRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

    @property
    def x_phone_verifiedid(self):
        r"""Gets the x_phone_verifiedid of this CreateCasesRequest.

        手机验证序列号id，如果是非注册联系方式则必填，通过\"查询已验证的列表\"接口查询获取

        :return: The x_phone_verifiedid of this CreateCasesRequest.
        :rtype: str
        """
        return self._x_phone_verifiedid

    @x_phone_verifiedid.setter
    def x_phone_verifiedid(self, x_phone_verifiedid):
        r"""Sets the x_phone_verifiedid of this CreateCasesRequest.

        手机验证序列号id，如果是非注册联系方式则必填，通过\"查询已验证的列表\"接口查询获取

        :param x_phone_verifiedid: The x_phone_verifiedid of this CreateCasesRequest.
        :type x_phone_verifiedid: str
        """
        self._x_phone_verifiedid = x_phone_verifiedid

    @property
    def x_email_verifiedid(self):
        r"""Gets the x_email_verifiedid of this CreateCasesRequest.

        邮件验证序列号id，如果是非注册联系方式则必填，通过\"查询已验证的列表\"接口查询获取

        :return: The x_email_verifiedid of this CreateCasesRequest.
        :rtype: str
        """
        return self._x_email_verifiedid

    @x_email_verifiedid.setter
    def x_email_verifiedid(self, x_email_verifiedid):
        r"""Sets the x_email_verifiedid of this CreateCasesRequest.

        邮件验证序列号id，如果是非注册联系方式则必填，通过\"查询已验证的列表\"接口查询获取

        :param x_email_verifiedid: The x_email_verifiedid of this CreateCasesRequest.
        :type x_email_verifiedid: str
        """
        self._x_email_verifiedid = x_email_verifiedid

    @property
    def body(self):
        r"""Gets the body of this CreateCasesRequest.

        :return: The body of this CreateCasesRequest.
        :rtype: :class:`huaweicloudsdkosm.v2.CreateOrderIncidentV2Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateCasesRequest.

        :param body: The body of this CreateCasesRequest.
        :type body: :class:`huaweicloudsdkosm.v2.CreateOrderIncidentV2Req`
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
        if not isinstance(other, CreateCasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
