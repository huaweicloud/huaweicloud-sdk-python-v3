# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyTokenAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity': 'AgencyTokenIdentity',
        'scope': 'AgencyTokenScope'
    }

    attribute_map = {
        'identity': 'identity',
        'scope': 'scope'
    }

    def __init__(self, identity=None, scope=None):
        r"""AgencyTokenAuth

        The model defined in huaweicloud sdk

        :param identity: 
        :type identity: :class:`huaweicloudsdkiam.v3.AgencyTokenIdentity`
        :param scope: 
        :type scope: :class:`huaweicloudsdkiam.v3.AgencyTokenScope`
        """
        
        

        self._identity = None
        self._scope = None
        self.discriminator = None

        self.identity = identity
        self.scope = scope

    @property
    def identity(self):
        r"""Gets the identity of this AgencyTokenAuth.

        :return: The identity of this AgencyTokenAuth.
        :rtype: :class:`huaweicloudsdkiam.v3.AgencyTokenIdentity`
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        r"""Sets the identity of this AgencyTokenAuth.

        :param identity: The identity of this AgencyTokenAuth.
        :type identity: :class:`huaweicloudsdkiam.v3.AgencyTokenIdentity`
        """
        self._identity = identity

    @property
    def scope(self):
        r"""Gets the scope of this AgencyTokenAuth.

        :return: The scope of this AgencyTokenAuth.
        :rtype: :class:`huaweicloudsdkiam.v3.AgencyTokenScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this AgencyTokenAuth.

        :param scope: The scope of this AgencyTokenAuth.
        :type scope: :class:`huaweicloudsdkiam.v3.AgencyTokenScope`
        """
        self._scope = scope

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
        if not isinstance(other, AgencyTokenAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
