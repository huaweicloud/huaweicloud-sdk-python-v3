# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore': 'ClusterDetailDatastore',
        'instances': 'list[ClusterDetailInstances]',
        'public_kibana_resp': 'PublicKibanaRespBody',
        'elb_white_list': 'ElbWhiteListResp',
        'updated': 'str',
        'name': 'str',
        'public_ip': 'str',
        'created': 'str',
        'id': 'str',
        'status': 'str',
        'endpoint': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'vpcep_ip': 'str',
        'bandwidth_size': 'int',
        'https_enable': 'bool',
        'disk_encrypted': 'bool',
        'authority_enable': 'bool',
        'backup_available': 'bool',
        'action_progress': 'object',
        'actions': 'list[str]',
        'enterprise_project_id': 'str',
        'tags': 'list[ClusterDetailTags]',
        'failed_reason': 'ClusterDetailFailedReasons',
        'period': 'bool'
    }

    attribute_map = {
        'datastore': 'datastore',
        'instances': 'instances',
        'public_kibana_resp': 'publicKibanaResp',
        'elb_white_list': 'elbWhiteList',
        'updated': 'updated',
        'name': 'name',
        'public_ip': 'publicIp',
        'created': 'created',
        'id': 'id',
        'status': 'status',
        'endpoint': 'endpoint',
        'vpc_id': 'vpcId',
        'subnet_id': 'subnetId',
        'security_group_id': 'securityGroupId',
        'vpcep_ip': 'vpcepIp',
        'bandwidth_size': 'bandwidthSize',
        'https_enable': 'httpsEnable',
        'disk_encrypted': 'diskEncrypted',
        'authority_enable': 'authorityEnable',
        'backup_available': 'backupAvailable',
        'action_progress': 'actionProgress',
        'actions': 'actions',
        'enterprise_project_id': 'enterpriseProjectId',
        'tags': 'tags',
        'failed_reason': 'failedReason',
        'period': 'period'
    }

    def __init__(self, datastore=None, instances=None, public_kibana_resp=None, elb_white_list=None, updated=None, name=None, public_ip=None, created=None, id=None, status=None, endpoint=None, vpc_id=None, subnet_id=None, security_group_id=None, vpcep_ip=None, bandwidth_size=None, https_enable=None, disk_encrypted=None, authority_enable=None, backup_available=None, action_progress=None, actions=None, enterprise_project_id=None, tags=None, failed_reason=None, period=None):
        """ShowClusterDetailResponse

        The model defined in huaweicloud sdk

        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcss.v1.ClusterDetailDatastore`
        :param instances: 节点对象列表。
        :type instances: list[:class:`huaweicloudsdkcss.v1.ClusterDetailInstances`]
        :param public_kibana_resp: 
        :type public_kibana_resp: :class:`huaweicloudsdkcss.v1.PublicKibanaRespBody`
        :param elb_white_list: 
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.ElbWhiteListResp`
        :param updated: 集群上次修改时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。
        :type updated: str
        :param name: 集群名称。
        :type name: str
        :param public_ip: 公网IP信息。
        :type public_ip: str
        :param created: 集群创建时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。
        :type created: str
        :param id: 集群ID。
        :type id: str
        :param status: 集群状态值。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。
        :type status: str
        :param endpoint: 用户VPC访问IP地址和端口号。
        :type endpoint: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param vpcep_ip: 终端节点IP。
        :type vpcep_ip: str
        :param bandwidth_size: 公网带宽大小。单位：Mbit/s
        :type bandwidth_size: int
        :param https_enable: 通信加密状态。 - false：未设置通信加密。 - true：已设置通信加密。
        :type https_enable: bool
        :param disk_encrypted: 磁盘是否加密。  - true : 磁盘已加密。 - false : 磁盘未加密。
        :type disk_encrypted: bool
        :param authority_enable: 是否开启认证，取值范围为true或false。默认关闭认证功能。 - true：表示集群开启认证。 - false：表示集群不开启认证。
        :type authority_enable: bool
        :param backup_available: 快照是否开启。 - true: 快照开启状态。 - false: 快照关闭状态。
        :type backup_available: bool
        :param action_progress: 集群行为进度，显示创建或扩容进度的百分比。
        :type action_progress: object
        :param actions: 集群当前行为。REBOOTING表示重启、GROWING表示扩容、RESTORING表示恢复集群、SNAPSHOTTING表示创建快照等。
        :type actions: list[str]
        :param enterprise_project_id: 集群所属的企业项目ID。  如果集群所属用户没有开通企业项目，则不会返回该参数。
        :type enterprise_project_id: str
        :param tags: 集群标签。
        :type tags: list[:class:`huaweicloudsdkcss.v1.ClusterDetailTags`]
        :param failed_reason: 
        :type failed_reason: :class:`huaweicloudsdkcss.v1.ClusterDetailFailedReasons`
        :param period: 是否为包周期集群。 - \&quot;true\&quot; 表示是包周期计费的集群。 - \&quot;false\&quot; 表示是按需计费的集群。
        :type period: bool
        """
        
        super(ShowClusterDetailResponse, self).__init__()

        self._datastore = None
        self._instances = None
        self._public_kibana_resp = None
        self._elb_white_list = None
        self._updated = None
        self._name = None
        self._public_ip = None
        self._created = None
        self._id = None
        self._status = None
        self._endpoint = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._vpcep_ip = None
        self._bandwidth_size = None
        self._https_enable = None
        self._disk_encrypted = None
        self._authority_enable = None
        self._backup_available = None
        self._action_progress = None
        self._actions = None
        self._enterprise_project_id = None
        self._tags = None
        self._failed_reason = None
        self._period = None
        self.discriminator = None

        if datastore is not None:
            self.datastore = datastore
        if instances is not None:
            self.instances = instances
        if public_kibana_resp is not None:
            self.public_kibana_resp = public_kibana_resp
        if elb_white_list is not None:
            self.elb_white_list = elb_white_list
        if updated is not None:
            self.updated = updated
        if name is not None:
            self.name = name
        if public_ip is not None:
            self.public_ip = public_ip
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if endpoint is not None:
            self.endpoint = endpoint
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if vpcep_ip is not None:
            self.vpcep_ip = vpcep_ip
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if https_enable is not None:
            self.https_enable = https_enable
        if disk_encrypted is not None:
            self.disk_encrypted = disk_encrypted
        if authority_enable is not None:
            self.authority_enable = authority_enable
        if backup_available is not None:
            self.backup_available = backup_available
        if action_progress is not None:
            self.action_progress = action_progress
        if actions is not None:
            self.actions = actions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if period is not None:
            self.period = period

    @property
    def datastore(self):
        """Gets the datastore of this ShowClusterDetailResponse.

        :return: The datastore of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.ClusterDetailDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ShowClusterDetailResponse.

        :param datastore: The datastore of this ShowClusterDetailResponse.
        :type datastore: :class:`huaweicloudsdkcss.v1.ClusterDetailDatastore`
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this ShowClusterDetailResponse.

        节点对象列表。

        :return: The instances of this ShowClusterDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ClusterDetailInstances`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ShowClusterDetailResponse.

        节点对象列表。

        :param instances: The instances of this ShowClusterDetailResponse.
        :type instances: list[:class:`huaweicloudsdkcss.v1.ClusterDetailInstances`]
        """
        self._instances = instances

    @property
    def public_kibana_resp(self):
        """Gets the public_kibana_resp of this ShowClusterDetailResponse.

        :return: The public_kibana_resp of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.PublicKibanaRespBody`
        """
        return self._public_kibana_resp

    @public_kibana_resp.setter
    def public_kibana_resp(self, public_kibana_resp):
        """Sets the public_kibana_resp of this ShowClusterDetailResponse.

        :param public_kibana_resp: The public_kibana_resp of this ShowClusterDetailResponse.
        :type public_kibana_resp: :class:`huaweicloudsdkcss.v1.PublicKibanaRespBody`
        """
        self._public_kibana_resp = public_kibana_resp

    @property
    def elb_white_list(self):
        """Gets the elb_white_list of this ShowClusterDetailResponse.

        :return: The elb_white_list of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.ElbWhiteListResp`
        """
        return self._elb_white_list

    @elb_white_list.setter
    def elb_white_list(self, elb_white_list):
        """Sets the elb_white_list of this ShowClusterDetailResponse.

        :param elb_white_list: The elb_white_list of this ShowClusterDetailResponse.
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.ElbWhiteListResp`
        """
        self._elb_white_list = elb_white_list

    @property
    def updated(self):
        """Gets the updated of this ShowClusterDetailResponse.

        集群上次修改时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。

        :return: The updated of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowClusterDetailResponse.

        集群上次修改时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。

        :param updated: The updated of this ShowClusterDetailResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def name(self):
        """Gets the name of this ShowClusterDetailResponse.

        集群名称。

        :return: The name of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowClusterDetailResponse.

        集群名称。

        :param name: The name of this ShowClusterDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def public_ip(self):
        """Gets the public_ip of this ShowClusterDetailResponse.

        公网IP信息。

        :return: The public_ip of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ShowClusterDetailResponse.

        公网IP信息。

        :param public_ip: The public_ip of this ShowClusterDetailResponse.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def created(self):
        """Gets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。

        :return: The created of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601： CCYY-MM-DDThh:mm:ss。

        :param created: The created of this ShowClusterDetailResponse.
        :type created: str
        """
        self._created = created

    @property
    def id(self):
        """Gets the id of this ShowClusterDetailResponse.

        集群ID。

        :return: The id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowClusterDetailResponse.

        集群ID。

        :param id: The id of this ShowClusterDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowClusterDetailResponse.

        集群状态值。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :return: The status of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClusterDetailResponse.

        集群状态值。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :param status: The status of this ShowClusterDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def endpoint(self):
        """Gets the endpoint of this ShowClusterDetailResponse.

        用户VPC访问IP地址和端口号。

        :return: The endpoint of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ShowClusterDetailResponse.

        用户VPC访问IP地址和端口号。

        :param endpoint: The endpoint of this ShowClusterDetailResponse.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowClusterDetailResponse.

        VPC ID。

        :return: The vpc_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowClusterDetailResponse.

        VPC ID。

        :param vpc_id: The vpc_id of this ShowClusterDetailResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowClusterDetailResponse.

        子网ID。

        :return: The subnet_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowClusterDetailResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ShowClusterDetailResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowClusterDetailResponse.

        安全组ID。

        :return: The security_group_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowClusterDetailResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowClusterDetailResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def vpcep_ip(self):
        """Gets the vpcep_ip of this ShowClusterDetailResponse.

        终端节点IP。

        :return: The vpcep_ip of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._vpcep_ip

    @vpcep_ip.setter
    def vpcep_ip(self, vpcep_ip):
        """Sets the vpcep_ip of this ShowClusterDetailResponse.

        终端节点IP。

        :param vpcep_ip: The vpcep_ip of this ShowClusterDetailResponse.
        :type vpcep_ip: str
        """
        self._vpcep_ip = vpcep_ip

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this ShowClusterDetailResponse.

        公网带宽大小。单位：Mbit/s

        :return: The bandwidth_size of this ShowClusterDetailResponse.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this ShowClusterDetailResponse.

        公网带宽大小。单位：Mbit/s

        :param bandwidth_size: The bandwidth_size of this ShowClusterDetailResponse.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def https_enable(self):
        """Gets the https_enable of this ShowClusterDetailResponse.

        通信加密状态。 - false：未设置通信加密。 - true：已设置通信加密。

        :return: The https_enable of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this ShowClusterDetailResponse.

        通信加密状态。 - false：未设置通信加密。 - true：已设置通信加密。

        :param https_enable: The https_enable of this ShowClusterDetailResponse.
        :type https_enable: bool
        """
        self._https_enable = https_enable

    @property
    def disk_encrypted(self):
        """Gets the disk_encrypted of this ShowClusterDetailResponse.

        磁盘是否加密。  - true : 磁盘已加密。 - false : 磁盘未加密。

        :return: The disk_encrypted of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._disk_encrypted

    @disk_encrypted.setter
    def disk_encrypted(self, disk_encrypted):
        """Sets the disk_encrypted of this ShowClusterDetailResponse.

        磁盘是否加密。  - true : 磁盘已加密。 - false : 磁盘未加密。

        :param disk_encrypted: The disk_encrypted of this ShowClusterDetailResponse.
        :type disk_encrypted: bool
        """
        self._disk_encrypted = disk_encrypted

    @property
    def authority_enable(self):
        """Gets the authority_enable of this ShowClusterDetailResponse.

        是否开启认证，取值范围为true或false。默认关闭认证功能。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :return: The authority_enable of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._authority_enable

    @authority_enable.setter
    def authority_enable(self, authority_enable):
        """Sets the authority_enable of this ShowClusterDetailResponse.

        是否开启认证，取值范围为true或false。默认关闭认证功能。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :param authority_enable: The authority_enable of this ShowClusterDetailResponse.
        :type authority_enable: bool
        """
        self._authority_enable = authority_enable

    @property
    def backup_available(self):
        """Gets the backup_available of this ShowClusterDetailResponse.

        快照是否开启。 - true: 快照开启状态。 - false: 快照关闭状态。

        :return: The backup_available of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._backup_available

    @backup_available.setter
    def backup_available(self, backup_available):
        """Sets the backup_available of this ShowClusterDetailResponse.

        快照是否开启。 - true: 快照开启状态。 - false: 快照关闭状态。

        :param backup_available: The backup_available of this ShowClusterDetailResponse.
        :type backup_available: bool
        """
        self._backup_available = backup_available

    @property
    def action_progress(self):
        """Gets the action_progress of this ShowClusterDetailResponse.

        集群行为进度，显示创建或扩容进度的百分比。

        :return: The action_progress of this ShowClusterDetailResponse.
        :rtype: object
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ShowClusterDetailResponse.

        集群行为进度，显示创建或扩容进度的百分比。

        :param action_progress: The action_progress of this ShowClusterDetailResponse.
        :type action_progress: object
        """
        self._action_progress = action_progress

    @property
    def actions(self):
        """Gets the actions of this ShowClusterDetailResponse.

        集群当前行为。REBOOTING表示重启、GROWING表示扩容、RESTORING表示恢复集群、SNAPSHOTTING表示创建快照等。

        :return: The actions of this ShowClusterDetailResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ShowClusterDetailResponse.

        集群当前行为。REBOOTING表示重启、GROWING表示扩容、RESTORING表示恢复集群、SNAPSHOTTING表示创建快照等。

        :param actions: The actions of this ShowClusterDetailResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowClusterDetailResponse.

        集群所属的企业项目ID。  如果集群所属用户没有开通企业项目，则不会返回该参数。

        :return: The enterprise_project_id of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowClusterDetailResponse.

        集群所属的企业项目ID。  如果集群所属用户没有开通企业项目，则不会返回该参数。

        :param enterprise_project_id: The enterprise_project_id of this ShowClusterDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ShowClusterDetailResponse.

        集群标签。

        :return: The tags of this ShowClusterDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ClusterDetailTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowClusterDetailResponse.

        集群标签。

        :param tags: The tags of this ShowClusterDetailResponse.
        :type tags: list[:class:`huaweicloudsdkcss.v1.ClusterDetailTags`]
        """
        self._tags = tags

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ShowClusterDetailResponse.

        :return: The failed_reason of this ShowClusterDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.ClusterDetailFailedReasons`
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ShowClusterDetailResponse.

        :param failed_reason: The failed_reason of this ShowClusterDetailResponse.
        :type failed_reason: :class:`huaweicloudsdkcss.v1.ClusterDetailFailedReasons`
        """
        self._failed_reason = failed_reason

    @property
    def period(self):
        """Gets the period of this ShowClusterDetailResponse.

        是否为包周期集群。 - \"true\" 表示是包周期计费的集群。 - \"false\" 表示是按需计费的集群。

        :return: The period of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowClusterDetailResponse.

        是否为包周期集群。 - \"true\" 表示是包周期计费的集群。 - \"false\" 表示是按需计费的集群。

        :param period: The period of this ShowClusterDetailResponse.
        :type period: bool
        """
        self._period = period

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
        if not isinstance(other, ShowClusterDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
