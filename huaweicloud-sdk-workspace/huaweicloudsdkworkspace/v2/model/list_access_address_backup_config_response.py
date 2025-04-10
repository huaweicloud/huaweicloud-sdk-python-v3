# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessAddressBackupConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config': 'list[AccessConfigInfo]'
    }

    attribute_map = {
        'access_config': 'access_config'
    }

    def __init__(self, access_config=None):
        r"""ListAccessAddressBackupConfigResponse

        The model defined in huaweicloud sdk

        :param access_config: 接入配置列表信息。
        :type access_config: list[:class:`huaweicloudsdkworkspace.v2.AccessConfigInfo`]
        """
        
        super(ListAccessAddressBackupConfigResponse, self).__init__()

        self._access_config = None
        self.discriminator = None

        if access_config is not None:
            self.access_config = access_config

    @property
    def access_config(self):
        r"""Gets the access_config of this ListAccessAddressBackupConfigResponse.

        接入配置列表信息。

        :return: The access_config of this ListAccessAddressBackupConfigResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccessConfigInfo`]
        """
        return self._access_config

    @access_config.setter
    def access_config(self, access_config):
        r"""Sets the access_config of this ListAccessAddressBackupConfigResponse.

        接入配置列表信息。

        :param access_config: The access_config of this ListAccessAddressBackupConfigResponse.
        :type access_config: list[:class:`huaweicloudsdkworkspace.v2.AccessConfigInfo`]
        """
        self._access_config = access_config

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
        if not isinstance(other, ListAccessAddressBackupConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
