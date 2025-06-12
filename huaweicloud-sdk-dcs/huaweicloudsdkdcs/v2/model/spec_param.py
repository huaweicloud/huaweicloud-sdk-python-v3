# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sharding_count': 'int',
        'replica_count': 'int',
        'cache_mode': 'str'
    }

    attribute_map = {
        'sharding_count': 'sharding_count',
        'replica_count': 'replica_count',
        'cache_mode': 'cache_mode'
    }

    def __init__(self, sharding_count=None, replica_count=None, cache_mode=None):
        r"""SpecParam

        The model defined in huaweicloud sdk

        :param sharding_count: **参数解释**： 实例分片数。 **约束限制**： 不涉及。 **取值范围**： 1-128。 **默认取值**： 不涉及。 
        :type sharding_count: int
        :param replica_count: 副本数 **参数解释**： 实例副本数。 **约束限制**： 不涉及。 **取值范围**： 1-10。 **默认取值**： 不涉及。
        :type replica_count: int
        :param cache_mode: 副本数 **参数解释**： 实例类型。 **约束限制**： 不涉及。 **取值范围**： 1.ha：主备类型 2.single：单机类型 3.ha_rw_split：读写分离类型 4.proxy：proxy集群类型 5.cluster：cluster集群类型 **默认取值**： 不涉及。
        :type cache_mode: str
        """
        
        

        self._sharding_count = None
        self._replica_count = None
        self._cache_mode = None
        self.discriminator = None

        if sharding_count is not None:
            self.sharding_count = sharding_count
        if replica_count is not None:
            self.replica_count = replica_count
        if cache_mode is not None:
            self.cache_mode = cache_mode

    @property
    def sharding_count(self):
        r"""Gets the sharding_count of this SpecParam.

        **参数解释**： 实例分片数。 **约束限制**： 不涉及。 **取值范围**： 1-128。 **默认取值**： 不涉及。 

        :return: The sharding_count of this SpecParam.
        :rtype: int
        """
        return self._sharding_count

    @sharding_count.setter
    def sharding_count(self, sharding_count):
        r"""Sets the sharding_count of this SpecParam.

        **参数解释**： 实例分片数。 **约束限制**： 不涉及。 **取值范围**： 1-128。 **默认取值**： 不涉及。 

        :param sharding_count: The sharding_count of this SpecParam.
        :type sharding_count: int
        """
        self._sharding_count = sharding_count

    @property
    def replica_count(self):
        r"""Gets the replica_count of this SpecParam.

        副本数 **参数解释**： 实例副本数。 **约束限制**： 不涉及。 **取值范围**： 1-10。 **默认取值**： 不涉及。

        :return: The replica_count of this SpecParam.
        :rtype: int
        """
        return self._replica_count

    @replica_count.setter
    def replica_count(self, replica_count):
        r"""Sets the replica_count of this SpecParam.

        副本数 **参数解释**： 实例副本数。 **约束限制**： 不涉及。 **取值范围**： 1-10。 **默认取值**： 不涉及。

        :param replica_count: The replica_count of this SpecParam.
        :type replica_count: int
        """
        self._replica_count = replica_count

    @property
    def cache_mode(self):
        r"""Gets the cache_mode of this SpecParam.

        副本数 **参数解释**： 实例类型。 **约束限制**： 不涉及。 **取值范围**： 1.ha：主备类型 2.single：单机类型 3.ha_rw_split：读写分离类型 4.proxy：proxy集群类型 5.cluster：cluster集群类型 **默认取值**： 不涉及。

        :return: The cache_mode of this SpecParam.
        :rtype: str
        """
        return self._cache_mode

    @cache_mode.setter
    def cache_mode(self, cache_mode):
        r"""Sets the cache_mode of this SpecParam.

        副本数 **参数解释**： 实例类型。 **约束限制**： 不涉及。 **取值范围**： 1.ha：主备类型 2.single：单机类型 3.ha_rw_split：读写分离类型 4.proxy：proxy集群类型 5.cluster：cluster集群类型 **默认取值**： 不涉及。

        :param cache_mode: The cache_mode of this SpecParam.
        :type cache_mode: str
        """
        self._cache_mode = cache_mode

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
        if not isinstance(other, SpecParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
