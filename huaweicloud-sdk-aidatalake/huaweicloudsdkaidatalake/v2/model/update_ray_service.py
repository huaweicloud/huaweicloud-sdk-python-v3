# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRayService:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'serve_config': 'ServeConfig',
        'cluster_config': 'RayClusterConfigV3',
        'redis_config': 'RedisConfig',
        'storages_config': 'StoragesConfig',
        'image': 'V2ImageBriefInfoAdmin',
        'history_server_config': 'HistoryServerConfig',
        'data_infos': 'list[DataInfo]'
    }

    attribute_map = {
        'type': 'type',
        'serve_config': 'serve_config',
        'cluster_config': 'cluster_config',
        'redis_config': 'redis_config',
        'storages_config': 'storages_config',
        'image': 'image',
        'history_server_config': 'history_server_config',
        'data_infos': 'data_infos'
    }

    def __init__(self, type=None, serve_config=None, cluster_config=None, redis_config=None, storages_config=None, image=None, history_server_config=None, data_infos=None):
        r"""UpdateRayService

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 
        :type type: str
        :param serve_config: 
        :type serve_config: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        :param cluster_config: 
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        :param redis_config: 
        :type redis_config: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        :param storages_config: 
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        :param history_server_config: 
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        :param data_infos: **参数解释**：模型信息列表（可选）。更新时如果模型没有变化，可以不填此字段；如果需要更新模型，则填写新的模型信息。 **约束限制**：不涉及。
        :type data_infos: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
        """
        
        

        self._type = None
        self._serve_config = None
        self._cluster_config = None
        self._redis_config = None
        self._storages_config = None
        self._image = None
        self._history_server_config = None
        self._data_infos = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if serve_config is not None:
            self.serve_config = serve_config
        if cluster_config is not None:
            self.cluster_config = cluster_config
        if redis_config is not None:
            self.redis_config = redis_config
        if storages_config is not None:
            self.storages_config = storages_config
        if image is not None:
            self.image = image
        if history_server_config is not None:
            self.history_server_config = history_server_config
        if data_infos is not None:
            self.data_infos = data_infos

    @property
    def type(self):
        r"""Gets the type of this UpdateRayService.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 

        :return: The type of this UpdateRayService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateRayService.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayService。 **默认取值**：不涉及。 

        :param type: The type of this UpdateRayService.
        :type type: str
        """
        self._type = type

    @property
    def serve_config(self):
        r"""Gets the serve_config of this UpdateRayService.

        :return: The serve_config of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        """
        return self._serve_config

    @serve_config.setter
    def serve_config(self, serve_config):
        r"""Sets the serve_config of this UpdateRayService.

        :param serve_config: The serve_config of this UpdateRayService.
        :type serve_config: :class:`huaweicloudsdkaidatalake.v2.ServeConfig`
        """
        self._serve_config = serve_config

    @property
    def cluster_config(self):
        r"""Gets the cluster_config of this UpdateRayService.

        :return: The cluster_config of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        return self._cluster_config

    @cluster_config.setter
    def cluster_config(self, cluster_config):
        r"""Sets the cluster_config of this UpdateRayService.

        :param cluster_config: The cluster_config of this UpdateRayService.
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        self._cluster_config = cluster_config

    @property
    def redis_config(self):
        r"""Gets the redis_config of this UpdateRayService.

        :return: The redis_config of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        return self._redis_config

    @redis_config.setter
    def redis_config(self, redis_config):
        r"""Sets the redis_config of this UpdateRayService.

        :param redis_config: The redis_config of this UpdateRayService.
        :type redis_config: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        self._redis_config = redis_config

    @property
    def storages_config(self):
        r"""Gets the storages_config of this UpdateRayService.

        :return: The storages_config of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        return self._storages_config

    @storages_config.setter
    def storages_config(self, storages_config):
        r"""Sets the storages_config of this UpdateRayService.

        :param storages_config: The storages_config of this UpdateRayService.
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        self._storages_config = storages_config

    @property
    def image(self):
        r"""Gets the image of this UpdateRayService.

        :return: The image of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UpdateRayService.

        :param image: The image of this UpdateRayService.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        self._image = image

    @property
    def history_server_config(self):
        r"""Gets the history_server_config of this UpdateRayService.

        :return: The history_server_config of this UpdateRayService.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        return self._history_server_config

    @history_server_config.setter
    def history_server_config(self, history_server_config):
        r"""Sets the history_server_config of this UpdateRayService.

        :param history_server_config: The history_server_config of this UpdateRayService.
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        self._history_server_config = history_server_config

    @property
    def data_infos(self):
        r"""Gets the data_infos of this UpdateRayService.

        **参数解释**：模型信息列表（可选）。更新时如果模型没有变化，可以不填此字段；如果需要更新模型，则填写新的模型信息。 **约束限制**：不涉及。

        :return: The data_infos of this UpdateRayService.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
        """
        return self._data_infos

    @data_infos.setter
    def data_infos(self, data_infos):
        r"""Sets the data_infos of this UpdateRayService.

        **参数解释**：模型信息列表（可选）。更新时如果模型没有变化，可以不填此字段；如果需要更新模型，则填写新的模型信息。 **约束限制**：不涉及。

        :param data_infos: The data_infos of this UpdateRayService.
        :type data_infos: list[:class:`huaweicloudsdkaidatalake.v2.DataInfo`]
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
        if not isinstance(other, UpdateRayService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
