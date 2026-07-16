# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunIdentityCreateReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorizer_type': 'CoreRunAuthorizerType',
        'authorizer_configuration': 'CoreRunAuthorizerConfiguration'
    }

    attribute_map = {
        'authorizer_type': 'authorizer_type',
        'authorizer_configuration': 'authorizer_configuration'
    }

    def __init__(self, authorizer_type=None, authorizer_configuration=None):
        r"""CoreRunIdentityCreateReqBody

        The model defined in huaweicloud sdk

        :param authorizer_type: 
        :type authorizer_type: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerType`
        :param authorizer_configuration: 
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerConfiguration`
        """
        
        

        self._authorizer_type = None
        self._authorizer_configuration = None
        self.discriminator = None

        self.authorizer_type = authorizer_type
        self.authorizer_configuration = authorizer_configuration

    @property
    def authorizer_type(self):
        r"""Gets the authorizer_type of this CoreRunIdentityCreateReqBody.

        :return: The authorizer_type of this CoreRunIdentityCreateReqBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerType`
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        r"""Sets the authorizer_type of this CoreRunIdentityCreateReqBody.

        :param authorizer_type: The authorizer_type of this CoreRunIdentityCreateReqBody.
        :type authorizer_type: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerType`
        """
        self._authorizer_type = authorizer_type

    @property
    def authorizer_configuration(self):
        r"""Gets the authorizer_configuration of this CoreRunIdentityCreateReqBody.

        :return: The authorizer_configuration of this CoreRunIdentityCreateReqBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerConfiguration`
        """
        return self._authorizer_configuration

    @authorizer_configuration.setter
    def authorizer_configuration(self, authorizer_configuration):
        r"""Sets the authorizer_configuration of this CoreRunIdentityCreateReqBody.

        :param authorizer_configuration: The authorizer_configuration of this CoreRunIdentityCreateReqBody.
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreRunAuthorizerConfiguration`
        """
        self._authorizer_configuration = authorizer_configuration

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoreRunIdentityCreateReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
