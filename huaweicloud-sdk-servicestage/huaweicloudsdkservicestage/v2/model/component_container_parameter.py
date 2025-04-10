# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentContainerParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'ComponentContainerSize',
        'env': 'list[ConfigurationEnvParam]',
        'storage': 'list[ComponentStorage]',
        'lifecycle': 'ConfigurationLifecycle',
        'probes': 'ConfigurationProbes'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'env': 'env',
        'storage': 'storage',
        'lifecycle': 'lifecycle',
        'probes': 'probes'
    }

    def __init__(self, name=None, size=None, env=None, storage=None, lifecycle=None, probes=None):
        r"""ComponentContainerParameter

        The model defined in huaweicloud sdk

        :param name: 容器名称
        :type name: str
        :param size: 
        :type size: :class:`huaweicloudsdkservicestage.v2.ComponentContainerSize`
        :param env: 应用环境变量。
        :type env: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        :param storage: 
        :type storage: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        :param lifecycle: 
        :type lifecycle: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        :param probes: 
        :type probes: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        """
        
        

        self._name = None
        self._size = None
        self._env = None
        self._storage = None
        self._lifecycle = None
        self._probes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if env is not None:
            self.env = env
        if storage is not None:
            self.storage = storage
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if probes is not None:
            self.probes = probes

    @property
    def name(self):
        r"""Gets the name of this ComponentContainerParameter.

        容器名称

        :return: The name of this ComponentContainerParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentContainerParameter.

        容器名称

        :param name: The name of this ComponentContainerParameter.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this ComponentContainerParameter.

        :return: The size of this ComponentContainerParameter.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentContainerSize`
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ComponentContainerParameter.

        :param size: The size of this ComponentContainerParameter.
        :type size: :class:`huaweicloudsdkservicestage.v2.ComponentContainerSize`
        """
        self._size = size

    @property
    def env(self):
        r"""Gets the env of this ComponentContainerParameter.

        应用环境变量。

        :return: The env of this ComponentContainerParameter.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        """
        return self._env

    @env.setter
    def env(self, env):
        r"""Sets the env of this ComponentContainerParameter.

        应用环境变量。

        :param env: The env of this ComponentContainerParameter.
        :type env: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        """
        self._env = env

    @property
    def storage(self):
        r"""Gets the storage of this ComponentContainerParameter.

        :return: The storage of this ComponentContainerParameter.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this ComponentContainerParameter.

        :param storage: The storage of this ComponentContainerParameter.
        :type storage: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        """
        self._storage = storage

    @property
    def lifecycle(self):
        r"""Gets the lifecycle of this ComponentContainerParameter.

        :return: The lifecycle of this ComponentContainerParameter.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        r"""Sets the lifecycle of this ComponentContainerParameter.

        :param lifecycle: The lifecycle of this ComponentContainerParameter.
        :type lifecycle: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        """
        self._lifecycle = lifecycle

    @property
    def probes(self):
        r"""Gets the probes of this ComponentContainerParameter.

        :return: The probes of this ComponentContainerParameter.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        r"""Sets the probes of this ComponentContainerParameter.

        :param probes: The probes of this ComponentContainerParameter.
        :type probes: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        """
        self._probes = probes

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
        if not isinstance(other, ComponentContainerParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
