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
        'updated': 'str',
        'name': 'str',
        'created': 'str',
        'id': 'str',
        'status': 'str',
        'endpoint': 'str',
        'action_progress': 'ClusterDetailActionProgress',
        'actions': 'list[ActionReq]',
        'failed_reasons': 'ClusterDetailFailedReasons',
        'authority_enable': 'bool',
        'https_enable': 'bool',
        'enterprise_project_id': 'str',
        'tags': 'list[ClusterDetailTags]'
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
        'https_enable': 'httpsEnable',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, datastore=None, instances=None, updated=None, name=None, created=None, id=None, status=None, endpoint=None, action_progress=None, actions=None, failed_reasons=None, authority_enable=None, https_enable=None, enterprise_project_id=None, tags=None):
        """ShowClusterDetailResponse - a model defined in huaweicloud sdk"""
        
        super(ShowClusterDetailResponse, self).__init__()

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
        self._https_enable = None
        self._enterprise_project_id = None
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
        if https_enable is not None:
            self.https_enable = https_enable
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def datastore(self):
        """Gets the datastore of this ShowClusterDetailResponse.


        :return: The datastore of this ShowClusterDetailResponse.
        :rtype: ClusterDetailDatastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ShowClusterDetailResponse.


        :param datastore: The datastore of this ShowClusterDetailResponse.
        :type: ClusterDetailDatastore
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this ShowClusterDetailResponse.

        节点对象列表。

        :return: The instances of this ShowClusterDetailResponse.
        :rtype: list[ClusterDetailInstances]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ShowClusterDetailResponse.

        节点对象列表。

        :param instances: The instances of this ShowClusterDetailResponse.
        :type: list[ClusterDetailInstances]
        """
        self._instances = instances

    @property
    def updated(self):
        """Gets the updated of this ShowClusterDetailResponse.

        集群上次修改时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :return: The updated of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowClusterDetailResponse.

        集群上次修改时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :param updated: The updated of this ShowClusterDetailResponse.
        :type: str
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
        :type: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :return: The created of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ShowClusterDetailResponse.

        集群创建时间，格式为ISO8601: CCYY-MM-DDThh:mm:ss。

        :param created: The created of this ShowClusterDetailResponse.
        :type: str
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
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowClusterDetailResponse.

        查询返回值。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :return: The status of this ShowClusterDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClusterDetailResponse.

        查询返回值。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :param status: The status of this ShowClusterDetailResponse.
        :type: str
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
        :type: str
        """
        self._endpoint = endpoint

    @property
    def action_progress(self):
        """Gets the action_progress of this ShowClusterDetailResponse.


        :return: The action_progress of this ShowClusterDetailResponse.
        :rtype: ClusterDetailActionProgress
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ShowClusterDetailResponse.


        :param action_progress: The action_progress of this ShowClusterDetailResponse.
        :type: ClusterDetailActionProgress
        """
        self._action_progress = action_progress

    @property
    def actions(self):
        """Gets the actions of this ShowClusterDetailResponse.

        集群当前行为集合。

        :return: The actions of this ShowClusterDetailResponse.
        :rtype: list[ActionReq]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ShowClusterDetailResponse.

        集群当前行为集合。

        :param actions: The actions of this ShowClusterDetailResponse.
        :type: list[ActionReq]
        """
        self._actions = actions

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this ShowClusterDetailResponse.


        :return: The failed_reasons of this ShowClusterDetailResponse.
        :rtype: ClusterDetailFailedReasons
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this ShowClusterDetailResponse.


        :param failed_reasons: The failed_reasons of this ShowClusterDetailResponse.
        :type: ClusterDetailFailedReasons
        """
        self._failed_reasons = failed_reasons

    @property
    def authority_enable(self):
        """Gets the authority_enable of this ShowClusterDetailResponse.

        是否开启认证，取值范围为true或false。默认关闭认证功能。当开启认证时，httpsEnable需要设置为true。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :return: The authority_enable of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._authority_enable

    @authority_enable.setter
    def authority_enable(self, authority_enable):
        """Sets the authority_enable of this ShowClusterDetailResponse.

        是否开启认证，取值范围为true或false。默认关闭认证功能。当开启认证时，httpsEnable需要设置为true。 - true：表示集群开启认证。 - false：表示集群不开启认证。

        :param authority_enable: The authority_enable of this ShowClusterDetailResponse.
        :type: bool
        """
        self._authority_enable = authority_enable

    @property
    def https_enable(self):
        """Gets the https_enable of this ShowClusterDetailResponse.


        :return: The https_enable of this ShowClusterDetailResponse.
        :rtype: bool
        """
        return self._https_enable

    @https_enable.setter
    def https_enable(self, https_enable):
        """Sets the https_enable of this ShowClusterDetailResponse.


        :param https_enable: The https_enable of this ShowClusterDetailResponse.
        :type: bool
        """
        self._https_enable = https_enable

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
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ShowClusterDetailResponse.

        集群标签。

        :return: The tags of this ShowClusterDetailResponse.
        :rtype: list[ClusterDetailTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowClusterDetailResponse.

        集群标签。

        :param tags: The tags of this ShowClusterDetailResponse.
        :type: list[ClusterDetailTags]
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
        if not isinstance(other, ShowClusterDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
