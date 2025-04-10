# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessClientResponse(SdkResponse):

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
        'access_mode': 'str',
        'status': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'access_connections': 'list[AccessConnectionInfo]',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'access_mode': 'access_mode',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'access_connections': 'access_connections',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, access_mode=None, status=None, vpc_id=None, subnet_id=None, access_connections=None, create_time=None):
        r"""CreateAccessClientResponse

        The model defined in huaweicloud sdk

        :param id: 客户端ID
        :type id: str
        :param name: 客户端名称
        :type name: str
        :param access_mode: 接入模式,SYSTEM,CUSTOM,AUTO
        :type access_mode: str
        :param status: 客户端状态,CREATING,RUNNING,DELETING,DELETED,CREATE_FAIL,DELETE_FAIL
        :type status: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param access_connections: 接入连接列表
        :type access_connections: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionInfo`]
        :param create_time: 实例创建时间戳
        :type create_time: datetime
        """
        
        super(CreateAccessClientResponse, self).__init__()

        self._id = None
        self._name = None
        self._access_mode = None
        self._status = None
        self._vpc_id = None
        self._subnet_id = None
        self._access_connections = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if access_mode is not None:
            self.access_mode = access_mode
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if access_connections is not None:
            self.access_connections = access_connections
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this CreateAccessClientResponse.

        客户端ID

        :return: The id of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAccessClientResponse.

        客户端ID

        :param id: The id of this CreateAccessClientResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateAccessClientResponse.

        客户端名称

        :return: The name of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAccessClientResponse.

        客户端名称

        :param name: The name of this CreateAccessClientResponse.
        :type name: str
        """
        self._name = name

    @property
    def access_mode(self):
        r"""Gets the access_mode of this CreateAccessClientResponse.

        接入模式,SYSTEM,CUSTOM,AUTO

        :return: The access_mode of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        r"""Sets the access_mode of this CreateAccessClientResponse.

        接入模式,SYSTEM,CUSTOM,AUTO

        :param access_mode: The access_mode of this CreateAccessClientResponse.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def status(self):
        r"""Gets the status of this CreateAccessClientResponse.

        客户端状态,CREATING,RUNNING,DELETING,DELETED,CREATE_FAIL,DELETE_FAIL

        :return: The status of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAccessClientResponse.

        客户端状态,CREATING,RUNNING,DELETING,DELETED,CREATE_FAIL,DELETE_FAIL

        :param status: The status of this CreateAccessClientResponse.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateAccessClientResponse.

        VPC ID

        :return: The vpc_id of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateAccessClientResponse.

        VPC ID

        :param vpc_id: The vpc_id of this CreateAccessClientResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateAccessClientResponse.

        子网ID

        :return: The subnet_id of this CreateAccessClientResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateAccessClientResponse.

        子网ID

        :param subnet_id: The subnet_id of this CreateAccessClientResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def access_connections(self):
        r"""Gets the access_connections of this CreateAccessClientResponse.

        接入连接列表

        :return: The access_connections of this CreateAccessClientResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionInfo`]
        """
        return self._access_connections

    @access_connections.setter
    def access_connections(self, access_connections):
        r"""Sets the access_connections of this CreateAccessClientResponse.

        接入连接列表

        :param access_connections: The access_connections of this CreateAccessClientResponse.
        :type access_connections: list[:class:`huaweicloudsdklakeformation.v1.AccessConnectionInfo`]
        """
        self._access_connections = access_connections

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateAccessClientResponse.

        实例创建时间戳

        :return: The create_time of this CreateAccessClientResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateAccessClientResponse.

        实例创建时间戳

        :param create_time: The create_time of this CreateAccessClientResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, CreateAccessClientResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
