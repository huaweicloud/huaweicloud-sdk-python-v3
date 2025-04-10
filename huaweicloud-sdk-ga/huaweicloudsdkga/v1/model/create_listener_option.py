# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateListenerOption:

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
        'description': 'str',
        'protocol': 'ListenerProtocol',
        'port_ranges': 'list[PortRange]',
        'client_affinity': 'ClientAffinity',
        'accelerator_id': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'protocol': 'protocol',
        'port_ranges': 'port_ranges',
        'client_affinity': 'client_affinity',
        'accelerator_id': 'accelerator_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, protocol=None, port_ranges=None, client_affinity=None, accelerator_id=None, tags=None):
        r"""CreateListenerOption

        The model defined in huaweicloud sdk

        :param name: 监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param protocol: 
        :type protocol: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        :param port_ranges: 监听端口范围列表。
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        :param client_affinity: 
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        :param accelerator_id: 全球加速实例ID。
        :type accelerator_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        
        

        self._name = None
        self._description = None
        self._protocol = None
        self._port_ranges = None
        self._client_affinity = None
        self._accelerator_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.protocol = protocol
        self.port_ranges = port_ranges
        if client_affinity is not None:
            self.client_affinity = client_affinity
        self.accelerator_id = accelerator_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateListenerOption.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this CreateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateListenerOption.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this CreateListenerOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateListenerOption.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this CreateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateListenerOption.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this CreateListenerOption.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        r"""Gets the protocol of this CreateListenerOption.

        :return: The protocol of this CreateListenerOption.
        :rtype: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CreateListenerOption.

        :param protocol: The protocol of this CreateListenerOption.
        :type protocol: :class:`huaweicloudsdkga.v1.ListenerProtocol`
        """
        self._protocol = protocol

    @property
    def port_ranges(self):
        r"""Gets the port_ranges of this CreateListenerOption.

        监听端口范围列表。

        :return: The port_ranges of this CreateListenerOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        r"""Sets the port_ranges of this CreateListenerOption.

        监听端口范围列表。

        :param port_ranges: The port_ranges of this CreateListenerOption.
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        self._port_ranges = port_ranges

    @property
    def client_affinity(self):
        r"""Gets the client_affinity of this CreateListenerOption.

        :return: The client_affinity of this CreateListenerOption.
        :rtype: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        return self._client_affinity

    @client_affinity.setter
    def client_affinity(self, client_affinity):
        r"""Sets the client_affinity of this CreateListenerOption.

        :param client_affinity: The client_affinity of this CreateListenerOption.
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        self._client_affinity = client_affinity

    @property
    def accelerator_id(self):
        r"""Gets the accelerator_id of this CreateListenerOption.

        全球加速实例ID。

        :return: The accelerator_id of this CreateListenerOption.
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        r"""Sets the accelerator_id of this CreateListenerOption.

        全球加速实例ID。

        :param accelerator_id: The accelerator_id of this CreateListenerOption.
        :type accelerator_id: str
        """
        self._accelerator_id = accelerator_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateListenerOption.

        标签列表。

        :return: The tags of this CreateListenerOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateListenerOption.

        标签列表。

        :param tags: The tags of this CreateListenerOption.
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
        if not isinstance(other, CreateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
