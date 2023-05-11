# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListenerDetail:

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
        'description': 'str',
        'protocol': 'ListenerProtocol',
        'status': 'ConfigStatus',
        'port_ranges': 'list[PortRange]',
        'client_affinity': 'ClientAffinity',
        'accelerator_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'frozen_info': 'FrozenInfo',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'protocol': 'protocol',
        'status': 'status',
        'port_ranges': 'port_ranges',
        'client_affinity': 'client_affinity',
        'accelerator_id': 'accelerator_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'frozen_info': 'frozen_info',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, protocol=None, status=None, port_ranges=None, client_affinity=None, accelerator_id=None, created_at=None, updated_at=None, domain_id=None, frozen_info=None, tags=None):
        """ListenerDetail

        The model defined in huaweicloud sdk

        :param id: 监听器ID。
        :type id: str
        :param name: 监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param protocol: 
        :type protocol: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        :param status: 
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        :param port_ranges: 监听端口范围列表。
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        :param client_affinity: 
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        :param accelerator_id: 全球加速实例ID。
        :type accelerator_id: str
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param domain_id: 租户ID。
        :type domain_id: str
        :param frozen_info: 
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._protocol = None
        self._status = None
        self._port_ranges = None
        self._client_affinity = None
        self._accelerator_id = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._frozen_info = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if port_ranges is not None:
            self.port_ranges = port_ranges
        if client_affinity is not None:
            self.client_affinity = client_affinity
        if accelerator_id is not None:
            self.accelerator_id = accelerator_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if frozen_info is not None:
            self.frozen_info = frozen_info
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this ListenerDetail.

        监听器ID。

        :return: The id of this ListenerDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListenerDetail.

        监听器ID。

        :param id: The id of this ListenerDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListenerDetail.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this ListenerDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListenerDetail.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this ListenerDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListenerDetail.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this ListenerDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListenerDetail.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this ListenerDetail.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        """Gets the protocol of this ListenerDetail.

        :return: The protocol of this ListenerDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListenerDetail.

        :param protocol: The protocol of this ListenerDetail.
        :type protocol: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        """
        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this ListenerDetail.

        :return: The status of this ListenerDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListenerDetail.

        :param status: The status of this ListenerDetail.
        :type status: :class:`huaweicloudsdkga.v1.ConfigStatus`
        """
        self._status = status

    @property
    def port_ranges(self):
        """Gets the port_ranges of this ListenerDetail.

        监听端口范围列表。

        :return: The port_ranges of this ListenerDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """Sets the port_ranges of this ListenerDetail.

        监听端口范围列表。

        :param port_ranges: The port_ranges of this ListenerDetail.
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        self._port_ranges = port_ranges

    @property
    def client_affinity(self):
        """Gets the client_affinity of this ListenerDetail.

        :return: The client_affinity of this ListenerDetail.
        :rtype: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        return self._client_affinity

    @client_affinity.setter
    def client_affinity(self, client_affinity):
        """Sets the client_affinity of this ListenerDetail.

        :param client_affinity: The client_affinity of this ListenerDetail.
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        self._client_affinity = client_affinity

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this ListenerDetail.

        全球加速实例ID。

        :return: The accelerator_id of this ListenerDetail.
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this ListenerDetail.

        全球加速实例ID。

        :param accelerator_id: The accelerator_id of this ListenerDetail.
        :type accelerator_id: str
        """
        self._accelerator_id = accelerator_id

    @property
    def created_at(self):
        """Gets the created_at of this ListenerDetail.

        创建时间。

        :return: The created_at of this ListenerDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListenerDetail.

        创建时间。

        :param created_at: The created_at of this ListenerDetail.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListenerDetail.

        更新时间。

        :return: The updated_at of this ListenerDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListenerDetail.

        更新时间。

        :param updated_at: The updated_at of this ListenerDetail.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this ListenerDetail.

        租户ID。

        :return: The domain_id of this ListenerDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListenerDetail.

        租户ID。

        :param domain_id: The domain_id of this ListenerDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def frozen_info(self):
        """Gets the frozen_info of this ListenerDetail.

        :return: The frozen_info of this ListenerDetail.
        :rtype: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        return self._frozen_info

    @frozen_info.setter
    def frozen_info(self, frozen_info):
        """Sets the frozen_info of this ListenerDetail.

        :param frozen_info: The frozen_info of this ListenerDetail.
        :type frozen_info: :class:`huaweicloudsdkga.v1.FrozenInfo`
        """
        self._frozen_info = frozen_info

    @property
    def tags(self):
        """Gets the tags of this ListenerDetail.

        标签列表。

        :return: The tags of this ListenerDetail.
        :rtype: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListenerDetail.

        标签列表。

        :param tags: The tags of this ListenerDetail.
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ListenerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
