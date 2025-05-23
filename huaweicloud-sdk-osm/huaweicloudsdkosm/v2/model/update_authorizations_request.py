# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuthorizationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization_id': 'str',
        'action_id': 'str',
        'x_site': 'int',
        'x_language': 'str',
        'x_time_zone': 'str',
        'body': 'OperateAuthorizationV2Req'
    }

    attribute_map = {
        'authorization_id': 'authorization_id',
        'action_id': 'action_id',
        'x_site': 'X-Site',
        'x_language': 'X-Language',
        'x_time_zone': 'X-Time-Zone',
        'body': 'body'
    }

    def __init__(self, authorization_id=None, action_id=None, x_site=None, x_language=None, x_time_zone=None, body=None):
        r"""UpdateAuthorizationsRequest

        The model defined in huaweicloud sdk

        :param authorization_id: 授权id
        :type authorization_id: str
        :param action_id: 操作id，reject，cancel
        :type action_id: str
        :param x_site: 对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。
        :type x_site: int
        :param x_language: 语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。
        :type x_language: str
        :param x_time_zone: 环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。
        :type x_time_zone: str
        :param body: Body of the UpdateAuthorizationsRequest
        :type body: :class:`huaweicloudsdkosm.v2.OperateAuthorizationV2Req`
        """
        
        

        self._authorization_id = None
        self._action_id = None
        self._x_site = None
        self._x_language = None
        self._x_time_zone = None
        self._body = None
        self.discriminator = None

        self.authorization_id = authorization_id
        if action_id is not None:
            self.action_id = action_id
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        if x_time_zone is not None:
            self.x_time_zone = x_time_zone
        if body is not None:
            self.body = body

    @property
    def authorization_id(self):
        r"""Gets the authorization_id of this UpdateAuthorizationsRequest.

        授权id

        :return: The authorization_id of this UpdateAuthorizationsRequest.
        :rtype: str
        """
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        r"""Sets the authorization_id of this UpdateAuthorizationsRequest.

        授权id

        :param authorization_id: The authorization_id of this UpdateAuthorizationsRequest.
        :type authorization_id: str
        """
        self._authorization_id = authorization_id

    @property
    def action_id(self):
        r"""Gets the action_id of this UpdateAuthorizationsRequest.

        操作id，reject，cancel

        :return: The action_id of this UpdateAuthorizationsRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this UpdateAuthorizationsRequest.

        操作id，reject，cancel

        :param action_id: The action_id of this UpdateAuthorizationsRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def x_site(self):
        r"""Gets the x_site of this UpdateAuthorizationsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :return: The x_site of this UpdateAuthorizationsRequest.
        :rtype: int
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        r"""Sets the x_site of this UpdateAuthorizationsRequest.

        对接站点信息。  0（中国站） 1（国际站），不填的话默认为0。

        :param x_site: The x_site of this UpdateAuthorizationsRequest.
        :type x_site: int
        """
        self._x_site = x_site

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateAuthorizationsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :return: The x_language of this UpdateAuthorizationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateAuthorizationsRequest.

        语言环境，值为通用的语言描述字符串，比如zh-cn等，默认为zh-cn。  会根据语言环境对应展示一些国际化的信息，比如工单类型名称等。

        :param x_language: The x_language of this UpdateAuthorizationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_time_zone(self):
        r"""Gets the x_time_zone of this UpdateAuthorizationsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :return: The x_time_zone of this UpdateAuthorizationsRequest.
        :rtype: str
        """
        return self._x_time_zone

    @x_time_zone.setter
    def x_time_zone(self, x_time_zone):
        r"""Sets the x_time_zone of this UpdateAuthorizationsRequest.

        环境时区，值为通用的时区描述字符串，比如GMT+8等，默认为GMT+8。  涉及时间的数据会根据环境时区处理。

        :param x_time_zone: The x_time_zone of this UpdateAuthorizationsRequest.
        :type x_time_zone: str
        """
        self._x_time_zone = x_time_zone

    @property
    def body(self):
        r"""Gets the body of this UpdateAuthorizationsRequest.

        :return: The body of this UpdateAuthorizationsRequest.
        :rtype: :class:`huaweicloudsdkosm.v2.OperateAuthorizationV2Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAuthorizationsRequest.

        :param body: The body of this UpdateAuthorizationsRequest.
        :type body: :class:`huaweicloudsdkosm.v2.OperateAuthorizationV2Req`
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
        if not isinstance(other, UpdateAuthorizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
