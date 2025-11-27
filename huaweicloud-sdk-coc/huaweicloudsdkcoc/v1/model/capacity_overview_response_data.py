# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityOverviewResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sum_size': 'str',
        'sum_cpu': 'str',
        'sum_mem': 'str',
        'provider': 'str',
        'type': 'str'
    }

    attribute_map = {
        'sum_size': 'sum_size',
        'sum_cpu': 'sum_cpu',
        'sum_mem': 'sum_mem',
        'provider': 'provider',
        'type': 'type'
    }

    def __init__(self, sum_size=None, sum_cpu=None, sum_mem=None, provider=None, type=None):
        r"""CapacityOverviewResponseData

        The model defined in huaweicloud sdk

        :param sum_size: **参数解释：** 硬盘大小总量。 **取值范围：** 云服务对应的总内存。
        :type sum_size: str
        :param sum_cpu: **参数解释：** CPU分配量总量。 **取值范围：** 不涉及。
        :type sum_cpu: str
        :param sum_mem: **参数解释：** 内存分配量总量。 **取值范围：** 不涉及。
        :type sum_mem: str
        :param provider: **参数解释：** 云服务类型。 **取值范围：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 云服务资源类型。。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。
        :type type: str
        """
        
        

        self._sum_size = None
        self._sum_cpu = None
        self._sum_mem = None
        self._provider = None
        self._type = None
        self.discriminator = None

        if sum_size is not None:
            self.sum_size = sum_size
        if sum_cpu is not None:
            self.sum_cpu = sum_cpu
        if sum_mem is not None:
            self.sum_mem = sum_mem
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type

    @property
    def sum_size(self):
        r"""Gets the sum_size of this CapacityOverviewResponseData.

        **参数解释：** 硬盘大小总量。 **取值范围：** 云服务对应的总内存。

        :return: The sum_size of this CapacityOverviewResponseData.
        :rtype: str
        """
        return self._sum_size

    @sum_size.setter
    def sum_size(self, sum_size):
        r"""Sets the sum_size of this CapacityOverviewResponseData.

        **参数解释：** 硬盘大小总量。 **取值范围：** 云服务对应的总内存。

        :param sum_size: The sum_size of this CapacityOverviewResponseData.
        :type sum_size: str
        """
        self._sum_size = sum_size

    @property
    def sum_cpu(self):
        r"""Gets the sum_cpu of this CapacityOverviewResponseData.

        **参数解释：** CPU分配量总量。 **取值范围：** 不涉及。

        :return: The sum_cpu of this CapacityOverviewResponseData.
        :rtype: str
        """
        return self._sum_cpu

    @sum_cpu.setter
    def sum_cpu(self, sum_cpu):
        r"""Sets the sum_cpu of this CapacityOverviewResponseData.

        **参数解释：** CPU分配量总量。 **取值范围：** 不涉及。

        :param sum_cpu: The sum_cpu of this CapacityOverviewResponseData.
        :type sum_cpu: str
        """
        self._sum_cpu = sum_cpu

    @property
    def sum_mem(self):
        r"""Gets the sum_mem of this CapacityOverviewResponseData.

        **参数解释：** 内存分配量总量。 **取值范围：** 不涉及。

        :return: The sum_mem of this CapacityOverviewResponseData.
        :rtype: str
        """
        return self._sum_mem

    @sum_mem.setter
    def sum_mem(self, sum_mem):
        r"""Sets the sum_mem of this CapacityOverviewResponseData.

        **参数解释：** 内存分配量总量。 **取值范围：** 不涉及。

        :param sum_mem: The sum_mem of this CapacityOverviewResponseData.
        :type sum_mem: str
        """
        self._sum_mem = sum_mem

    @property
    def provider(self):
        r"""Gets the provider of this CapacityOverviewResponseData.

        **参数解释：** 云服务类型。 **取值范围：** 不涉及。

        :return: The provider of this CapacityOverviewResponseData.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CapacityOverviewResponseData.

        **参数解释：** 云服务类型。 **取值范围：** 不涉及。

        :param provider: The provider of this CapacityOverviewResponseData.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this CapacityOverviewResponseData.

        **参数解释：** 云服务资源类型。。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :return: The type of this CapacityOverviewResponseData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CapacityOverviewResponseData.

        **参数解释：** 云服务资源类型。。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。

        :param type: The type of this CapacityOverviewResponseData.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CapacityOverviewResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
