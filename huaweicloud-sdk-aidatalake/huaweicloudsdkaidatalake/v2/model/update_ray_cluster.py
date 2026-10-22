# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRayCluster:

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
        'cluster_config': 'RayClusterConfigV3',
        'redis_config': 'RedisConfig',
        'storages_config': 'StoragesConfig',
        'image': 'V2ImageBriefInfoAdmin',
        'history_server_config': 'HistoryServerConfig'
    }

    attribute_map = {
        'type': 'type',
        'cluster_config': 'cluster_config',
        'redis_config': 'redis_config',
        'storages_config': 'storages_config',
        'image': 'image',
        'history_server_config': 'history_server_config'
    }

    def __init__(self, type=None, cluster_config=None, redis_config=None, storages_config=None, image=None, history_server_config=None):
        r"""UpdateRayCluster

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayCluster。 **默认取值**：不涉及。 
        :type type: str
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
        """
        
        

        self._type = None
        self._cluster_config = None
        self._redis_config = None
        self._storages_config = None
        self._image = None
        self._history_server_config = None
        self.discriminator = None

        if type is not None:
            self.type = type
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

    @property
    def type(self):
        r"""Gets the type of this UpdateRayCluster.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayCluster。 **默认取值**：不涉及。 

        :return: The type of this UpdateRayCluster.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateRayCluster.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayCluster。 **默认取值**：不涉及。 

        :param type: The type of this UpdateRayCluster.
        :type type: str
        """
        self._type = type

    @property
    def cluster_config(self):
        r"""Gets the cluster_config of this UpdateRayCluster.

        :return: The cluster_config of this UpdateRayCluster.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        return self._cluster_config

    @cluster_config.setter
    def cluster_config(self, cluster_config):
        r"""Sets the cluster_config of this UpdateRayCluster.

        :param cluster_config: The cluster_config of this UpdateRayCluster.
        :type cluster_config: :class:`huaweicloudsdkaidatalake.v2.RayClusterConfigV3`
        """
        self._cluster_config = cluster_config

    @property
    def redis_config(self):
        r"""Gets the redis_config of this UpdateRayCluster.

        :return: The redis_config of this UpdateRayCluster.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        return self._redis_config

    @redis_config.setter
    def redis_config(self, redis_config):
        r"""Sets the redis_config of this UpdateRayCluster.

        :param redis_config: The redis_config of this UpdateRayCluster.
        :type redis_config: :class:`huaweicloudsdkaidatalake.v2.RedisConfig`
        """
        self._redis_config = redis_config

    @property
    def storages_config(self):
        r"""Gets the storages_config of this UpdateRayCluster.

        :return: The storages_config of this UpdateRayCluster.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        return self._storages_config

    @storages_config.setter
    def storages_config(self, storages_config):
        r"""Sets the storages_config of this UpdateRayCluster.

        :param storages_config: The storages_config of this UpdateRayCluster.
        :type storages_config: :class:`huaweicloudsdkaidatalake.v2.StoragesConfig`
        """
        self._storages_config = storages_config

    @property
    def image(self):
        r"""Gets the image of this UpdateRayCluster.

        :return: The image of this UpdateRayCluster.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UpdateRayCluster.

        :param image: The image of this UpdateRayCluster.
        :type image: :class:`huaweicloudsdkaidatalake.v2.V2ImageBriefInfoAdmin`
        """
        self._image = image

    @property
    def history_server_config(self):
        r"""Gets the history_server_config of this UpdateRayCluster.

        :return: The history_server_config of this UpdateRayCluster.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        return self._history_server_config

    @history_server_config.setter
    def history_server_config(self, history_server_config):
        r"""Sets the history_server_config of this UpdateRayCluster.

        :param history_server_config: The history_server_config of this UpdateRayCluster.
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        self._history_server_config = history_server_config

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
        if not isinstance(other, UpdateRayCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
