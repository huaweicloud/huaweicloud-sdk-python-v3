# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceNodeDTO:

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
        'private_ip': 'str',
        'status': 'str',
        'create_user': 'str',
        'create_time': 'str',
        'gateway_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'private_ip': 'private_ip',
        'status': 'status',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'gateway_version': 'gateway_version'
    }

    def __init__(self, id=None, name=None, private_ip=None, status=None, create_user=None, create_time=None, gateway_version=None):
        """InstanceNodeDTO

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param private_ip: 节点IP地址。
        :type private_ip: str
        :param status: 节点状态。
        :type status: str
        :param create_user: 节点创建人。
        :type create_user: str
        :param create_time: 节点创建时间。
        :type create_time: str
        :param gateway_version: 节点版本号。
        :type gateway_version: str
        """
        
        

        self._id = None
        self._name = None
        self._private_ip = None
        self._status = None
        self._create_user = None
        self._create_time = None
        self._gateway_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if private_ip is not None:
            self.private_ip = private_ip
        if status is not None:
            self.status = status
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if gateway_version is not None:
            self.gateway_version = gateway_version

    @property
    def id(self):
        """Gets the id of this InstanceNodeDTO.

        节点ID。

        :return: The id of this InstanceNodeDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceNodeDTO.

        节点ID。

        :param id: The id of this InstanceNodeDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this InstanceNodeDTO.

        节点名称。

        :return: The name of this InstanceNodeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceNodeDTO.

        节点名称。

        :param name: The name of this InstanceNodeDTO.
        :type name: str
        """
        self._name = name

    @property
    def private_ip(self):
        """Gets the private_ip of this InstanceNodeDTO.

        节点IP地址。

        :return: The private_ip of this InstanceNodeDTO.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this InstanceNodeDTO.

        节点IP地址。

        :param private_ip: The private_ip of this InstanceNodeDTO.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def status(self):
        """Gets the status of this InstanceNodeDTO.

        节点状态。

        :return: The status of this InstanceNodeDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceNodeDTO.

        节点状态。

        :param status: The status of this InstanceNodeDTO.
        :type status: str
        """
        self._status = status

    @property
    def create_user(self):
        """Gets the create_user of this InstanceNodeDTO.

        节点创建人。

        :return: The create_user of this InstanceNodeDTO.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this InstanceNodeDTO.

        节点创建人。

        :param create_user: The create_user of this InstanceNodeDTO.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this InstanceNodeDTO.

        节点创建时间。

        :return: The create_time of this InstanceNodeDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceNodeDTO.

        节点创建时间。

        :param create_time: The create_time of this InstanceNodeDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def gateway_version(self):
        """Gets the gateway_version of this InstanceNodeDTO.

        节点版本号。

        :return: The gateway_version of this InstanceNodeDTO.
        :rtype: str
        """
        return self._gateway_version

    @gateway_version.setter
    def gateway_version(self, gateway_version):
        """Sets the gateway_version of this InstanceNodeDTO.

        节点版本号。

        :param gateway_version: The gateway_version of this InstanceNodeDTO.
        :type gateway_version: str
        """
        self._gateway_version = gateway_version

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
        if not isinstance(other, InstanceNodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
