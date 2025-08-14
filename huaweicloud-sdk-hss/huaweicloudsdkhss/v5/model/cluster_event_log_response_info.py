# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterEventLogResponseInfo:

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
        'cluster_type': 'str',
        'time': 'int',
        'namespace': 'str',
        'event_name': 'str',
        'event_type': 'str',
        'resource_type': 'str',
        'resource_name': 'str',
        'reason': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'time': 'time',
        'namespace': 'namespace',
        'event_name': 'event_name',
        'event_type': 'event_type',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'reason': 'reason',
        'line_num': 'line_num'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cluster_type=None, time=None, namespace=None, event_name=None, event_type=None, resource_type=None, resource_name=None, reason=None, line_num=None):
        r"""ClusterEventLogResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param time: 日志产生的时间
        :type time: int
        :param namespace: 触发事件的命名空间
        :type namespace: str
        :param event_name: 事件名称
        :type event_name: str
        :param event_type: 事件类型
        :type event_type: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param reason: 事件触发的原因
        :type reason: str
        :param line_num: cce集群事件的行号
        :type line_num: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._time = None
        self._namespace = None
        self._event_name = None
        self._event_type = None
        self._resource_type = None
        self._resource_name = None
        self._reason = None
        self._line_num = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if time is not None:
            self.time = time
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
        if line_num is not None:
            self.line_num = line_num

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterEventLogResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterEventLogResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterEventLogResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterEventLogResponseInfo.

        集群id

        :return: The cluster_id of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterEventLogResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterEventLogResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterEventLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterEventLogResponseInfo.

        集群类型，包含以下几种： - cce：cce集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ClusterEventLogResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def time(self):
        r"""Gets the time of this ClusterEventLogResponseInfo.

        日志产生的时间

        :return: The time of this ClusterEventLogResponseInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ClusterEventLogResponseInfo.

        日志产生的时间

        :param time: The time of this ClusterEventLogResponseInfo.
        :type time: int
        """
        self._time = time

    @property
    def namespace(self):
        r"""Gets the namespace of this ClusterEventLogResponseInfo.

        触发事件的命名空间

        :return: The namespace of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ClusterEventLogResponseInfo.

        触发事件的命名空间

        :param namespace: The namespace of this ClusterEventLogResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def event_name(self):
        r"""Gets the event_name of this ClusterEventLogResponseInfo.

        事件名称

        :return: The event_name of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ClusterEventLogResponseInfo.

        事件名称

        :param event_name: The event_name of this ClusterEventLogResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        r"""Gets the event_type of this ClusterEventLogResponseInfo.

        事件类型

        :return: The event_type of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ClusterEventLogResponseInfo.

        事件类型

        :param event_type: The event_type of this ClusterEventLogResponseInfo.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ClusterEventLogResponseInfo.

        资源类型

        :return: The resource_type of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ClusterEventLogResponseInfo.

        资源类型

        :param resource_type: The resource_type of this ClusterEventLogResponseInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ClusterEventLogResponseInfo.

        资源名称

        :return: The resource_name of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ClusterEventLogResponseInfo.

        资源名称

        :param resource_name: The resource_name of this ClusterEventLogResponseInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def reason(self):
        r"""Gets the reason of this ClusterEventLogResponseInfo.

        事件触发的原因

        :return: The reason of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ClusterEventLogResponseInfo.

        事件触发的原因

        :param reason: The reason of this ClusterEventLogResponseInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def line_num(self):
        r"""Gets the line_num of this ClusterEventLogResponseInfo.

        cce集群事件的行号

        :return: The line_num of this ClusterEventLogResponseInfo.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ClusterEventLogResponseInfo.

        cce集群事件的行号

        :param line_num: The line_num of this ClusterEventLogResponseInfo.
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
        if not isinstance(other, ClusterEventLogResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
