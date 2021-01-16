# coding: utf-8

import pprint
import re

import six





class BasicInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'version': 'str',
        'service_type': 'str',
        'purchase_type': 'str',
        'sign_algorithm': 'str',
        'consensus': 'str',
        'charging_mode': 'int',
        'version_type': 'int',
        'database_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_type': 'str',
        'cluster_az': 'str',
        'created_time': 'str',
        'deploy_type': 'str',
        'is_cross_region': 'bool',
        'is_support_rollback': 'bool',
        'is_support_restful': 'bool',
        'is_old_service': 'bool',
        'old_service_version': 'str',
        'agent_portal_addrs': 'list[str]',
        'status': 'str',
        'process_status': 'str',
        'order_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'service_type': 'service_type',
        'purchase_type': 'purchase_type',
        'sign_algorithm': 'sign_algorithm',
        'consensus': 'consensus',
        'charging_mode': 'charging_mode',
        'version_type': 'version_type',
        'database_type': 'database_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type',
        'cluster_az': 'cluster_az',
        'created_time': 'created_time',
        'deploy_type': 'deploy_type',
        'is_cross_region': 'is_cross_region',
        'is_support_rollback': 'is_support_rollback',
        'is_support_restful': 'is_support_restful',
        'is_old_service': 'is_old_service',
        'old_service_version': 'old_service_version',
        'agent_portal_addrs': 'agent_portal_addrs',
        'status': 'status',
        'process_status': 'process_status',
        'order_status': 'order_status'
    }

    def __init__(self, id=None, name=None, version=None, service_type=None, purchase_type=None, sign_algorithm=None, consensus=None, charging_mode=None, version_type=None, database_type=None, cluster_id=None, cluster_name=None, cluster_type=None, cluster_az=None, created_time=None, deploy_type=None, is_cross_region=None, is_support_rollback=None, is_support_restful=None, is_old_service=None, old_service_version=None, agent_portal_addrs=None, status=None, process_status=None, order_status=None):
        """BasicInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._version = None
        self._service_type = None
        self._purchase_type = None
        self._sign_algorithm = None
        self._consensus = None
        self._charging_mode = None
        self._version_type = None
        self._database_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_type = None
        self._cluster_az = None
        self._created_time = None
        self._deploy_type = None
        self._is_cross_region = None
        self._is_support_rollback = None
        self._is_support_restful = None
        self._is_old_service = None
        self._old_service_version = None
        self._agent_portal_addrs = None
        self._status = None
        self._process_status = None
        self._order_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if service_type is not None:
            self.service_type = service_type
        if purchase_type is not None:
            self.purchase_type = purchase_type
        if sign_algorithm is not None:
            self.sign_algorithm = sign_algorithm
        if consensus is not None:
            self.consensus = consensus
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if version_type is not None:
            self.version_type = version_type
        if database_type is not None:
            self.database_type = database_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_az is not None:
            self.cluster_az = cluster_az
        if created_time is not None:
            self.created_time = created_time
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if is_cross_region is not None:
            self.is_cross_region = is_cross_region
        if is_support_rollback is not None:
            self.is_support_rollback = is_support_rollback
        if is_support_restful is not None:
            self.is_support_restful = is_support_restful
        if is_old_service is not None:
            self.is_old_service = is_old_service
        if old_service_version is not None:
            self.old_service_version = old_service_version
        if agent_portal_addrs is not None:
            self.agent_portal_addrs = agent_portal_addrs
        if status is not None:
            self.status = status
        if process_status is not None:
            self.process_status = process_status
        if order_status is not None:
            self.order_status = order_status

    @property
    def id(self):
        """Gets the id of this BasicInfo.

        BCS服务ID

        :return: The id of this BasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicInfo.

        BCS服务ID

        :param id: The id of this BasicInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BasicInfo.

        BCS服务名

        :return: The name of this BasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicInfo.

        BCS服务名

        :param name: The name of this BasicInfo.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this BasicInfo.

        BCS服务版本信息

        :return: The version of this BasicInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BasicInfo.

        BCS服务版本信息

        :param version: The version of this BasicInfo.
        :type: str
        """
        self._version = version

    @property
    def service_type(self):
        """Gets the service_type of this BasicInfo.

        BCS服务的类型，分为：联盟链（union），私有链（private）

        :return: The service_type of this BasicInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this BasicInfo.

        BCS服务的类型，分为：联盟链（union），私有链（private）

        :param service_type: The service_type of this BasicInfo.
        :type: str
        """
        self._service_type = service_type

    @property
    def purchase_type(self):
        """Gets the purchase_type of this BasicInfo.

        BCS服务部署类型，分为一键购买（onestep），普通购买（normal）

        :return: The purchase_type of this BasicInfo.
        :rtype: str
        """
        return self._purchase_type

    @purchase_type.setter
    def purchase_type(self, purchase_type):
        """Sets the purchase_type of this BasicInfo.

        BCS服务部署类型，分为一键购买（onestep），普通购买（normal）

        :param purchase_type: The purchase_type of this BasicInfo.
        :type: str
        """
        self._purchase_type = purchase_type

    @property
    def sign_algorithm(self):
        """Gets the sign_algorithm of this BasicInfo.

        BCS服务安全机制，分为ECDSA（ECDSA），国密算法（sm2）

        :return: The sign_algorithm of this BasicInfo.
        :rtype: str
        """
        return self._sign_algorithm

    @sign_algorithm.setter
    def sign_algorithm(self, sign_algorithm):
        """Sets the sign_algorithm of this BasicInfo.

        BCS服务安全机制，分为ECDSA（ECDSA），国密算法（sm2）

        :param sign_algorithm: The sign_algorithm of this BasicInfo.
        :type: str
        """
        self._sign_algorithm = sign_algorithm

    @property
    def consensus(self):
        """Gets the consensus of this BasicInfo.

        BCS服务的共识策略，分为测试策略（solo），快速拜占庭容错算法（sflic）,Kafka(kafka)

        :return: The consensus of this BasicInfo.
        :rtype: str
        """
        return self._consensus

    @consensus.setter
    def consensus(self, consensus):
        """Sets the consensus of this BasicInfo.

        BCS服务的共识策略，分为测试策略（solo），快速拜占庭容错算法（sflic）,Kafka(kafka)

        :param consensus: The consensus of this BasicInfo.
        :type: str
        """
        self._consensus = consensus

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BasicInfo.

        BCS服务付费模式，分为按需（1），包周期（0）

        :return: The charging_mode of this BasicInfo.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BasicInfo.

        BCS服务付费模式，分为按需（1），包周期（0）

        :param charging_mode: The charging_mode of this BasicInfo.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def version_type(self):
        """Gets the version_type of this BasicInfo.

        BCS服务版本类型，分为基础版（1），专业版（2），铂金版（3）

        :return: The version_type of this BasicInfo.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this BasicInfo.

        BCS服务版本类型，分为基础版（1），专业版（2），铂金版（3）

        :param version_type: The version_type of this BasicInfo.
        :type: int
        """
        self._version_type = version_type

    @property
    def database_type(self):
        """Gets the database_type of this BasicInfo.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb）

        :return: The database_type of this BasicInfo.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """Sets the database_type of this BasicInfo.

        BCS服务数据库类型，包括文件数据库（goleveldb），NoSQL（couchdb）

        :param database_type: The database_type of this BasicInfo.
        :type: str
        """
        self._database_type = database_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BasicInfo.

        BCS服务所在集群ID

        :return: The cluster_id of this BasicInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BasicInfo.

        BCS服务所在集群ID

        :param cluster_id: The cluster_id of this BasicInfo.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this BasicInfo.

        BCS服务所在集群名称

        :return: The cluster_name of this BasicInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this BasicInfo.

        BCS服务所在集群名称

        :param cluster_name: The cluster_name of this BasicInfo.
        :type: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """Gets the cluster_type of this BasicInfo.

        BCS服务的集群类型，分为CCE集群（空），IEF集群（ief）

        :return: The cluster_type of this BasicInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this BasicInfo.

        BCS服务的集群类型，分为CCE集群（空），IEF集群（ief）

        :param cluster_type: The cluster_type of this BasicInfo.
        :type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_az(self):
        """Gets the cluster_az of this BasicInfo.

        BCS多可用区标示，分为：多可用区（yes），非多可用区（no）

        :return: The cluster_az of this BasicInfo.
        :rtype: str
        """
        return self._cluster_az

    @cluster_az.setter
    def cluster_az(self, cluster_az):
        """Sets the cluster_az of this BasicInfo.

        BCS多可用区标示，分为：多可用区（yes），非多可用区（no）

        :param cluster_az: The cluster_az of this BasicInfo.
        :type: str
        """
        self._cluster_az = cluster_az

    @property
    def created_time(self):
        """Gets the created_time of this BasicInfo.

        BCS服务创建时间

        :return: The created_time of this BasicInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this BasicInfo.

        BCS服务创建时间

        :param created_time: The created_time of this BasicInfo.
        :type: str
        """
        self._created_time = created_time

    @property
    def deploy_type(self):
        """Gets the deploy_type of this BasicInfo.

        BCS服务联盟链下生效，分为邀请方（create），被邀请方（invite）

        :return: The deploy_type of this BasicInfo.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this BasicInfo.

        BCS服务联盟链下生效，分为邀请方（create），被邀请方（invite）

        :param deploy_type: The deploy_type of this BasicInfo.
        :type: str
        """
        self._deploy_type = deploy_type

    @property
    def is_cross_region(self):
        """Gets the is_cross_region of this BasicInfo.

        BCS服务是否跨region

        :return: The is_cross_region of this BasicInfo.
        :rtype: bool
        """
        return self._is_cross_region

    @is_cross_region.setter
    def is_cross_region(self, is_cross_region):
        """Sets the is_cross_region of this BasicInfo.

        BCS服务是否跨region

        :param is_cross_region: The is_cross_region of this BasicInfo.
        :type: bool
        """
        self._is_cross_region = is_cross_region

    @property
    def is_support_rollback(self):
        """Gets the is_support_rollback of this BasicInfo.

        BCS服务升级失败，是否支持回滚

        :return: The is_support_rollback of this BasicInfo.
        :rtype: bool
        """
        return self._is_support_rollback

    @is_support_rollback.setter
    def is_support_rollback(self, is_support_rollback):
        """Sets the is_support_rollback of this BasicInfo.

        BCS服务升级失败，是否支持回滚

        :param is_support_rollback: The is_support_rollback of this BasicInfo.
        :type: bool
        """
        self._is_support_rollback = is_support_rollback

    @property
    def is_support_restful(self):
        """Gets the is_support_restful of this BasicInfo.

        BCS服务是否添加RESTful APIs支持，分为支持（true），不支持（false）

        :return: The is_support_restful of this BasicInfo.
        :rtype: bool
        """
        return self._is_support_restful

    @is_support_restful.setter
    def is_support_restful(self, is_support_restful):
        """Sets the is_support_restful of this BasicInfo.

        BCS服务是否添加RESTful APIs支持，分为支持（true），不支持（false）

        :param is_support_restful: The is_support_restful of this BasicInfo.
        :type: bool
        """
        self._is_support_restful = is_support_restful

    @property
    def is_old_service(self):
        """Gets the is_old_service of this BasicInfo.

        区分BCS是否新服务，分为老服务（true），新服务（false）

        :return: The is_old_service of this BasicInfo.
        :rtype: bool
        """
        return self._is_old_service

    @is_old_service.setter
    def is_old_service(self, is_old_service):
        """Sets the is_old_service of this BasicInfo.

        区分BCS是否新服务，分为老服务（true），新服务（false）

        :param is_old_service: The is_old_service of this BasicInfo.
        :type: bool
        """
        self._is_old_service = is_old_service

    @property
    def old_service_version(self):
        """Gets the old_service_version of this BasicInfo.

        BCS服务为老服务时，此字段为老服务版本号

        :return: The old_service_version of this BasicInfo.
        :rtype: str
        """
        return self._old_service_version

    @old_service_version.setter
    def old_service_version(self, old_service_version):
        """Sets the old_service_version of this BasicInfo.

        BCS服务为老服务时，此字段为老服务版本号

        :param old_service_version: The old_service_version of this BasicInfo.
        :type: str
        """
        self._old_service_version = old_service_version

    @property
    def agent_portal_addrs(self):
        """Gets the agent_portal_addrs of this BasicInfo.

        BCS服务用户数据面agent地址端口列表

        :return: The agent_portal_addrs of this BasicInfo.
        :rtype: list[str]
        """
        return self._agent_portal_addrs

    @agent_portal_addrs.setter
    def agent_portal_addrs(self, agent_portal_addrs):
        """Sets the agent_portal_addrs of this BasicInfo.

        BCS服务用户数据面agent地址端口列表

        :param agent_portal_addrs: The agent_portal_addrs of this BasicInfo.
        :type: list[str]
        """
        self._agent_portal_addrs = agent_portal_addrs

    @property
    def status(self):
        """Gets the status of this BasicInfo.

        BCS服务状态，分为正常（Normal），异常（Abnormal），弹性IP异常（EipAbnormal），已冻结（Freeze），休眠中（Hibernation），未知（其余值）

        :return: The status of this BasicInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BasicInfo.

        BCS服务状态，分为正常（Normal），异常（Abnormal），弹性IP异常（EipAbnormal），已冻结（Freeze），休眠中（Hibernation），未知（其余值）

        :param status: The status of this BasicInfo.
        :type: str
        """
        self._status = status

    @property
    def process_status(self):
        """Gets the process_status of this BasicInfo.

        BCS服务处理状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（IsScaling），删除中（IsDeleting），添加中（IsAdding）

        :return: The process_status of this BasicInfo.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this BasicInfo.

        BCS服务处理状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（IsScaling），删除中（IsDeleting），添加中（IsAdding）

        :param process_status: The process_status of this BasicInfo.
        :type: str
        """
        self._process_status = process_status

    @property
    def order_status(self):
        """Gets the order_status of this BasicInfo.

        BCS服务为包周期模式时，返回值为0（订单未成功）,1（订单异常）,2（订单正常）

        :return: The order_status of this BasicInfo.
        :rtype: int
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this BasicInfo.

        BCS服务为包周期模式时，返回值为0（订单未成功）,1（订单异常）,2（订单正常）

        :param order_status: The order_status of this BasicInfo.
        :type: int
        """
        self._order_status = order_status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
