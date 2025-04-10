# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authentication_failure': 'CasServiceResponseAuthenticationFailure',
        'authentication_success': 'CasServiceResponseAuthenticationSuccess'
    }

    attribute_map = {
        'authentication_failure': 'authenticationFailure',
        'authentication_success': 'authenticationSuccess'
    }

    def __init__(self, authentication_failure=None, authentication_success=None):
        r"""ServiceResponse

        The model defined in huaweicloud sdk

        :param authentication_failure: 
        :type authentication_failure: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationFailure`
        :param authentication_success: 
        :type authentication_success: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationSuccess`
        """
        
        

        self._authentication_failure = None
        self._authentication_success = None
        self.discriminator = None

        if authentication_failure is not None:
            self.authentication_failure = authentication_failure
        if authentication_success is not None:
            self.authentication_success = authentication_success

    @property
    def authentication_failure(self):
        r"""Gets the authentication_failure of this ServiceResponse.

        :return: The authentication_failure of this ServiceResponse.
        :rtype: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationFailure`
        """
        return self._authentication_failure

    @authentication_failure.setter
    def authentication_failure(self, authentication_failure):
        r"""Sets the authentication_failure of this ServiceResponse.

        :param authentication_failure: The authentication_failure of this ServiceResponse.
        :type authentication_failure: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationFailure`
        """
        self._authentication_failure = authentication_failure

    @property
    def authentication_success(self):
        r"""Gets the authentication_success of this ServiceResponse.

        :return: The authentication_success of this ServiceResponse.
        :rtype: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationSuccess`
        """
        return self._authentication_success

    @authentication_success.setter
    def authentication_success(self, authentication_success):
        r"""Sets the authentication_success of this ServiceResponse.

        :param authentication_success: The authentication_success of this ServiceResponse.
        :type authentication_success: :class:`huaweicloudsdkorgid.v1.CasServiceResponseAuthenticationSuccess`
        """
        self._authentication_success = authentication_success

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
        if not isinstance(other, ServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
