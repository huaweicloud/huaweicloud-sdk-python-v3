# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionUserRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'group': 'list[str]',
        'http': 'CreateSubscriptionUserRequestHttpEndpointInfo',
        'https': 'CreateSubscriptionUserRequestHttpsEndpointInfo',
        'sms': 'CreateSubscriptionUserRequestSmsEndpointInfo',
        'email': 'CreateSubscriptionUserRequestEmailEndpointInfo'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'http': 'http',
        'https': 'https',
        'sms': 'sms',
        'email': 'email'
    }

    def __init__(self, name=None, group=None, http=None, https=None, sms=None, email=None):
        r"""CreateSubscriptionUserRequestBody

        The model defined in huaweicloud sdk

        :param name: 订阅用户名称。
        :type name: str
        :param group: 订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。
        :type group: list[str]
        :param http: 
        :type http: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        :param https: 
        :type https: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        :param sms: 
        :type sms: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        :param email: 
        :type email: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        """
        
        

        self._name = None
        self._group = None
        self._http = None
        self._https = None
        self._sms = None
        self._email = None
        self.discriminator = None

        self.name = name
        if group is not None:
            self.group = group
        if http is not None:
            self.http = http
        if https is not None:
            self.https = https
        if sms is not None:
            self.sms = sms
        if email is not None:
            self.email = email

    @property
    def name(self):
        r"""Gets the name of this CreateSubscriptionUserRequestBody.

        订阅用户名称。

        :return: The name of this CreateSubscriptionUserRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSubscriptionUserRequestBody.

        订阅用户名称。

        :param name: The name of this CreateSubscriptionUserRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def group(self):
        r"""Gets the group of this CreateSubscriptionUserRequestBody.

        订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。

        :return: The group of this CreateSubscriptionUserRequestBody.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this CreateSubscriptionUserRequestBody.

        订阅用户分组。每个订阅分组只能包含中英文、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符。

        :param group: The group of this CreateSubscriptionUserRequestBody.
        :type group: list[str]
        """
        self._group = group

    @property
    def http(self):
        r"""Gets the http of this CreateSubscriptionUserRequestBody.

        :return: The http of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        """
        return self._http

    @http.setter
    def http(self, http):
        r"""Sets the http of this CreateSubscriptionUserRequestBody.

        :param http: The http of this CreateSubscriptionUserRequestBody.
        :type http: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpEndpointInfo`
        """
        self._http = http

    @property
    def https(self):
        r"""Gets the https of this CreateSubscriptionUserRequestBody.

        :return: The https of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        """
        return self._https

    @https.setter
    def https(self, https):
        r"""Sets the https of this CreateSubscriptionUserRequestBody.

        :param https: The https of this CreateSubscriptionUserRequestBody.
        :type https: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestHttpsEndpointInfo`
        """
        self._https = https

    @property
    def sms(self):
        r"""Gets the sms of this CreateSubscriptionUserRequestBody.

        :return: The sms of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        r"""Sets the sms of this CreateSubscriptionUserRequestBody.

        :param sms: The sms of this CreateSubscriptionUserRequestBody.
        :type sms: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestSmsEndpointInfo`
        """
        self._sms = sms

    @property
    def email(self):
        r"""Gets the email of this CreateSubscriptionUserRequestBody.

        :return: The email of this CreateSubscriptionUserRequestBody.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CreateSubscriptionUserRequestBody.

        :param email: The email of this CreateSubscriptionUserRequestBody.
        :type email: :class:`huaweicloudsdksmnglobal.v2.CreateSubscriptionUserRequestEmailEndpointInfo`
        """
        self._email = email

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
        if not isinstance(other, CreateSubscriptionUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
