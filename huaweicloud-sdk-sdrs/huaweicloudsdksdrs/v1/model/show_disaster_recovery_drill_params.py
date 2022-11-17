# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDisasterRecoveryDrillParams:

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
        'drill_vpc_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'server_group_id': 'str',
        'drill_servers': 'list[DrillServerParams]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'drill_vpc_id': 'drill_vpc_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'server_group_id': 'server_group_id',
        'drill_servers': 'drill_servers'
    }

    def __init__(self, id=None, name=None, status=None, drill_vpc_id=None, created_at=None, updated_at=None, server_group_id=None, drill_servers=None):
        """ShowDisasterRecoveryDrillParams

        The model defined in huaweicloud sdk

        :param id: 容灾演练的ID。
        :type id: str
        :param name: 容灾演练的名称。
        :type name: str
        :param status: 容灾演练的状态。
        :type status: str
        :param drill_vpc_id: 演练虚拟私有云id。
        :type drill_vpc_id: str
        :param created_at: 创建时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type created_at: str
        :param updated_at: 更新时间。默认格式为：\&quot;yyyy-MM-dd HH:mm:ss.SSS\&quot;，例：\&quot;2019-04-01 12:00:00.000\&quot;。
        :type updated_at: str
        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param drill_servers: 演练云服务器列表。
        :type drill_servers: list[:class:`huaweicloudsdksdrs.v1.DrillServerParams`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._drill_vpc_id = None
        self._created_at = None
        self._updated_at = None
        self._server_group_id = None
        self._drill_servers = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.drill_vpc_id = drill_vpc_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.server_group_id = server_group_id
        self.drill_servers = drill_servers

    @property
    def id(self):
        """Gets the id of this ShowDisasterRecoveryDrillParams.

        容灾演练的ID。

        :return: The id of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDisasterRecoveryDrillParams.

        容灾演练的ID。

        :param id: The id of this ShowDisasterRecoveryDrillParams.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDisasterRecoveryDrillParams.

        容灾演练的名称。

        :return: The name of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDisasterRecoveryDrillParams.

        容灾演练的名称。

        :param name: The name of this ShowDisasterRecoveryDrillParams.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ShowDisasterRecoveryDrillParams.

        容灾演练的状态。

        :return: The status of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDisasterRecoveryDrillParams.

        容灾演练的状态。

        :param status: The status of this ShowDisasterRecoveryDrillParams.
        :type status: str
        """
        self._status = status

    @property
    def drill_vpc_id(self):
        """Gets the drill_vpc_id of this ShowDisasterRecoveryDrillParams.

        演练虚拟私有云id。

        :return: The drill_vpc_id of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._drill_vpc_id

    @drill_vpc_id.setter
    def drill_vpc_id(self, drill_vpc_id):
        """Sets the drill_vpc_id of this ShowDisasterRecoveryDrillParams.

        演练虚拟私有云id。

        :param drill_vpc_id: The drill_vpc_id of this ShowDisasterRecoveryDrillParams.
        :type drill_vpc_id: str
        """
        self._drill_vpc_id = drill_vpc_id

    @property
    def created_at(self):
        """Gets the created_at of this ShowDisasterRecoveryDrillParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The created_at of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowDisasterRecoveryDrillParams.

        创建时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param created_at: The created_at of this ShowDisasterRecoveryDrillParams.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowDisasterRecoveryDrillParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :return: The updated_at of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowDisasterRecoveryDrillParams.

        更新时间。默认格式为：\"yyyy-MM-dd HH:mm:ss.SSS\"，例：\"2019-04-01 12:00:00.000\"。

        :param updated_at: The updated_at of this ShowDisasterRecoveryDrillParams.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ShowDisasterRecoveryDrillParams.

        保护组的ID。

        :return: The server_group_id of this ShowDisasterRecoveryDrillParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ShowDisasterRecoveryDrillParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this ShowDisasterRecoveryDrillParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def drill_servers(self):
        """Gets the drill_servers of this ShowDisasterRecoveryDrillParams.

        演练云服务器列表。

        :return: The drill_servers of this ShowDisasterRecoveryDrillParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.DrillServerParams`]
        """
        return self._drill_servers

    @drill_servers.setter
    def drill_servers(self, drill_servers):
        """Sets the drill_servers of this ShowDisasterRecoveryDrillParams.

        演练云服务器列表。

        :param drill_servers: The drill_servers of this ShowDisasterRecoveryDrillParams.
        :type drill_servers: list[:class:`huaweicloudsdksdrs.v1.DrillServerParams`]
        """
        self._drill_servers = drill_servers

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
        if not isinstance(other, ShowDisasterRecoveryDrillParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
