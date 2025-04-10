# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentSnapshotContext:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'available_replica': 'int',
        'build': 'str',
        'build_id': 'str',
        'build_log_id': 'str',
        'env_id': 'str',
        'id': 'str',
        'image_url': 'str',
        'job_id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'name': 'str',
        'operation': 'str',
        'operation_status': 'str',
        'replica': 'int',
        'resource_limit': 'str',
        'runtime': 'str',
        'source': 'str',
        'status': 'str',
        'version': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'available_replica': 'available_replica',
        'build': 'build',
        'build_id': 'build_id',
        'build_log_id': 'build_log_id',
        'env_id': 'env_id',
        'id': 'id',
        'image_url': 'image_url',
        'job_id': 'job_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'name': 'name',
        'operation': 'operation',
        'operation_status': 'operation_status',
        'replica': 'replica',
        'resource_limit': 'resource_limit',
        'runtime': 'runtime',
        'source': 'source',
        'status': 'status',
        'version': 'version',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, app_id=None, available_replica=None, build=None, build_id=None, build_log_id=None, env_id=None, id=None, image_url=None, job_id=None, log_group_id=None, log_stream_id=None, name=None, operation=None, operation_status=None, replica=None, resource_limit=None, runtime=None, source=None, status=None, version=None, created_at=None, updated_at=None):
        r"""ComponentSnapshotContext

        The model defined in huaweicloud sdk

        :param app_id: 应用ID。
        :type app_id: str
        :param available_replica: 可用实例个数。
        :type available_replica: int
        :param build: 组件构建信息。
        :type build: str
        :param build_id: 构建任务ID。
        :type build_id: str
        :param build_log_id: 构建日志ID。
        :type build_log_id: str
        :param env_id: 环境ID。
        :type env_id: str
        :param id: 组件ID。
        :type id: str
        :param image_url: 镜像地址。
        :type image_url: str
        :param job_id: 任务ID。
        :type job_id: str
        :param log_group_id: LTS日志组的ID。
        :type log_group_id: str
        :param log_stream_id: LTS日志流的ID
        :type log_stream_id: str
        :param name: 组件名称。
        :type name: str
        :param operation: 组件操作。
        :type operation: str
        :param operation_status: 组件操作状态。
        :type operation_status: str
        :param replica: 实例个数。
        :type replica: int
        :param resource_limit: 组件规格。
        :type resource_limit: str
        :param runtime: 语言/运行时。
        :type runtime: str
        :param source: 组件源信息。
        :type source: str
        :param status: 组件状态。
        :type status: str
        :param version: 组件版本。
        :type version: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._app_id = None
        self._available_replica = None
        self._build = None
        self._build_id = None
        self._build_log_id = None
        self._env_id = None
        self._id = None
        self._image_url = None
        self._job_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._name = None
        self._operation = None
        self._operation_status = None
        self._replica = None
        self._resource_limit = None
        self._runtime = None
        self._source = None
        self._status = None
        self._version = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if available_replica is not None:
            self.available_replica = available_replica
        if build is not None:
            self.build = build
        if build_id is not None:
            self.build_id = build_id
        if build_log_id is not None:
            self.build_log_id = build_log_id
        if env_id is not None:
            self.env_id = env_id
        if id is not None:
            self.id = id
        if image_url is not None:
            self.image_url = image_url
        if job_id is not None:
            self.job_id = job_id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if name is not None:
            self.name = name
        if operation is not None:
            self.operation = operation
        if operation_status is not None:
            self.operation_status = operation_status
        if replica is not None:
            self.replica = replica
        if resource_limit is not None:
            self.resource_limit = resource_limit
        if runtime is not None:
            self.runtime = runtime
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def app_id(self):
        r"""Gets the app_id of this ComponentSnapshotContext.

        应用ID。

        :return: The app_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ComponentSnapshotContext.

        应用ID。

        :param app_id: The app_id of this ComponentSnapshotContext.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def available_replica(self):
        r"""Gets the available_replica of this ComponentSnapshotContext.

        可用实例个数。

        :return: The available_replica of this ComponentSnapshotContext.
        :rtype: int
        """
        return self._available_replica

    @available_replica.setter
    def available_replica(self, available_replica):
        r"""Sets the available_replica of this ComponentSnapshotContext.

        可用实例个数。

        :param available_replica: The available_replica of this ComponentSnapshotContext.
        :type available_replica: int
        """
        self._available_replica = available_replica

    @property
    def build(self):
        r"""Gets the build of this ComponentSnapshotContext.

        组件构建信息。

        :return: The build of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this ComponentSnapshotContext.

        组件构建信息。

        :param build: The build of this ComponentSnapshotContext.
        :type build: str
        """
        self._build = build

    @property
    def build_id(self):
        r"""Gets the build_id of this ComponentSnapshotContext.

        构建任务ID。

        :return: The build_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        r"""Sets the build_id of this ComponentSnapshotContext.

        构建任务ID。

        :param build_id: The build_id of this ComponentSnapshotContext.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def build_log_id(self):
        r"""Gets the build_log_id of this ComponentSnapshotContext.

        构建日志ID。

        :return: The build_log_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._build_log_id

    @build_log_id.setter
    def build_log_id(self, build_log_id):
        r"""Sets the build_log_id of this ComponentSnapshotContext.

        构建日志ID。

        :param build_log_id: The build_log_id of this ComponentSnapshotContext.
        :type build_log_id: str
        """
        self._build_log_id = build_log_id

    @property
    def env_id(self):
        r"""Gets the env_id of this ComponentSnapshotContext.

        环境ID。

        :return: The env_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ComponentSnapshotContext.

        环境ID。

        :param env_id: The env_id of this ComponentSnapshotContext.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def id(self):
        r"""Gets the id of this ComponentSnapshotContext.

        组件ID。

        :return: The id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentSnapshotContext.

        组件ID。

        :param id: The id of this ComponentSnapshotContext.
        :type id: str
        """
        self._id = id

    @property
    def image_url(self):
        r"""Gets the image_url of this ComponentSnapshotContext.

        镜像地址。

        :return: The image_url of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this ComponentSnapshotContext.

        镜像地址。

        :param image_url: The image_url of this ComponentSnapshotContext.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def job_id(self):
        r"""Gets the job_id of this ComponentSnapshotContext.

        任务ID。

        :return: The job_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ComponentSnapshotContext.

        任务ID。

        :param job_id: The job_id of this ComponentSnapshotContext.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ComponentSnapshotContext.

        LTS日志组的ID。

        :return: The log_group_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ComponentSnapshotContext.

        LTS日志组的ID。

        :param log_group_id: The log_group_id of this ComponentSnapshotContext.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this ComponentSnapshotContext.

        LTS日志流的ID

        :return: The log_stream_id of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this ComponentSnapshotContext.

        LTS日志流的ID

        :param log_stream_id: The log_stream_id of this ComponentSnapshotContext.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def name(self):
        r"""Gets the name of this ComponentSnapshotContext.

        组件名称。

        :return: The name of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentSnapshotContext.

        组件名称。

        :param name: The name of this ComponentSnapshotContext.
        :type name: str
        """
        self._name = name

    @property
    def operation(self):
        r"""Gets the operation of this ComponentSnapshotContext.

        组件操作。

        :return: The operation of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ComponentSnapshotContext.

        组件操作。

        :param operation: The operation of this ComponentSnapshotContext.
        :type operation: str
        """
        self._operation = operation

    @property
    def operation_status(self):
        r"""Gets the operation_status of this ComponentSnapshotContext.

        组件操作状态。

        :return: The operation_status of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        r"""Sets the operation_status of this ComponentSnapshotContext.

        组件操作状态。

        :param operation_status: The operation_status of this ComponentSnapshotContext.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def replica(self):
        r"""Gets the replica of this ComponentSnapshotContext.

        实例个数。

        :return: The replica of this ComponentSnapshotContext.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        r"""Sets the replica of this ComponentSnapshotContext.

        实例个数。

        :param replica: The replica of this ComponentSnapshotContext.
        :type replica: int
        """
        self._replica = replica

    @property
    def resource_limit(self):
        r"""Gets the resource_limit of this ComponentSnapshotContext.

        组件规格。

        :return: The resource_limit of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._resource_limit

    @resource_limit.setter
    def resource_limit(self, resource_limit):
        r"""Sets the resource_limit of this ComponentSnapshotContext.

        组件规格。

        :param resource_limit: The resource_limit of this ComponentSnapshotContext.
        :type resource_limit: str
        """
        self._resource_limit = resource_limit

    @property
    def runtime(self):
        r"""Gets the runtime of this ComponentSnapshotContext.

        语言/运行时。

        :return: The runtime of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ComponentSnapshotContext.

        语言/运行时。

        :param runtime: The runtime of this ComponentSnapshotContext.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def source(self):
        r"""Gets the source of this ComponentSnapshotContext.

        组件源信息。

        :return: The source of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ComponentSnapshotContext.

        组件源信息。

        :param source: The source of this ComponentSnapshotContext.
        :type source: str
        """
        self._source = source

    @property
    def status(self):
        r"""Gets the status of this ComponentSnapshotContext.

        组件状态。

        :return: The status of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ComponentSnapshotContext.

        组件状态。

        :param status: The status of this ComponentSnapshotContext.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this ComponentSnapshotContext.

        组件版本。

        :return: The version of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentSnapshotContext.

        组件版本。

        :param version: The version of this ComponentSnapshotContext.
        :type version: str
        """
        self._version = version

    @property
    def created_at(self):
        r"""Gets the created_at of this ComponentSnapshotContext.

        创建时间。

        :return: The created_at of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ComponentSnapshotContext.

        创建时间。

        :param created_at: The created_at of this ComponentSnapshotContext.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ComponentSnapshotContext.

        更新时间。

        :return: The updated_at of this ComponentSnapshotContext.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ComponentSnapshotContext.

        更新时间。

        :param updated_at: The updated_at of this ComponentSnapshotContext.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ComponentSnapshotContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
