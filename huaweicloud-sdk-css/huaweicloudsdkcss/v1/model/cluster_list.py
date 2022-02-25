# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datastore': 'ClusterListDatastore',
        'instances': 'list[ClusterListInstances]',
        'updated': 'str',
        'name': 'str',
        'created': 'str',
        'id': 'str',
        'status': 'str',
        'endpoint': 'str',
        'action_progress': 'ClusterListActionProgress',
        'actions': 'list[str]',
        'failed_reasons': 'ClusterListFailedReasons',
        'authority_enable': 'bool',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'enterprise_project_id': 'str',
        'period': 'bool',
        'https_enable': 'bool',
        'tags': 'list[ClusterListTags]'
    }

    attribute_map = {
        'datastore': 'datastore',
        'instances': 'instances',
        'updated': 'updated',
        'name': 'name',
        'created': 'created',
        'id': 'id',
        'status': 'status',
        'endpoint': 'endpoint',
        'action_progress': 'actionProgress',
        'actions': 'actions',
        'failed_reasons': 'failed_reasons',
        'authority_enable': 'authorityEnable',
        'vpc_id': 'vpcId',
        'subnet_id': 'subnetId',
        'security_group_id': 'securityGroupId',
        'enterprise_project_id': 'enterprise_project_id',
        'period': 'period',
        'https_enable': 'httpsEnable',
        'tags': 'tags'
    }

    def __init__(self, datastore=None, instances=None, updated=None, name=None, created=None, id=None, status=None, endpoint=None, action_progress=None, actions=None, failed_reasons=None, authority_enable=None, vpc_id=None, subnet_id=None, security_group_id=None, enterprise_project_id=None, period=None, https_enable=None, tags=None):
        """ClusterList - a model defined in huaweicloud sdk"""
        
        

        self._datastore = None
        self._instances = None
        self._updated = None
        self._name = None
        self._created = None
        self._id = None
        self._status = None
        self._endpoint = None
        self._action_progress = None
        self._actions = None
        self._failed_reasons = None
        self._authority_enable = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._enterprise_project_id = None
        self._period = None
        self._https_enable = None
        self._tags = None
        self.discriminator = None

        if datastore is not None:
            self.datastore = datastore
        if instances is not None:
            self.instances = instances
        if updated is not None:
            self.updated = updated
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if endpoint is not None:
            self.endpoint = endpoint
        if action_progress is not None:
            self.action_progress = action_progress
        if actions is not None:
            self.actions = actions
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons
        if authority_enable is not None:
            self.authority_enable = authority_enable
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if period is not None:
            self.period = period
        if https_enable is not None:
            self.https_enable = https_enable
        if tags is not None:
            self.tags = tags

    @property
    def datastore(self):
        """Gets the datastore of this ClusterList.


        :return: The datastore of this ClusterList.
        :rtype: ClusterListDatastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ClusterList.


        :param datastore: The datastore of this ClusterList.
        :type: ClusterListDatastore
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this ClusterList.

        节点对象列表。

        :return: The instances of this ClusterList.
        :rtype: list[ClusterListInstances]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ClusterList.

        节点对象列表。

        :param instances: The instances of this ClusterList.
        :type: list[ClusterListInstances]
        """
        self._instances = instances

    @property
    def updated(self):
        """Gets the updated of this ClusterList.

        集群上次修改时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :return: The updated of this ClusterList.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ClusterList.

        集群上次修改时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :param updated: The updated of this ClusterList.
        :type: str
        """
        self._updated = updated

    @property
    def name(self):
        """Gets the name of this ClusterList.

        集群名称。

        :return: The name of this ClusterList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterList.

        集群名称。

        :param name: The name of this ClusterList.
        :type: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ClusterList.

        集群创建时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。     说明：返回的集群列表信息按照创建时间降序排序，即创建时间最新的集群排在最前。

        :return: The created of this ClusterList.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClusterList.

        集群创建时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。     说明：返回的集群列表信息按照创建时间降序排序，即创建时间最新的集群排在最前。

        :param created: The created of this ClusterList.
        :type: str
        """
        self._created = created

    @property
    def id(self):
        """Gets the id of this ClusterList.

        集群ID。

        :return: The id of this ClusterList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterList.

        集群ID。

        :param id: The id of this ClusterList.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ClusterList.

        查询返回值。  - 100：创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :return: The status of this ClusterList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterList.

        查询返回值。  - 100：创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :param status: The status of this ClusterList.
        :type: str
        """
        self._status = status

    @property
    def endpoint(self):
        """Gets the endpoint of this ClusterList.

        用户VPC访问IP地址和端口号。

        :return: The endpoint of this ClusterList.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ClusterList.

        用户VPC访问IP地址和端口号。

        :param endpoint: The endpoint of this ClusterList.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def action_progress(self):
        """Gets the action_progress of this ClusterList.


        :return: The action_progress of this ClusterList.
        :rtype: ClusterListActionProgress
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ClusterList.


        :param action_progress: The action_progress of this ClusterList.
        :type: ClusterListActionProgress
        """
        self._action_progress = action_progress

    @property
    def actions(self):
        """Gets the actions of this ClusterList.

        集群当前行为，REBOOTING表示重启，GROWING表示扩容，RESTORING表示恢复集群，SNAPSHOTTING表示创建快照。

        :return: The actions of this ClusterList.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ClusterList.

        集群当前行为，REBOOTING表示重启，GROWING表示扩容，RESTORING表示恢复集群，SNAPSHOTTING表示创建快照。

        :param actions: The actions of this ClusterList.
        :type: list[str]
        """
        self._actions = actions

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this ClusterList.


        :return: The failed_reasons of this ClusterList.
        :rtype: ClusterListFailedReasons
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this ClusterList.


        :param failed_reasons: The failed_reasons of this ClusterList.
        :type: ClusterListFailedReasons
        """
        self._failed_reasons = failed_reasons

    @property
    def authority_enable(self):
        """Gets the authority_enable of this ClusterList.

        是否开启认证，取值范围为true或false。默认关闭认证功能。当开启认证时，httpsEnable需要设置为true。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :return: The authority_enable of this ClusterList.
        :rtype: bool
        """
        return self._authority_enable

    @authority_enable.setter
    def authority_enable(self, authority_enable):
        """Sets the authority_enable of this ClusterList.

        是否开启认证，取值范围为true或false。默认关闭认证功能。当开启认证时，httpsEnable需要设置为true。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :param authority_enable: The authority_enable of this ClusterList.
        :type: bool
        """
        self._authority_enable = authority_enable

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClusterList.

        VPC ID。

        :return: The vpc_id of this ClusterList.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClusterList.

        VPC ID。

        :param vpc_id: The vpc_id of this ClusterList.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ClusterList.

        子网ID。

        :return: The subnet_id of this ClusterList.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ClusterList.

        子网ID。

        :param subnet_id: The subnet_id of this ClusterList.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ClusterList.

        安全组ID。

        :return: The security_group_id of this ClusterList.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ClusterList.

        安全组ID。

        :param security_group_id: The security_group_id of this ClusterList.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ClusterList.

        集群所属的企业项目ID。  如果集群所属用户没有开通企业项目，则不会返回该参数。

        :return: The enterprise_project_id of this ClusterList.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ClusterList.

        集群所属的企业项目ID。  如果集群所属用户没有开通企业项目，则不会返回该参数。

        :param enterprise_project_id: The enterprise_project_id of this ClusterList.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def period(self):
        """Gets the period of this ClusterList.

        是为包周期集群。

        :return: The period of this ClusterList.
        :rtype: bool
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ClusterList.

        是为包周期集群。

        :param period: The period of this ClusterList.
        :type: bool
        """
        self._period = period

    @property
    def https_enable(self):
        """Gets the https_enable of this ClusterList.

        是否开启https访问。

        :return: The https_enable of this ClusterList.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this ClusterList.

        是否开启https访问。

        :param https_enable: The https_enable of this ClusterList.
        :type: bool
        """
        self._https_enable = https_enable

    @property
    def tags(self):
        """Gets the tags of this ClusterList.

        集群标签。

        :return: The tags of this ClusterList.
        :rtype: list[ClusterListTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClusterList.

        集群标签。

        :param tags: The tags of this ClusterList.
        :type: list[ClusterListTags]
        """
        self._tags = tags

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
        if not isinstance(other, ClusterList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
