# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPasswordlessConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_ips': 'list[str]',
        'total_count': 'int'
    }

    attribute_map = {
        'config_ips': 'config_ips',
        'total_count': 'total_count'
    }

    def __init__(self, config_ips=None, total_count=None):
        r"""ShowPasswordlessConfigResponse

        The model defined in huaweicloud sdk

        :param config_ips: 免密配置,IP与网段的列表,仅支持ipv4的IP或网段。
        :type config_ips: list[str]
        :param total_count: 免密配置的总数。
        :type total_count: int
        """
        
        super(ShowPasswordlessConfigResponse, self).__init__()

        self._config_ips = None
        self._total_count = None
        self.discriminator = None

        if config_ips is not None:
            self.config_ips = config_ips
        if total_count is not None:
            self.total_count = total_count

    @property
    def config_ips(self):
        r"""Gets the config_ips of this ShowPasswordlessConfigResponse.

        免密配置,IP与网段的列表,仅支持ipv4的IP或网段。

        :return: The config_ips of this ShowPasswordlessConfigResponse.
        :rtype: list[str]
        """
        return self._config_ips

    @config_ips.setter
    def config_ips(self, config_ips):
        r"""Sets the config_ips of this ShowPasswordlessConfigResponse.

        免密配置,IP与网段的列表,仅支持ipv4的IP或网段。

        :param config_ips: The config_ips of this ShowPasswordlessConfigResponse.
        :type config_ips: list[str]
        """
        self._config_ips = config_ips

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowPasswordlessConfigResponse.

        免密配置的总数。

        :return: The total_count of this ShowPasswordlessConfigResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowPasswordlessConfigResponse.

        免密配置的总数。

        :param total_count: The total_count of this ShowPasswordlessConfigResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowPasswordlessConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
