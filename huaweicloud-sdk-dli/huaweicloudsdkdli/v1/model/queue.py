# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Queue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_id': 'int',
        'queue_name': 'str',
        'description': 'str',
        'owner': 'str',
        'create_time': 'int',
        'queue_type': 'str',
        'cu_count': 'int',
        'charging_mode': 'int',
        'resource_id': 'str',
        'enterprise_project_id': 'str',
        'cidr_in_vpc': 'str',
        'cidr_in_mgntsubnet': 'str',
        'cidr_in_subnet': 'str',
        'resource_mode': 'int',
        'platform': 'str',
        'is_restarting': 'bool',
        'labels': 'str',
        'feature': 'str',
        'resource_type': 'str',
        'cu_spec': 'int',
        'cu_scale_out_limit': 'int',
        'cu_scale_in_limit': 'int',
        'elastic_resource_pool_name': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'queue_name': 'queue_name',
        'description': 'description',
        'owner': 'owner',
        'create_time': 'create_time',
        'queue_type': 'queue_type',
        'cu_count': 'cu_count',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'enterprise_project_id': 'enterprise_project_id',
        'cidr_in_vpc': 'cidr_in_vpc',
        'cidr_in_mgntsubnet': 'cidr_in_mgntsubnet',
        'cidr_in_subnet': 'cidr_in_subnet',
        'resource_mode': 'resource_mode',
        'platform': 'platform',
        'is_restarting': 'is_restarting',
        'labels': 'labels',
        'feature': 'feature',
        'resource_type': 'resource_type',
        'cu_spec': 'cu_spec',
        'cu_scale_out_limit': 'cu_scale_out_limit',
        'cu_scale_in_limit': 'cu_scale_in_limit',
        'elastic_resource_pool_name': 'elastic_resource_pool_name'
    }

    def __init__(self, queue_id=None, queue_name=None, description=None, owner=None, create_time=None, queue_type=None, cu_count=None, charging_mode=None, resource_id=None, enterprise_project_id=None, cidr_in_vpc=None, cidr_in_mgntsubnet=None, cidr_in_subnet=None, resource_mode=None, platform=None, is_restarting=None, labels=None, feature=None, resource_type=None, cu_spec=None, cu_scale_out_limit=None, cu_scale_in_limit=None, elastic_resource_pool_name=None):
        """Queue

        The model defined in huaweicloud sdk

        :param queue_id: 队列ID。
        :type queue_id: int
        :param queue_name: 队列名称。
        :type queue_name: str
        :param description: 队列描述信息。
        :type description: str
        :param owner: 创建队列的用户。
        :type owner: str
        :param create_time: 创建队列的时间。是单位为“毫秒”的时间戳。
        :type create_time: int
        :param queue_type: 队列的类型。： sql general all 如果不指定，默认为“sql”。
        :type queue_type: str
        :param cu_count: 队列的实际CU。
        :type cu_count: int
        :param charging_mode: 队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。
        :type charging_mode: int
        :param resource_id: 队列的资源ID。
        :type resource_id: str
        :param enterprise_project_id: 企业项目ID。0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。
        :type enterprise_project_id: str
        :param cidr_in_vpc: 队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。
        :type cidr_in_vpc: str
        :param cidr_in_mgntsubnet: 管理子网的网段。
        :type cidr_in_mgntsubnet: str
        :param cidr_in_subnet: 子网网段。
        :type cidr_in_subnet: str
        :param resource_mode: 队列类型。 0：共享队列 1：专属队列
        :type resource_mode: int
        :param platform: 队列计算资源的cpu架构。
        :type platform: str
        :param is_restarting: 是否在重启状态。默认值为“false”。
        :type is_restarting: bool
        :param labels: 队列的标签信息，目前只支持设置跨az配置，multi_az&#x3D;2
        :type labels: str
        :param feature: 队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。
        :type feature: str
        :param resource_type: 队列所属资源类型, vm或container。
        :type resource_type: str
        :param cu_spec: 队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。
        :type cu_spec: int
        :param cu_scale_out_limit: 当前队列弹性扩缩容的CU值上限。
        :type cu_scale_out_limit: int
        :param cu_scale_in_limit: 当前队列弹性扩缩容的CU值下限。
        :type cu_scale_in_limit: int
        :param elastic_resource_pool_name: 弹性资源池名称。
        :type elastic_resource_pool_name: str
        """
        
        

        self._queue_id = None
        self._queue_name = None
        self._description = None
        self._owner = None
        self._create_time = None
        self._queue_type = None
        self._cu_count = None
        self._charging_mode = None
        self._resource_id = None
        self._enterprise_project_id = None
        self._cidr_in_vpc = None
        self._cidr_in_mgntsubnet = None
        self._cidr_in_subnet = None
        self._resource_mode = None
        self._platform = None
        self._is_restarting = None
        self._labels = None
        self._feature = None
        self._resource_type = None
        self._cu_spec = None
        self._cu_scale_out_limit = None
        self._cu_scale_in_limit = None
        self._elastic_resource_pool_name = None
        self.discriminator = None

        if queue_id is not None:
            self.queue_id = queue_id
        if queue_name is not None:
            self.queue_name = queue_name
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if create_time is not None:
            self.create_time = create_time
        if queue_type is not None:
            self.queue_type = queue_type
        if cu_count is not None:
            self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        if cidr_in_mgntsubnet is not None:
            self.cidr_in_mgntsubnet = cidr_in_mgntsubnet
        if cidr_in_subnet is not None:
            self.cidr_in_subnet = cidr_in_subnet
        if resource_mode is not None:
            self.resource_mode = resource_mode
        if platform is not None:
            self.platform = platform
        if is_restarting is not None:
            self.is_restarting = is_restarting
        if labels is not None:
            self.labels = labels
        if feature is not None:
            self.feature = feature
        if resource_type is not None:
            self.resource_type = resource_type
        if cu_spec is not None:
            self.cu_spec = cu_spec
        if cu_scale_out_limit is not None:
            self.cu_scale_out_limit = cu_scale_out_limit
        if cu_scale_in_limit is not None:
            self.cu_scale_in_limit = cu_scale_in_limit
        if elastic_resource_pool_name is not None:
            self.elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def queue_id(self):
        """Gets the queue_id of this Queue.

        队列ID。

        :return: The queue_id of this Queue.
        :rtype: int
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this Queue.

        队列ID。

        :param queue_id: The queue_id of this Queue.
        :type queue_id: int
        """
        self._queue_id = queue_id

    @property
    def queue_name(self):
        """Gets the queue_name of this Queue.

        队列名称。

        :return: The queue_name of this Queue.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this Queue.

        队列名称。

        :param queue_name: The queue_name of this Queue.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def description(self):
        """Gets the description of this Queue.

        队列描述信息。

        :return: The description of this Queue.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Queue.

        队列描述信息。

        :param description: The description of this Queue.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        """Gets the owner of this Queue.

        创建队列的用户。

        :return: The owner of this Queue.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Queue.

        创建队列的用户。

        :param owner: The owner of this Queue.
        :type owner: str
        """
        self._owner = owner

    @property
    def create_time(self):
        """Gets the create_time of this Queue.

        创建队列的时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this Queue.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Queue.

        创建队列的时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this Queue.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def queue_type(self):
        """Gets the queue_type of this Queue.

        队列的类型。： sql general all 如果不指定，默认为“sql”。

        :return: The queue_type of this Queue.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this Queue.

        队列的类型。： sql general all 如果不指定，默认为“sql”。

        :param queue_type: The queue_type of this Queue.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def cu_count(self):
        """Gets the cu_count of this Queue.

        队列的实际CU。

        :return: The cu_count of this Queue.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        """Sets the cu_count of this Queue.

        队列的实际CU。

        :param cu_count: The cu_count of this Queue.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this Queue.

        队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。

        :return: The charging_mode of this Queue.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this Queue.

        队列的收费模式。 “1”表示按照CU时收费。 “2”表示按照包年包月收费。

        :param charging_mode: The charging_mode of this Queue.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        """Gets the resource_id of this Queue.

        队列的资源ID。

        :return: The resource_id of this Queue.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Queue.

        队列的资源ID。

        :param resource_id: The resource_id of this Queue.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Queue.

        企业项目ID。0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :return: The enterprise_project_id of this Queue.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Queue.

        企业项目ID。0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :param enterprise_project_id: The enterprise_project_id of this Queue.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cidr_in_vpc(self):
        """Gets the cidr_in_vpc of this Queue.

        队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。

        :return: The cidr_in_vpc of this Queue.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        """Sets the cidr_in_vpc of this Queue.

        队列的虚拟私有云（VPC）的网段。建议使用网段：10.0.0.0/8~28，172.16.0.0/12~28，192.168.0.0/16~28。

        :param cidr_in_vpc: The cidr_in_vpc of this Queue.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def cidr_in_mgntsubnet(self):
        """Gets the cidr_in_mgntsubnet of this Queue.

        管理子网的网段。

        :return: The cidr_in_mgntsubnet of this Queue.
        :rtype: str
        """
        return self._cidr_in_mgntsubnet

    @cidr_in_mgntsubnet.setter
    def cidr_in_mgntsubnet(self, cidr_in_mgntsubnet):
        """Sets the cidr_in_mgntsubnet of this Queue.

        管理子网的网段。

        :param cidr_in_mgntsubnet: The cidr_in_mgntsubnet of this Queue.
        :type cidr_in_mgntsubnet: str
        """
        self._cidr_in_mgntsubnet = cidr_in_mgntsubnet

    @property
    def cidr_in_subnet(self):
        """Gets the cidr_in_subnet of this Queue.

        子网网段。

        :return: The cidr_in_subnet of this Queue.
        :rtype: str
        """
        return self._cidr_in_subnet

    @cidr_in_subnet.setter
    def cidr_in_subnet(self, cidr_in_subnet):
        """Sets the cidr_in_subnet of this Queue.

        子网网段。

        :param cidr_in_subnet: The cidr_in_subnet of this Queue.
        :type cidr_in_subnet: str
        """
        self._cidr_in_subnet = cidr_in_subnet

    @property
    def resource_mode(self):
        """Gets the resource_mode of this Queue.

        队列类型。 0：共享队列 1：专属队列

        :return: The resource_mode of this Queue.
        :rtype: int
        """
        return self._resource_mode

    @resource_mode.setter
    def resource_mode(self, resource_mode):
        """Sets the resource_mode of this Queue.

        队列类型。 0：共享队列 1：专属队列

        :param resource_mode: The resource_mode of this Queue.
        :type resource_mode: int
        """
        self._resource_mode = resource_mode

    @property
    def platform(self):
        """Gets the platform of this Queue.

        队列计算资源的cpu架构。

        :return: The platform of this Queue.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Queue.

        队列计算资源的cpu架构。

        :param platform: The platform of this Queue.
        :type platform: str
        """
        self._platform = platform

    @property
    def is_restarting(self):
        """Gets the is_restarting of this Queue.

        是否在重启状态。默认值为“false”。

        :return: The is_restarting of this Queue.
        :rtype: bool
        """
        return self._is_restarting

    @is_restarting.setter
    def is_restarting(self, is_restarting):
        """Sets the is_restarting of this Queue.

        是否在重启状态。默认值为“false”。

        :param is_restarting: The is_restarting of this Queue.
        :type is_restarting: bool
        """
        self._is_restarting = is_restarting

    @property
    def labels(self):
        """Gets the labels of this Queue.

        队列的标签信息，目前只支持设置跨az配置，multi_az=2

        :return: The labels of this Queue.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Queue.

        队列的标签信息，目前只支持设置跨az配置，multi_az=2

        :param labels: The labels of this Queue.
        :type labels: str
        """
        self._labels = labels

    @property
    def feature(self):
        """Gets the feature of this Queue.

        队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。

        :return: The feature of this Queue.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this Queue.

        队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。

        :param feature: The feature of this Queue.
        :type feature: str
        """
        self._feature = feature

    @property
    def resource_type(self):
        """Gets the resource_type of this Queue.

        队列所属资源类型, vm或container。

        :return: The resource_type of this Queue.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Queue.

        队列所属资源类型, vm或container。

        :param resource_type: The resource_type of this Queue.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def cu_spec(self):
        """Gets the cu_spec of this Queue.

        队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。

        :return: The cu_spec of this Queue.
        :rtype: int
        """
        return self._cu_spec

    @cu_spec.setter
    def cu_spec(self, cu_spec):
        """Sets the cu_spec of this Queue.

        队列的规格大小。对于包周期队列，表示包周期部分的CU值；对于按需队列，表示用户购买队列时的初始值。

        :param cu_spec: The cu_spec of this Queue.
        :type cu_spec: int
        """
        self._cu_spec = cu_spec

    @property
    def cu_scale_out_limit(self):
        """Gets the cu_scale_out_limit of this Queue.

        当前队列弹性扩缩容的CU值上限。

        :return: The cu_scale_out_limit of this Queue.
        :rtype: int
        """
        return self._cu_scale_out_limit

    @cu_scale_out_limit.setter
    def cu_scale_out_limit(self, cu_scale_out_limit):
        """Sets the cu_scale_out_limit of this Queue.

        当前队列弹性扩缩容的CU值上限。

        :param cu_scale_out_limit: The cu_scale_out_limit of this Queue.
        :type cu_scale_out_limit: int
        """
        self._cu_scale_out_limit = cu_scale_out_limit

    @property
    def cu_scale_in_limit(self):
        """Gets the cu_scale_in_limit of this Queue.

        当前队列弹性扩缩容的CU值下限。

        :return: The cu_scale_in_limit of this Queue.
        :rtype: int
        """
        return self._cu_scale_in_limit

    @cu_scale_in_limit.setter
    def cu_scale_in_limit(self, cu_scale_in_limit):
        """Sets the cu_scale_in_limit of this Queue.

        当前队列弹性扩缩容的CU值下限。

        :param cu_scale_in_limit: The cu_scale_in_limit of this Queue.
        :type cu_scale_in_limit: int
        """
        self._cu_scale_in_limit = cu_scale_in_limit

    @property
    def elastic_resource_pool_name(self):
        """Gets the elastic_resource_pool_name of this Queue.

        弹性资源池名称。

        :return: The elastic_resource_pool_name of this Queue.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        """Sets the elastic_resource_pool_name of this Queue.

        弹性资源池名称。

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this Queue.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

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
        if not isinstance(other, Queue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
