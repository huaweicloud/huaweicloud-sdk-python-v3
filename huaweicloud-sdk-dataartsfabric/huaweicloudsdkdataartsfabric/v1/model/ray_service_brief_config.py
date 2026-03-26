# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayServiceBriefConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ray_serve_config': 'RayServeConfig',
        'ray_cluster_config': 'RayClusterConfig',
        'log_config': 'RayServiceLogConfig',
        'oidc_config': 'OidcConfig',
        'api_config': 'ApiConfig',
        'agency_config': 'AgencyConfig'
    }

    attribute_map = {
        'ray_serve_config': 'ray_serve_config',
        'ray_cluster_config': 'ray_cluster_config',
        'log_config': 'log_config',
        'oidc_config': 'oidc_config',
        'api_config': 'api_config',
        'agency_config': 'agency_config'
    }

    def __init__(self, ray_serve_config=None, ray_cluster_config=None, log_config=None, oidc_config=None, api_config=None, agency_config=None):
        r"""RayServiceBriefConfig

        The model defined in huaweicloud sdk

        :param ray_serve_config: 
        :type ray_serve_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServeConfig`
        :param ray_cluster_config: 
        :type ray_cluster_config: :class:`huaweicloudsdkdataartsfabric.v1.RayClusterConfig`
        :param log_config: 
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceLogConfig`
        :param oidc_config: 
        :type oidc_config: :class:`huaweicloudsdkdataartsfabric.v1.OidcConfig`
        :param api_config: 
        :type api_config: :class:`huaweicloudsdkdataartsfabric.v1.ApiConfig`
        :param agency_config: 
        :type agency_config: :class:`huaweicloudsdkdataartsfabric.v1.AgencyConfig`
        """
        
        

        self._ray_serve_config = None
        self._ray_cluster_config = None
        self._log_config = None
        self._oidc_config = None
        self._api_config = None
        self._agency_config = None
        self.discriminator = None

        self.ray_serve_config = ray_serve_config
        self.ray_cluster_config = ray_cluster_config
        if log_config is not None:
            self.log_config = log_config
        if oidc_config is not None:
            self.oidc_config = oidc_config
        if api_config is not None:
            self.api_config = api_config
        if agency_config is not None:
            self.agency_config = agency_config

    @property
    def ray_serve_config(self):
        r"""Gets the ray_serve_config of this RayServiceBriefConfig.

        :return: The ray_serve_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayServeConfig`
        """
        return self._ray_serve_config

    @ray_serve_config.setter
    def ray_serve_config(self, ray_serve_config):
        r"""Sets the ray_serve_config of this RayServiceBriefConfig.

        :param ray_serve_config: The ray_serve_config of this RayServiceBriefConfig.
        :type ray_serve_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServeConfig`
        """
        self._ray_serve_config = ray_serve_config

    @property
    def ray_cluster_config(self):
        r"""Gets the ray_cluster_config of this RayServiceBriefConfig.

        :return: The ray_cluster_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayClusterConfig`
        """
        return self._ray_cluster_config

    @ray_cluster_config.setter
    def ray_cluster_config(self, ray_cluster_config):
        r"""Sets the ray_cluster_config of this RayServiceBriefConfig.

        :param ray_cluster_config: The ray_cluster_config of this RayServiceBriefConfig.
        :type ray_cluster_config: :class:`huaweicloudsdkdataartsfabric.v1.RayClusterConfig`
        """
        self._ray_cluster_config = ray_cluster_config

    @property
    def log_config(self):
        r"""Gets the log_config of this RayServiceBriefConfig.

        :return: The log_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this RayServiceBriefConfig.

        :param log_config: The log_config of this RayServiceBriefConfig.
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceLogConfig`
        """
        self._log_config = log_config

    @property
    def oidc_config(self):
        r"""Gets the oidc_config of this RayServiceBriefConfig.

        :return: The oidc_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.OidcConfig`
        """
        return self._oidc_config

    @oidc_config.setter
    def oidc_config(self, oidc_config):
        r"""Sets the oidc_config of this RayServiceBriefConfig.

        :param oidc_config: The oidc_config of this RayServiceBriefConfig.
        :type oidc_config: :class:`huaweicloudsdkdataartsfabric.v1.OidcConfig`
        """
        self._oidc_config = oidc_config

    @property
    def api_config(self):
        r"""Gets the api_config of this RayServiceBriefConfig.

        :return: The api_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ApiConfig`
        """
        return self._api_config

    @api_config.setter
    def api_config(self, api_config):
        r"""Sets the api_config of this RayServiceBriefConfig.

        :param api_config: The api_config of this RayServiceBriefConfig.
        :type api_config: :class:`huaweicloudsdkdataartsfabric.v1.ApiConfig`
        """
        self._api_config = api_config

    @property
    def agency_config(self):
        r"""Gets the agency_config of this RayServiceBriefConfig.

        :return: The agency_config of this RayServiceBriefConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.AgencyConfig`
        """
        return self._agency_config

    @agency_config.setter
    def agency_config(self, agency_config):
        r"""Sets the agency_config of this RayServiceBriefConfig.

        :param agency_config: The agency_config of this RayServiceBriefConfig.
        :type agency_config: :class:`huaweicloudsdkdataartsfabric.v1.AgencyConfig`
        """
        self._agency_config = agency_config

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
        if not isinstance(other, RayServiceBriefConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
