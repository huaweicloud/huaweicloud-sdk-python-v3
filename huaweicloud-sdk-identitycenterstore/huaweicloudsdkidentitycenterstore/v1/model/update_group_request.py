# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupRequest:

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
        'group_id': 'str',
        'body': 'UpdateGroupReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'identity_store_id': 'identity_store_id',
        'group_id': 'group_id',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, identity_store_id=None, group_id=None, body=None):
        r"""UpdateGroupRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param group_id: 身份源中IAM身份中心用户组的全局唯一标识符（ID）
        :type group_id: str
        :param body: Body of the UpdateGroupRequest
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupReqBody`
        """
        
        

        self._x_security_token = None
        self._identity_store_id = None
        self._group_id = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.identity_store_id = identity_store_id
        self.group_id = group_id
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this UpdateGroupRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this UpdateGroupRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this UpdateGroupRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this UpdateGroupRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this UpdateGroupRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this UpdateGroupRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this UpdateGroupRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this UpdateGroupRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateGroupRequest.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :return: The group_id of this UpdateGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateGroupRequest.

        身份源中IAM身份中心用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this UpdateGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body(self):
        r"""Gets the body of this UpdateGroupRequest.

        :return: The body of this UpdateGroupRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGroupRequest.

        :param body: The body of this UpdateGroupRequest.
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupReqBody`
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
        if not isinstance(other, UpdateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
