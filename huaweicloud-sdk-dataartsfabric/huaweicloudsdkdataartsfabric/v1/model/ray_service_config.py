# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayServiceConfig:

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
        'agency_config': 'AgencyConfig',
        'data_infos': 'list[DataBriefInfo]'
    }

    attribute_map = {
        'ray_serve_config': 'ray_serve_config',
        'ray_cluster_config': 'ray_cluster_config',
        'log_config': 'log_config',
        'oidc_config': 'oidc_config',
        'api_config': 'api_config',
        'agency_config': 'agency_config',
        'data_infos': 'data_infos'
    }

    def __init__(self, ray_serve_config=None, ray_cluster_config=None, log_config=None, oidc_config=None, api_config=None, agency_config=None, data_infos=None):
        r"""RayServiceConfig

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
        :param data_infos: **参数解释**：数据信息。 **约束限制**：不涉及。 **取值范围**：[0,1]。 **默认取值**：不涉及。 
        :type data_infos: list[:class:`huaweicloudsdkdataartsfabric.v1.DataBriefInfo`]
        """
        
        

        self._ray_serve_config = None
        self._ray_cluster_config = None
        self._log_config = None
        self._oidc_config = None
        self._api_config = None
        self._agency_config = None
        self._data_infos = None
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
        if data_infos is not None:
            self.data_infos = data_infos

    @property
    def ray_serve_config(self):
        r"""Gets the ray_serve_config of this RayServiceConfig.

        :return: The ray_serve_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayServeConfig`
        """
        return self._ray_serve_config

    @ray_serve_config.setter
    def ray_serve_config(self, ray_serve_config):
        r"""Sets the ray_serve_config of this RayServiceConfig.

        :param ray_serve_config: The ray_serve_config of this RayServiceConfig.
        :type ray_serve_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServeConfig`
        """
        self._ray_serve_config = ray_serve_config

    @property
    def ray_cluster_config(self):
        r"""Gets the ray_cluster_config of this RayServiceConfig.

        :return: The ray_cluster_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayClusterConfig`
        """
        return self._ray_cluster_config

    @ray_cluster_config.setter
    def ray_cluster_config(self, ray_cluster_config):
        r"""Sets the ray_cluster_config of this RayServiceConfig.

        :param ray_cluster_config: The ray_cluster_config of this RayServiceConfig.
        :type ray_cluster_config: :class:`huaweicloudsdkdataartsfabric.v1.RayClusterConfig`
        """
        self._ray_cluster_config = ray_cluster_config

    @property
    def log_config(self):
        r"""Gets the log_config of this RayServiceConfig.

        :return: The log_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceLogConfig`
        """
        return self._log_config

    @log_config.setter
    def log_config(self, log_config):
        r"""Sets the log_config of this RayServiceConfig.

        :param log_config: The log_config of this RayServiceConfig.
        :type log_config: :class:`huaweicloudsdkdataartsfabric.v1.RayServiceLogConfig`
        """
        self._log_config = log_config

    @property
    def oidc_config(self):
        r"""Gets the oidc_config of this RayServiceConfig.

        :return: The oidc_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.OidcConfig`
        """
        return self._oidc_config

    @oidc_config.setter
    def oidc_config(self, oidc_config):
        r"""Sets the oidc_config of this RayServiceConfig.

        :param oidc_config: The oidc_config of this RayServiceConfig.
        :type oidc_config: :class:`huaweicloudsdkdataartsfabric.v1.OidcConfig`
        """
        self._oidc_config = oidc_config

    @property
    def api_config(self):
        r"""Gets the api_config of this RayServiceConfig.

        :return: The api_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ApiConfig`
        """
        return self._api_config

    @api_config.setter
    def api_config(self, api_config):
        r"""Sets the api_config of this RayServiceConfig.

        :param api_config: The api_config of this RayServiceConfig.
        :type api_config: :class:`huaweicloudsdkdataartsfabric.v1.ApiConfig`
        """
        self._api_config = api_config

    @property
    def agency_config(self):
        r"""Gets the agency_config of this RayServiceConfig.

        :return: The agency_config of this RayServiceConfig.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.AgencyConfig`
        """
        return self._agency_config

    @agency_config.setter
    def agency_config(self, agency_config):
        r"""Sets the agency_config of this RayServiceConfig.

        :param agency_config: The agency_config of this RayServiceConfig.
        :type agency_config: :class:`huaweicloudsdkdataartsfabric.v1.AgencyConfig`
        """
        self._agency_config = agency_config

    @property
    def data_infos(self):
        r"""Gets the data_infos of this RayServiceConfig.

        **参数解释**：数据信息。 **约束限制**：不涉及。 **取值范围**：[0,1]。 **默认取值**：不涉及。 

        :return: The data_infos of this RayServiceConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.DataBriefInfo`]
        """
        return self._data_infos

    @data_infos.setter
    def data_infos(self, data_infos):
        r"""Sets the data_infos of this RayServiceConfig.

        **参数解释**：数据信息。 **约束限制**：不涉及。 **取值范围**：[0,1]。 **默认取值**：不涉及。 

        :param data_infos: The data_infos of this RayServiceConfig.
        :type data_infos: list[:class:`huaweicloudsdkdataartsfabric.v1.DataBriefInfo`]
        """
        self._data_infos = data_infos

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
        if not isinstance(other, RayServiceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
