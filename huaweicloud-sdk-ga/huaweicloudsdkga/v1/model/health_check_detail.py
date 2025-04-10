# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCheckDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'endpoint_group_id': 'str',
        'protocol': 'HealthCheckProtocol',
        'status': 'ConfigStatus',
        'port': 'int',
        'interval': 'int',
        'timeout': 'int',
        'max_retries': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'enabled': 'bool',
        'frozen_info': 'FrozenInfo'
    }

    attribute_map = {
        'id': 'id',
        'endpoint_group_id': 'endpoint_group_id',
        'protocol': 'protocol',
        'status': 'status',
        'port': 'port',
        'interval': 'interval',
        'timeout': 'timeout',
        'max_retries': 'max_retries',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'enabled': 'enabled',
        'frozen_info': 'frozen_info'
    }

    def __init__(self, id=None, endpoint_group_id=None, protocol=None, status=None, port=None, interval=None, timeout=None, max_retries=None, created_at=None, updated_at=None, domain_id=None, enabled=None, frozen_info=None):
        r"""HealthCheckDetail

        The model defined in huaweicloud sdk

        :param id: 健康检查ID。
        :type id: str
        :param endpoint_group_id: 终端节点组ID。
        :type endpoint_group_id: str
        :param protocol: 
        :type protocol: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param port: 健康检查的端口。
        :type port: int
        :param interval: 健康检查的时间间隔，单位为秒。
        :type interval: int
        :param timeout: 健康检查的超时时间，单位为秒。建议该值小于interval的值。
        :type timeout: int
        :param max_retries: 最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。
        :type max_retries: int
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param domain_id: 租户ID。
        :type domain_id: str
        :param enabled: 是否开启健康检查。
        :type enabled: bool
        :param frozen_info: 
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        
        

        self._id = None
        self._endpoint_group_id = None
        self._protocol = None
        self._status = None
        self._port = None
        self._interval = None
        self._timeout = None
        self._max_retries = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._enabled = None
        self._frozen_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if endpoint_group_id is not None:
            self.endpoint_group_id = endpoint_group_id
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if max_retries is not None:
            self.max_retries = max_retries
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if enabled is not None:
            self.enabled = enabled
        if frozen_info is not None:
            self.frozen_info = frozen_info

    @property
    def id(self):
        r"""Gets the id of this HealthCheckDetail.

        健康检查ID。

        :return: The id of this HealthCheckDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HealthCheckDetail.

        健康检查ID。

        :param id: The id of this HealthCheckDetail.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_group_id(self):
        r"""Gets the endpoint_group_id of this HealthCheckDetail.

        终端节点组ID。

        :return: The endpoint_group_id of this HealthCheckDetail.
        :rtype: str
        """
        return self._endpoint_group_id

    @endpoint_group_id.setter
    def endpoint_group_id(self, endpoint_group_id):
        r"""Sets the endpoint_group_id of this HealthCheckDetail.

        终端节点组ID。

        :param endpoint_group_id: The endpoint_group_id of this HealthCheckDetail.
        :type endpoint_group_id: str
        """
        self._endpoint_group_id = endpoint_group_id

    @property
    def protocol(self):
        r"""Gets the protocol of this HealthCheckDetail.

        :return: The protocol of this HealthCheckDetail.
        :rtype: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this HealthCheckDetail.

        :param protocol: The protocol of this HealthCheckDetail.
        :type protocol: :class:`huaweicloudsdkga.v1.HealthCheckProtocol`
        """
        self._protocol = protocol

    @property
    def status(self):
        r"""Gets the status of this HealthCheckDetail.

        :return: The status of this HealthCheckDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HealthCheckDetail.

        :param status: The status of this HealthCheckDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this HealthCheckDetail.

        健康检查的端口。

        :return: The port of this HealthCheckDetail.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this HealthCheckDetail.

        健康检查的端口。

        :param port: The port of this HealthCheckDetail.
        :type port: int
        """
        self._port = port

    @property
    def interval(self):
        r"""Gets the interval of this HealthCheckDetail.

        健康检查的时间间隔，单位为秒。

        :return: The interval of this HealthCheckDetail.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this HealthCheckDetail.

        健康检查的时间间隔，单位为秒。

        :param interval: The interval of this HealthCheckDetail.
        :type interval: int
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this HealthCheckDetail.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :return: The timeout of this HealthCheckDetail.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this HealthCheckDetail.

        健康检查的超时时间，单位为秒。建议该值小于interval的值。

        :param timeout: The timeout of this HealthCheckDetail.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def max_retries(self):
        r"""Gets the max_retries of this HealthCheckDetail.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :return: The max_retries of this HealthCheckDetail.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this HealthCheckDetail.

        最大重试次数。将终端节点的状态从“健康”设置为“不健康”或从“不健康”设置为“健康”所需的连续健康检查次数。

        :param max_retries: The max_retries of this HealthCheckDetail.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def created_at(self):
        r"""Gets the created_at of this HealthCheckDetail.

        创建时间。

        :return: The created_at of this HealthCheckDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HealthCheckDetail.

        创建时间。

        :param created_at: The created_at of this HealthCheckDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this HealthCheckDetail.

        更新时间。

        :return: The updated_at of this HealthCheckDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this HealthCheckDetail.

        更新时间。

        :param updated_at: The updated_at of this HealthCheckDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this HealthCheckDetail.

        租户ID。

        :return: The domain_id of this HealthCheckDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this HealthCheckDetail.

        租户ID。

        :param domain_id: The domain_id of this HealthCheckDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enabled(self):
        r"""Gets the enabled of this HealthCheckDetail.

        是否开启健康检查。

        :return: The enabled of this HealthCheckDetail.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this HealthCheckDetail.

        是否开启健康检查。

        :param enabled: The enabled of this HealthCheckDetail.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def frozen_info(self):
        r"""Gets the frozen_info of this HealthCheckDetail.

        :return: The frozen_info of this HealthCheckDetail.
        :rtype: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        return self._frozen_info

    @frozen_info.setter
    def frozen_info(self, frozen_info):
        r"""Sets the frozen_info of this HealthCheckDetail.

        :param frozen_info: The frozen_info of this HealthCheckDetail.
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        self._frozen_info = frozen_info

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
        if not isinstance(other, HealthCheckDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
