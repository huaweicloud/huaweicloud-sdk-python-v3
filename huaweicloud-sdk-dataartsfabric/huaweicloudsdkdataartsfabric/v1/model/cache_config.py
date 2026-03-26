# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mnt_path': 'str',
        'cache_ins_id': 'str'
    }

    attribute_map = {
        'mnt_path': 'mnt_path',
        'cache_ins_id': 'cache_ins_id'
    }

    def __init__(self, mnt_path=None, cache_ins_id=None):
        r"""CacheConfig

        The model defined in huaweicloud sdk

        :param mnt_path: **参数解释**：挂载路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type mnt_path: str
        :param cache_ins_id: **参数解释**：分布式缓存id。 **约束限制**：不涉及。 **取值范围**：已创建的分布式缓存资源id。 **默认取值**：不涉及。 
        :type cache_ins_id: str
        """
        
        

        self._mnt_path = None
        self._cache_ins_id = None
        self.discriminator = None

        self.mnt_path = mnt_path
        self.cache_ins_id = cache_ins_id

    @property
    def mnt_path(self):
        r"""Gets the mnt_path of this CacheConfig.

        **参数解释**：挂载路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The mnt_path of this CacheConfig.
        :rtype: str
        """
        return self._mnt_path

    @mnt_path.setter
    def mnt_path(self, mnt_path):
        r"""Sets the mnt_path of this CacheConfig.

        **参数解释**：挂载路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param mnt_path: The mnt_path of this CacheConfig.
        :type mnt_path: str
        """
        self._mnt_path = mnt_path

    @property
    def cache_ins_id(self):
        r"""Gets the cache_ins_id of this CacheConfig.

        **参数解释**：分布式缓存id。 **约束限制**：不涉及。 **取值范围**：已创建的分布式缓存资源id。 **默认取值**：不涉及。 

        :return: The cache_ins_id of this CacheConfig.
        :rtype: str
        """
        return self._cache_ins_id

    @cache_ins_id.setter
    def cache_ins_id(self, cache_ins_id):
        r"""Sets the cache_ins_id of this CacheConfig.

        **参数解释**：分布式缓存id。 **约束限制**：不涉及。 **取值范围**：已创建的分布式缓存资源id。 **默认取值**：不涉及。 

        :param cache_ins_id: The cache_ins_id of this CacheConfig.
        :type cache_ins_id: str
        """
        self._cache_ins_id = cache_ins_id

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
        if not isinstance(other, CacheConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
