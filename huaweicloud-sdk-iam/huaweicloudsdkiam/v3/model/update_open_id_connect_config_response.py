# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpenIdConnectConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'openid_connect_config': 'OpenIdConnectConfig'
    }

    attribute_map = {
        'openid_connect_config': 'openid_connect_config'
    }

    def __init__(self, openid_connect_config=None):
        """UpdateOpenIdConnectConfigResponse

        The model defined in huaweicloud sdk

        :param openid_connect_config: 
        :type openid_connect_config: :class:`huaweicloudsdkiam.v3.OpenIdConnectConfig`
        """
        
        super(UpdateOpenIdConnectConfigResponse, self).__init__()

        self._openid_connect_config = None
        self.discriminator = None

        if openid_connect_config is not None:
            self.openid_connect_config = openid_connect_config

    @property
    def openid_connect_config(self):
        """Gets the openid_connect_config of this UpdateOpenIdConnectConfigResponse.

        :return: The openid_connect_config of this UpdateOpenIdConnectConfigResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.OpenIdConnectConfig`
        """
        return self._openid_connect_config

    @openid_connect_config.setter
    def openid_connect_config(self, openid_connect_config):
        """Sets the openid_connect_config of this UpdateOpenIdConnectConfigResponse.

        :param openid_connect_config: The openid_connect_config of this UpdateOpenIdConnectConfigResponse.
        :type openid_connect_config: :class:`huaweicloudsdkiam.v3.OpenIdConnectConfig`
        """
        self._openid_connect_config = openid_connect_config

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
        if not isinstance(other, UpdateOpenIdConnectConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
