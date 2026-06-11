# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceFlavorOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'str',
        'storage': 'str',
        'size': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'num': 'num',
        'storage': 'storage',
        'size': 'size',
        'spec_code': 'spec_code'
    }

    def __init__(self, num=None, storage=None, size=None, spec_code=None):
        r"""CreateInstanceFlavorOption

        The model defined in huaweicloud sdk

        :param num: **参数解释：** 节点数量。 **约束限制：** 不涉及。 **取值范围：** - GeminiDB Cassandra实例的节点数量可取3~60。 - GeminiDB Mongo 4.0版本副本集实例的节点数量为3。 - GeminiDB Influx集群实例的节点数量可取3~16。 - GeminiDB Influx单节点实例的节点数量可取1。 - GeminiDB Redis实例的节点数量可取3~12。 **默认取值：** 不涉及。
        :type num: str
        :param storage: **参数解释：** 磁盘类型。 **约束限制：** 不涉及。 **取值范围：** 取值为“ULTRAHIGH”，表示SSD盘。 **默认取值：** 不涉及。
        :type storage: str
        :param size: **参数解释：** 磁盘大小。必须为整数，单位为GB。 **约束限制：** GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx的最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关。GeminiDB Redis的最大和最小磁盘容量与节点数和实例的性能规格有关。 **取值范围：** - GeminiDB Cassandra请参见数据库实例规格。 - GeminiDB Mongo请参见数据库实例规格。 - GeminiDB Influx请参见数据库实例规格。 - GeminiDB Redis请参见数据库实例规格。 **默认取值：** 不涉及。
        :type size: str
        :param spec_code: -| **参数解释：** 资源规格编码。 **约束限制：** 不涉及。 **取值范围：** 获取方法请参见查询数据库规格 - QueryingInstanceSpecifications中响应参数“spec_code”的值。 **默认取值：** 不涉及。
        :type spec_code: str
        """
        
        

        self._num = None
        self._storage = None
        self._size = None
        self._spec_code = None
        self.discriminator = None

        self.num = num
        self.storage = storage
        self.size = size
        self.spec_code = spec_code

    @property
    def num(self):
        r"""Gets the num of this CreateInstanceFlavorOption.

        **参数解释：** 节点数量。 **约束限制：** 不涉及。 **取值范围：** - GeminiDB Cassandra实例的节点数量可取3~60。 - GeminiDB Mongo 4.0版本副本集实例的节点数量为3。 - GeminiDB Influx集群实例的节点数量可取3~16。 - GeminiDB Influx单节点实例的节点数量可取1。 - GeminiDB Redis实例的节点数量可取3~12。 **默认取值：** 不涉及。

        :return: The num of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this CreateInstanceFlavorOption.

        **参数解释：** 节点数量。 **约束限制：** 不涉及。 **取值范围：** - GeminiDB Cassandra实例的节点数量可取3~60。 - GeminiDB Mongo 4.0版本副本集实例的节点数量为3。 - GeminiDB Influx集群实例的节点数量可取3~16。 - GeminiDB Influx单节点实例的节点数量可取1。 - GeminiDB Redis实例的节点数量可取3~12。 **默认取值：** 不涉及。

        :param num: The num of this CreateInstanceFlavorOption.
        :type num: str
        """
        self._num = num

    @property
    def storage(self):
        r"""Gets the storage of this CreateInstanceFlavorOption.

        **参数解释：** 磁盘类型。 **约束限制：** 不涉及。 **取值范围：** 取值为“ULTRAHIGH”，表示SSD盘。 **默认取值：** 不涉及。

        :return: The storage of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this CreateInstanceFlavorOption.

        **参数解释：** 磁盘类型。 **约束限制：** 不涉及。 **取值范围：** 取值为“ULTRAHIGH”，表示SSD盘。 **默认取值：** 不涉及。

        :param storage: The storage of this CreateInstanceFlavorOption.
        :type storage: str
        """
        self._storage = storage

    @property
    def size(self):
        r"""Gets the size of this CreateInstanceFlavorOption.

        **参数解释：** 磁盘大小。必须为整数，单位为GB。 **约束限制：** GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx的最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关。GeminiDB Redis的最大和最小磁盘容量与节点数和实例的性能规格有关。 **取值范围：** - GeminiDB Cassandra请参见数据库实例规格。 - GeminiDB Mongo请参见数据库实例规格。 - GeminiDB Influx请参见数据库实例规格。 - GeminiDB Redis请参见数据库实例规格。 **默认取值：** 不涉及。

        :return: The size of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateInstanceFlavorOption.

        **参数解释：** 磁盘大小。必须为整数，单位为GB。 **约束限制：** GeminiDB Cassandra，GeminiDB Mongo，GeminiDB Influx的最小磁盘容量100GB，最大磁盘容量与实例的性能规格有关。GeminiDB Redis的最大和最小磁盘容量与节点数和实例的性能规格有关。 **取值范围：** - GeminiDB Cassandra请参见数据库实例规格。 - GeminiDB Mongo请参见数据库实例规格。 - GeminiDB Influx请参见数据库实例规格。 - GeminiDB Redis请参见数据库实例规格。 **默认取值：** 不涉及。

        :param size: The size of this CreateInstanceFlavorOption.
        :type size: str
        """
        self._size = size

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateInstanceFlavorOption.

        -| **参数解释：** 资源规格编码。 **约束限制：** 不涉及。 **取值范围：** 获取方法请参见查询数据库规格 - QueryingInstanceSpecifications中响应参数“spec_code”的值。 **默认取值：** 不涉及。

        :return: The spec_code of this CreateInstanceFlavorOption.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateInstanceFlavorOption.

        -| **参数解释：** 资源规格编码。 **约束限制：** 不涉及。 **取值范围：** 获取方法请参见查询数据库规格 - QueryingInstanceSpecifications中响应参数“spec_code”的值。 **默认取值：** 不涉及。

        :param spec_code: The spec_code of this CreateInstanceFlavorOption.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, CreateInstanceFlavorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
