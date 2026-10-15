# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthReportConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'list[InstanceHealthReportConfigDto]'
    }

    attribute_map = {
        'configs': 'configs'
    }

    def __init__(self, configs=None):
        r"""ListHealthReportConfigsResponse

        The model defined in huaweicloud sdk

        :param configs: 实例配置详情列表。
        :type configs: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReportConfigDto`]
        """
        
        super().__init__()

        self._configs = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs

    @property
    def configs(self):
        r"""Gets the configs of this ListHealthReportConfigsResponse.

        实例配置详情列表。

        :return: The configs of this ListHealthReportConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReportConfigDto`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this ListHealthReportConfigsResponse.

        实例配置详情列表。

        :param configs: The configs of this ListHealthReportConfigsResponse.
        :type configs: list[:class:`huaweicloudsdkdas.v3.InstanceHealthReportConfigDto`]
        """
        self._configs = configs

    def to_dict(self):
        import warnings
        warnings.warn("ListHealthReportConfigsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListHealthReportConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
