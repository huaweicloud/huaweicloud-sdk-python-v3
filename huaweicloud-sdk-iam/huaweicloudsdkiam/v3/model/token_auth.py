# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity': 'TokenAuthIdentity'
    }

    attribute_map = {
        'identity': 'identity'
    }

    def __init__(self, identity=None):
        """TokenAuth

        The model defined in huaweicloud sdk

        :param identity: 
        :type identity: :class:`huaweicloudsdkiam.v3.TokenAuthIdentity`
        """
        
        

        self._identity = None
        self.discriminator = None

        self.identity = identity

    @property
    def identity(self):
        """Gets the identity of this TokenAuth.

        :return: The identity of this TokenAuth.
        :rtype: :class:`huaweicloudsdkiam.v3.TokenAuthIdentity`
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this TokenAuth.

        :param identity: The identity of this TokenAuth.
        :type identity: :class:`huaweicloudsdkiam.v3.TokenAuthIdentity`
        """
        self._identity = identity

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
        if not isinstance(other, TokenAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
