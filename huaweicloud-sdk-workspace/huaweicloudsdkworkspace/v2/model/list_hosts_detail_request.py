# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'availability_zone': 'str',
        'host_id': 'str',
        'enterprise_project_id': 'str',
        'host_type': 'str',
        'host_type_name': 'str',
        'state': 'str',
        'limit': 'int',
        'offset': 'int',
        'marker': 'str',
        'changes_since': 'str'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'host_id': 'host_id',
        'enterprise_project_id': 'enterprise_project_id',
        'host_type': 'host_type',
        'host_type_name': 'host_type_name',
        'state': 'state',
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'changes_since': 'changes_since'
    }

    def __init__(self, name=None, availability_zone=None, host_id=None, enterprise_project_id=None, host_type=None, host_type_name=None, state=None, limit=None, offset=None, marker=None, changes_since=None):
        r"""ListHostsDetailRequest

        The model defined in huaweicloud sdk

        :param name: 云办公主机名称。
        :type name: str
        :param availability_zone: 云办公主机所属区域。
        :type availability_zone: str
        :param host_id: 云办公主机的id。
        :type host_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param host_type: 类型。
        :type host_type: str
        :param host_type_name: 云办公主机类型名称。
        :type host_type_name: str
        :param state: 云办公主机状态，available-可用的，fault-错误的，released-释放的。
        :type state: str
        :param limit: 每页显示的数量。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param marker: 上一页显示的最后记录的id，与offset同时使用时不生效。
        :type marker: str
        :param changes_since: 过滤指定时间起状态变更的专属主机。 日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm 如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。
        :type changes_since: str
        """
        
        

        self._name = None
        self._availability_zone = None
        self._host_id = None
        self._enterprise_project_id = None
        self._host_type = None
        self._host_type_name = None
        self._state = None
        self._limit = None
        self._offset = None
        self._marker = None
        self._changes_since = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if host_id is not None:
            self.host_id = host_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_type is not None:
            self.host_type = host_type
        if host_type_name is not None:
            self.host_type_name = host_type_name
        if state is not None:
            self.state = state
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if changes_since is not None:
            self.changes_since = changes_since

    @property
    def name(self):
        r"""Gets the name of this ListHostsDetailRequest.

        云办公主机名称。

        :return: The name of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListHostsDetailRequest.

        云办公主机名称。

        :param name: The name of this ListHostsDetailRequest.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListHostsDetailRequest.

        云办公主机所属区域。

        :return: The availability_zone of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListHostsDetailRequest.

        云办公主机所属区域。

        :param availability_zone: The availability_zone of this ListHostsDetailRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostsDetailRequest.

        云办公主机的id。

        :return: The host_id of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostsDetailRequest.

        云办公主机的id。

        :param host_id: The host_id of this ListHostsDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostsDetailRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostsDetailRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListHostsDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_type(self):
        r"""Gets the host_type of this ListHostsDetailRequest.

        类型。

        :return: The host_type of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this ListHostsDetailRequest.

        类型。

        :param host_type: The host_type of this ListHostsDetailRequest.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_type_name(self):
        r"""Gets the host_type_name of this ListHostsDetailRequest.

        云办公主机类型名称。

        :return: The host_type_name of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._host_type_name

    @host_type_name.setter
    def host_type_name(self, host_type_name):
        r"""Sets the host_type_name of this ListHostsDetailRequest.

        云办公主机类型名称。

        :param host_type_name: The host_type_name of this ListHostsDetailRequest.
        :type host_type_name: str
        """
        self._host_type_name = host_type_name

    @property
    def state(self):
        r"""Gets the state of this ListHostsDetailRequest.

        云办公主机状态，available-可用的，fault-错误的，released-释放的。

        :return: The state of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListHostsDetailRequest.

        云办公主机状态，available-可用的，fault-错误的，released-释放的。

        :param state: The state of this ListHostsDetailRequest.
        :type state: str
        """
        self._state = state

    @property
    def limit(self):
        r"""Gets the limit of this ListHostsDetailRequest.

        每页显示的数量。

        :return: The limit of this ListHostsDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostsDetailRequest.

        每页显示的数量。

        :param limit: The limit of this ListHostsDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHostsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListHostsDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostsDetailRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListHostsDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListHostsDetailRequest.

        上一页显示的最后记录的id，与offset同时使用时不生效。

        :return: The marker of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListHostsDetailRequest.

        上一页显示的最后记录的id，与offset同时使用时不生效。

        :param marker: The marker of this ListHostsDetailRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def changes_since(self):
        r"""Gets the changes_since of this ListHostsDetailRequest.

        过滤指定时间起状态变更的专属主机。 日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm 如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。

        :return: The changes_since of this ListHostsDetailRequest.
        :rtype: str
        """
        return self._changes_since

    @changes_since.setter
    def changes_since(self, changes_since):
        r"""Sets the changes_since of this ListHostsDetailRequest.

        过滤指定时间起状态变更的专属主机。 日期和时间戳的格式为ISO 8601：CCYY-MM-DDThh:mm:ss±hh:mm 如果包含“hh:mm”值，则将时区作为UTC的偏移量返回。例如，“2015-08-27T09:49:58-05:00”。如果您省略时区，则假定为UTC时区。

        :param changes_since: The changes_since of this ListHostsDetailRequest.
        :type changes_since: str
        """
        self._changes_since = changes_since

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
        if not isinstance(other, ListHostsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
