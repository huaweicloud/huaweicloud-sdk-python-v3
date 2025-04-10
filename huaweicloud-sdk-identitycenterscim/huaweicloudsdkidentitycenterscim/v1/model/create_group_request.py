# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'tenant_id': 'str',
        'body': 'CreateGroupReqBody'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'tenant_id': 'tenant_id',
        'body': 'body'
    }

    def __init__(self, authorization=None, tenant_id=None, body=None):
        r"""CreateGroupRequest

        The model defined in huaweicloud sdk

        :param authorization: 承载令牌
        :type authorization: str
        :param tenant_id: 租户的全局唯一标识符（ID）
        :type tenant_id: str
        :param body: Body of the CreateGroupRequest
        :type body: :class:`huaweicloudsdkidentitycenterscim.v1.CreateGroupReqBody`
        """
        
        

        self._authorization = None
        self._tenant_id = None
        self._body = None
        self.discriminator = None

        self.authorization = authorization
        self.tenant_id = tenant_id
        if body is not None:
            self.body = body

    @property
    def authorization(self):
        r"""Gets the authorization of this CreateGroupRequest.

        承载令牌

        :return: The authorization of this CreateGroupRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this CreateGroupRequest.

        承载令牌

        :param authorization: The authorization of this CreateGroupRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateGroupRequest.

        租户的全局唯一标识符（ID）

        :return: The tenant_id of this CreateGroupRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateGroupRequest.

        租户的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this CreateGroupRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def body(self):
        r"""Gets the body of this CreateGroupRequest.

        :return: The body of this CreateGroupRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.CreateGroupReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateGroupRequest.

        :param body: The body of this CreateGroupRequest.
        :type body: :class:`huaweicloudsdkidentitycenterscim.v1.CreateGroupReqBody`
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
        if not isinstance(other, CreateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
