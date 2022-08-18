# coding: utf-8

import re
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
        'network_version': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_name': 'server_name',
        'server_id': 'server_id',
        'network_version': 'network_version'
    }

    def __init__(self, offset=None, limit=None, server_name=None, server_id=None, network_version=None):
        """ListCloudPhoneServersRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param server_name: 云手机服务器名称，支持模糊查询。
        :type server_name: str
        :param server_id: 服务器id。
        :type server_id: str
        :param network_version: 云手机服务器是否为自定义网络标识 - v1：系统定义网络的云手机服务器。 - v2：自定义网络的云手机服务器。
        :type network_version: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_name = None
        self._server_id = None
        self._network_version = None
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

    @property
    def offset(self):
        """Gets the offset of this ListCloudPhoneServersRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCloudPhoneServersRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListCloudPhoneServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCloudPhoneServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListCloudPhoneServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCloudPhoneServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListCloudPhoneServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_name(self):
        """Gets the server_name of this ListCloudPhoneServersRequest.

        云手机服务器名称，支持模糊查询。

        :return: The server_name of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this ListCloudPhoneServersRequest.

        云手机服务器名称，支持模糊查询。

        :param server_name: The server_name of this ListCloudPhoneServersRequest.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_id(self):
        """Gets the server_id of this ListCloudPhoneServersRequest.

        服务器id。

        :return: The server_id of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListCloudPhoneServersRequest.

        服务器id。

        :param server_id: The server_id of this ListCloudPhoneServersRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def network_version(self):
        """Gets the network_version of this ListCloudPhoneServersRequest.

        云手机服务器是否为自定义网络标识 - v1：系统定义网络的云手机服务器。 - v2：自定义网络的云手机服务器。

        :return: The network_version of this ListCloudPhoneServersRequest.
        :rtype: str
        """
        return self._network_version

    @network_version.setter
    def network_version(self, network_version):
        """Sets the network_version of this ListCloudPhoneServersRequest.

        云手机服务器是否为自定义网络标识 - v1：系统定义网络的云手机服务器。 - v2：自定义网络的云手机服务器。

        :param network_version: The network_version of this ListCloudPhoneServersRequest.
        :type network_version: str
        """
        self._network_version = network_version

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
