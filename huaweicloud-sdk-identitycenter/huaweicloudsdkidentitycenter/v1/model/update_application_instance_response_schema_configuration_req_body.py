# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApplicationInstanceResponseSchemaConfigurationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'response_schema_config': 'ResponseSchemaConfigDto'
    }

    attribute_map = {
        'response_schema_config': 'response_schema_config'
    }

    def __init__(self, response_schema_config=None):
        r"""UpdateApplicationInstanceResponseSchemaConfigurationReqBody

        The model defined in huaweicloud sdk

        :param response_schema_config: 
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        
        

        self._response_schema_config = None
        self.discriminator = None

        self.response_schema_config = response_schema_config

    @property
    def response_schema_config(self):
        r"""Gets the response_schema_config of this UpdateApplicationInstanceResponseSchemaConfigurationReqBody.

        :return: The response_schema_config of this UpdateApplicationInstanceResponseSchemaConfigurationReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        return self._response_schema_config

    @response_schema_config.setter
    def response_schema_config(self, response_schema_config):
        r"""Sets the response_schema_config of this UpdateApplicationInstanceResponseSchemaConfigurationReqBody.

        :param response_schema_config: The response_schema_config of this UpdateApplicationInstanceResponseSchemaConfigurationReqBody.
        :type response_schema_config: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaConfigDto`
        """
        self._response_schema_config = response_schema_config

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
        if not isinstance(other, UpdateApplicationInstanceResponseSchemaConfigurationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
