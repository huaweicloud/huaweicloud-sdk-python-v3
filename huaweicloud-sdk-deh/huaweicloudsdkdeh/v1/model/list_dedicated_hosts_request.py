# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dedicated_host_id': 'str',
        'name': 'str',
        'host_type': 'str',
        'host_type_name': 'str',
        'flavor': 'str',
        'state': 'str',
        'tenant': 'str',
        'availability_zone': 'str',
        'limit': 'int',
        'marker': 'str',
        'tags': 'str',
        'instance_uuid': 'str',
        'released_at': 'str',
        'changes_since': 'str'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id',
        'name': 'name',
        'host_type': 'host_type',
        'host_type_name': 'host_type_name',
        'flavor': 'flavor',
        'state': 'state',
        'tenant': 'tenant',
        'availability_zone': 'availability_zone',
        'limit': 'limit',
        'marker': 'marker',
        'tags': 'tags',
        'instance_uuid': 'instance_uuid',
        'released_at': 'released_at',
        'changes_since': 'changes-since'
    }

    def __init__(self, dedicated_host_id=None, name=None, host_type=None, host_type_name=None, flavor=None, state=None, tenant=None, availability_zone=None, limit=None, marker=None, tags=None, instance_uuid=None, released_at=None, changes_since=None):
        """ListDedicatedHostsRequest

        The model defined in huaweicloud sdk

        :param dedicated_host_id: 专属主机ID。
        :type dedicated_host_id: str
        :param name: 专属主机名称。
        :type name: str
        :param host_type: 专属主机类型。
        :type host_type: str
        :param host_type_name: 专属主机类型的名称。
        :type host_type_name: str
        :param flavor: 规格ID。
        :type flavor: str
        :param state: 专属主机状态。  取值范围：“available”、“fault”或“released”。
        :type state: str
        :param tenant: 取值范围：租户ID或“all”。  只有管理员可以指定该参数。
        :type tenant: str
        :param availability_zone: 专属主机所属AZ。
        :type availability_zone: str
        :param limit: 每个页面上显示的条目数。
        :type limit: int
        :param marker: 该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。
        :type marker: str
        :param tags: 专属主机标签。
        :type tags: str
        :param instance_uuid: 专属主机上的云服务器ID。
        :type instance_uuid: str
        :param released_at: 专属主机的释放时间。
        :type released_at: str
        :param changes_since: 当专属主机更新了状态时，按日期和时间戳过滤响应。为了便于记录更改，还可能返回最近删除的专属主机。  日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm  如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。
        :type changes_since: str
        """
        
        

        self._dedicated_host_id = None
        self._name = None
        self._host_type = None
        self._host_type_name = None
        self._flavor = None
        self._state = None
        self._tenant = None
        self._availability_zone = None
        self._limit = None
        self._marker = None
        self._tags = None
        self._instance_uuid = None
        self._released_at = None
        self._changes_since = None
        self.discriminator = None

        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if name is not None:
            self.name = name
        if host_type is not None:
            self.host_type = host_type
        if host_type_name is not None:
            self.host_type_name = host_type_name
        if flavor is not None:
            self.flavor = flavor
        if state is not None:
            self.state = state
        if tenant is not None:
            self.tenant = tenant
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if tags is not None:
            self.tags = tags
        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if released_at is not None:
            self.released_at = released_at
        if changes_since is not None:
            self.changes_since = changes_since

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ListDedicatedHostsRequest.

        专属主机ID。

        :return: The dedicated_host_id of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ListDedicatedHostsRequest.

        专属主机ID。

        :param dedicated_host_id: The dedicated_host_id of this ListDedicatedHostsRequest.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def name(self):
        """Gets the name of this ListDedicatedHostsRequest.

        专属主机名称。

        :return: The name of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDedicatedHostsRequest.

        专属主机名称。

        :param name: The name of this ListDedicatedHostsRequest.
        :type name: str
        """
        self._name = name

    @property
    def host_type(self):
        """Gets the host_type of this ListDedicatedHostsRequest.

        专属主机类型。

        :return: The host_type of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this ListDedicatedHostsRequest.

        专属主机类型。

        :param host_type: The host_type of this ListDedicatedHostsRequest.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_type_name(self):
        """Gets the host_type_name of this ListDedicatedHostsRequest.

        专属主机类型的名称。

        :return: The host_type_name of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._host_type_name

    @host_type_name.setter
    def host_type_name(self, host_type_name):
        """Sets the host_type_name of this ListDedicatedHostsRequest.

        专属主机类型的名称。

        :param host_type_name: The host_type_name of this ListDedicatedHostsRequest.
        :type host_type_name: str
        """
        self._host_type_name = host_type_name

    @property
    def flavor(self):
        """Gets the flavor of this ListDedicatedHostsRequest.

        规格ID。

        :return: The flavor of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ListDedicatedHostsRequest.

        规格ID。

        :param flavor: The flavor of this ListDedicatedHostsRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def state(self):
        """Gets the state of this ListDedicatedHostsRequest.

        专属主机状态。  取值范围：“available”、“fault”或“released”。

        :return: The state of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListDedicatedHostsRequest.

        专属主机状态。  取值范围：“available”、“fault”或“released”。

        :param state: The state of this ListDedicatedHostsRequest.
        :type state: str
        """
        self._state = state

    @property
    def tenant(self):
        """Gets the tenant of this ListDedicatedHostsRequest.

        取值范围：租户ID或“all”。  只有管理员可以指定该参数。

        :return: The tenant of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this ListDedicatedHostsRequest.

        取值范围：租户ID或“all”。  只有管理员可以指定该参数。

        :param tenant: The tenant of this ListDedicatedHostsRequest.
        :type tenant: str
        """
        self._tenant = tenant

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListDedicatedHostsRequest.

        专属主机所属AZ。

        :return: The availability_zone of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListDedicatedHostsRequest.

        专属主机所属AZ。

        :param availability_zone: The availability_zone of this ListDedicatedHostsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def limit(self):
        """Gets the limit of this ListDedicatedHostsRequest.

        每个页面上显示的条目数。

        :return: The limit of this ListDedicatedHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDedicatedHostsRequest.

        每个页面上显示的条目数。

        :param limit: The limit of this ListDedicatedHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDedicatedHostsRequest.

        该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。

        :return: The marker of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDedicatedHostsRequest.

        该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。

        :param marker: The marker of this ListDedicatedHostsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def tags(self):
        """Gets the tags of this ListDedicatedHostsRequest.

        专属主机标签。

        :return: The tags of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListDedicatedHostsRequest.

        专属主机标签。

        :param tags: The tags of this ListDedicatedHostsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this ListDedicatedHostsRequest.

        专属主机上的云服务器ID。

        :return: The instance_uuid of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this ListDedicatedHostsRequest.

        专属主机上的云服务器ID。

        :param instance_uuid: The instance_uuid of this ListDedicatedHostsRequest.
        :type instance_uuid: str
        """
        self._instance_uuid = instance_uuid

    @property
    def released_at(self):
        """Gets the released_at of this ListDedicatedHostsRequest.

        专属主机的释放时间。

        :return: The released_at of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        """Sets the released_at of this ListDedicatedHostsRequest.

        专属主机的释放时间。

        :param released_at: The released_at of this ListDedicatedHostsRequest.
        :type released_at: str
        """
        self._released_at = released_at

    @property
    def changes_since(self):
        """Gets the changes_since of this ListDedicatedHostsRequest.

        当专属主机更新了状态时，按日期和时间戳过滤响应。为了便于记录更改，还可能返回最近删除的专属主机。  日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm  如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。

        :return: The changes_since of this ListDedicatedHostsRequest.
        :rtype: str
        """
        return self._changes_since

    @changes_since.setter
    def changes_since(self, changes_since):
        """Sets the changes_since of this ListDedicatedHostsRequest.

        当专属主机更新了状态时，按日期和时间戳过滤响应。为了便于记录更改，还可能返回最近删除的专属主机。  日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm  如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。

        :param changes_since: The changes_since of this ListDedicatedHostsRequest.
        :type changes_since: str
        """
        self._changes_since = changes_since

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
        if not isinstance(other, ListDedicatedHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
