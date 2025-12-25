# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipe': 'str',
        'shards': 'float',
        'storage_mode': 'str',
        'ttl': 'float'
    }

    attribute_map = {
        'pipe': 'pipe',
        'shards': 'shards',
        'storage_mode': 'storage_mode',
        'ttl': 'ttl'
    }

    def __init__(self, pipe=None, shards=None, storage_mode=None, ttl=None):
        r"""ListCollectConfigResponseBodyTarget

        The model defined in huaweicloud sdk

        :param pipe: 管道
        :type pipe: str
        :param shards: 分片
        :type shards: float
        :param storage_mode: 存储模式
        :type storage_mode: str
        :param ttl: ttl时间
        :type ttl: float
        """
        
        

        self._pipe = None
        self._shards = None
        self._storage_mode = None
        self._ttl = None
        self.discriminator = None

        if pipe is not None:
            self.pipe = pipe
        if shards is not None:
            self.shards = shards
        if storage_mode is not None:
            self.storage_mode = storage_mode
        if ttl is not None:
            self.ttl = ttl

    @property
    def pipe(self):
        r"""Gets the pipe of this ListCollectConfigResponseBodyTarget.

        管道

        :return: The pipe of this ListCollectConfigResponseBodyTarget.
        :rtype: str
        """
        return self._pipe

    @pipe.setter
    def pipe(self, pipe):
        r"""Sets the pipe of this ListCollectConfigResponseBodyTarget.

        管道

        :param pipe: The pipe of this ListCollectConfigResponseBodyTarget.
        :type pipe: str
        """
        self._pipe = pipe

    @property
    def shards(self):
        r"""Gets the shards of this ListCollectConfigResponseBodyTarget.

        分片

        :return: The shards of this ListCollectConfigResponseBodyTarget.
        :rtype: float
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this ListCollectConfigResponseBodyTarget.

        分片

        :param shards: The shards of this ListCollectConfigResponseBodyTarget.
        :type shards: float
        """
        self._shards = shards

    @property
    def storage_mode(self):
        r"""Gets the storage_mode of this ListCollectConfigResponseBodyTarget.

        存储模式

        :return: The storage_mode of this ListCollectConfigResponseBodyTarget.
        :rtype: str
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        r"""Sets the storage_mode of this ListCollectConfigResponseBodyTarget.

        存储模式

        :param storage_mode: The storage_mode of this ListCollectConfigResponseBodyTarget.
        :type storage_mode: str
        """
        self._storage_mode = storage_mode

    @property
    def ttl(self):
        r"""Gets the ttl of this ListCollectConfigResponseBodyTarget.

        ttl时间

        :return: The ttl of this ListCollectConfigResponseBodyTarget.
        :rtype: float
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ListCollectConfigResponseBodyTarget.

        ttl时间

        :param ttl: The ttl of this ListCollectConfigResponseBodyTarget.
        :type ttl: float
        """
        self._ttl = ttl

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
        if not isinstance(other, ListCollectConfigResponseBodyTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
