# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'description': 'str',
        'name': 'str',
        'alarm_notify': 'AlarmNotifyInfo',
        'task_type': 'str',
        'source_endpoint': 'Endpoint',
        'target_endpoint': 'Endpoint',
        'node_type': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'store_db_info': 'bool',
        'is_recreate': 'bool',
        'job_direction': 'str',
        'is_target_readonly': 'bool',
        'replace_definer': 'bool',
        'tags': 'list[ResourceTag]',
        'db_use_type': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'description': 'description',
        'name': 'name',
        'alarm_notify': 'alarm_notify',
        'task_type': 'task_type',
        'source_endpoint': 'source_endpoint',
        'target_endpoint': 'target_endpoint',
        'node_type': 'node_type',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'store_db_info': 'store_db_info',
        'is_recreate': 'is_recreate',
        'job_direction': 'job_direction',
        'is_target_readonly': 'is_target_readonly',
        'replace_definer': 'replace_definer',
        'tags': 'tags',
        'db_use_type': 'db_use_type',
        'product_id': 'product_id'
    }

    def __init__(self, job_id=None, description=None, name=None, alarm_notify=None, task_type=None, source_endpoint=None, target_endpoint=None, node_type=None, engine_type=None, net_type=None, store_db_info=None, is_recreate=None, job_direction=None, is_target_readonly=None, replace_definer=None, tags=None, db_use_type=None, product_id=None):
        """ModifyJobReq

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param description: 任务描述，修改任务描述时必填。
        :type description: str
        :param name: 任务名称，修改任务名称时必填
        :type name: str
        :param alarm_notify: 
        :type alarm_notify: :class:`huaweicloudsdkdrs.v3.AlarmNotifyInfo`
        :param task_type: 任务模式，FULL_TRANS：全量；FULL_INCR_TRANS：全量+增量；INCR_TRANS：增量。
        :type task_type: str
        :param source_endpoint: 
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param target_endpoint: 
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param node_type: node规格类型，测试连接之后修改调用时必填。
        :type node_type: str
        :param engine_type: 引擎类型，测试连接之后修改调用时必填。mysql：迁移，同步使用。mongodb：迁移使用。cloudDataGuard-mysql：灾备使用
        :type engine_type: str
        :param net_type: 网络类型，测试连接之后修改调用时必填。
        :type net_type: str
        :param store_db_info: 保存数据库信息，测试连接之后修改调用时必填为true。
        :type store_db_info: bool
        :param is_recreate: 是否为重建任务。
        :type is_recreate: bool
        :param job_direction: 迁移方向,up 入云 灾备场景时对应本云为备,down 出云 灾备场景时对应本云为主,non-dbs 自建
        :type job_direction: str
        :param is_target_readonly: 目标实例是否限制为只读。
        :type is_target_readonly: bool
        :param replace_definer: 所有Definer是否迁移到该用户下，MySQL数据库支持该设置，测试连接之后修改调用时必填。 - true：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限 - false：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。
        :type replace_definer: bool
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        :param db_use_type: 迁移类型，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备
        :type db_use_type: str
        :param product_id: 产品ID。
        :type product_id: str
        """
        
        

        self._job_id = None
        self._description = None
        self._name = None
        self._alarm_notify = None
        self._task_type = None
        self._source_endpoint = None
        self._target_endpoint = None
        self._node_type = None
        self._engine_type = None
        self._net_type = None
        self._store_db_info = None
        self._is_recreate = None
        self._job_direction = None
        self._is_target_readonly = None
        self._replace_definer = None
        self._tags = None
        self._db_use_type = None
        self._product_id = None
        self.discriminator = None

        self.job_id = job_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if task_type is not None:
            self.task_type = task_type
        if source_endpoint is not None:
            self.source_endpoint = source_endpoint
        if target_endpoint is not None:
            self.target_endpoint = target_endpoint
        if node_type is not None:
            self.node_type = node_type
        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if store_db_info is not None:
            self.store_db_info = store_db_info
        if is_recreate is not None:
            self.is_recreate = is_recreate
        if job_direction is not None:
            self.job_direction = job_direction
        if is_target_readonly is not None:
            self.is_target_readonly = is_target_readonly
        if replace_definer is not None:
            self.replace_definer = replace_definer
        if tags is not None:
            self.tags = tags
        if db_use_type is not None:
            self.db_use_type = db_use_type
        if product_id is not None:
            self.product_id = product_id

    @property
    def job_id(self):
        """Gets the job_id of this ModifyJobReq.

        任务id

        :return: The job_id of this ModifyJobReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ModifyJobReq.

        任务id

        :param job_id: The job_id of this ModifyJobReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def description(self):
        """Gets the description of this ModifyJobReq.

        任务描述，修改任务描述时必填。

        :return: The description of this ModifyJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyJobReq.

        任务描述，修改任务描述时必填。

        :param description: The description of this ModifyJobReq.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this ModifyJobReq.

        任务名称，修改任务名称时必填

        :return: The name of this ModifyJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyJobReq.

        任务名称，修改任务名称时必填

        :param name: The name of this ModifyJobReq.
        :type name: str
        """
        self._name = name

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this ModifyJobReq.

        :return: The alarm_notify of this ModifyJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.AlarmNotifyInfo`
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this ModifyJobReq.

        :param alarm_notify: The alarm_notify of this ModifyJobReq.
        :type alarm_notify: :class:`huaweicloudsdkdrs.v3.AlarmNotifyInfo`
        """
        self._alarm_notify = alarm_notify

    @property
    def task_type(self):
        """Gets the task_type of this ModifyJobReq.

        任务模式，FULL_TRANS：全量；FULL_INCR_TRANS：全量+增量；INCR_TRANS：增量。

        :return: The task_type of this ModifyJobReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ModifyJobReq.

        任务模式，FULL_TRANS：全量；FULL_INCR_TRANS：全量+增量；INCR_TRANS：增量。

        :param task_type: The task_type of this ModifyJobReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this ModifyJobReq.

        :return: The source_endpoint of this ModifyJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this ModifyJobReq.

        :param source_endpoint: The source_endpoint of this ModifyJobReq.
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this ModifyJobReq.

        :return: The target_endpoint of this ModifyJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this ModifyJobReq.

        :param target_endpoint: The target_endpoint of this ModifyJobReq.
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._target_endpoint = target_endpoint

    @property
    def node_type(self):
        """Gets the node_type of this ModifyJobReq.

        node规格类型，测试连接之后修改调用时必填。

        :return: The node_type of this ModifyJobReq.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ModifyJobReq.

        node规格类型，测试连接之后修改调用时必填。

        :param node_type: The node_type of this ModifyJobReq.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def engine_type(self):
        """Gets the engine_type of this ModifyJobReq.

        引擎类型，测试连接之后修改调用时必填。mysql：迁移，同步使用。mongodb：迁移使用。cloudDataGuard-mysql：灾备使用

        :return: The engine_type of this ModifyJobReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this ModifyJobReq.

        引擎类型，测试连接之后修改调用时必填。mysql：迁移，同步使用。mongodb：迁移使用。cloudDataGuard-mysql：灾备使用

        :param engine_type: The engine_type of this ModifyJobReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        """Gets the net_type of this ModifyJobReq.

        网络类型，测试连接之后修改调用时必填。

        :return: The net_type of this ModifyJobReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this ModifyJobReq.

        网络类型，测试连接之后修改调用时必填。

        :param net_type: The net_type of this ModifyJobReq.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def store_db_info(self):
        """Gets the store_db_info of this ModifyJobReq.

        保存数据库信息，测试连接之后修改调用时必填为true。

        :return: The store_db_info of this ModifyJobReq.
        :rtype: bool
        """
        return self._store_db_info

    @store_db_info.setter
    def store_db_info(self, store_db_info):
        """Sets the store_db_info of this ModifyJobReq.

        保存数据库信息，测试连接之后修改调用时必填为true。

        :param store_db_info: The store_db_info of this ModifyJobReq.
        :type store_db_info: bool
        """
        self._store_db_info = store_db_info

    @property
    def is_recreate(self):
        """Gets the is_recreate of this ModifyJobReq.

        是否为重建任务。

        :return: The is_recreate of this ModifyJobReq.
        :rtype: bool
        """
        return self._is_recreate

    @is_recreate.setter
    def is_recreate(self, is_recreate):
        """Sets the is_recreate of this ModifyJobReq.

        是否为重建任务。

        :param is_recreate: The is_recreate of this ModifyJobReq.
        :type is_recreate: bool
        """
        self._is_recreate = is_recreate

    @property
    def job_direction(self):
        """Gets the job_direction of this ModifyJobReq.

        迁移方向,up 入云 灾备场景时对应本云为备,down 出云 灾备场景时对应本云为主,non-dbs 自建

        :return: The job_direction of this ModifyJobReq.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this ModifyJobReq.

        迁移方向,up 入云 灾备场景时对应本云为备,down 出云 灾备场景时对应本云为主,non-dbs 自建

        :param job_direction: The job_direction of this ModifyJobReq.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def is_target_readonly(self):
        """Gets the is_target_readonly of this ModifyJobReq.

        目标实例是否限制为只读。

        :return: The is_target_readonly of this ModifyJobReq.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        """Sets the is_target_readonly of this ModifyJobReq.

        目标实例是否限制为只读。

        :param is_target_readonly: The is_target_readonly of this ModifyJobReq.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def replace_definer(self):
        """Gets the replace_definer of this ModifyJobReq.

        所有Definer是否迁移到该用户下，MySQL数据库支持该设置，测试连接之后修改调用时必填。 - true：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限 - false：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。

        :return: The replace_definer of this ModifyJobReq.
        :rtype: bool
        """
        return self._replace_definer

    @replace_definer.setter
    def replace_definer(self, replace_definer):
        """Sets the replace_definer of this ModifyJobReq.

        所有Definer是否迁移到该用户下，MySQL数据库支持该设置，测试连接之后修改调用时必填。 - true：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限 - false：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。

        :param replace_definer: The replace_definer of this ModifyJobReq.
        :type replace_definer: bool
        """
        self._replace_definer = replace_definer

    @property
    def tags(self):
        """Gets the tags of this ModifyJobReq.

        标签信息

        :return: The tags of this ModifyJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ModifyJobReq.

        标签信息

        :param tags: The tags of this ModifyJobReq.
        :type tags: list[:class:`huaweicloudsdkdrs.v3.ResourceTag`]
        """
        self._tags = tags

    @property
    def db_use_type(self):
        """Gets the db_use_type of this ModifyJobReq.

        迁移类型，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :return: The db_use_type of this ModifyJobReq.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this ModifyJobReq.

        迁移类型，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :param db_use_type: The db_use_type of this ModifyJobReq.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def product_id(self):
        """Gets the product_id of this ModifyJobReq.

        产品ID。

        :return: The product_id of this ModifyJobReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ModifyJobReq.

        产品ID。

        :param product_id: The product_id of this ModifyJobReq.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, ModifyJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
