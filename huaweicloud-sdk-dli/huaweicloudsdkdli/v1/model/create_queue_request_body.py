# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueueRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'queue_type': 'str',
        'description': 'str',
        'cu_count': 'int',
        'charging_mode': 'int',
        'enterprise_project_id': 'str',
        'platform': 'str',
        'resource_mode': 'int',
        'labels': 'list[object]',
        'feature': 'str',
        'tags': 'list[Tag]',
        'elastic_resource_pool_name': 'str',
        'properties': 'CreateQueueRequestBodyProperties',
        'engine': 'str'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'queue_type': 'queue_type',
        'description': 'description',
        'cu_count': 'cu_count',
        'charging_mode': 'charging_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'platform': 'platform',
        'resource_mode': 'resource_mode',
        'labels': 'labels',
        'feature': 'feature',
        'tags': 'tags',
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'properties': 'properties',
        'engine': 'engine'
    }

    def __init__(self, queue_name=None, queue_type=None, description=None, cu_count=None, charging_mode=None, enterprise_project_id=None, platform=None, resource_mode=None, labels=None, feature=None, tags=None, elastic_resource_pool_name=None, properties=None, engine=None):
        r"""CreateQueueRequestBody

        The model defined in huaweicloud sdk

        :param queue_name: 新建的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。\\n说明： \\n队列名称不区分大小写，系统会自动转换为小写。
        :type queue_name: str
        :param queue_type: 队列的类型,。有如下两种类型： sql general 如果不指定，默认为sql。
        :type queue_type: str
        :param description: 队列的描述信息。
        :type description: str
        :param cu_count: 队列的实际CU。
        :type cu_count: int
        :param charging_mode: 队列的收费模式。只能设置为“1”，表示按照CU时收费。
        :type charging_mode: int
        :param enterprise_project_id: 企业项目ID，“0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。
        :type enterprise_project_id: str
        :param platform: 队列计算资源的cpu架构。
        :type platform: str
        :param resource_mode: 队列资源模式。支持以下两种类型：0：共享资源模式1：专属资源模式
        :type resource_mode: int
        :param labels: 创建队列的标签信息，目前包括队列是否跨AZ的标签信息（Json字符串），且只支持值为“2”，即创建一个计算资源分布在2个可用区的双AZ队列
        :type labels: list[object]
        :param feature: 队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。
        :type feature: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param elastic_resource_pool_name: 新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。
        :type elastic_resource_pool_name: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkdli.v1.CreateQueueRequestBodyProperties`
        :param engine: 只有在queue_type是sql条件下才可配置，默认是spark。可以选择spark引擎或hetuEngin。
        :type engine: str
        """
        
        

        self._queue_name = None
        self._queue_type = None
        self._description = None
        self._cu_count = None
        self._charging_mode = None
        self._enterprise_project_id = None
        self._platform = None
        self._resource_mode = None
        self._labels = None
        self._feature = None
        self._tags = None
        self._elastic_resource_pool_name = None
        self._properties = None
        self._engine = None
        self.discriminator = None

        self.queue_name = queue_name
        if queue_type is not None:
            self.queue_type = queue_type
        if description is not None:
            self.description = description
        self.cu_count = cu_count
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if platform is not None:
            self.platform = platform
        if resource_mode is not None:
            self.resource_mode = resource_mode
        if labels is not None:
            self.labels = labels
        if feature is not None:
            self.feature = feature
        if tags is not None:
            self.tags = tags
        if elastic_resource_pool_name is not None:
            self.elastic_resource_pool_name = elastic_resource_pool_name
        if properties is not None:
            self.properties = properties
        if engine is not None:
            self.engine = engine

    @property
    def queue_name(self):
        r"""Gets the queue_name of this CreateQueueRequestBody.

        新建的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。\\n说明： \\n队列名称不区分大小写，系统会自动转换为小写。

        :return: The queue_name of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this CreateQueueRequestBody.

        新建的队列名称，名称只能包含数字、英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。\\n说明： \\n队列名称不区分大小写，系统会自动转换为小写。

        :param queue_name: The queue_name of this CreateQueueRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def queue_type(self):
        r"""Gets the queue_type of this CreateQueueRequestBody.

        队列的类型,。有如下两种类型： sql general 如果不指定，默认为sql。

        :return: The queue_type of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        r"""Sets the queue_type of this CreateQueueRequestBody.

        队列的类型,。有如下两种类型： sql general 如果不指定，默认为sql。

        :param queue_type: The queue_type of this CreateQueueRequestBody.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def description(self):
        r"""Gets the description of this CreateQueueRequestBody.

        队列的描述信息。

        :return: The description of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateQueueRequestBody.

        队列的描述信息。

        :param description: The description of this CreateQueueRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def cu_count(self):
        r"""Gets the cu_count of this CreateQueueRequestBody.

        队列的实际CU。

        :return: The cu_count of this CreateQueueRequestBody.
        :rtype: int
        """
        return self._cu_count

    @cu_count.setter
    def cu_count(self, cu_count):
        r"""Sets the cu_count of this CreateQueueRequestBody.

        队列的实际CU。

        :param cu_count: The cu_count of this CreateQueueRequestBody.
        :type cu_count: int
        """
        self._cu_count = cu_count

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateQueueRequestBody.

        队列的收费模式。只能设置为“1”，表示按照CU时收费。

        :return: The charging_mode of this CreateQueueRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateQueueRequestBody.

        队列的收费模式。只能设置为“1”，表示按照CU时收费。

        :param charging_mode: The charging_mode of this CreateQueueRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateQueueRequestBody.

        企业项目ID，“0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :return: The enterprise_project_id of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateQueueRequestBody.

        企业项目ID，“0”表示default，即默认的企业项目。 说明： 开通了企业管理服务的用户可设置该参数绑定指定的项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateQueueRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def platform(self):
        r"""Gets the platform of this CreateQueueRequestBody.

        队列计算资源的cpu架构。

        :return: The platform of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this CreateQueueRequestBody.

        队列计算资源的cpu架构。

        :param platform: The platform of this CreateQueueRequestBody.
        :type platform: str
        """
        self._platform = platform

    @property
    def resource_mode(self):
        r"""Gets the resource_mode of this CreateQueueRequestBody.

        队列资源模式。支持以下两种类型：0：共享资源模式1：专属资源模式

        :return: The resource_mode of this CreateQueueRequestBody.
        :rtype: int
        """
        return self._resource_mode

    @resource_mode.setter
    def resource_mode(self, resource_mode):
        r"""Sets the resource_mode of this CreateQueueRequestBody.

        队列资源模式。支持以下两种类型：0：共享资源模式1：专属资源模式

        :param resource_mode: The resource_mode of this CreateQueueRequestBody.
        :type resource_mode: int
        """
        self._resource_mode = resource_mode

    @property
    def labels(self):
        r"""Gets the labels of this CreateQueueRequestBody.

        创建队列的标签信息，目前包括队列是否跨AZ的标签信息（Json字符串），且只支持值为“2”，即创建一个计算资源分布在2个可用区的双AZ队列

        :return: The labels of this CreateQueueRequestBody.
        :rtype: list[object]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateQueueRequestBody.

        创建队列的标签信息，目前包括队列是否跨AZ的标签信息（Json字符串），且只支持值为“2”，即创建一个计算资源分布在2个可用区的双AZ队列

        :param labels: The labels of this CreateQueueRequestBody.
        :type labels: list[object]
        """
        self._labels = labels

    @property
    def feature(self):
        r"""Gets the feature of this CreateQueueRequestBody.

        队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。

        :return: The feature of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this CreateQueueRequestBody.

        队列特性。支持以下两种类型：basic：基础型ai：AI增强型（仅SQL的x86_64专属队列支持选择）默认值为“basic”。

        :param feature: The feature of this CreateQueueRequestBody.
        :type feature: str
        """
        self._feature = feature

    @property
    def tags(self):
        r"""Gets the tags of this CreateQueueRequestBody.

        标签

        :return: The tags of this CreateQueueRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateQueueRequestBody.

        标签

        :param tags: The tags of this CreateQueueRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this CreateQueueRequestBody.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :return: The elastic_resource_pool_name of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this CreateQueueRequestBody.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this CreateQueueRequestBody.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def properties(self):
        r"""Gets the properties of this CreateQueueRequestBody.

        :return: The properties of this CreateQueueRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.CreateQueueRequestBodyProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this CreateQueueRequestBody.

        :param properties: The properties of this CreateQueueRequestBody.
        :type properties: :class:`huaweicloudsdkdli.v1.CreateQueueRequestBodyProperties`
        """
        self._properties = properties

    @property
    def engine(self):
        r"""Gets the engine of this CreateQueueRequestBody.

        只有在queue_type是sql条件下才可配置，默认是spark。可以选择spark引擎或hetuEngin。

        :return: The engine of this CreateQueueRequestBody.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateQueueRequestBody.

        只有在queue_type是sql条件下才可配置，默认是spark。可以选择spark引擎或hetuEngin。

        :param engine: The engine of this CreateQueueRequestBody.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, CreateQueueRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
