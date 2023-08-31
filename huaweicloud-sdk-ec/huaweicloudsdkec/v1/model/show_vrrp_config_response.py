# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVrrpConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vrrp_configs': 'list[VrrpConfigItem]'
    }

    attribute_map = {
        'vrrp_configs': 'vrrp_configs'
    }

    def __init__(self, vrrp_configs=None):
        """ShowVrrpConfigResponse

        The model defined in huaweicloud sdk

        :param vrrp_configs: 
        :type vrrp_configs: list[:class:`huaweicloudsdkec.v1.VrrpConfigItem`]
        """
        
        super(ShowVrrpConfigResponse, self).__init__()

        self._vrrp_configs = None
        self.discriminator = None

        if vrrp_configs is not None:
            self.vrrp_configs = vrrp_configs

    @property
    def vrrp_configs(self):
        """Gets the vrrp_configs of this ShowVrrpConfigResponse.

        :return: The vrrp_configs of this ShowVrrpConfigResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.VrrpConfigItem`]
        """
        return self._vrrp_configs

    @vrrp_configs.setter
    def vrrp_configs(self, vrrp_configs):
        """Sets the vrrp_configs of this ShowVrrpConfigResponse.

        :param vrrp_configs: The vrrp_configs of this ShowVrrpConfigResponse.
        :type vrrp_configs: list[:class:`huaweicloudsdkec.v1.VrrpConfigItem`]
        """
        self._vrrp_configs = vrrp_configs

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
        if not isinstance(other, ShowVrrpConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
