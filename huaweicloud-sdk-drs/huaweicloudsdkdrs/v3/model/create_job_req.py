# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bind_eip': 'bool',
        'db_use_type': 'str',
        'name': 'str',
        'description': 'str',
        'engine_type': 'str',
        'is_target_readonly': 'bool',
        'job_direction': 'str',
        'multi_write': 'bool',
        'net_type': 'str',
        'node_num': 'int',
        'node_type': 'str',
        'source_endpoint': 'Endpoint',
        'target_endpoint': 'Endpoint',
        'tags': 'list[ResourceTag]',
        'task_type': 'str',
        'customize_sutnet_id': 'str',
        'product_id': 'str',
        'sys_tags': 'list[ResourceTag]',
        'expired_days': 'str',
        'master_az': 'str',
        'slave_az': 'str'
    }

    attribute_map = {
        'bind_eip': 'bind_eip',
        'db_use_type': 'db_use_type',
        'name': 'name',
        'description': 'description',
        'engine_type': 'engine_type',
        'is_target_readonly': 'is_target_readonly',
        'job_direction': 'job_direction',
        'multi_write': 'multi_write',
        'net_type': 'net_type',
        'node_num': 'node_num',
        'node_type': 'node_type',
        'source_endpoint': 'source_endpoint',
        'target_endpoint': 'target_endpoint',
        'tags': 'tags',
        'task_type': 'task_type',
        'customize_sutnet_id': 'customize_sutnet_id',
        'product_id': 'product_id',
        'sys_tags': 'sys_tags',
        'expired_days': 'expired_days',
        'master_az': 'master_az',
        'slave_az': 'slave_az'
    }

    def __init__(self, bind_eip=None, db_use_type=None, name=None, description=None, engine_type=None, is_target_readonly=None, job_direction=None, multi_write=None, net_type=None, node_num=None, node_type=None, source_endpoint=None, target_endpoint=None, tags=None, task_type=None, customize_sutnet_id=None, product_id=None, sys_tags=None, expired_days=None, master_az=None, slave_az=None):
        """CreateJobReq

        The model defined in huaweicloud sdk

        :param bind_eip: 是否绑定eip，网络类型为eip时必填且为true
        :type bind_eip: bool
        :param db_use_type: 迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备
        :type db_use_type: str
        :param name: 任务名称，约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。
        :type name: str
        :param description: 任务描述。  **约束**：任务描述不能超过256位，且不能包含!&lt;&gt;&amp;&#39;\&quot;\\特殊字符。
        :type description: str
        :param engine_type: 引擎类型 - mysql：迁移，同步使用 - mongodb：迁移使用 - cloudDataGuard-mysql：灾备使用 - gaussdbv5，postgresql：同步使用
        :type engine_type: str
        :param is_target_readonly: 指定目标实例是否限制为只读，MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。
        :type is_target_readonly: bool
        :param job_direction: 迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建
        :type job_direction: str
        :param multi_write: - db_use_type 是cloudDataGuard时，必填，灾备类型是双主灾备时 muti_write取值true, 否则为false。 - db_use_type 是其他类型时，muti_write是非必选参数
        :type multi_write: bool
        :param net_type: 网络类型
        :type net_type: str
        :param node_num: 节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填，[1-32]，MySQL双主灾备时会默认设置为2。
        :type node_num: int
        :param node_type: 规格类型。
        :type node_type: str
        :param source_endpoint: 
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param target_endpoint: 
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param tags: 标签信息。
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        :param task_type: 迁移模式，FULL_TRANS 全量,FULL_INCR_TRANS 全量+增量,INCR_TRANS 增量，灾备场景单主灾备仅支持全量加增量（FULL_INCR_TRANS）
        :type task_type: str
        :param customize_sutnet_id: DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID，UUID格式。
        :type customize_sutnet_id: str
        :param product_id: 产品id。
        :type product_id: str
        :param sys_tags: 企业项目，不填默认为default，key值必须为_sys_enterprise_project_id，value为企业项目ID，只能有一个企业项目。
        :type sys_tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        :param expired_days: 任务处于异常状态一段时间后，将会自动结束，单位为天。(范围14-100)，不传默认为14天。
        :type expired_days: str
        :param master_az: 主备任务主任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka
        :type master_az: str
        :param slave_az: 主备任务备任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka
        :type slave_az: str
        """
        
        

        self._bind_eip = None
        self._db_use_type = None
        self._name = None
        self._description = None
        self._engine_type = None
        self._is_target_readonly = None
        self._job_direction = None
        self._multi_write = None
        self._net_type = None
        self._node_num = None
        self._node_type = None
        self._source_endpoint = None
        self._target_endpoint = None
        self._tags = None
        self._task_type = None
        self._customize_sutnet_id = None
        self._product_id = None
        self._sys_tags = None
        self._expired_days = None
        self._master_az = None
        self._slave_az = None
        self.discriminator = None

        if bind_eip is not None:
            self.bind_eip = bind_eip
        self.db_use_type = db_use_type
        self.name = name
        if description is not None:
            self.description = description
        self.engine_type = engine_type
        if is_target_readonly is not None:
            self.is_target_readonly = is_target_readonly
        self.job_direction = job_direction
        if multi_write is not None:
            self.multi_write = multi_write
        self.net_type = net_type
        if node_num is not None:
            self.node_num = node_num
        self.node_type = node_type
        self.source_endpoint = source_endpoint
        self.target_endpoint = target_endpoint
        if tags is not None:
            self.tags = tags
        self.task_type = task_type
        self.customize_sutnet_id = customize_sutnet_id
        if product_id is not None:
            self.product_id = product_id
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if expired_days is not None:
            self.expired_days = expired_days
        if master_az is not None:
            self.master_az = master_az
        if slave_az is not None:
            self.slave_az = slave_az

    @property
    def bind_eip(self):
        """Gets the bind_eip of this CreateJobReq.

        是否绑定eip，网络类型为eip时必填且为true

        :return: The bind_eip of this CreateJobReq.
        :rtype: bool
        """
        return self._bind_eip

    @bind_eip.setter
    def bind_eip(self, bind_eip):
        """Sets the bind_eip of this CreateJobReq.

        是否绑定eip，网络类型为eip时必填且为true

        :param bind_eip: The bind_eip of this CreateJobReq.
        :type bind_eip: bool
        """
        self._bind_eip = bind_eip

    @property
    def db_use_type(self):
        """Gets the db_use_type of this CreateJobReq.

        迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :return: The db_use_type of this CreateJobReq.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this CreateJobReq.

        迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :param db_use_type: The db_use_type of this CreateJobReq.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def name(self):
        """Gets the name of this CreateJobReq.

        任务名称，约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。

        :return: The name of this CreateJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateJobReq.

        任务名称，约束：任务名称在4位到50位之间，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。

        :param name: The name of this CreateJobReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateJobReq.

        任务描述。  **约束**：任务描述不能超过256位，且不能包含!<>&'\"\\特殊字符。

        :return: The description of this CreateJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateJobReq.

        任务描述。  **约束**：任务描述不能超过256位，且不能包含!<>&'\"\\特殊字符。

        :param description: The description of this CreateJobReq.
        :type description: str
        """
        self._description = description

    @property
    def engine_type(self):
        """Gets the engine_type of this CreateJobReq.

        引擎类型 - mysql：迁移，同步使用 - mongodb：迁移使用 - cloudDataGuard-mysql：灾备使用 - gaussdbv5，postgresql：同步使用

        :return: The engine_type of this CreateJobReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this CreateJobReq.

        引擎类型 - mysql：迁移，同步使用 - mongodb：迁移使用 - cloudDataGuard-mysql：灾备使用 - gaussdbv5，postgresql：同步使用

        :param engine_type: The engine_type of this CreateJobReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def is_target_readonly(self):
        """Gets the is_target_readonly of this CreateJobReq.

        指定目标实例是否限制为只读，MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。

        :return: The is_target_readonly of this CreateJobReq.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        """Sets the is_target_readonly of this CreateJobReq.

        指定目标实例是否限制为只读，MySQL迁移和灾备，且job_direction为up时设置有效。（灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true）。

        :param is_target_readonly: The is_target_readonly of this CreateJobReq.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def job_direction(self):
        """Gets the job_direction of this CreateJobReq.

        迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建

        :return: The job_direction of this CreateJobReq.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this CreateJobReq.

        迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建

        :param job_direction: The job_direction of this CreateJobReq.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def multi_write(self):
        """Gets the multi_write of this CreateJobReq.

        - db_use_type 是cloudDataGuard时，必填，灾备类型是双主灾备时 muti_write取值true, 否则为false。 - db_use_type 是其他类型时，muti_write是非必选参数

        :return: The multi_write of this CreateJobReq.
        :rtype: bool
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        """Sets the multi_write of this CreateJobReq.

        - db_use_type 是cloudDataGuard时，必填，灾备类型是双主灾备时 muti_write取值true, 否则为false。 - db_use_type 是其他类型时，muti_write是非必选参数

        :param multi_write: The multi_write of this CreateJobReq.
        :type multi_write: bool
        """
        self._multi_write = multi_write

    @property
    def net_type(self):
        """Gets the net_type of this CreateJobReq.

        网络类型

        :return: The net_type of this CreateJobReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this CreateJobReq.

        网络类型

        :param net_type: The net_type of this CreateJobReq.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def node_num(self):
        """Gets the node_num of this CreateJobReq.

        节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填，[1-32]，MySQL双主灾备时会默认设置为2。

        :return: The node_num of this CreateJobReq.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this CreateJobReq.

        节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填，[1-32]，MySQL双主灾备时会默认设置为2。

        :param node_num: The node_num of this CreateJobReq.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_type(self):
        """Gets the node_type of this CreateJobReq.

        规格类型。

        :return: The node_type of this CreateJobReq.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this CreateJobReq.

        规格类型。

        :param node_type: The node_type of this CreateJobReq.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this CreateJobReq.


        :return: The source_endpoint of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this CreateJobReq.


        :param source_endpoint: The source_endpoint of this CreateJobReq.
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this CreateJobReq.


        :return: The target_endpoint of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this CreateJobReq.


        :param target_endpoint: The target_endpoint of this CreateJobReq.
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._target_endpoint = target_endpoint

    @property
    def tags(self):
        """Gets the tags of this CreateJobReq.

        标签信息。

        :return: The tags of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateJobReq.

        标签信息。

        :param tags: The tags of this CreateJobReq.
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def task_type(self):
        """Gets the task_type of this CreateJobReq.

        迁移模式，FULL_TRANS 全量,FULL_INCR_TRANS 全量+增量,INCR_TRANS 增量，灾备场景单主灾备仅支持全量加增量（FULL_INCR_TRANS）

        :return: The task_type of this CreateJobReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateJobReq.

        迁移模式，FULL_TRANS 全量,FULL_INCR_TRANS 全量+增量,INCR_TRANS 增量，灾备场景单主灾备仅支持全量加增量（FULL_INCR_TRANS）

        :param task_type: The task_type of this CreateJobReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def customize_sutnet_id(self):
        """Gets the customize_sutnet_id of this CreateJobReq.

        DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :return: The customize_sutnet_id of this CreateJobReq.
        :rtype: str
        """
        return self._customize_sutnet_id

    @customize_sutnet_id.setter
    def customize_sutnet_id(self, customize_sutnet_id):
        """Sets the customize_sutnet_id of this CreateJobReq.

        DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID，UUID格式。

        :param customize_sutnet_id: The customize_sutnet_id of this CreateJobReq.
        :type customize_sutnet_id: str
        """
        self._customize_sutnet_id = customize_sutnet_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateJobReq.

        产品id。

        :return: The product_id of this CreateJobReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateJobReq.

        产品id。

        :param product_id: The product_id of this CreateJobReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def sys_tags(self):
        """Gets the sys_tags of this CreateJobReq.

        企业项目，不填默认为default，key值必须为_sys_enterprise_project_id，value为企业项目ID，只能有一个企业项目。

        :return: The sys_tags of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this CreateJobReq.

        企业项目，不填默认为default，key值必须为_sys_enterprise_project_id，value为企业项目ID，只能有一个企业项目。

        :param sys_tags: The sys_tags of this CreateJobReq.
        :type sys_tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        self._sys_tags = sys_tags

    @property
    def expired_days(self):
        """Gets the expired_days of this CreateJobReq.

        任务处于异常状态一段时间后，将会自动结束，单位为天。(范围14-100)，不传默认为14天。

        :return: The expired_days of this CreateJobReq.
        :rtype: str
        """
        return self._expired_days

    @expired_days.setter
    def expired_days(self, expired_days):
        """Sets the expired_days of this CreateJobReq.

        任务处于异常状态一段时间后，将会自动结束，单位为天。(范围14-100)，不传默认为14天。

        :param expired_days: The expired_days of this CreateJobReq.
        :type expired_days: str
        """
        self._expired_days = expired_days

    @property
    def master_az(self):
        """Gets the master_az of this CreateJobReq.

        主备任务主任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka

        :return: The master_az of this CreateJobReq.
        :rtype: str
        """
        return self._master_az

    @master_az.setter
    def master_az(self, master_az):
        """Sets the master_az of this CreateJobReq.

        主备任务主任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka

        :param master_az: The master_az of this CreateJobReq.
        :type master_az: str
        """
        self._master_az = master_az

    @property
    def slave_az(self):
        """Gets the slave_az of this CreateJobReq.

        主备任务备任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka

        :return: The slave_az of this CreateJobReq.
        :rtype: str
        """
        return self._slave_az

    @slave_az.setter
    def slave_az(self, slave_az):
        """Sets the slave_az of this CreateJobReq.

        主备任务备任务所在可用区code，可以通过查询规格未售罄的可用区接口获取 - master_az和slave_az同时填写时生效 - 目前支持mysql，gaussdbv5ha-to-kafka

        :param slave_az: The slave_az of this CreateJobReq.
        :type slave_az: str
        """
        self._slave_az = slave_az

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
        if not isinstance(other, CreateJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
