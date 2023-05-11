# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetIdTokenAuthParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_token': 'GetIdTokenIdTokenBody',
        'scope': 'GetIdTokenIdScopeBody'
    }

    attribute_map = {
        'id_token': 'id_token',
        'scope': 'scope'
    }

    def __init__(self, id_token=None, scope=None):
        """GetIdTokenAuthParams

        The model defined in huaweicloud sdk

        :param id_token: 
        :type id_token: :class:`huaweicloudsdkiam.v3.GetIdTokenIdTokenBody`
        :param scope: 
        :type scope: :class:`huaweicloudsdkiam.v3.GetIdTokenIdScopeBody`
        """
        
        

        self._id_token = None
        self._scope = None
        self.discriminator = None

        self.id_token = id_token
        if scope is not None:
            self.scope = scope

    @property
    def id_token(self):
        """Gets the id_token of this GetIdTokenAuthParams.

        :return: The id_token of this GetIdTokenAuthParams.
        :rtype: :class:`huaweicloudsdkiam.v3.GetIdTokenIdTokenBody`
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this GetIdTokenAuthParams.

        :param id_token: The id_token of this GetIdTokenAuthParams.
        :type id_token: :class:`huaweicloudsdkiam.v3.GetIdTokenIdTokenBody`
        """
        self._id_token = id_token

    @property
    def scope(self):
        """Gets the scope of this GetIdTokenAuthParams.

        :return: The scope of this GetIdTokenAuthParams.
        :rtype: :class:`huaweicloudsdkiam.v3.GetIdTokenIdScopeBody`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GetIdTokenAuthParams.

        :param scope: The scope of this GetIdTokenAuthParams.
        :type scope: :class:`huaweicloudsdkiam.v3.GetIdTokenIdScopeBody`
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
        if not isinstance(other, GetIdTokenAuthParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
