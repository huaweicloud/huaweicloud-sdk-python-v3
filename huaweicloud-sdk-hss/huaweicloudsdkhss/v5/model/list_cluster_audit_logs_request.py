# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterAuditLogsRequest:

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
        'host_name': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'verb': 'str',
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
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'verb': 'verb',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'line_num': 'line_num'
    }

    def __init__(self, enterprise_project_id=None, cluster_id=None, cluster_name=None, host_name=None, host_id=None, host_ip=None, verb=None, start_time=None, end_time=None, limit=None, offset=None, line_num=None):
        r"""ListClusterAuditLogsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_id: 主机id
        :type host_id: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param verb: 审计日志对应的动作，包含以下几种： - create：创建资源 - delete：删除资源 - deletecollection：批量删除资源集合 - patch：修改资源 - update：更新资源 - get：获取资源 - list：获取资源列表 - watch：监控资源
        :type verb: str
        :param start_time: 查询日志范围的最小时间
        :type start_time: int
        :param end_time: 查询日志范围的最大时间
        :type end_time: int
        :param limit: 每页显示个数，默认为10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param line_num: 查询cce集群日志时需要传的分页行号
        :type line_num: str
        """
        
        

        self._enterprise_project_id = None
        self._cluster_id = None
        self._cluster_name = None
        self._host_name = None
        self._host_id = None
        self._host_ip = None
        self._verb = None
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
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if verb is not None:
            self.verb = verb
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if line_num is not None:
            self.line_num = line_num

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListClusterAuditLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListClusterAuditLogsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListClusterAuditLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListClusterAuditLogsRequest.

        集群id

        :return: The cluster_id of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListClusterAuditLogsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListClusterAuditLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListClusterAuditLogsRequest.

        集群名称

        :return: The cluster_name of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListClusterAuditLogsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListClusterAuditLogsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListClusterAuditLogsRequest.

        主机名称

        :return: The host_name of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListClusterAuditLogsRequest.

        主机名称

        :param host_name: The host_name of this ListClusterAuditLogsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListClusterAuditLogsRequest.

        主机id

        :return: The host_id of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListClusterAuditLogsRequest.

        主机id

        :param host_id: The host_id of this ListClusterAuditLogsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListClusterAuditLogsRequest.

        主机ip

        :return: The host_ip of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListClusterAuditLogsRequest.

        主机ip

        :param host_ip: The host_ip of this ListClusterAuditLogsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def verb(self):
        r"""Gets the verb of this ListClusterAuditLogsRequest.

        审计日志对应的动作，包含以下几种： - create：创建资源 - delete：删除资源 - deletecollection：批量删除资源集合 - patch：修改资源 - update：更新资源 - get：获取资源 - list：获取资源列表 - watch：监控资源

        :return: The verb of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        r"""Sets the verb of this ListClusterAuditLogsRequest.

        审计日志对应的动作，包含以下几种： - create：创建资源 - delete：删除资源 - deletecollection：批量删除资源集合 - patch：修改资源 - update：更新资源 - get：获取资源 - list：获取资源列表 - watch：监控资源

        :param verb: The verb of this ListClusterAuditLogsRequest.
        :type verb: str
        """
        self._verb = verb

    @property
    def start_time(self):
        r"""Gets the start_time of this ListClusterAuditLogsRequest.

        查询日志范围的最小时间

        :return: The start_time of this ListClusterAuditLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListClusterAuditLogsRequest.

        查询日志范围的最小时间

        :param start_time: The start_time of this ListClusterAuditLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListClusterAuditLogsRequest.

        查询日志范围的最大时间

        :return: The end_time of this ListClusterAuditLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListClusterAuditLogsRequest.

        查询日志范围的最大时间

        :param end_time: The end_time of this ListClusterAuditLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterAuditLogsRequest.

        每页显示个数，默认为10

        :return: The limit of this ListClusterAuditLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterAuditLogsRequest.

        每页显示个数，默认为10

        :param limit: The limit of this ListClusterAuditLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterAuditLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListClusterAuditLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterAuditLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListClusterAuditLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def line_num(self):
        r"""Gets the line_num of this ListClusterAuditLogsRequest.

        查询cce集群日志时需要传的分页行号

        :return: The line_num of this ListClusterAuditLogsRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListClusterAuditLogsRequest.

        查询cce集群日志时需要传的分页行号

        :param line_num: The line_num of this ListClusterAuditLogsRequest.
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
        if not isinstance(other, ListClusterAuditLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
