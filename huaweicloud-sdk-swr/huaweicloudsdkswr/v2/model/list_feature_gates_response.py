# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFeatureGatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_domain_name': 'bool',
        'enable_combination_retention': 'bool',
        'enable_artifact_scanning': 'bool'
    }

    attribute_map = {
        'enable_domain_name': 'enableDomainName',
        'enable_combination_retention': 'enableCombinationRetention',
        'enable_artifact_scanning': 'enableArtifactScanning'
    }

    def __init__(self, enable_domain_name=None, enable_combination_retention=None, enable_artifact_scanning=None):
        r"""ListFeatureGatesResponse

        The model defined in huaweicloud sdk

        :param enable_domain_name: 是否开启域名管理
        :type enable_domain_name: bool
        :param enable_combination_retention: 老化策略是否支持多条规则
        :type enable_combination_retention: bool
        :param enable_artifact_scanning: 是否支持制品扫描
        :type enable_artifact_scanning: bool
        """
        
        super().__init__()

        self._enable_domain_name = None
        self._enable_combination_retention = None
        self._enable_artifact_scanning = None
        self.discriminator = None

        if enable_domain_name is not None:
            self.enable_domain_name = enable_domain_name
        if enable_combination_retention is not None:
            self.enable_combination_retention = enable_combination_retention
        if enable_artifact_scanning is not None:
            self.enable_artifact_scanning = enable_artifact_scanning

    @property
    def enable_domain_name(self):
        r"""Gets the enable_domain_name of this ListFeatureGatesResponse.

        是否开启域名管理

        :return: The enable_domain_name of this ListFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_domain_name

    @enable_domain_name.setter
    def enable_domain_name(self, enable_domain_name):
        r"""Sets the enable_domain_name of this ListFeatureGatesResponse.

        是否开启域名管理

        :param enable_domain_name: The enable_domain_name of this ListFeatureGatesResponse.
        :type enable_domain_name: bool
        """
        self._enable_domain_name = enable_domain_name

    @property
    def enable_combination_retention(self):
        r"""Gets the enable_combination_retention of this ListFeatureGatesResponse.

        老化策略是否支持多条规则

        :return: The enable_combination_retention of this ListFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_combination_retention

    @enable_combination_retention.setter
    def enable_combination_retention(self, enable_combination_retention):
        r"""Sets the enable_combination_retention of this ListFeatureGatesResponse.

        老化策略是否支持多条规则

        :param enable_combination_retention: The enable_combination_retention of this ListFeatureGatesResponse.
        :type enable_combination_retention: bool
        """
        self._enable_combination_retention = enable_combination_retention

    @property
    def enable_artifact_scanning(self):
        r"""Gets the enable_artifact_scanning of this ListFeatureGatesResponse.

        是否支持制品扫描

        :return: The enable_artifact_scanning of this ListFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_artifact_scanning

    @enable_artifact_scanning.setter
    def enable_artifact_scanning(self, enable_artifact_scanning):
        r"""Sets the enable_artifact_scanning of this ListFeatureGatesResponse.

        是否支持制品扫描

        :param enable_artifact_scanning: The enable_artifact_scanning of this ListFeatureGatesResponse.
        :type enable_artifact_scanning: bool
        """
        self._enable_artifact_scanning = enable_artifact_scanning

    def to_dict(self):
        import warnings
        warnings.warn("ListFeatureGatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFeatureGatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
