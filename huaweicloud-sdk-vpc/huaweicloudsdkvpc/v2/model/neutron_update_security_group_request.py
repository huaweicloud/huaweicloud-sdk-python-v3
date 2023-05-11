# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdateSecurityGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str',
        'body': 'NeutronUpdateSecurityGroupRequestBody'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'body': 'body'
    }

    def __init__(self, security_group_id=None, body=None):
        """NeutronUpdateSecurityGroupRequest

        The model defined in huaweicloud sdk

        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param body: Body of the NeutronUpdateSecurityGroupRequest
        :type body: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupRequestBody`
        """
        
        

        self._security_group_id = None
        self._body = None
        self.discriminator = None

        self.security_group_id = security_group_id
        if body is not None:
            self.body = body

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NeutronUpdateSecurityGroupRequest.

        安全组ID

        :return: The security_group_id of this NeutronUpdateSecurityGroupRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NeutronUpdateSecurityGroupRequest.

        安全组ID

        :param security_group_id: The security_group_id of this NeutronUpdateSecurityGroupRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def body(self):
        """Gets the body of this NeutronUpdateSecurityGroupRequest.

        :return: The body of this NeutronUpdateSecurityGroupRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NeutronUpdateSecurityGroupRequest.

        :param body: The body of this NeutronUpdateSecurityGroupRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.NeutronUpdateSecurityGroupRequestBody`
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
        if not isinstance(other, NeutronUpdateSecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
