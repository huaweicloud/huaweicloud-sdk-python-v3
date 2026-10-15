# coding: utf-8

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
        'slave_az': 'str',
        'charging_mode': 'str',
        'period_order': 'PeriodOrderInfo',
        'public_ip_list': 'list[PublicIpConfig]',
        'is_open_fast_clean': 'bool'
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
        'slave_az': 'slave_az',
        'charging_mode': 'charging_mode',
        'period_order': 'period_order',
        'public_ip_list': 'public_ip_list',
        'is_open_fast_clean': 'is_open_fast_clean'
    }

    def __init__(self, bind_eip=None, db_use_type=None, name=None, description=None, engine_type=None, is_target_readonly=None, job_direction=None, multi_write=None, net_type=None, node_num=None, node_type=None, source_endpoint=None, target_endpoint=None, tags=None, task_type=None, customize_sutnet_id=None, product_id=None, sys_tags=None, expired_days=None, master_az=None, slave_az=None, charging_mode=None, period_order=None, public_ip_list=None, is_open_fast_clean=None):
        r"""CreateJobReq

        The model defined in huaweicloud sdk

        :param bind_eip: **参数解释**：  是否绑定EIP（弹性公网IP）。  **约束限制**：  网络类型为EIP时必填且为true。  **取值范围**：  - true：绑定EIP - false：不绑定EIP  **默认取值**：  不涉及
        :type bind_eip: bool
        :param db_use_type: **参数解释**：  迁移任务的业务场景类型。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及
        :type db_use_type: str
        :param name: **参数解释**：  任务名称。  **约束限制**：  - 必须以字母开头，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  长度为4-50个字符。  **默认取值**：  不涉及
        :type name: str
        :param description: **参数解释**：  任务描述。  **约束限制**：  不能超过256位，且不能包含!&lt;&gt;&amp;&#39;\&quot;特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type description: str
        :param engine_type: **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL到MySQL迁移，MySQL到MySQL同步 - mongodb：MongoDB到DDS迁移与同步 - cloudDataGuard-mysql：MySQL到MySQL灾备 - gaussdbv5：GaussDB同步 - postgresql：PostgreSQL到PostgreSQL同步 - mysql-to-kafka：MySQL到Kafka同步 - taurus-to-kafka：TaurusDB到Kafka同步 - gaussdbv5ha-to-kafka：GaussDB集中式版到Kafka同步 - oracle-to-gaussdbv5：Oracle-GaussDB分布式版 - oracle-to-gaussdbv5ha：Oracle-GaussDB集中式版 - gaussdbv5-to-oracle：GaussDB分布式版-Oracle - gaussdbv5ha-to-oracle：GaussDB集中式版-Oracle - gaussdbv5-to-kafka：GaussDB分布式版-Kafka  详细取值可参考引擎类型说明。  **默认取值**：  不涉及
        :type engine_type: str
        :param is_target_readonly: **参数解释**：  指定目标实例是否限制为只读。  **约束限制**：  - MySQL迁移和灾备，且job_direction为up时设置有效。 - 灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true。  **取值范围**：  - true：目标实例限制为只读 - false：目标实例不限制为只读  **默认取值**：  不涉及
        :type is_target_readonly: bool
        :param job_direction: **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及
        :type job_direction: str
        :param multi_write: **参数解释**：  是否为双主灾备模式。  **约束限制**：  - db_use_type为cloudDataGuard时必填。 - db_use_type为其他类型时为非必选参数。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false
        :type multi_write: bool
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及
        :type net_type: str
        :param node_num: **参数解释**：  节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填。MySQL双主灾备时会默认设置为2。  **约束限制**：  不涉及。  **取值范围**：  1-32  **默认取值**：  不涉及
        :type node_num: int
        :param node_type: **参数解释**：  DRS任务实例规格编码，决定迁移实例的计算资源大小。  **约束限制**：  不涉及。  **取值范围**：  - micro：极小规格 - small：小规格 - medium：中规格 - high：大规格 - xlarge：超大规格 - 2xlarge：极大规格  具体某种场景支持的取值可以通过查询可用的Node规格接口获取。  **默认取值**：  high
        :type node_type: str
        :param source_endpoint: 
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param target_endpoint: 
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param tags: **参数解释**：  标签信息列表，详情请参见ResourceTag对象定义。  **约束限制**：  最多添加20个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        :param task_type: **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择全量加增量（FULL_INCR_TRANS）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  FULL_INCR_TRANS
        :type task_type: str
        :param customize_sutnet_id: **参数解释**：  DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID。  **约束限制**：  UUID格式。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type customize_sutnet_id: str
        :param product_id: **参数解释**：  产品ID，用于标识包年包月任务对应的产品。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type product_id: str
        :param sys_tags: **参数解释**：  企业项目标签列表，详情请参见ResourceTag对象定义。  **约束限制**：  - 不填默认为default。 - key值必须为_sys_enterprise_project_id，value为企业项目ID。 - 只能填一个企业项目。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type sys_tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        :param expired_days: **参数解释**：  任务处于异常状态一段时间后自动结束的天数。  **约束限制**：  不涉及。  **取值范围**：  14-100  **默认取值**：  14
        :type expired_days: str
        :param master_az: **参数解释**：  主备任务主任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type master_az: str
        :param slave_az: **参数解释**：  主备任务备任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type slave_az: str
        :param charging_mode: **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  - db_use_type为migration时不支持包年包月。 - 支持的engine_type为：mysql，cloudDataGuard-mysql，postgresql，gaussdbv5ha-to-kafka。  **取值范围**：  - period：包年包月 - on_demand：按需计费  **默认取值**：  on_demand
        :type charging_mode: str
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v3.PeriodOrderInfo`
        :param public_ip_list: **参数解释**：  指定公网IP的信息列表，详情请参见PublicIpConfig对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v3.PublicIpConfig`]
        :param is_open_fast_clean: **参数解释**：  是否开启云数据库RDS for MySQL或MariaDB的Binlog快速清理。  **约束限制**：  不涉及。  **取值范围**：  - true：开启Binlog快速清理 - false：不开启Binlog快速清理  **默认取值**：  false
        :type is_open_fast_clean: bool
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
        self._charging_mode = None
        self._period_order = None
        self._public_ip_list = None
        self._is_open_fast_clean = None
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
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_order is not None:
            self.period_order = period_order
        if public_ip_list is not None:
            self.public_ip_list = public_ip_list
        if is_open_fast_clean is not None:
            self.is_open_fast_clean = is_open_fast_clean

    @property
    def bind_eip(self):
        r"""Gets the bind_eip of this CreateJobReq.

        **参数解释**：  是否绑定EIP（弹性公网IP）。  **约束限制**：  网络类型为EIP时必填且为true。  **取值范围**：  - true：绑定EIP - false：不绑定EIP  **默认取值**：  不涉及

        :return: The bind_eip of this CreateJobReq.
        :rtype: bool
        """
        return self._bind_eip

    @bind_eip.setter
    def bind_eip(self, bind_eip):
        r"""Sets the bind_eip of this CreateJobReq.

        **参数解释**：  是否绑定EIP（弹性公网IP）。  **约束限制**：  网络类型为EIP时必填且为true。  **取值范围**：  - true：绑定EIP - false：不绑定EIP  **默认取值**：  不涉及

        :param bind_eip: The bind_eip of this CreateJobReq.
        :type bind_eip: bool
        """
        self._bind_eip = bind_eip

    @property
    def db_use_type(self):
        r"""Gets the db_use_type of this CreateJobReq.

        **参数解释**：  迁移任务的业务场景类型。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :return: The db_use_type of this CreateJobReq.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        r"""Sets the db_use_type of this CreateJobReq.

        **参数解释**：  迁移任务的业务场景类型。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :param db_use_type: The db_use_type of this CreateJobReq.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def name(self):
        r"""Gets the name of this CreateJobReq.

        **参数解释**：  任务名称。  **约束限制**：  - 必须以字母开头，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  长度为4-50个字符。  **默认取值**：  不涉及

        :return: The name of this CreateJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateJobReq.

        **参数解释**：  任务名称。  **约束限制**：  - 必须以字母开头，不区分大小写，可以包含字母、数字、中划线或下划线，不能包括其他特殊字符。  **取值范围**：  长度为4-50个字符。  **默认取值**：  不涉及

        :param name: The name of this CreateJobReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateJobReq.

        **参数解释**：  任务描述。  **约束限制**：  不能超过256位，且不能包含!<>&'\"特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The description of this CreateJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateJobReq.

        **参数解释**：  任务描述。  **约束限制**：  不能超过256位，且不能包含!<>&'\"特殊字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param description: The description of this CreateJobReq.
        :type description: str
        """
        self._description = description

    @property
    def engine_type(self):
        r"""Gets the engine_type of this CreateJobReq.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL到MySQL迁移，MySQL到MySQL同步 - mongodb：MongoDB到DDS迁移与同步 - cloudDataGuard-mysql：MySQL到MySQL灾备 - gaussdbv5：GaussDB同步 - postgresql：PostgreSQL到PostgreSQL同步 - mysql-to-kafka：MySQL到Kafka同步 - taurus-to-kafka：TaurusDB到Kafka同步 - gaussdbv5ha-to-kafka：GaussDB集中式版到Kafka同步 - oracle-to-gaussdbv5：Oracle-GaussDB分布式版 - oracle-to-gaussdbv5ha：Oracle-GaussDB集中式版 - gaussdbv5-to-oracle：GaussDB分布式版-Oracle - gaussdbv5ha-to-oracle：GaussDB集中式版-Oracle - gaussdbv5-to-kafka：GaussDB分布式版-Kafka  详细取值可参考引擎类型说明。  **默认取值**：  不涉及

        :return: The engine_type of this CreateJobReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this CreateJobReq.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL到MySQL迁移，MySQL到MySQL同步 - mongodb：MongoDB到DDS迁移与同步 - cloudDataGuard-mysql：MySQL到MySQL灾备 - gaussdbv5：GaussDB同步 - postgresql：PostgreSQL到PostgreSQL同步 - mysql-to-kafka：MySQL到Kafka同步 - taurus-to-kafka：TaurusDB到Kafka同步 - gaussdbv5ha-to-kafka：GaussDB集中式版到Kafka同步 - oracle-to-gaussdbv5：Oracle-GaussDB分布式版 - oracle-to-gaussdbv5ha：Oracle-GaussDB集中式版 - gaussdbv5-to-oracle：GaussDB分布式版-Oracle - gaussdbv5ha-to-oracle：GaussDB集中式版-Oracle - gaussdbv5-to-kafka：GaussDB分布式版-Kafka  详细取值可参考引擎类型说明。  **默认取值**：  不涉及

        :param engine_type: The engine_type of this CreateJobReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def is_target_readonly(self):
        r"""Gets the is_target_readonly of this CreateJobReq.

        **参数解释**：  指定目标实例是否限制为只读。  **约束限制**：  - MySQL迁移和灾备，且job_direction为up时设置有效。 - 灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true。  **取值范围**：  - true：目标实例限制为只读 - false：目标实例不限制为只读  **默认取值**：  不涉及

        :return: The is_target_readonly of this CreateJobReq.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        r"""Sets the is_target_readonly of this CreateJobReq.

        **参数解释**：  指定目标实例是否限制为只读。  **约束限制**：  - MySQL迁移和灾备，且job_direction为up时设置有效。 - 灾备场景下，单主灾备且本云为备为必填且为true，不填默认设置为true。  **取值范围**：  - true：目标实例限制为只读 - false：目标实例不限制为只读  **默认取值**：  不涉及

        :param is_target_readonly: The is_target_readonly of this CreateJobReq.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def job_direction(self):
        r"""Gets the job_direction of this CreateJobReq.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :return: The job_direction of this CreateJobReq.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this CreateJobReq.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :param job_direction: The job_direction of this CreateJobReq.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def multi_write(self):
        r"""Gets the multi_write of this CreateJobReq.

        **参数解释**：  是否为双主灾备模式。  **约束限制**：  - db_use_type为cloudDataGuard时必填。 - db_use_type为其他类型时为非必选参数。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false

        :return: The multi_write of this CreateJobReq.
        :rtype: bool
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        r"""Sets the multi_write of this CreateJobReq.

        **参数解释**：  是否为双主灾备模式。  **约束限制**：  - db_use_type为cloudDataGuard时必填。 - db_use_type为其他类型时为非必选参数。  **取值范围**：  - true：双主灾备 - false：非双主灾备  **默认取值**：  false

        :param multi_write: The multi_write of this CreateJobReq.
        :type multi_write: bool
        """
        self._multi_write = multi_write

    @property
    def net_type(self):
        r"""Gets the net_type of this CreateJobReq.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及

        :return: The net_type of this CreateJobReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this CreateJobReq.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及

        :param net_type: The net_type of this CreateJobReq.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def node_num(self):
        r"""Gets the node_num of this CreateJobReq.

        **参数解释**：  节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填。MySQL双主灾备时会默认设置为2。  **约束限制**：  不涉及。  **取值范围**：  1-32  **默认取值**：  不涉及

        :return: The node_num of this CreateJobReq.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this CreateJobReq.

        **参数解释**：  节点个数。MongoDB数据库时对应源端分片个数，源库为集群时必填。MySQL双主灾备时会默认设置为2。  **约束限制**：  不涉及。  **取值范围**：  1-32  **默认取值**：  不涉及

        :param node_num: The node_num of this CreateJobReq.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_type(self):
        r"""Gets the node_type of this CreateJobReq.

        **参数解释**：  DRS任务实例规格编码，决定迁移实例的计算资源大小。  **约束限制**：  不涉及。  **取值范围**：  - micro：极小规格 - small：小规格 - medium：中规格 - high：大规格 - xlarge：超大规格 - 2xlarge：极大规格  具体某种场景支持的取值可以通过查询可用的Node规格接口获取。  **默认取值**：  high

        :return: The node_type of this CreateJobReq.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this CreateJobReq.

        **参数解释**：  DRS任务实例规格编码，决定迁移实例的计算资源大小。  **约束限制**：  不涉及。  **取值范围**：  - micro：极小规格 - small：小规格 - medium：中规格 - high：大规格 - xlarge：超大规格 - 2xlarge：极大规格  具体某种场景支持的取值可以通过查询可用的Node规格接口获取。  **默认取值**：  high

        :param node_type: The node_type of this CreateJobReq.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def source_endpoint(self):
        r"""Gets the source_endpoint of this CreateJobReq.

        :return: The source_endpoint of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        r"""Sets the source_endpoint of this CreateJobReq.

        :param source_endpoint: The source_endpoint of this CreateJobReq.
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        r"""Gets the target_endpoint of this CreateJobReq.

        :return: The target_endpoint of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        r"""Sets the target_endpoint of this CreateJobReq.

        :param target_endpoint: The target_endpoint of this CreateJobReq.
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._target_endpoint = target_endpoint

    @property
    def tags(self):
        r"""Gets the tags of this CreateJobReq.

        **参数解释**：  标签信息列表，详情请参见ResourceTag对象定义。  **约束限制**：  最多添加20个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The tags of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateJobReq.

        **参数解释**：  标签信息列表，详情请参见ResourceTag对象定义。  **约束限制**：  最多添加20个标签。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param tags: The tags of this CreateJobReq.
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def task_type(self):
        r"""Gets the task_type of this CreateJobReq.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择全量加增量（FULL_INCR_TRANS）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  FULL_INCR_TRANS

        :return: The task_type of this CreateJobReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this CreateJobReq.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  单主灾备场景仅支持选择全量加增量（FULL_INCR_TRANS）。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  FULL_INCR_TRANS

        :param task_type: The task_type of this CreateJobReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def customize_sutnet_id(self):
        r"""Gets the customize_sutnet_id of this CreateJobReq.

        **参数解释**：  DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID。  **约束限制**：  UUID格式。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The customize_sutnet_id of this CreateJobReq.
        :rtype: str
        """
        return self._customize_sutnet_id

    @customize_sutnet_id.setter
    def customize_sutnet_id(self, customize_sutnet_id):
        r"""Sets the customize_sutnet_id of this CreateJobReq.

        **参数解释**：  DRS实例所在子网ID，对应目标库相同VPC下已创建的子网（subnet）的网络ID。  **约束限制**：  UUID格式。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param customize_sutnet_id: The customize_sutnet_id of this CreateJobReq.
        :type customize_sutnet_id: str
        """
        self._customize_sutnet_id = customize_sutnet_id

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateJobReq.

        **参数解释**：  产品ID，用于标识包年包月任务对应的产品。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The product_id of this CreateJobReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateJobReq.

        **参数解释**：  产品ID，用于标识包年包月任务对应的产品。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param product_id: The product_id of this CreateJobReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this CreateJobReq.

        **参数解释**：  企业项目标签列表，详情请参见ResourceTag对象定义。  **约束限制**：  - 不填默认为default。 - key值必须为_sys_enterprise_project_id，value为企业项目ID。 - 只能填一个企业项目。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The sys_tags of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this CreateJobReq.

        **参数解释**：  企业项目标签列表，详情请参见ResourceTag对象定义。  **约束限制**：  - 不填默认为default。 - key值必须为_sys_enterprise_project_id，value为企业项目ID。 - 只能填一个企业项目。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param sys_tags: The sys_tags of this CreateJobReq.
        :type sys_tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        self._sys_tags = sys_tags

    @property
    def expired_days(self):
        r"""Gets the expired_days of this CreateJobReq.

        **参数解释**：  任务处于异常状态一段时间后自动结束的天数。  **约束限制**：  不涉及。  **取值范围**：  14-100  **默认取值**：  14

        :return: The expired_days of this CreateJobReq.
        :rtype: str
        """
        return self._expired_days

    @expired_days.setter
    def expired_days(self, expired_days):
        r"""Sets the expired_days of this CreateJobReq.

        **参数解释**：  任务处于异常状态一段时间后自动结束的天数。  **约束限制**：  不涉及。  **取值范围**：  14-100  **默认取值**：  14

        :param expired_days: The expired_days of this CreateJobReq.
        :type expired_days: str
        """
        self._expired_days = expired_days

    @property
    def master_az(self):
        r"""Gets the master_az of this CreateJobReq.

        **参数解释**：  主备任务主任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The master_az of this CreateJobReq.
        :rtype: str
        """
        return self._master_az

    @master_az.setter
    def master_az(self, master_az):
        r"""Sets the master_az of this CreateJobReq.

        **参数解释**：  主备任务主任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param master_az: The master_az of this CreateJobReq.
        :type master_az: str
        """
        self._master_az = master_az

    @property
    def slave_az(self):
        r"""Gets the slave_az of this CreateJobReq.

        **参数解释**：  主备任务备任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The slave_az of this CreateJobReq.
        :rtype: str
        """
        return self._slave_az

    @slave_az.setter
    def slave_az(self, slave_az):
        r"""Sets the slave_az of this CreateJobReq.

        **参数解释**：  主备任务备任务所在可用区编码，可以通过查询规格未售罄的可用区接口获取。  **约束限制**：  - master_az和slave_az同时填写时生效。 - 目前支持mysql，gaussdbv5ha-to-kafka。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param slave_az: The slave_az of this CreateJobReq.
        :type slave_az: str
        """
        self._slave_az = slave_az

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateJobReq.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  - db_use_type为migration时不支持包年包月。 - 支持的engine_type为：mysql，cloudDataGuard-mysql，postgresql，gaussdbv5ha-to-kafka。  **取值范围**：  - period：包年包月 - on_demand：按需计费  **默认取值**：  on_demand

        :return: The charging_mode of this CreateJobReq.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateJobReq.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  - db_use_type为migration时不支持包年包月。 - 支持的engine_type为：mysql，cloudDataGuard-mysql，postgresql，gaussdbv5ha-to-kafka。  **取值范围**：  - period：包年包月 - on_demand：按需计费  **默认取值**：  on_demand

        :param charging_mode: The charging_mode of this CreateJobReq.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_order(self):
        r"""Gets the period_order of this CreateJobReq.

        :return: The period_order of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.PeriodOrderInfo`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        r"""Sets the period_order of this CreateJobReq.

        :param period_order: The period_order of this CreateJobReq.
        :type period_order: :class:`huaweicloudsdkdrs.v3.PeriodOrderInfo`
        """
        self._period_order = period_order

    @property
    def public_ip_list(self):
        r"""Gets the public_ip_list of this CreateJobReq.

        **参数解释**：  指定公网IP的信息列表，详情请参见PublicIpConfig对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The public_ip_list of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.PublicIpConfig`]
        """
        return self._public_ip_list

    @public_ip_list.setter
    def public_ip_list(self, public_ip_list):
        r"""Sets the public_ip_list of this CreateJobReq.

        **参数解释**：  指定公网IP的信息列表，详情请参见PublicIpConfig对象定义。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param public_ip_list: The public_ip_list of this CreateJobReq.
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v3.PublicIpConfig`]
        """
        self._public_ip_list = public_ip_list

    @property
    def is_open_fast_clean(self):
        r"""Gets the is_open_fast_clean of this CreateJobReq.

        **参数解释**：  是否开启云数据库RDS for MySQL或MariaDB的Binlog快速清理。  **约束限制**：  不涉及。  **取值范围**：  - true：开启Binlog快速清理 - false：不开启Binlog快速清理  **默认取值**：  false

        :return: The is_open_fast_clean of this CreateJobReq.
        :rtype: bool
        """
        return self._is_open_fast_clean

    @is_open_fast_clean.setter
    def is_open_fast_clean(self, is_open_fast_clean):
        r"""Sets the is_open_fast_clean of this CreateJobReq.

        **参数解释**：  是否开启云数据库RDS for MySQL或MariaDB的Binlog快速清理。  **约束限制**：  不涉及。  **取值范围**：  - true：开启Binlog快速清理 - false：不开启Binlog快速清理  **默认取值**：  false

        :param is_open_fast_clean: The is_open_fast_clean of this CreateJobReq.
        :type is_open_fast_clean: bool
        """
        self._is_open_fast_clean = is_open_fast_clean

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
