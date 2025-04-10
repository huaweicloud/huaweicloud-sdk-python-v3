# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env': 'list[ConfigurationEnvParam]',
        'storage': 'list[ComponentStorage]',
        'strategy': 'ConfigurationStrategy',
        'lifecycle': 'ConfigurationLifecycle',
        'scheduler': 'ConfigurationScheduler',
        'probes': 'ConfigurationProbes',
        'container_spec': 'ConfigurationContainerSpec'
    }

    attribute_map = {
        'env': 'env',
        'storage': 'storage',
        'strategy': 'strategy',
        'lifecycle': 'lifecycle',
        'scheduler': 'scheduler',
        'probes': 'probes',
        'container_spec': 'container_spec'
    }

    def __init__(self, env=None, storage=None, strategy=None, lifecycle=None, scheduler=None, probes=None, container_spec=None):
        r"""InstanceConfiguration

        The model defined in huaweicloud sdk

        :param env: 应用环境变量。
        :type env: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        :param storage: 
        :type storage: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkservicestage.v2.ConfigurationStrategy`
        :param lifecycle: 
        :type lifecycle: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        :param scheduler: 
        :type scheduler: :class:`huaweicloudsdkservicestage.v2.ConfigurationScheduler`
        :param probes: 
        :type probes: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        :param container_spec: 
        :type container_spec: :class:`huaweicloudsdkservicestage.v2.ConfigurationContainerSpec`
        """
        
        

        self._env = None
        self._storage = None
        self._strategy = None
        self._lifecycle = None
        self._scheduler = None
        self._probes = None
        self._container_spec = None
        self.discriminator = None

        if env is not None:
            self.env = env
        if storage is not None:
            self.storage = storage
        if strategy is not None:
            self.strategy = strategy
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if scheduler is not None:
            self.scheduler = scheduler
        if probes is not None:
            self.probes = probes
        if container_spec is not None:
            self.container_spec = container_spec

    @property
    def env(self):
        r"""Gets the env of this InstanceConfiguration.

        应用环境变量。

        :return: The env of this InstanceConfiguration.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        """
        return self._env

    @env.setter
    def env(self, env):
        r"""Sets the env of this InstanceConfiguration.

        应用环境变量。

        :param env: The env of this InstanceConfiguration.
        :type env: list[:class:`huaweicloudsdkservicestage.v2.ConfigurationEnvParam`]
        """
        self._env = env

    @property
    def storage(self):
        r"""Gets the storage of this InstanceConfiguration.

        :return: The storage of this InstanceConfiguration.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this InstanceConfiguration.

        :param storage: The storage of this InstanceConfiguration.
        :type storage: list[:class:`huaweicloudsdkservicestage.v2.ComponentStorage`]
        """
        self._storage = storage

    @property
    def strategy(self):
        r"""Gets the strategy of this InstanceConfiguration.

        :return: The strategy of this InstanceConfiguration.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationStrategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this InstanceConfiguration.

        :param strategy: The strategy of this InstanceConfiguration.
        :type strategy: :class:`huaweicloudsdkservicestage.v2.ConfigurationStrategy`
        """
        self._strategy = strategy

    @property
    def lifecycle(self):
        r"""Gets the lifecycle of this InstanceConfiguration.

        :return: The lifecycle of this InstanceConfiguration.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        r"""Sets the lifecycle of this InstanceConfiguration.

        :param lifecycle: The lifecycle of this InstanceConfiguration.
        :type lifecycle: :class:`huaweicloudsdkservicestage.v2.ConfigurationLifecycle`
        """
        self._lifecycle = lifecycle

    @property
    def scheduler(self):
        r"""Gets the scheduler of this InstanceConfiguration.

        :return: The scheduler of this InstanceConfiguration.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationScheduler`
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        r"""Sets the scheduler of this InstanceConfiguration.

        :param scheduler: The scheduler of this InstanceConfiguration.
        :type scheduler: :class:`huaweicloudsdkservicestage.v2.ConfigurationScheduler`
        """
        self._scheduler = scheduler

    @property
    def probes(self):
        r"""Gets the probes of this InstanceConfiguration.

        :return: The probes of this InstanceConfiguration.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        r"""Sets the probes of this InstanceConfiguration.

        :param probes: The probes of this InstanceConfiguration.
        :type probes: :class:`huaweicloudsdkservicestage.v2.ConfigurationProbes`
        """
        self._probes = probes

    @property
    def container_spec(self):
        r"""Gets the container_spec of this InstanceConfiguration.

        :return: The container_spec of this InstanceConfiguration.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ConfigurationContainerSpec`
        """
        return self._container_spec

    @container_spec.setter
    def container_spec(self, container_spec):
        r"""Sets the container_spec of this InstanceConfiguration.

        :param container_spec: The container_spec of this InstanceConfiguration.
        :type container_spec: :class:`huaweicloudsdkservicestage.v2.ConfigurationContainerSpec`
        """
        self._container_spec = container_spec

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
        if not isinstance(other, InstanceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
