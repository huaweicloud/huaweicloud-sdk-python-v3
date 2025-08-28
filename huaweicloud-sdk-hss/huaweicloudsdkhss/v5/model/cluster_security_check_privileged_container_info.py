# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckPrivilegedContainerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_name': 'str',
        'container_id': 'str',
        'container_status': 'str',
        'pod_name': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'event_abstract': 'str'
    }

    attribute_map = {
        'container_name': 'container_name',
        'container_id': 'container_id',
        'container_status': 'container_status',
        'pod_name': 'pod_name',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'event_abstract': 'event_abstract'
    }

    def __init__(self, container_name=None, container_id=None, container_status=None, pod_name=None, host_name=None, private_ip=None, public_ip=None, event_abstract=None):
        r"""ClusterSecurityCheckPrivilegedContainerInfo

        The model defined in huaweicloud sdk

        :param container_name: **参数解释**： 容器名称 **取值范围**： 不涉及 
        :type container_name: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 不涉及 
        :type container_id: str
        :param container_status: **参数解释**： 容器状态 **取值范围**： - running：运行中 - terminated：已结束 
        :type container_status: str
        :param pod_name: **参数解释**： pod名称 **取值范围**： 不涉及 
        :type pod_name: str
        :param host_name: **参数解释**： 节点名称 **取值范围**： 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**： 私有IP地址 **取值范围**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 公有IP地址 **取值范围**： 不涉及 
        :type public_ip: str
        :param event_abstract: **参数解释**： 事件摘要 **取值范围**： 不涉及 
        :type event_abstract: str
        """
        
        

        self._container_name = None
        self._container_id = None
        self._container_status = None
        self._pod_name = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._event_abstract = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if container_status is not None:
            self.container_status = container_status
        if pod_name is not None:
            self.pod_name = pod_name
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if event_abstract is not None:
            self.event_abstract = event_abstract

    @property
    def container_name(self):
        r"""Gets the container_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :return: The container_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :param container_name: The container_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :return: The container_id of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :param container_id: The container_id of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_status(self):
        r"""Gets the container_status of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器状态 **取值范围**： - running：运行中 - terminated：已结束 

        :return: The container_status of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 容器状态 **取值范围**： - running：运行中 - terminated：已结束 

        :param container_status: The container_status of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： pod名称 **取值范围**： 不涉及 

        :return: The pod_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： pod名称 **取值范围**： 不涉及 

        :param pod_name: The pod_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :return: The host_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :param host_name: The host_name of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :return: The private_ip of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :param private_ip: The private_ip of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :return: The public_ip of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :param public_ip: The public_ip of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def event_abstract(self):
        r"""Gets the event_abstract of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 事件摘要 **取值范围**： 不涉及 

        :return: The event_abstract of this ClusterSecurityCheckPrivilegedContainerInfo.
        :rtype: str
        """
        return self._event_abstract

    @event_abstract.setter
    def event_abstract(self, event_abstract):
        r"""Sets the event_abstract of this ClusterSecurityCheckPrivilegedContainerInfo.

        **参数解释**： 事件摘要 **取值范围**： 不涉及 

        :param event_abstract: The event_abstract of this ClusterSecurityCheckPrivilegedContainerInfo.
        :type event_abstract: str
        """
        self._event_abstract = event_abstract

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
        if not isinstance(other, ClusterSecurityCheckPrivilegedContainerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
