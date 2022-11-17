# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateExternalEntityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'space_id': 'str',
        'external_id': 'str',
        'protocol': 'str',
        'connection_type': 'str',
        'create_time': 'str',
        'last_modify_time': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'space_id': 'space_id',
        'external_id': 'external_id',
        'protocol': 'protocol',
        'connection_type': 'connection_type',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, node_id=None, space_id=None, external_id=None, protocol=None, connection_type=None, create_time=None, last_modify_time=None):
        """UpdateExternalEntityResponse

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param space_id: 资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.
        :type space_id: str
        :param external_id: 外部实体ID
        :type external_id: str
        :param protocol: 接入协议类型
        :type protocol: str
        :param connection_type: 连接类型(client和server)
        :type connection_type: str
        :param create_time: 创建时间
        :type create_time: str
        :param last_modify_time: 最后修改时间
        :type last_modify_time: str
        """
        
        super(UpdateExternalEntityResponse, self).__init__()

        self._node_id = None
        self._space_id = None
        self._external_id = None
        self._protocol = None
        self._connection_type = None
        self._create_time = None
        self._last_modify_time = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if space_id is not None:
            self.space_id = space_id
        if external_id is not None:
            self.external_id = external_id
        if protocol is not None:
            self.protocol = protocol
        if connection_type is not None:
            self.connection_type = connection_type
        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time

    @property
    def node_id(self):
        """Gets the node_id of this UpdateExternalEntityResponse.

        节点ID

        :return: The node_id of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateExternalEntityResponse.

        节点ID

        :param node_id: The node_id of this UpdateExternalEntityResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def space_id(self):
        """Gets the space_id of this UpdateExternalEntityResponse.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.

        :return: The space_id of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this UpdateExternalEntityResponse.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.

        :param space_id: The space_id of this UpdateExternalEntityResponse.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def external_id(self):
        """Gets the external_id of this UpdateExternalEntityResponse.

        外部实体ID

        :return: The external_id of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this UpdateExternalEntityResponse.

        外部实体ID

        :param external_id: The external_id of this UpdateExternalEntityResponse.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def protocol(self):
        """Gets the protocol of this UpdateExternalEntityResponse.

        接入协议类型

        :return: The protocol of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateExternalEntityResponse.

        接入协议类型

        :param protocol: The protocol of this UpdateExternalEntityResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def connection_type(self):
        """Gets the connection_type of this UpdateExternalEntityResponse.

        连接类型(client和server)

        :return: The connection_type of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this UpdateExternalEntityResponse.

        连接类型(client和server)

        :param connection_type: The connection_type of this UpdateExternalEntityResponse.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def create_time(self):
        """Gets the create_time of this UpdateExternalEntityResponse.

        创建时间

        :return: The create_time of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateExternalEntityResponse.

        创建时间

        :param create_time: The create_time of this UpdateExternalEntityResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this UpdateExternalEntityResponse.

        最后修改时间

        :return: The last_modify_time of this UpdateExternalEntityResponse.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this UpdateExternalEntityResponse.

        最后修改时间

        :param last_modify_time: The last_modify_time of this UpdateExternalEntityResponse.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

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
        if not isinstance(other, UpdateExternalEntityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
