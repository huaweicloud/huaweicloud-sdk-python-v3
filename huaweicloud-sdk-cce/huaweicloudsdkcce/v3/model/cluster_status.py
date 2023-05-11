# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'job_id': 'str',
        'reason': 'str',
        'message': 'str',
        'endpoints': 'list[ClusterEndpoints]',
        'is_locked': 'bool',
        'lock_scene': 'str',
        'lock_source': 'str',
        'lock_source_id': 'str',
        'delete_option': 'object',
        'delete_status': 'object'
    }

    attribute_map = {
        'phase': 'phase',
        'job_id': 'jobID',
        'reason': 'reason',
        'message': 'message',
        'endpoints': 'endpoints',
        'is_locked': 'isLocked',
        'lock_scene': 'lockScene',
        'lock_source': 'lockSource',
        'lock_source_id': 'lockSourceId',
        'delete_option': 'deleteOption',
        'delete_status': 'deleteStatus'
    }

    def __init__(self, phase=None, job_id=None, reason=None, message=None, endpoints=None, is_locked=None, lock_scene=None, lock_source=None, lock_source_id=None, delete_option=None, delete_status=None):
        """ClusterStatus

        The model defined in huaweicloud sdk

        :param phase: 集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Empty：集群无任何资源
        :type phase: str
        :param job_id: 作业ID
        :type job_id: str
        :param reason: 集群变为当前状态的原因，在集群在非“Available”状态下时，会返回此参数。
        :type reason: str
        :param message: 集群变为当前状态的原因的详细信息，在集群在非“Available”状态下时，会返回此参数。
        :type message: str
        :param endpoints: 集群中 kube-apiserver 的访问地址。
        :type endpoints: list[:class:`huaweicloudsdkcce.v3.ClusterEndpoints`]
        :param is_locked: CBC资源锁定
        :type is_locked: bool
        :param lock_scene: CBC资源锁定场景
        :type lock_scene: str
        :param lock_source: 锁定资源
        :type lock_source: str
        :param lock_source_id: 锁定的资源ID
        :type lock_source_id: str
        :param delete_option: 删除配置状态（仅删除请求响应包含）
        :type delete_option: object
        :param delete_status: 删除状态信息（仅删除请求响应包含）
        :type delete_status: object
        """
        
        

        self._phase = None
        self._job_id = None
        self._reason = None
        self._message = None
        self._endpoints = None
        self._is_locked = None
        self._lock_scene = None
        self._lock_source = None
        self._lock_source_id = None
        self._delete_option = None
        self._delete_status = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if job_id is not None:
            self.job_id = job_id
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message
        if endpoints is not None:
            self.endpoints = endpoints
        if is_locked is not None:
            self.is_locked = is_locked
        if lock_scene is not None:
            self.lock_scene = lock_scene
        if lock_source is not None:
            self.lock_source = lock_source
        if lock_source_id is not None:
            self.lock_source_id = lock_source_id
        if delete_option is not None:
            self.delete_option = delete_option
        if delete_status is not None:
            self.delete_status = delete_status

    @property
    def phase(self):
        """Gets the phase of this ClusterStatus.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Empty：集群无任何资源

        :return: The phase of this ClusterStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this ClusterStatus.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - RollingBack：回滚中，表示集群正处于回滚过程中。 - RollbackFailed：回滚异常，表示集群回滚异常。 - Empty：集群无任何资源

        :param phase: The phase of this ClusterStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def job_id(self):
        """Gets the job_id of this ClusterStatus.

        作业ID

        :return: The job_id of this ClusterStatus.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ClusterStatus.

        作业ID

        :param job_id: The job_id of this ClusterStatus.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def reason(self):
        """Gets the reason of this ClusterStatus.

        集群变为当前状态的原因，在集群在非“Available”状态下时，会返回此参数。

        :return: The reason of this ClusterStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ClusterStatus.

        集群变为当前状态的原因，在集群在非“Available”状态下时，会返回此参数。

        :param reason: The reason of this ClusterStatus.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        """Gets the message of this ClusterStatus.

        集群变为当前状态的原因的详细信息，在集群在非“Available”状态下时，会返回此参数。

        :return: The message of this ClusterStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClusterStatus.

        集群变为当前状态的原因的详细信息，在集群在非“Available”状态下时，会返回此参数。

        :param message: The message of this ClusterStatus.
        :type message: str
        """
        self._message = message

    @property
    def endpoints(self):
        """Gets the endpoints of this ClusterStatus.

        集群中 kube-apiserver 的访问地址。

        :return: The endpoints of this ClusterStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ClusterEndpoints`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ClusterStatus.

        集群中 kube-apiserver 的访问地址。

        :param endpoints: The endpoints of this ClusterStatus.
        :type endpoints: list[:class:`huaweicloudsdkcce.v3.ClusterEndpoints`]
        """
        self._endpoints = endpoints

    @property
    def is_locked(self):
        """Gets the is_locked of this ClusterStatus.

        CBC资源锁定

        :return: The is_locked of this ClusterStatus.
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this ClusterStatus.

        CBC资源锁定

        :param is_locked: The is_locked of this ClusterStatus.
        :type is_locked: bool
        """
        self._is_locked = is_locked

    @property
    def lock_scene(self):
        """Gets the lock_scene of this ClusterStatus.

        CBC资源锁定场景

        :return: The lock_scene of this ClusterStatus.
        :rtype: str
        """
        return self._lock_scene

    @lock_scene.setter
    def lock_scene(self, lock_scene):
        """Sets the lock_scene of this ClusterStatus.

        CBC资源锁定场景

        :param lock_scene: The lock_scene of this ClusterStatus.
        :type lock_scene: str
        """
        self._lock_scene = lock_scene

    @property
    def lock_source(self):
        """Gets the lock_source of this ClusterStatus.

        锁定资源

        :return: The lock_source of this ClusterStatus.
        :rtype: str
        """
        return self._lock_source

    @lock_source.setter
    def lock_source(self, lock_source):
        """Sets the lock_source of this ClusterStatus.

        锁定资源

        :param lock_source: The lock_source of this ClusterStatus.
        :type lock_source: str
        """
        self._lock_source = lock_source

    @property
    def lock_source_id(self):
        """Gets the lock_source_id of this ClusterStatus.

        锁定的资源ID

        :return: The lock_source_id of this ClusterStatus.
        :rtype: str
        """
        return self._lock_source_id

    @lock_source_id.setter
    def lock_source_id(self, lock_source_id):
        """Sets the lock_source_id of this ClusterStatus.

        锁定的资源ID

        :param lock_source_id: The lock_source_id of this ClusterStatus.
        :type lock_source_id: str
        """
        self._lock_source_id = lock_source_id

    @property
    def delete_option(self):
        """Gets the delete_option of this ClusterStatus.

        删除配置状态（仅删除请求响应包含）

        :return: The delete_option of this ClusterStatus.
        :rtype: object
        """
        return self._delete_option

    @delete_option.setter
    def delete_option(self, delete_option):
        """Sets the delete_option of this ClusterStatus.

        删除配置状态（仅删除请求响应包含）

        :param delete_option: The delete_option of this ClusterStatus.
        :type delete_option: object
        """
        self._delete_option = delete_option

    @property
    def delete_status(self):
        """Gets the delete_status of this ClusterStatus.

        删除状态信息（仅删除请求响应包含）

        :return: The delete_status of this ClusterStatus.
        :rtype: object
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        """Sets the delete_status of this ClusterStatus.

        删除状态信息（仅删除请求响应包含）

        :param delete_status: The delete_status of this ClusterStatus.
        :type delete_status: object
        """
        self._delete_status = delete_status

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
        if not isinstance(other, ClusterStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
