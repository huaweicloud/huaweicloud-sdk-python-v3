# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('x_password')

    openapi_types = {
        'conference_id': 'str',
        'x_conference_authorization': 'str',
        'x_password': 'str',
        'x_login_type': 'int',
        'x_nonce': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'x_conference_authorization': 'X-Conference-Authorization',
        'x_password': 'X-Password',
        'x_login_type': 'X-Login-Type',
        'x_nonce': 'X-Nonce'
    }

    def __init__(self, conference_id=None, x_conference_authorization=None, x_password=None, x_login_type=None, x_nonce=None):
        """CreateConfTokenRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。 &gt; 创建会议时返回的conferenceID。不是vmrConferenceID。 
        :type conference_id: str
        :param x_conference_authorization: 会控Token。 &gt; * 仅会控Token保活场景需要携带 &gt; * 如果会话已过期并且请求中携带了密码，则进行重新鉴权并回复新的会控Token
        :type x_conference_authorization: str
        :param x_password: 会议的主持人密码。 &gt; 对于会控Token保活场景，不对主持人密码鉴权。
        :type x_password: str
        :param x_login_type: 请求类型。 - 1: 业务固定为1。
        :type x_login_type: int
        :param x_nonce: 用户临时nonce token。
        :type x_nonce: str
        """
        
        

        self._conference_id = None
        self._x_conference_authorization = None
        self._x_password = None
        self._x_login_type = None
        self._x_nonce = None
        self.discriminator = None

        self.conference_id = conference_id
        if x_conference_authorization is not None:
            self.x_conference_authorization = x_conference_authorization
        self.x_password = x_password
        self.x_login_type = x_login_type
        if x_nonce is not None:
            self.x_nonce = x_nonce

    @property
    def conference_id(self):
        """Gets the conference_id of this CreateConfTokenRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :return: The conference_id of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this CreateConfTokenRequest.

        会议ID。 > 创建会议时返回的conferenceID。不是vmrConferenceID。 

        :param conference_id: The conference_id of this CreateConfTokenRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def x_conference_authorization(self):
        """Gets the x_conference_authorization of this CreateConfTokenRequest.

        会控Token。 > * 仅会控Token保活场景需要携带 > * 如果会话已过期并且请求中携带了密码，则进行重新鉴权并回复新的会控Token

        :return: The x_conference_authorization of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_conference_authorization

    @x_conference_authorization.setter
    def x_conference_authorization(self, x_conference_authorization):
        """Sets the x_conference_authorization of this CreateConfTokenRequest.

        会控Token。 > * 仅会控Token保活场景需要携带 > * 如果会话已过期并且请求中携带了密码，则进行重新鉴权并回复新的会控Token

        :param x_conference_authorization: The x_conference_authorization of this CreateConfTokenRequest.
        :type x_conference_authorization: str
        """
        self._x_conference_authorization = x_conference_authorization

    @property
    def x_password(self):
        """Gets the x_password of this CreateConfTokenRequest.

        会议的主持人密码。 > 对于会控Token保活场景，不对主持人密码鉴权。

        :return: The x_password of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_password

    @x_password.setter
    def x_password(self, x_password):
        """Sets the x_password of this CreateConfTokenRequest.

        会议的主持人密码。 > 对于会控Token保活场景，不对主持人密码鉴权。

        :param x_password: The x_password of this CreateConfTokenRequest.
        :type x_password: str
        """
        self._x_password = x_password

    @property
    def x_login_type(self):
        """Gets the x_login_type of this CreateConfTokenRequest.

        请求类型。 - 1: 业务固定为1。

        :return: The x_login_type of this CreateConfTokenRequest.
        :rtype: int
        """
        return self._x_login_type

    @x_login_type.setter
    def x_login_type(self, x_login_type):
        """Sets the x_login_type of this CreateConfTokenRequest.

        请求类型。 - 1: 业务固定为1。

        :param x_login_type: The x_login_type of this CreateConfTokenRequest.
        :type x_login_type: int
        """
        self._x_login_type = x_login_type

    @property
    def x_nonce(self):
        """Gets the x_nonce of this CreateConfTokenRequest.

        用户临时nonce token。

        :return: The x_nonce of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_nonce

    @x_nonce.setter
    def x_nonce(self, x_nonce):
        """Sets the x_nonce of this CreateConfTokenRequest.

        用户临时nonce token。

        :param x_nonce: The x_nonce of this CreateConfTokenRequest.
        :type x_nonce: str
        """
        self._x_nonce = x_nonce

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
        if not isinstance(other, CreateConfTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
