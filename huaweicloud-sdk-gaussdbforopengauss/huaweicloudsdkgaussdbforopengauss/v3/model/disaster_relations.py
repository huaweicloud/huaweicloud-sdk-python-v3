# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisasterRelations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_type': 'str',
        'name': 'str',
        'disaster_role': 'str',
        'created': 'str',
        'updated': 'str',
        'slave_region_instance_info': 'RegionInstanceInfo',
        'master_region_instance_info': 'RegionInstanceInfo',
        'id': 'str',
        'synchronization_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'status': 'str',
        'precheck_failed_reason': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'disaster_type': 'disaster_type',
        'name': 'name',
        'disaster_role': 'disaster_role',
        'created': 'created',
        'updated': 'updated',
        'slave_region_instance_info': 'slave_region_instance_info',
        'master_region_instance_info': 'master_region_instance_info',
        'id': 'id',
        'synchronization_id': 'synchronization_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'status': 'status',
        'precheck_failed_reason': 'precheck_failed_reason',
        'actions': 'actions'
    }

    def __init__(self, disaster_type=None, name=None, disaster_role=None, created=None, updated=None, slave_region_instance_info=None, master_region_instance_info=None, id=None, synchronization_id=None, instance_id=None, instance_name=None, instance_status=None, status=None, precheck_failed_reason=None, actions=None):
        r"""DisasterRelations

        The model defined in huaweicloud sdk

        :param disaster_type: 容灾类型。
        :type disaster_type: str
        :param name: 容灾任务名称。
        :type name: str
        :param disaster_role: 容灾角色。
        :type disaster_role: str
        :param created: 创建时间，格式为“yyyy-mm-dd hh:mm:ss”。
        :type created: str
        :param updated: 更新时间，格式为“yyyy-mm-dd hh:mm:ss”。
        :type updated: str
        :param slave_region_instance_info: 
        :type slave_region_instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        :param master_region_instance_info: 
        :type master_region_instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        :param id: 容灾记录id。
        :type id: str
        :param synchronization_id: 容灾关系唯一id。
        :type synchronization_id: str
        :param instance_id: 当前region实例id。
        :type instance_id: str
        :param instance_name: 当前region实例名称。
        :type instance_name: str
        :param instance_status: 当前region实例状态。
        :type instance_status: str
        :param status: 容灾记录状态。
        :type status: str
        :param precheck_failed_reason: 预校验失败原因。
        :type precheck_failed_reason: str
        :param actions: 实例当前操作action。
        :type actions: list[str]
        """
        
        

        self._disaster_type = None
        self._name = None
        self._disaster_role = None
        self._created = None
        self._updated = None
        self._slave_region_instance_info = None
        self._master_region_instance_info = None
        self._id = None
        self._synchronization_id = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._status = None
        self._precheck_failed_reason = None
        self._actions = None
        self.discriminator = None

        if disaster_type is not None:
            self.disaster_type = disaster_type
        if name is not None:
            self.name = name
        if disaster_role is not None:
            self.disaster_role = disaster_role
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if slave_region_instance_info is not None:
            self.slave_region_instance_info = slave_region_instance_info
        if master_region_instance_info is not None:
            self.master_region_instance_info = master_region_instance_info
        if id is not None:
            self.id = id
        if synchronization_id is not None:
            self.synchronization_id = synchronization_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if status is not None:
            self.status = status
        if precheck_failed_reason is not None:
            self.precheck_failed_reason = precheck_failed_reason
        if actions is not None:
            self.actions = actions

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this DisasterRelations.

        容灾类型。

        :return: The disaster_type of this DisasterRelations.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this DisasterRelations.

        容灾类型。

        :param disaster_type: The disaster_type of this DisasterRelations.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

    @property
    def name(self):
        r"""Gets the name of this DisasterRelations.

        容灾任务名称。

        :return: The name of this DisasterRelations.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DisasterRelations.

        容灾任务名称。

        :param name: The name of this DisasterRelations.
        :type name: str
        """
        self._name = name

    @property
    def disaster_role(self):
        r"""Gets the disaster_role of this DisasterRelations.

        容灾角色。

        :return: The disaster_role of this DisasterRelations.
        :rtype: str
        """
        return self._disaster_role

    @disaster_role.setter
    def disaster_role(self, disaster_role):
        r"""Sets the disaster_role of this DisasterRelations.

        容灾角色。

        :param disaster_role: The disaster_role of this DisasterRelations.
        :type disaster_role: str
        """
        self._disaster_role = disaster_role

    @property
    def created(self):
        r"""Gets the created of this DisasterRelations.

        创建时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :return: The created of this DisasterRelations.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this DisasterRelations.

        创建时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :param created: The created of this DisasterRelations.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this DisasterRelations.

        更新时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :return: The updated of this DisasterRelations.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this DisasterRelations.

        更新时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :param updated: The updated of this DisasterRelations.
        :type updated: str
        """
        self._updated = updated

    @property
    def slave_region_instance_info(self):
        r"""Gets the slave_region_instance_info of this DisasterRelations.

        :return: The slave_region_instance_info of this DisasterRelations.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        """
        return self._slave_region_instance_info

    @slave_region_instance_info.setter
    def slave_region_instance_info(self, slave_region_instance_info):
        r"""Sets the slave_region_instance_info of this DisasterRelations.

        :param slave_region_instance_info: The slave_region_instance_info of this DisasterRelations.
        :type slave_region_instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        """
        self._slave_region_instance_info = slave_region_instance_info

    @property
    def master_region_instance_info(self):
        r"""Gets the master_region_instance_info of this DisasterRelations.

        :return: The master_region_instance_info of this DisasterRelations.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        """
        return self._master_region_instance_info

    @master_region_instance_info.setter
    def master_region_instance_info(self, master_region_instance_info):
        r"""Sets the master_region_instance_info of this DisasterRelations.

        :param master_region_instance_info: The master_region_instance_info of this DisasterRelations.
        :type master_region_instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.RegionInstanceInfo`
        """
        self._master_region_instance_info = master_region_instance_info

    @property
    def id(self):
        r"""Gets the id of this DisasterRelations.

        容灾记录id。

        :return: The id of this DisasterRelations.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DisasterRelations.

        容灾记录id。

        :param id: The id of this DisasterRelations.
        :type id: str
        """
        self._id = id

    @property
    def synchronization_id(self):
        r"""Gets the synchronization_id of this DisasterRelations.

        容灾关系唯一id。

        :return: The synchronization_id of this DisasterRelations.
        :rtype: str
        """
        return self._synchronization_id

    @synchronization_id.setter
    def synchronization_id(self, synchronization_id):
        r"""Sets the synchronization_id of this DisasterRelations.

        容灾关系唯一id。

        :param synchronization_id: The synchronization_id of this DisasterRelations.
        :type synchronization_id: str
        """
        self._synchronization_id = synchronization_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DisasterRelations.

        当前region实例id。

        :return: The instance_id of this DisasterRelations.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DisasterRelations.

        当前region实例id。

        :param instance_id: The instance_id of this DisasterRelations.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DisasterRelations.

        当前region实例名称。

        :return: The instance_name of this DisasterRelations.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DisasterRelations.

        当前region实例名称。

        :param instance_name: The instance_name of this DisasterRelations.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this DisasterRelations.

        当前region实例状态。

        :return: The instance_status of this DisasterRelations.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this DisasterRelations.

        当前region实例状态。

        :param instance_status: The instance_status of this DisasterRelations.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def status(self):
        r"""Gets the status of this DisasterRelations.

        容灾记录状态。

        :return: The status of this DisasterRelations.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DisasterRelations.

        容灾记录状态。

        :param status: The status of this DisasterRelations.
        :type status: str
        """
        self._status = status

    @property
    def precheck_failed_reason(self):
        r"""Gets the precheck_failed_reason of this DisasterRelations.

        预校验失败原因。

        :return: The precheck_failed_reason of this DisasterRelations.
        :rtype: str
        """
        return self._precheck_failed_reason

    @precheck_failed_reason.setter
    def precheck_failed_reason(self, precheck_failed_reason):
        r"""Sets the precheck_failed_reason of this DisasterRelations.

        预校验失败原因。

        :param precheck_failed_reason: The precheck_failed_reason of this DisasterRelations.
        :type precheck_failed_reason: str
        """
        self._precheck_failed_reason = precheck_failed_reason

    @property
    def actions(self):
        r"""Gets the actions of this DisasterRelations.

        实例当前操作action。

        :return: The actions of this DisasterRelations.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this DisasterRelations.

        实例当前操作action。

        :param actions: The actions of this DisasterRelations.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, DisasterRelations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
