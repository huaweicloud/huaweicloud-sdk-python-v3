# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSsoConfigurationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sso_configuration': 'SSOConfigurationDto',
        'configuration_type': 'str'
    }

    attribute_map = {
        'sso_configuration': 'sso_configuration',
        'configuration_type': 'configuration_type'
    }

    def __init__(self, sso_configuration=None, configuration_type=None):
        r"""UpdateSsoConfigurationReqBody

        The model defined in huaweicloud sdk

        :param sso_configuration: 
        :type sso_configuration: :class:`huaweicloudsdkidentitycenter.v1.SSOConfigurationDto`
        :param configuration_type: 配置类型
        :type configuration_type: str
        """
        
        

        self._sso_configuration = None
        self._configuration_type = None
        self.discriminator = None

        self.sso_configuration = sso_configuration
        self.configuration_type = configuration_type

    @property
    def sso_configuration(self):
        r"""Gets the sso_configuration of this UpdateSsoConfigurationReqBody.

        :return: The sso_configuration of this UpdateSsoConfigurationReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.SSOConfigurationDto`
        """
        return self._sso_configuration

    @sso_configuration.setter
    def sso_configuration(self, sso_configuration):
        r"""Sets the sso_configuration of this UpdateSsoConfigurationReqBody.

        :param sso_configuration: The sso_configuration of this UpdateSsoConfigurationReqBody.
        :type sso_configuration: :class:`huaweicloudsdkidentitycenter.v1.SSOConfigurationDto`
        """
        self._sso_configuration = sso_configuration

    @property
    def configuration_type(self):
        r"""Gets the configuration_type of this UpdateSsoConfigurationReqBody.

        配置类型

        :return: The configuration_type of this UpdateSsoConfigurationReqBody.
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        r"""Sets the configuration_type of this UpdateSsoConfigurationReqBody.

        配置类型

        :param configuration_type: The configuration_type of this UpdateSsoConfigurationReqBody.
        :type configuration_type: str
        """
        self._configuration_type = configuration_type

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
        if not isinstance(other, UpdateSsoConfigurationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
