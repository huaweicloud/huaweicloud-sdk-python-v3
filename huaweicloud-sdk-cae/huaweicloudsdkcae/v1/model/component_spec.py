# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentSpec:

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
        'access_info': 'list[Access]',
        'image_url': 'str',
        'available_replica': 'int',
        'job_id': 'str',
        'build_id': 'str',
        'status': 'str',
        'build_log_id': 'str'
    }

    attribute_map = {
        'runtime': 'runtime',
        'env_id': 'env_id',
        'replica': 'replica',
        'source': 'source',
        'build': 'build',
        'resource_limit': 'resource_limit',
        'access_info': 'access_info',
        'image_url': 'image_url',
        'available_replica': 'available_replica',
        'job_id': 'job_id',
        'build_id': 'build_id',
        'status': 'status',
        'build_log_id': 'build_log_id'
    }

    def __init__(self, runtime=None, env_id=None, replica=None, source=None, build=None, resource_limit=None, access_info=None, image_url=None, available_replica=None, job_id=None, build_id=None, status=None, build_log_id=None):
        """ComponentSpec

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
        :param access_info: 访问方式列表。
        :type access_info: list[:class:`huaweicloudsdkcae.v1.Access`]
        :param image_url: 镜像地址。
        :type image_url: str
        :param available_replica: 可用实例个数。
        :type available_replica: int
        :param job_id: 任务ID。
        :type job_id: str
        :param build_id: 构建任务ID。
        :type build_id: str
        :param status: 组件状态。
        :type status: str
        :param build_log_id: 构建日志ID。
        :type build_log_id: str
        """
        
        

        self._runtime = None
        self._env_id = None
        self._replica = None
        self._source = None
        self._build = None
        self._resource_limit = None
        self._access_info = None
        self._image_url = None
        self._available_replica = None
        self._job_id = None
        self._build_id = None
        self._status = None
        self._build_log_id = None
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
        if access_info is not None:
            self.access_info = access_info
        if image_url is not None:
            self.image_url = image_url
        if available_replica is not None:
            self.available_replica = available_replica
        if job_id is not None:
            self.job_id = job_id
        if build_id is not None:
            self.build_id = build_id
        if status is not None:
            self.status = status
        if build_log_id is not None:
            self.build_log_id = build_log_id

    @property
    def runtime(self):
        """Gets the runtime of this ComponentSpec.

        语言/运行时。

        :return: The runtime of this ComponentSpec.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ComponentSpec.

        语言/运行时。

        :param runtime: The runtime of this ComponentSpec.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def env_id(self):
        """Gets the env_id of this ComponentSpec.

        环境ID。

        :return: The env_id of this ComponentSpec.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ComponentSpec.

        环境ID。

        :param env_id: The env_id of this ComponentSpec.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def replica(self):
        """Gets the replica of this ComponentSpec.

        实例个数。

        :return: The replica of this ComponentSpec.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this ComponentSpec.

        实例个数。

        :param replica: The replica of this ComponentSpec.
        :type replica: int
        """
        self._replica = replica

    @property
    def source(self):
        """Gets the source of this ComponentSpec.

        :return: The source of this ComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Source`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentSpec.

        :param source: The source of this ComponentSpec.
        :type source: :class:`huaweicloudsdkcae.v1.Source`
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this ComponentSpec.

        :return: The build of this ComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ComponentSpec.

        :param build: The build of this ComponentSpec.
        :type build: :class:`huaweicloudsdkcae.v1.Build`
        """
        self._build = build

    @property
    def resource_limit(self):
        """Gets the resource_limit of this ComponentSpec.

        :return: The resource_limit of this ComponentSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        """Sets the resource_limit of this ComponentSpec.

        :param resource_limit: The resource_limit of this ComponentSpec.
        :type resource_limit: :class:`huaweicloudsdkcae.v1.ResourceLimit`
        """
        self._resource_limit = resource_limit

    @property
    def access_info(self):
        """Gets the access_info of this ComponentSpec.

        访问方式列表。

        :return: The access_info of this ComponentSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.Access`]
        """
        return self._access_info

    @access_info.setter
    def access_info(self, access_info):
        """Sets the access_info of this ComponentSpec.

        访问方式列表。

        :param access_info: The access_info of this ComponentSpec.
        :type access_info: list[:class:`huaweicloudsdkcae.v1.Access`]
        """
        self._access_info = access_info

    @property
    def image_url(self):
        """Gets the image_url of this ComponentSpec.

        镜像地址。

        :return: The image_url of this ComponentSpec.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ComponentSpec.

        镜像地址。

        :param image_url: The image_url of this ComponentSpec.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def available_replica(self):
        """Gets the available_replica of this ComponentSpec.

        可用实例个数。

        :return: The available_replica of this ComponentSpec.
        :rtype: int
        """
        return self._available_replica

    @available_replica.setter
    def available_replica(self, available_replica):
        """Sets the available_replica of this ComponentSpec.

        可用实例个数。

        :param available_replica: The available_replica of this ComponentSpec.
        :type available_replica: int
        """
        self._available_replica = available_replica

    @property
    def job_id(self):
        """Gets the job_id of this ComponentSpec.

        任务ID。

        :return: The job_id of this ComponentSpec.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ComponentSpec.

        任务ID。

        :param job_id: The job_id of this ComponentSpec.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_id(self):
        """Gets the build_id of this ComponentSpec.

        构建任务ID。

        :return: The build_id of this ComponentSpec.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this ComponentSpec.

        构建任务ID。

        :param build_id: The build_id of this ComponentSpec.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def status(self):
        """Gets the status of this ComponentSpec.

        组件状态。

        :return: The status of this ComponentSpec.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentSpec.

        组件状态。

        :param status: The status of this ComponentSpec.
        :type status: str
        """
        self._status = status

    @property
    def build_log_id(self):
        """Gets the build_log_id of this ComponentSpec.

        构建日志ID。

        :return: The build_log_id of this ComponentSpec.
        :rtype: str
        """
        return self._build_log_id

    @build_log_id.setter
    def build_log_id(self, build_log_id):
        """Sets the build_log_id of this ComponentSpec.

        构建日志ID。

        :param build_log_id: The build_log_id of this ComponentSpec.
        :type build_log_id: str
        """
        self._build_log_id = build_log_id

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
        if not isinstance(other, ComponentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
