# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'server_name': 'str',
        'server_id': 'str',
        'network_version': 'str',
        'phone_model_name': 'str',
        'create_since': 'int',
        'create_until': 'int',
        'status': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_name': 'server_name',
        'server_id': 'server_id',
        'network_version': 'network_version',
        'phone_model_name': 'phone_model_name',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'status': 'status'
    }

    def __init__(self, offset=None, limit=None, server_name=None, server_id=None, network_version=None, phone_model_name=None, create_since=None, create_until=None, status=None):
        r"""ListCloudPhoneServersRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param server_name: 云手机服务器名称，支持模糊查询。
        :type server_name: str
        :param server_id: 云手机服务器的唯一标识。
        :type server_id: str
        :param network_version: 云手机服务器是否为自定义网络标识。 - v1：系统定义网络的云手机服务器 - v2：自定义网络的云手机服务器
        :type network_version: str
        :param phone_model_name: 手机规格名称。
        :type phone_model_name: str
        :param create_since: 查询的起始时间戳。
        :type create_since: int
        :param create_until: 查询的结束时间戳。
        :type create_until: int
        :param status: 服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中
        :type status: int
        """
        
        

        self._offset = None
        self._limit = None
        self._server_name = None
        self._server_id = None
        self._network_version = None
        self._phone_model_name = None
        self._create_since = None
        self._create_until = None
        self._status = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if server_name is not None:
            self.server_name = server_name
        if server_id is not None:
            self.server_id = server_id
        if network_version is not None:
            self.network_version = network_version
        if phone_model_name is not None:
            self.phone_model_name = phone_model_name
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if status is not None:
            self.status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListCloudPhoneServersRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCloudPhoneServersRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListCloudPhoneServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCloudPhoneServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCloudPhoneServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListCloudPhoneServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_name(self):
        r"""Gets the server_name of this ListCloudPhoneServersRequest.

        云手机服务器名称，支持模糊查询。

        :return: The server_name of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListCloudPhoneServersRequest.

        云手机服务器名称，支持模糊查询。

        :param server_name: The server_name of this ListCloudPhoneServersRequest.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_id(self):
        r"""Gets the server_id of this ListCloudPhoneServersRequest.

        云手机服务器的唯一标识。

        :return: The server_id of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListCloudPhoneServersRequest.

        云手机服务器的唯一标识。

        :param server_id: The server_id of this ListCloudPhoneServersRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def network_version(self):
        r"""Gets the network_version of this ListCloudPhoneServersRequest.

        云手机服务器是否为自定义网络标识。 - v1：系统定义网络的云手机服务器 - v2：自定义网络的云手机服务器

        :return: The network_version of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._network_version

    @network_version.setter
    def network_version(self, network_version):
        r"""Sets the network_version of this ListCloudPhoneServersRequest.

        云手机服务器是否为自定义网络标识。 - v1：系统定义网络的云手机服务器 - v2：自定义网络的云手机服务器

        :param network_version: The network_version of this ListCloudPhoneServersRequest.
        :type network_version: str
        """
        self._network_version = network_version

    @property
    def phone_model_name(self):
        r"""Gets the phone_model_name of this ListCloudPhoneServersRequest.

        手机规格名称。

        :return: The phone_model_name of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        r"""Sets the phone_model_name of this ListCloudPhoneServersRequest.

        手机规格名称。

        :param phone_model_name: The phone_model_name of this ListCloudPhoneServersRequest.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def create_since(self):
        r"""Gets the create_since of this ListCloudPhoneServersRequest.

        查询的起始时间戳。

        :return: The create_since of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListCloudPhoneServersRequest.

        查询的起始时间戳。

        :param create_since: The create_since of this ListCloudPhoneServersRequest.
        :type create_since: int
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this ListCloudPhoneServersRequest.

        查询的结束时间戳。

        :return: The create_until of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListCloudPhoneServersRequest.

        查询的结束时间戳。

        :param create_until: The create_until of this ListCloudPhoneServersRequest.
        :type create_until: int
        """
        self._create_until = create_until

    @property
    def status(self):
        r"""Gets the status of this ListCloudPhoneServersRequest.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :return: The status of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCloudPhoneServersRequest.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :param status: The status of this ListCloudPhoneServersRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListCloudPhoneServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
