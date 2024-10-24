# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccountAssignmentRequest:

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
        'instance_id': 'str',
        'x_security_token': 'str',
        'body': 'CreateAccountAssignmentReqBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_security_token': 'X-Security-Token',
        'body': 'body'
    }

    def __init__(self, instance_id=None, x_security_token=None, body=None):
        """CreateAccountAssignmentRequest

        The model defined in huaweicloud sdk

        :param instance_id: IAM身份中心实例的全局唯一标识符（ID）。
        :type instance_id: str
        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param body: Body of the CreateAccountAssignmentRequest
        :type body: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentReqBody`
        """
        
        

        self._instance_id = None
        self._x_security_token = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_security_token is not None:
            self.x_security_token = x_security_token
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateAccountAssignmentRequest.

        IAM身份中心实例的全局唯一标识符（ID）。

        :return: The instance_id of this CreateAccountAssignmentRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateAccountAssignmentRequest.

        IAM身份中心实例的全局唯一标识符（ID）。

        :param instance_id: The instance_id of this CreateAccountAssignmentRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_security_token(self):
        """Gets the x_security_token of this CreateAccountAssignmentRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this CreateAccountAssignmentRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this CreateAccountAssignmentRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this CreateAccountAssignmentRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def body(self):
        """Gets the body of this CreateAccountAssignmentRequest.

        :return: The body of this CreateAccountAssignmentRequest.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateAccountAssignmentRequest.

        :param body: The body of this CreateAccountAssignmentRequest.
        :type body: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentReqBody`
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
        if not isinstance(other, CreateAccountAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
