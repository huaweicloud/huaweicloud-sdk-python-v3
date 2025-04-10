# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInstanceStatusRsp:

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
        'pod_ip': 'str',
        'host_ip': 'str',
        'host_name': 'str',
        'start_time': 'str',
        'container_statuses': 'list[TaskInstanceContainerStatusRsp]'
    }

    attribute_map = {
        'phase': 'phase',
        'pod_ip': 'pod_ip',
        'host_ip': 'host_ip',
        'host_name': 'host_name',
        'start_time': 'start_time',
        'container_statuses': 'container_statuses'
    }

    def __init__(self, phase=None, pod_ip=None, host_ip=None, host_name=None, start_time=None, container_statuses=None):
        r"""TaskInstanceStatusRsp

        The model defined in huaweicloud sdk

        :param phase: 实例执行状态
        :type phase: str
        :param pod_ip: 实例IP
        :type pod_ip: str
        :param host_ip: 实例所在节点IP
        :type host_ip: str
        :param host_name: 计算节点的名称
        :type host_name: str
        :param start_time: 实例创建时间
        :type start_time: str
        :param container_statuses: 实例状态信息
        :type container_statuses: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceContainerStatusRsp`]
        """
        
        

        self._phase = None
        self._pod_ip = None
        self._host_ip = None
        self._host_name = None
        self._start_time = None
        self._container_statuses = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if host_ip is not None:
            self.host_ip = host_ip
        if host_name is not None:
            self.host_name = host_name
        if start_time is not None:
            self.start_time = start_time
        if container_statuses is not None:
            self.container_statuses = container_statuses

    @property
    def phase(self):
        r"""Gets the phase of this TaskInstanceStatusRsp.

        实例执行状态

        :return: The phase of this TaskInstanceStatusRsp.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this TaskInstanceStatusRsp.

        实例执行状态

        :param phase: The phase of this TaskInstanceStatusRsp.
        :type phase: str
        """
        self._phase = phase

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this TaskInstanceStatusRsp.

        实例IP

        :return: The pod_ip of this TaskInstanceStatusRsp.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this TaskInstanceStatusRsp.

        实例IP

        :param pod_ip: The pod_ip of this TaskInstanceStatusRsp.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def host_ip(self):
        r"""Gets the host_ip of this TaskInstanceStatusRsp.

        实例所在节点IP

        :return: The host_ip of this TaskInstanceStatusRsp.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this TaskInstanceStatusRsp.

        实例所在节点IP

        :param host_ip: The host_ip of this TaskInstanceStatusRsp.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_name(self):
        r"""Gets the host_name of this TaskInstanceStatusRsp.

        计算节点的名称

        :return: The host_name of this TaskInstanceStatusRsp.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this TaskInstanceStatusRsp.

        计算节点的名称

        :param host_name: The host_name of this TaskInstanceStatusRsp.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskInstanceStatusRsp.

        实例创建时间

        :return: The start_time of this TaskInstanceStatusRsp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskInstanceStatusRsp.

        实例创建时间

        :param start_time: The start_time of this TaskInstanceStatusRsp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def container_statuses(self):
        r"""Gets the container_statuses of this TaskInstanceStatusRsp.

        实例状态信息

        :return: The container_statuses of this TaskInstanceStatusRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceContainerStatusRsp`]
        """
        return self._container_statuses

    @container_statuses.setter
    def container_statuses(self, container_statuses):
        r"""Sets the container_statuses of this TaskInstanceStatusRsp.

        实例状态信息

        :param container_statuses: The container_statuses of this TaskInstanceStatusRsp.
        :type container_statuses: list[:class:`huaweicloudsdkeihealth.v1.TaskInstanceContainerStatusRsp`]
        """
        self._container_statuses = container_statuses

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
        if not isinstance(other, TaskInstanceStatusRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
