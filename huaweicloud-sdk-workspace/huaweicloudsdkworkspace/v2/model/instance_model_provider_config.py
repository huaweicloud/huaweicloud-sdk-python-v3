# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceModelProviderConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'provider_id': 'str',
        'name': 'str',
        'provider_type': 'str',
        'update_time': 'str',
        'api_base_url': 'str',
        'custom_config': 'ProviderCustomConfig',
        'models': 'list[ModelInfo]'
    }

    attribute_map = {
        'id': 'id',
        'provider_id': 'provider_id',
        'name': 'name',
        'provider_type': 'provider_type',
        'update_time': 'update_time',
        'api_base_url': 'api_base_url',
        'custom_config': 'custom_config',
        'models': 'models'
    }

    def __init__(self, id=None, provider_id=None, name=None, provider_type=None, update_time=None, api_base_url=None, custom_config=None, models=None):
        r"""InstanceModelProviderConfig

        The model defined in huaweicloud sdk

        :param id: 供应商配置主键 ID
        :type id: str
        :param provider_id: 供应商标识
        :type provider_id: str
        :param name: 供应商名称
        :type name: str
        :param provider_type: 供应商类型
        :type provider_type: str
        :param update_time: 供应商更新时间
        :type update_time: str
        :param api_base_url: 供应商 API 地址
        :type api_base_url: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param models: 模型列表
        :type models: list[:class:`huaweicloudsdkworkspace.v2.ModelInfo`]
        """
        
        

        self._id = None
        self._provider_id = None
        self._name = None
        self._provider_type = None
        self._update_time = None
        self._api_base_url = None
        self._custom_config = None
        self._models = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider_id is not None:
            self.provider_id = provider_id
        if name is not None:
            self.name = name
        if provider_type is not None:
            self.provider_type = provider_type
        if update_time is not None:
            self.update_time = update_time
        if api_base_url is not None:
            self.api_base_url = api_base_url
        if custom_config is not None:
            self.custom_config = custom_config
        if models is not None:
            self.models = models

    @property
    def id(self):
        r"""Gets the id of this InstanceModelProviderConfig.

        供应商配置主键 ID

        :return: The id of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceModelProviderConfig.

        供应商配置主键 ID

        :param id: The id of this InstanceModelProviderConfig.
        :type id: str
        """
        self._id = id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this InstanceModelProviderConfig.

        供应商标识

        :return: The provider_id of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this InstanceModelProviderConfig.

        供应商标识

        :param provider_id: The provider_id of this InstanceModelProviderConfig.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def name(self):
        r"""Gets the name of this InstanceModelProviderConfig.

        供应商名称

        :return: The name of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceModelProviderConfig.

        供应商名称

        :param name: The name of this InstanceModelProviderConfig.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        r"""Gets the provider_type of this InstanceModelProviderConfig.

        供应商类型

        :return: The provider_type of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this InstanceModelProviderConfig.

        供应商类型

        :param provider_type: The provider_type of this InstanceModelProviderConfig.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def update_time(self):
        r"""Gets the update_time of this InstanceModelProviderConfig.

        供应商更新时间

        :return: The update_time of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InstanceModelProviderConfig.

        供应商更新时间

        :param update_time: The update_time of this InstanceModelProviderConfig.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def api_base_url(self):
        r"""Gets the api_base_url of this InstanceModelProviderConfig.

        供应商 API 地址

        :return: The api_base_url of this InstanceModelProviderConfig.
        :rtype: str
        """
        return self._api_base_url

    @api_base_url.setter
    def api_base_url(self, api_base_url):
        r"""Sets the api_base_url of this InstanceModelProviderConfig.

        供应商 API 地址

        :param api_base_url: The api_base_url of this InstanceModelProviderConfig.
        :type api_base_url: str
        """
        self._api_base_url = api_base_url

    @property
    def custom_config(self):
        r"""Gets the custom_config of this InstanceModelProviderConfig.

        :return: The custom_config of this InstanceModelProviderConfig.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this InstanceModelProviderConfig.

        :param custom_config: The custom_config of this InstanceModelProviderConfig.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def models(self):
        r"""Gets the models of this InstanceModelProviderConfig.

        模型列表

        :return: The models of this InstanceModelProviderConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ModelInfo`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this InstanceModelProviderConfig.

        模型列表

        :param models: The models of this InstanceModelProviderConfig.
        :type models: list[:class:`huaweicloudsdkworkspace.v2.ModelInfo`]
        """
        self._models = models

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
        if not isinstance(other, InstanceModelProviderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
