# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime': 'str',
        'env_id': 'str',
        'replica': 'int',
        'source': 'Source',
        'build': 'Build',
        'resource_limit': 'ResourceLimit',
        'available_replica': 'int',
        'status': 'str'
    }

    attribute_map = {
        'runtime': 'runtime',
        'env_id': 'env_id',
        'replica': 'replica',
        'source': 'source',
        'build': 'build',
        'resource_limit': 'resource_limit',
        'available_replica': 'available_replica',
        'status': 'status'
    }

    def __init__(self, runtime=None, env_id=None, replica=None, source=None, build=None, resource_limit=None, available_replica=None, status=None):
        """CreateComponentSpec

        The model defined in huaweicloud sdk

        :param runtime: 语言/运行时。
        :type runtime: str
        :param env_id: 环境ID。
        :type env_id: str
        :param replica: 实例个数。
        :type replica: int
        :param source: 
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        :param build: 
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        :param resource_limit: 
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        :param available_replica: 可用实例个数。
        :type available_replica: int
        :param status: 组件状态。
        :type status: str
        """
        
        

        self._runtime = None
        self._env_id = None
        self._replica = None
        self._source = None
        self._build = None
        self._resource_limit = None
        self._available_replica = None
        self._status = None
        self.discriminator = None

        if runtime is not None:
            self.runtime = runtime
        if env_id is not None:
            self.env_id = env_id
        if replica is not None:
            self.replica = replica
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        if resource_limit is not None:
            self.resource_limit = resource_limit
        if available_replica is not None:
            self.available_replica = available_replica
        if status is not None:
            self.status = status

    @property
    def runtime(self):
        """Gets the runtime of this CreateComponentSpec.

        语言/运行时。

        :return: The runtime of this CreateComponentSpec.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this CreateComponentSpec.

        语言/运行时。

        :param runtime: The runtime of this CreateComponentSpec.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def env_id(self):
        """Gets the env_id of this CreateComponentSpec.

        环境ID。

        :return: The env_id of this CreateComponentSpec.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this CreateComponentSpec.

        环境ID。

        :param env_id: The env_id of this CreateComponentSpec.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def replica(self):
        """Gets the replica of this CreateComponentSpec.

        实例个数。

        :return: The replica of this CreateComponentSpec.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this CreateComponentSpec.

        实例个数。

        :param replica: The replica of this CreateComponentSpec.
        :type replica: int
        """
        self._replica = replica

    @property
    def source(self):
        """Gets the source of this CreateComponentSpec.

        :return: The source of this CreateComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Source`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateComponentSpec.

        :param source: The source of this CreateComponentSpec.
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this CreateComponentSpec.

        :return: The build of this CreateComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this CreateComponentSpec.

        :param build: The build of this CreateComponentSpec.
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        """
        self._build = build

    @property
    def resource_limit(self):
        """Gets the resource_limit of this CreateComponentSpec.

        :return: The resource_limit of this CreateComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        """Sets the resource_limit of this CreateComponentSpec.

        :param resource_limit: The resource_limit of this CreateComponentSpec.
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        self._resource_limit = resource_limit

    @property
    def available_replica(self):
        """Gets the available_replica of this CreateComponentSpec.

        可用实例个数。

        :return: The available_replica of this CreateComponentSpec.
        :rtype: int
        """
        return self._available_replica

    @available_replica.setter
    def available_replica(self, available_replica):
        """Sets the available_replica of this CreateComponentSpec.

        可用实例个数。

        :param available_replica: The available_replica of this CreateComponentSpec.
        :type available_replica: int
        """
        self._available_replica = available_replica

    @property
    def status(self):
        """Gets the status of this CreateComponentSpec.

        组件状态。

        :return: The status of this CreateComponentSpec.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateComponentSpec.

        组件状态。

        :param status: The status of this CreateComponentSpec.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CreateComponentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
