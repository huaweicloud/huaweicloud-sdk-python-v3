# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'FlavorId',
        'storage_size': 'str',
        'num_cpu': 'str',
        'num_cpu_init': 'str',
        'memory_size': 'str',
        'memory_size_init': 'str',
        'label': 'str',
        'custom': 'bool'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'storage_size': 'storage_size',
        'num_cpu': 'num_cpu',
        'num_cpu_init': 'num_cpu_init',
        'memory_size': 'memory_size',
        'memory_size_init': 'memory_size_init',
        'label': 'label',
        'custom': 'custom'
    }

    def __init__(self, flavor_id=None, storage_size=None, num_cpu=None, num_cpu_init=None, memory_size=None, memory_size_init=None, label=None, custom=None):
        r"""FlavorView

        The model defined in huaweicloud sdk

        :param flavor_id: 
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        :param storage_size: 存储大小。
        :type storage_size: str
        :param num_cpu: CPU限制。
        :type num_cpu: str
        :param num_cpu_init: CPU初始。
        :type num_cpu_init: str
        :param memory_size: 内存限制。
        :type memory_size: str
        :param memory_size_init: 内存初始。
        :type memory_size_init: str
        :param label: 展示标签。
        :type label: str
        :param custom: 是否是自定义资源规格。
        :type custom: bool
        """
        
        

        self._flavor_id = None
        self._storage_size = None
        self._num_cpu = None
        self._num_cpu_init = None
        self._memory_size = None
        self._memory_size_init = None
        self._label = None
        self._custom = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if storage_size is not None:
            self.storage_size = storage_size
        if num_cpu is not None:
            self.num_cpu = num_cpu
        if num_cpu_init is not None:
            self.num_cpu_init = num_cpu_init
        if memory_size is not None:
            self.memory_size = memory_size
        if memory_size_init is not None:
            self.memory_size_init = memory_size_init
        if label is not None:
            self.label = label
        if custom is not None:
            self.custom = custom

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this FlavorView.

        :return: The flavor_id of this FlavorView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this FlavorView.

        :param flavor_id: The flavor_id of this FlavorView.
        :type flavor_id: :class:`huaweicloudsdkservicestage.v2.FlavorId`
        """
        self._flavor_id = flavor_id

    @property
    def storage_size(self):
        r"""Gets the storage_size of this FlavorView.

        存储大小。

        :return: The storage_size of this FlavorView.
        :rtype: str
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        r"""Sets the storage_size of this FlavorView.

        存储大小。

        :param storage_size: The storage_size of this FlavorView.
        :type storage_size: str
        """
        self._storage_size = storage_size

    @property
    def num_cpu(self):
        r"""Gets the num_cpu of this FlavorView.

        CPU限制。

        :return: The num_cpu of this FlavorView.
        :rtype: str
        """
        return self._num_cpu

    @num_cpu.setter
    def num_cpu(self, num_cpu):
        r"""Sets the num_cpu of this FlavorView.

        CPU限制。

        :param num_cpu: The num_cpu of this FlavorView.
        :type num_cpu: str
        """
        self._num_cpu = num_cpu

    @property
    def num_cpu_init(self):
        r"""Gets the num_cpu_init of this FlavorView.

        CPU初始。

        :return: The num_cpu_init of this FlavorView.
        :rtype: str
        """
        return self._num_cpu_init

    @num_cpu_init.setter
    def num_cpu_init(self, num_cpu_init):
        r"""Sets the num_cpu_init of this FlavorView.

        CPU初始。

        :param num_cpu_init: The num_cpu_init of this FlavorView.
        :type num_cpu_init: str
        """
        self._num_cpu_init = num_cpu_init

    @property
    def memory_size(self):
        r"""Gets the memory_size of this FlavorView.

        内存限制。

        :return: The memory_size of this FlavorView.
        :rtype: str
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        r"""Sets the memory_size of this FlavorView.

        内存限制。

        :param memory_size: The memory_size of this FlavorView.
        :type memory_size: str
        """
        self._memory_size = memory_size

    @property
    def memory_size_init(self):
        r"""Gets the memory_size_init of this FlavorView.

        内存初始。

        :return: The memory_size_init of this FlavorView.
        :rtype: str
        """
        return self._memory_size_init

    @memory_size_init.setter
    def memory_size_init(self, memory_size_init):
        r"""Sets the memory_size_init of this FlavorView.

        内存初始。

        :param memory_size_init: The memory_size_init of this FlavorView.
        :type memory_size_init: str
        """
        self._memory_size_init = memory_size_init

    @property
    def label(self):
        r"""Gets the label of this FlavorView.

        展示标签。

        :return: The label of this FlavorView.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this FlavorView.

        展示标签。

        :param label: The label of this FlavorView.
        :type label: str
        """
        self._label = label

    @property
    def custom(self):
        r"""Gets the custom of this FlavorView.

        是否是自定义资源规格。

        :return: The custom of this FlavorView.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        r"""Sets the custom of this FlavorView.

        是否是自定义资源规格。

        :param custom: The custom of this FlavorView.
        :type custom: bool
        """
        self._custom = custom

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
        if not isinstance(other, FlavorView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
