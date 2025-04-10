# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupMembershipsForMemberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'identity_store_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'identity_store_id': 'identity_store_id',
        'limit': 'limit',
        'marker': 'marker',
        'user_id': 'user_id'
    }

    def __init__(self, x_security_token=None, identity_store_id=None, limit=None, marker=None, user_id=None):
        r"""ListGroupMembershipsForMemberRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param limit: 每个请求返回的最大结果数
        :type limit: int
        :param marker: 分页标记
        :type marker: str
        :param user_id: 用户唯一标识
        :type user_id: str
        """
        
        

        self._x_security_token = None
        self._identity_store_id = None
        self._limit = None
        self._marker = None
        self._user_id = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.identity_store_id = identity_store_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        self.user_id = user_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListGroupMembershipsForMemberRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListGroupMembershipsForMemberRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListGroupMembershipsForMemberRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListGroupMembershipsForMemberRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this ListGroupMembershipsForMemberRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this ListGroupMembershipsForMemberRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this ListGroupMembershipsForMemberRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this ListGroupMembershipsForMemberRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupMembershipsForMemberRequest.

        每个请求返回的最大结果数

        :return: The limit of this ListGroupMembershipsForMemberRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupMembershipsForMemberRequest.

        每个请求返回的最大结果数

        :param limit: The limit of this ListGroupMembershipsForMemberRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListGroupMembershipsForMemberRequest.

        分页标记

        :return: The marker of this ListGroupMembershipsForMemberRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGroupMembershipsForMemberRequest.

        分页标记

        :param marker: The marker of this ListGroupMembershipsForMemberRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def user_id(self):
        r"""Gets the user_id of this ListGroupMembershipsForMemberRequest.

        用户唯一标识

        :return: The user_id of this ListGroupMembershipsForMemberRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListGroupMembershipsForMemberRequest.

        用户唯一标识

        :param user_id: The user_id of this ListGroupMembershipsForMemberRequest.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ListGroupMembershipsForMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
