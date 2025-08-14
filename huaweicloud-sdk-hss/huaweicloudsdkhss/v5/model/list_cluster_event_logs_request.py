# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterEventLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'namespace': 'str',
        'event_name': 'str',
        'event_type': 'str',
        'resource_type': 'str',
        'resource_name': 'str',
        'reason': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'line_num': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'namespace': 'namespace',
        'event_name': 'event_name',
        'event_type': 'event_type',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'reason': 'reason',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'line_num': 'line_num'
    }

    def __init__(self, enterprise_project_id=None, cluster_id=None, cluster_name=None, namespace=None, event_name=None, event_type=None, resource_type=None, resource_name=None, reason=None, start_time=None, end_time=None, limit=None, offset=None, line_num=None):
        r"""ListClusterEventLogsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param namespace: 产生事件的命名空间
        :type namespace: str
        :param event_name: 事件名称
        :type event_name: str
        :param event_type: 事件类型，包含以下几种： - Warning：警告事件 - Normal：普通事件
        :type event_type: str
        :param resource_type: 产生事件的资源类型
        :type resource_type: str
        :param resource_name: 产生事件的资源名称
        :type resource_name: str
        :param reason: 事件的触发原因
        :type reason: str
        :param start_time: 查询日志范围的最小时间
        :type start_time: int
        :param end_time: 查询日志范围的最大时间
        :type end_time: int
        :param limit: 每页显示个数，默认为10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param line_num: 查询cce集群事件时需要传的分页行号
        :type line_num: str
        """
        
        

        self._enterprise_project_id = None
        self._cluster_id = None
        self._cluster_name = None
        self._namespace = None
        self._event_name = None
        self._event_type = None
        self._resource_type = None
        self._resource_name = None
        self._reason = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._line_num = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if namespace is not None:
            self.namespace = namespace
        if event_name is not None:
            self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if reason is not None:
            self.reason = reason
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if line_num is not None:
            self.line_num = line_num

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClusterEventLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClusterEventLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListClusterEventLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListClusterEventLogsRequest.

        集群id

        :return: The cluster_id of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListClusterEventLogsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListClusterEventLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListClusterEventLogsRequest.

        集群名称

        :return: The cluster_name of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListClusterEventLogsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListClusterEventLogsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ListClusterEventLogsRequest.

        产生事件的命名空间

        :return: The namespace of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListClusterEventLogsRequest.

        产生事件的命名空间

        :param namespace: The namespace of this ListClusterEventLogsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def event_name(self):
        r"""Gets the event_name of this ListClusterEventLogsRequest.

        事件名称

        :return: The event_name of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListClusterEventLogsRequest.

        事件名称

        :param event_name: The event_name of this ListClusterEventLogsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ListClusterEventLogsRequest.

        事件类型，包含以下几种： - Warning：警告事件 - Normal：普通事件

        :return: The event_type of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListClusterEventLogsRequest.

        事件类型，包含以下几种： - Warning：警告事件 - Normal：普通事件

        :param event_type: The event_type of this ListClusterEventLogsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListClusterEventLogsRequest.

        产生事件的资源类型

        :return: The resource_type of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListClusterEventLogsRequest.

        产生事件的资源类型

        :param resource_type: The resource_type of this ListClusterEventLogsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListClusterEventLogsRequest.

        产生事件的资源名称

        :return: The resource_name of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListClusterEventLogsRequest.

        产生事件的资源名称

        :param resource_name: The resource_name of this ListClusterEventLogsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def reason(self):
        r"""Gets the reason of this ListClusterEventLogsRequest.

        事件的触发原因

        :return: The reason of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ListClusterEventLogsRequest.

        事件的触发原因

        :param reason: The reason of this ListClusterEventLogsRequest.
        :type reason: str
        """
        self._reason = reason

    @property
    def start_time(self):
        r"""Gets the start_time of this ListClusterEventLogsRequest.

        查询日志范围的最小时间

        :return: The start_time of this ListClusterEventLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListClusterEventLogsRequest.

        查询日志范围的最小时间

        :param start_time: The start_time of this ListClusterEventLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListClusterEventLogsRequest.

        查询日志范围的最大时间

        :return: The end_time of this ListClusterEventLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListClusterEventLogsRequest.

        查询日志范围的最大时间

        :param end_time: The end_time of this ListClusterEventLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterEventLogsRequest.

        每页显示个数，默认为10

        :return: The limit of this ListClusterEventLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterEventLogsRequest.

        每页显示个数，默认为10

        :param limit: The limit of this ListClusterEventLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterEventLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListClusterEventLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterEventLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListClusterEventLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def line_num(self):
        r"""Gets the line_num of this ListClusterEventLogsRequest.

        查询cce集群事件时需要传的分页行号

        :return: The line_num of this ListClusterEventLogsRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListClusterEventLogsRequest.

        查询cce集群事件时需要传的分页行号

        :param line_num: The line_num of this ListClusterEventLogsRequest.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, ListClusterEventLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
