# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedHostType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_type': 'str',
        'vcpus': 'int',
        'cores': 'int',
        'sockets': 'int',
        'memory': 'int',
        'supported_flavors': 'list[str]',
        'category': 'str',
        'availability_zone_offerings': 'list[DedicatedHostTypeOffering]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'host_type': 'host_type',
        'vcpus': 'vcpus',
        'cores': 'cores',
        'sockets': 'sockets',
        'memory': 'memory',
        'supported_flavors': 'supported_flavors',
        'category': 'category',
        'availability_zone_offerings': 'availability_zone_offerings',
        'page_info': 'page_info'
    }

    def __init__(self, host_type=None, vcpus=None, cores=None, sockets=None, memory=None, supported_flavors=None, category=None, availability_zone_offerings=None, page_info=None):
        r"""DedicatedHostType

        The model defined in huaweicloud sdk

        :param host_type: 专属主机类型。
        :type host_type: str
        :param vcpus: 专属主机类型的vCPU数量。
        :type vcpus: int
        :param cores: 专属主机类型的核心数量。
        :type cores: int
        :param sockets: 专属主机类型的物理套接字数量。
        :type sockets: int
        :param memory: 专属主机类型的内存大小。
        :type memory: int
        :param supported_flavors: 专属主机规格列表。
        :type supported_flavors: list[str]
        :param category: 专属主机类型的类别。
        :type category: str
        :param availability_zone_offerings: 
        :type availability_zone_offerings: list[:class:`huaweicloudsdkdeh.v1.DedicatedHostTypeOffering`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdeh.v1.PageInfo`
        """
        
        

        self._host_type = None
        self._vcpus = None
        self._cores = None
        self._sockets = None
        self._memory = None
        self._supported_flavors = None
        self._category = None
        self._availability_zone_offerings = None
        self._page_info = None
        self.discriminator = None

        self.host_type = host_type
        self.vcpus = vcpus
        self.cores = cores
        self.sockets = sockets
        self.memory = memory
        self.supported_flavors = supported_flavors
        self.category = category
        if availability_zone_offerings is not None:
            self.availability_zone_offerings = availability_zone_offerings
        self.page_info = page_info

    @property
    def host_type(self):
        r"""Gets the host_type of this DedicatedHostType.

        专属主机类型。

        :return: The host_type of this DedicatedHostType.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this DedicatedHostType.

        专属主机类型。

        :param host_type: The host_type of this DedicatedHostType.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def vcpus(self):
        r"""Gets the vcpus of this DedicatedHostType.

        专属主机类型的vCPU数量。

        :return: The vcpus of this DedicatedHostType.
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this DedicatedHostType.

        专属主机类型的vCPU数量。

        :param vcpus: The vcpus of this DedicatedHostType.
        :type vcpus: int
        """
        self._vcpus = vcpus

    @property
    def cores(self):
        r"""Gets the cores of this DedicatedHostType.

        专属主机类型的核心数量。

        :return: The cores of this DedicatedHostType.
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        r"""Sets the cores of this DedicatedHostType.

        专属主机类型的核心数量。

        :param cores: The cores of this DedicatedHostType.
        :type cores: int
        """
        self._cores = cores

    @property
    def sockets(self):
        r"""Gets the sockets of this DedicatedHostType.

        专属主机类型的物理套接字数量。

        :return: The sockets of this DedicatedHostType.
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        r"""Sets the sockets of this DedicatedHostType.

        专属主机类型的物理套接字数量。

        :param sockets: The sockets of this DedicatedHostType.
        :type sockets: int
        """
        self._sockets = sockets

    @property
    def memory(self):
        r"""Gets the memory of this DedicatedHostType.

        专属主机类型的内存大小。

        :return: The memory of this DedicatedHostType.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this DedicatedHostType.

        专属主机类型的内存大小。

        :param memory: The memory of this DedicatedHostType.
        :type memory: int
        """
        self._memory = memory

    @property
    def supported_flavors(self):
        r"""Gets the supported_flavors of this DedicatedHostType.

        专属主机规格列表。

        :return: The supported_flavors of this DedicatedHostType.
        :rtype: list[str]
        """
        return self._supported_flavors

    @supported_flavors.setter
    def supported_flavors(self, supported_flavors):
        r"""Sets the supported_flavors of this DedicatedHostType.

        专属主机规格列表。

        :param supported_flavors: The supported_flavors of this DedicatedHostType.
        :type supported_flavors: list[str]
        """
        self._supported_flavors = supported_flavors

    @property
    def category(self):
        r"""Gets the category of this DedicatedHostType.

        专属主机类型的类别。

        :return: The category of this DedicatedHostType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this DedicatedHostType.

        专属主机类型的类别。

        :param category: The category of this DedicatedHostType.
        :type category: str
        """
        self._category = category

    @property
    def availability_zone_offerings(self):
        r"""Gets the availability_zone_offerings of this DedicatedHostType.

        :return: The availability_zone_offerings of this DedicatedHostType.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.DedicatedHostTypeOffering`]
        """
        return self._availability_zone_offerings

    @availability_zone_offerings.setter
    def availability_zone_offerings(self, availability_zone_offerings):
        r"""Sets the availability_zone_offerings of this DedicatedHostType.

        :param availability_zone_offerings: The availability_zone_offerings of this DedicatedHostType.
        :type availability_zone_offerings: list[:class:`huaweicloudsdkdeh.v1.DedicatedHostTypeOffering`]
        """
        self._availability_zone_offerings = availability_zone_offerings

    @property
    def page_info(self):
        r"""Gets the page_info of this DedicatedHostType.

        :return: The page_info of this DedicatedHostType.
        :rtype: :class:`huaweicloudsdkdeh.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this DedicatedHostType.

        :param page_info: The page_info of this DedicatedHostType.
        :type page_info: :class:`huaweicloudsdkdeh.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, DedicatedHostType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
