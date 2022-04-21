# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAvailableRdsList:

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
        'project_id': 'str',
        'status': 'str',
        'name': 'str',
        'engine_name': 'str',
        'engine_software_version': 'str',
        'private_ip': 'str',
        'mode': 'str',
        'port': 'int',
        'az_code': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'projectId',
        'status': 'status',
        'name': 'name',
        'engine_name': 'engineName',
        'engine_software_version': 'engineSoftwareVersion',
        'private_ip': 'privateIp',
        'mode': 'mode',
        'port': 'port',
        'az_code': 'azCode',
        'time_zone': 'timeZone'
    }

    def __init__(self, id=None, project_id=None, status=None, name=None, engine_name=None, engine_software_version=None, private_ip=None, mode=None, port=None, az_code=None, time_zone=None):
        """QueryAvailableRdsList

        The model defined in huaweicloud sdk

        :param id: 数据库实例 ID。
        :type id: str
        :param project_id: 数据库实例所在租户在某一region下的project ID。
        :type project_id: str
        :param status: 数据库实例状态。
        :type status: str
        :param name: 数据库实例名称。
        :type name: str
        :param engine_name: 数据库实例引擎名称。
        :type engine_name: str
        :param engine_software_version: 数据库实例引擎版本。
        :type engine_software_version: str
        :param private_ip: 数据库实例内网连接地址。
        :type private_ip: str
        :param mode: 数据库实例类型（主备或单机）。
        :type mode: str
        :param port: 数据库实例端口。
        :type port: int
        :param az_code: 可用区。
        :type az_code: str
        :param time_zone: 时区。
        :type time_zone: str
        """
        
        

        self._id = None
        self._project_id = None
        self._status = None
        self._name = None
        self._engine_name = None
        self._engine_software_version = None
        self._private_ip = None
        self._mode = None
        self._port = None
        self._az_code = None
        self._time_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_software_version is not None:
            self.engine_software_version = engine_software_version
        if private_ip is not None:
            self.private_ip = private_ip
        if mode is not None:
            self.mode = mode
        if port is not None:
            self.port = port
        if az_code is not None:
            self.az_code = az_code
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        """Gets the id of this QueryAvailableRdsList.

        数据库实例 ID。

        :return: The id of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryAvailableRdsList.

        数据库实例 ID。

        :param id: The id of this QueryAvailableRdsList.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this QueryAvailableRdsList.

        数据库实例所在租户在某一region下的project ID。

        :return: The project_id of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this QueryAvailableRdsList.

        数据库实例所在租户在某一region下的project ID。

        :param project_id: The project_id of this QueryAvailableRdsList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this QueryAvailableRdsList.

        数据库实例状态。

        :return: The status of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryAvailableRdsList.

        数据库实例状态。

        :param status: The status of this QueryAvailableRdsList.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this QueryAvailableRdsList.

        数据库实例名称。

        :return: The name of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryAvailableRdsList.

        数据库实例名称。

        :param name: The name of this QueryAvailableRdsList.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        """Gets the engine_name of this QueryAvailableRdsList.

        数据库实例引擎名称。

        :return: The engine_name of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this QueryAvailableRdsList.

        数据库实例引擎名称。

        :param engine_name: The engine_name of this QueryAvailableRdsList.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_software_version(self):
        """Gets the engine_software_version of this QueryAvailableRdsList.

        数据库实例引擎版本。

        :return: The engine_software_version of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._engine_software_version

    @engine_software_version.setter
    def engine_software_version(self, engine_software_version):
        """Sets the engine_software_version of this QueryAvailableRdsList.

        数据库实例引擎版本。

        :param engine_software_version: The engine_software_version of this QueryAvailableRdsList.
        :type engine_software_version: str
        """
        self._engine_software_version = engine_software_version

    @property
    def private_ip(self):
        """Gets the private_ip of this QueryAvailableRdsList.

        数据库实例内网连接地址。

        :return: The private_ip of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this QueryAvailableRdsList.

        数据库实例内网连接地址。

        :param private_ip: The private_ip of this QueryAvailableRdsList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def mode(self):
        """Gets the mode of this QueryAvailableRdsList.

        数据库实例类型（主备或单机）。

        :return: The mode of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this QueryAvailableRdsList.

        数据库实例类型（主备或单机）。

        :param mode: The mode of this QueryAvailableRdsList.
        :type mode: str
        """
        self._mode = mode

    @property
    def port(self):
        """Gets the port of this QueryAvailableRdsList.

        数据库实例端口。

        :return: The port of this QueryAvailableRdsList.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this QueryAvailableRdsList.

        数据库实例端口。

        :param port: The port of this QueryAvailableRdsList.
        :type port: int
        """
        self._port = port

    @property
    def az_code(self):
        """Gets the az_code of this QueryAvailableRdsList.

        可用区。

        :return: The az_code of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this QueryAvailableRdsList.

        可用区。

        :param az_code: The az_code of this QueryAvailableRdsList.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def time_zone(self):
        """Gets the time_zone of this QueryAvailableRdsList.

        时区。

        :return: The time_zone of this QueryAvailableRdsList.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this QueryAvailableRdsList.

        时区。

        :param time_zone: The time_zone of this QueryAvailableRdsList.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, QueryAvailableRdsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
