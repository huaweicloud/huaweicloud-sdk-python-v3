# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'type': 'str',
        'limit': 'int',
        'marker': 'str',
        'resource_id_list': 'list[str]',
        'name': 'str',
        'region_id': 'str',
        'az_id': 'str',
        'ip_type': 'str',
        'ip': 'str',
        'status': 'str',
        'agent_state': 'str',
        'image_name': 'str',
        'os_type': 'str',
        'tag': 'str',
        'tag_key': 'str',
        'group_id': 'str',
        'component_id': 'str',
        'application_id': 'str',
        'cce_cluster_id': 'str',
        'vpc_id': 'str',
        'ep_id': 'str',
        'is_delegated': 'bool'
    }

    attribute_map = {
        'provider': 'provider',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker',
        'resource_id_list': 'resource_id_list',
        'name': 'name',
        'region_id': 'region_id',
        'az_id': 'az_id',
        'ip_type': 'ip_type',
        'ip': 'ip',
        'status': 'status',
        'agent_state': 'agent_state',
        'image_name': 'image_name',
        'os_type': 'os_type',
        'tag': 'tag',
        'tag_key': 'tag_key',
        'group_id': 'group_id',
        'component_id': 'component_id',
        'application_id': 'application_id',
        'cce_cluster_id': 'cce_cluster_id',
        'vpc_id': 'vpc_id',
        'ep_id': 'ep_id',
        'is_delegated': 'is_delegated'
    }

    def __init__(self, provider=None, type=None, limit=None, marker=None, resource_id_list=None, name=None, region_id=None, az_id=None, ip_type=None, ip=None, status=None, agent_state=None, image_name=None, os_type=None, tag=None, tag_key=None, group_id=None, component_id=None, application_id=None, cce_cluster_id=None, vpc_id=None, ep_id=None, is_delegated=None):
        """ListResourceRequest

        The model defined in huaweicloud sdk

        :param provider: 云服务名称
        :type provider: str
        :param type: 资源类型名称
        :type type: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param resource_id_list: 资源id列表
        :type resource_id_list: list[str]
        :param name: 名称
        :type name: str
        :param region_id: region id
        :type region_id: str
        :param az_id: az id
        :type az_id: str
        :param ip_type: ip类型，fixed：内网IP，floating：弹性公网IP
        :type ip_type: str
        :param ip: ip
        :type ip: str
        :param status: 资源状态
        :type status: str
        :param agent_state: agent状态
        :type agent_state: str
        :param image_name: 镜像名称，模糊匹配
        :type image_name: str
        :param os_type: 系统类型
        :type os_type: str
        :param tag: 标签的值
        :type tag: str
        :param tag_key: 标签的key
        :type tag_key: str
        :param group_id: 分组id
        :type group_id: str
        :param component_id: 组件id
        :type component_id: str
        :param application_id: 应用id
        :type application_id: str
        :param cce_cluster_id: cce集群id
        :type cce_cluster_id: str
        :param vpc_id: vpc id
        :type vpc_id: str
        :param ep_id: 企业项目id
        :type ep_id: str
        :param is_delegated: 资源是否已托管
        :type is_delegated: bool
        """
        
        

        self._provider = None
        self._type = None
        self._limit = None
        self._marker = None
        self._resource_id_list = None
        self._name = None
        self._region_id = None
        self._az_id = None
        self._ip_type = None
        self._ip = None
        self._status = None
        self._agent_state = None
        self._image_name = None
        self._os_type = None
        self._tag = None
        self._tag_key = None
        self._group_id = None
        self._component_id = None
        self._application_id = None
        self._cce_cluster_id = None
        self._vpc_id = None
        self._ep_id = None
        self._is_delegated = None
        self.discriminator = None

        self.provider = provider
        self.type = type
        self.limit = limit
        if marker is not None:
            self.marker = marker
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if az_id is not None:
            self.az_id = az_id
        if ip_type is not None:
            self.ip_type = ip_type
        if ip is not None:
            self.ip = ip
        if status is not None:
            self.status = status
        if agent_state is not None:
            self.agent_state = agent_state
        if image_name is not None:
            self.image_name = image_name
        if os_type is not None:
            self.os_type = os_type
        if tag is not None:
            self.tag = tag
        if tag_key is not None:
            self.tag_key = tag_key
        if group_id is not None:
            self.group_id = group_id
        if component_id is not None:
            self.component_id = component_id
        if application_id is not None:
            self.application_id = application_id
        if cce_cluster_id is not None:
            self.cce_cluster_id = cce_cluster_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if ep_id is not None:
            self.ep_id = ep_id
        if is_delegated is not None:
            self.is_delegated = is_delegated

    @property
    def provider(self):
        """Gets the provider of this ListResourceRequest.

        云服务名称

        :return: The provider of this ListResourceRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListResourceRequest.

        云服务名称

        :param provider: The provider of this ListResourceRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ListResourceRequest.

        资源类型名称

        :return: The type of this ListResourceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListResourceRequest.

        资源类型名称

        :param type: The type of this ListResourceRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListResourceRequest.

        最大的返回数量

        :return: The limit of this ListResourceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceRequest.

        最大的返回数量

        :param limit: The limit of this ListResourceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResourceRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListResourceRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResourceRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListResourceRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def resource_id_list(self):
        """Gets the resource_id_list of this ListResourceRequest.

        资源id列表

        :return: The resource_id_list of this ListResourceRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        """Sets the resource_id_list of this ListResourceRequest.

        资源id列表

        :param resource_id_list: The resource_id_list of this ListResourceRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name(self):
        """Gets the name of this ListResourceRequest.

        名称

        :return: The name of this ListResourceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListResourceRequest.

        名称

        :param name: The name of this ListResourceRequest.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        """Gets the region_id of this ListResourceRequest.

        region id

        :return: The region_id of this ListResourceRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListResourceRequest.

        region id

        :param region_id: The region_id of this ListResourceRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_id(self):
        """Gets the az_id of this ListResourceRequest.

        az id

        :return: The az_id of this ListResourceRequest.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        """Sets the az_id of this ListResourceRequest.

        az id

        :param az_id: The az_id of this ListResourceRequest.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def ip_type(self):
        """Gets the ip_type of this ListResourceRequest.

        ip类型，fixed：内网IP，floating：弹性公网IP

        :return: The ip_type of this ListResourceRequest.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this ListResourceRequest.

        ip类型，fixed：内网IP，floating：弹性公网IP

        :param ip_type: The ip_type of this ListResourceRequest.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip(self):
        """Gets the ip of this ListResourceRequest.

        ip

        :return: The ip of this ListResourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListResourceRequest.

        ip

        :param ip: The ip of this ListResourceRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        """Gets the status of this ListResourceRequest.

        资源状态

        :return: The status of this ListResourceRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListResourceRequest.

        资源状态

        :param status: The status of this ListResourceRequest.
        :type status: str
        """
        self._status = status

    @property
    def agent_state(self):
        """Gets the agent_state of this ListResourceRequest.

        agent状态

        :return: The agent_state of this ListResourceRequest.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        """Sets the agent_state of this ListResourceRequest.

        agent状态

        :param agent_state: The agent_state of this ListResourceRequest.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def image_name(self):
        """Gets the image_name of this ListResourceRequest.

        镜像名称，模糊匹配

        :return: The image_name of this ListResourceRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListResourceRequest.

        镜像名称，模糊匹配

        :param image_name: The image_name of this ListResourceRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        """Gets the os_type of this ListResourceRequest.

        系统类型

        :return: The os_type of this ListResourceRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListResourceRequest.

        系统类型

        :param os_type: The os_type of this ListResourceRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def tag(self):
        """Gets the tag of this ListResourceRequest.

        标签的值

        :return: The tag of this ListResourceRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListResourceRequest.

        标签的值

        :param tag: The tag of this ListResourceRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def tag_key(self):
        """Gets the tag_key of this ListResourceRequest.

        标签的key

        :return: The tag_key of this ListResourceRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this ListResourceRequest.

        标签的key

        :param tag_key: The tag_key of this ListResourceRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def group_id(self):
        """Gets the group_id of this ListResourceRequest.

        分组id

        :return: The group_id of this ListResourceRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListResourceRequest.

        分组id

        :param group_id: The group_id of this ListResourceRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def component_id(self):
        """Gets the component_id of this ListResourceRequest.

        组件id

        :return: The component_id of this ListResourceRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListResourceRequest.

        组件id

        :param component_id: The component_id of this ListResourceRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        """Gets the application_id of this ListResourceRequest.

        应用id

        :return: The application_id of this ListResourceRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListResourceRequest.

        应用id

        :param application_id: The application_id of this ListResourceRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def cce_cluster_id(self):
        """Gets the cce_cluster_id of this ListResourceRequest.

        cce集群id

        :return: The cce_cluster_id of this ListResourceRequest.
        :rtype: str
        """
        return self._cce_cluster_id

    @cce_cluster_id.setter
    def cce_cluster_id(self, cce_cluster_id):
        """Sets the cce_cluster_id of this ListResourceRequest.

        cce集群id

        :param cce_cluster_id: The cce_cluster_id of this ListResourceRequest.
        :type cce_cluster_id: str
        """
        self._cce_cluster_id = cce_cluster_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListResourceRequest.

        vpc id

        :return: The vpc_id of this ListResourceRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListResourceRequest.

        vpc id

        :param vpc_id: The vpc_id of this ListResourceRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def ep_id(self):
        """Gets the ep_id of this ListResourceRequest.

        企业项目id

        :return: The ep_id of this ListResourceRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ListResourceRequest.

        企业项目id

        :param ep_id: The ep_id of this ListResourceRequest.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def is_delegated(self):
        """Gets the is_delegated of this ListResourceRequest.

        资源是否已托管

        :return: The is_delegated of this ListResourceRequest.
        :rtype: bool
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        """Sets the is_delegated of this ListResourceRequest.

        资源是否已托管

        :param is_delegated: The is_delegated of this ListResourceRequest.
        :type is_delegated: bool
        """
        self._is_delegated = is_delegated

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
        if not isinstance(other, ListResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
