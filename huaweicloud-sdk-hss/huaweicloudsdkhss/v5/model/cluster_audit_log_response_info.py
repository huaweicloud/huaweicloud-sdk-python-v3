# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterAuditLogResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'time': 'int',
        'content': 'str',
        'cluster_type': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'time': 'time',
        'content': 'content',
        'cluster_type': 'cluster_type',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'line_num': 'line_num'
    }

    def __init__(self, cluster_name=None, cluster_id=None, time=None, content=None, cluster_type=None, host_id=None, host_name=None, host_ip=None, line_num=None):
        r"""ClusterAuditLogResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param time: 日志产生的时间
        :type time: int
        :param content: 审计日志的内容，json格式的字符串
        :type content: str
        :param cluster_type: 集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param host_id: 主机ID
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param line_num: cce集群日志的行号
        :type line_num: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._time = None
        self._content = None
        self._cluster_type = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._line_num = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if time is not None:
            self.time = time
        if content is not None:
            self.content = content
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if line_num is not None:
            self.line_num = line_num

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterAuditLogResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterAuditLogResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterAuditLogResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterAuditLogResponseInfo.

        集群id

        :return: The cluster_id of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterAuditLogResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterAuditLogResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def time(self):
        r"""Gets the time of this ClusterAuditLogResponseInfo.

        日志产生的时间

        :return: The time of this ClusterAuditLogResponseInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ClusterAuditLogResponseInfo.

        日志产生的时间

        :param time: The time of this ClusterAuditLogResponseInfo.
        :type time: int
        """
        self._time = time

    @property
    def content(self):
        r"""Gets the content of this ClusterAuditLogResponseInfo.

        审计日志的内容，json格式的字符串

        :return: The content of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ClusterAuditLogResponseInfo.

        审计日志的内容，json格式的字符串

        :param content: The content of this ClusterAuditLogResponseInfo.
        :type content: str
        """
        self._content = content

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterAuditLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterAuditLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ClusterAuditLogResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def host_id(self):
        r"""Gets the host_id of this ClusterAuditLogResponseInfo.

        主机ID

        :return: The host_id of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ClusterAuditLogResponseInfo.

        主机ID

        :param host_id: The host_id of this ClusterAuditLogResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ClusterAuditLogResponseInfo.

        主机名称

        :return: The host_name of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ClusterAuditLogResponseInfo.

        主机名称

        :param host_name: The host_name of this ClusterAuditLogResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ClusterAuditLogResponseInfo.

        主机ip

        :return: The host_ip of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ClusterAuditLogResponseInfo.

        主机ip

        :param host_ip: The host_ip of this ClusterAuditLogResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def line_num(self):
        r"""Gets the line_num of this ClusterAuditLogResponseInfo.

        cce集群日志的行号

        :return: The line_num of this ClusterAuditLogResponseInfo.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ClusterAuditLogResponseInfo.

        cce集群日志的行号

        :param line_num: The line_num of this ClusterAuditLogResponseInfo.
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
        if not isinstance(other, ClusterAuditLogResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
