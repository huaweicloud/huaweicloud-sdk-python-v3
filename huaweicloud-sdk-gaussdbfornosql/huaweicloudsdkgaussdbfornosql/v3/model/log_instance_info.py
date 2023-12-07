# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogInstanceInfo:

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
        'status': 'str',
        'mode': 'str',
        'datastore': 'InstancesDatastoreResult',
        'actions': 'list[str]',
        'enterprise_project_id': 'str',
        'supported_log_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'mode': 'mode',
        'datastore': 'datastore',
        'actions': 'actions',
        'enterprise_project_id': 'enterprise_project_id',
        'supported_log_types': 'supported_log_types'
    }

    def __init__(self, id=None, name=None, status=None, mode=None, datastore=None, actions=None, enterprise_project_id=None, supported_log_types=None):
        """LogInstanceInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param status: 实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点失败。
        :type status: str
        :param mode: 实例类型。 - 取值为“Cluster”，表示GeminiDB Redis集群实例类型。
        :type mode: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.InstancesDatastoreResult`
        :param actions: 实例正在执行的动作。
        :type actions: list[str]
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param supported_log_types: 日志类型。slow_log表示慢日志，audit_log表示审计日志。
        :type supported_log_types: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._mode = None
        self._datastore = None
        self._actions = None
        self._enterprise_project_id = None
        self._supported_log_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if mode is not None:
            self.mode = mode
        if datastore is not None:
            self.datastore = datastore
        if actions is not None:
            self.actions = actions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if supported_log_types is not None:
            self.supported_log_types = supported_log_types

    @property
    def id(self):
        """Gets the id of this LogInstanceInfo.

        实例ID。

        :return: The id of this LogInstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogInstanceInfo.

        实例ID。

        :param id: The id of this LogInstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this LogInstanceInfo.

        实例名称。

        :return: The name of this LogInstanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogInstanceInfo.

        实例名称。

        :param name: The name of this LogInstanceInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this LogInstanceInfo.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点失败。

        :return: The status of this LogInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LogInstanceInfo.

        实例状态。 取值： - normal，表示实例正常。 - abnormal，表示实例异常。 - creating，表示实例创建中。 - frozen，表示实例被冻结。 - data_disk_full，表示实例磁盘已满。 - createfail，表示实例创建失败。 - enlargefail，表示实例扩容节点失败。

        :param status: The status of this LogInstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def mode(self):
        """Gets the mode of this LogInstanceInfo.

        实例类型。 - 取值为“Cluster”，表示GeminiDB Redis集群实例类型。

        :return: The mode of this LogInstanceInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this LogInstanceInfo.

        实例类型。 - 取值为“Cluster”，表示GeminiDB Redis集群实例类型。

        :param mode: The mode of this LogInstanceInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def datastore(self):
        """Gets the datastore of this LogInstanceInfo.

        :return: The datastore of this LogInstanceInfo.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.InstancesDatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this LogInstanceInfo.

        :param datastore: The datastore of this LogInstanceInfo.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.InstancesDatastoreResult`
        """
        self._datastore = datastore

    @property
    def actions(self):
        """Gets the actions of this LogInstanceInfo.

        实例正在执行的动作。

        :return: The actions of this LogInstanceInfo.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this LogInstanceInfo.

        实例正在执行的动作。

        :param actions: The actions of this LogInstanceInfo.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LogInstanceInfo.

        企业项目ID。

        :return: The enterprise_project_id of this LogInstanceInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LogInstanceInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this LogInstanceInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def supported_log_types(self):
        """Gets the supported_log_types of this LogInstanceInfo.

        日志类型。slow_log表示慢日志，audit_log表示审计日志。

        :return: The supported_log_types of this LogInstanceInfo.
        :rtype: list[str]
        """
        return self._supported_log_types

    @supported_log_types.setter
    def supported_log_types(self, supported_log_types):
        """Sets the supported_log_types of this LogInstanceInfo.

        日志类型。slow_log表示慢日志，audit_log表示审计日志。

        :param supported_log_types: The supported_log_types of this LogInstanceInfo.
        :type supported_log_types: list[str]
        """
        self._supported_log_types = supported_log_types

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
        if not isinstance(other, LogInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
