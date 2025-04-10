# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigurationDataItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'str',
        'uid': 'str',
        'metadata': 'AccessConfigurationMetadata',
        'type': 'str',
        'domain_names': 'list[str]',
        'access_control': 'AccessControl',
        'ports': 'list[AccessConfigurationPort]',
        'elb_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'uid': 'uid',
        'metadata': 'metadata',
        'type': 'type',
        'domain_names': 'domain_names',
        'access_control': 'access_control',
        'ports': 'ports',
        'elb_id': 'elb_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip'
    }

    def __init__(self, operator=None, uid=None, metadata=None, type=None, domain_names=None, access_control=None, ports=None, elb_id=None, public_ip=None, private_ip=None):
        r"""AccessConfigurationDataItems

        The model defined in huaweicloud sdk

        :param operator: 配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\&quot;add\&quot;,\&quot;copy\&quot;,\&quot;modify\&quot;,\&quot;delete\&quot;，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\&quot;copy\&quot;,\&quot;modify\&quot;,\&quot;delete\&quot;时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\&quot;copy\&quot;,\&quot;modify\&quot;时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 
        :type operator: str
        :param uid: 访问方式的uid。
        :type uid: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.AccessConfigurationMetadata`
        :param type: 访问方式类型。
        :type type: str
        :param domain_names: 内网访问方式域名。
        :type domain_names: list[str]
        :param access_control: 
        :type access_control: :class:`huaweicloudsdkcae.v1.AccessControl`
        :param ports: 访问方式配置端口、协议、证书、URL路径等信息列表。
        :type ports: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationPort`]
        :param elb_id: 用户选择的elb的ID。
        :type elb_id: str
        :param public_ip: 响应体参数，用户选择的elb的公网ip。
        :type public_ip: str
        :param private_ip: 响应体参数，用户选择的elb的私网ip。
        :type private_ip: str
        """
        
        

        self._operator = None
        self._uid = None
        self._metadata = None
        self._type = None
        self._domain_names = None
        self._access_control = None
        self._ports = None
        self._elb_id = None
        self._public_ip = None
        self._private_ip = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        if uid is not None:
            self.uid = uid
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type
        if domain_names is not None:
            self.domain_names = domain_names
        if access_control is not None:
            self.access_control = access_control
        if ports is not None:
            self.ports = ports
        if elb_id is not None:
            self.elb_id = elb_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip

    @property
    def operator(self):
        r"""Gets the operator of this AccessConfigurationDataItems.

        配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\"add\",\"copy\",\"modify\",\"delete\"，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\"copy\",\"modify\",\"delete\"时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\"copy\",\"modify\"时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 

        :return: The operator of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this AccessConfigurationDataItems.

        配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\"add\",\"copy\",\"modify\",\"delete\"，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\"copy\",\"modify\",\"delete\"时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\"copy\",\"modify\"时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 

        :param operator: The operator of this AccessConfigurationDataItems.
        :type operator: str
        """
        self._operator = operator

    @property
    def uid(self):
        r"""Gets the uid of this AccessConfigurationDataItems.

        访问方式的uid。

        :return: The uid of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this AccessConfigurationDataItems.

        访问方式的uid。

        :param uid: The uid of this AccessConfigurationDataItems.
        :type uid: str
        """
        self._uid = uid

    @property
    def metadata(self):
        r"""Gets the metadata of this AccessConfigurationDataItems.

        :return: The metadata of this AccessConfigurationDataItems.
        :rtype: :class:`huaweicloudsdkcae.v1.AccessConfigurationMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this AccessConfigurationDataItems.

        :param metadata: The metadata of this AccessConfigurationDataItems.
        :type metadata: :class:`huaweicloudsdkcae.v1.AccessConfigurationMetadata`
        """
        self._metadata = metadata

    @property
    def type(self):
        r"""Gets the type of this AccessConfigurationDataItems.

        访问方式类型。

        :return: The type of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccessConfigurationDataItems.

        访问方式类型。

        :param type: The type of this AccessConfigurationDataItems.
        :type type: str
        """
        self._type = type

    @property
    def domain_names(self):
        r"""Gets the domain_names of this AccessConfigurationDataItems.

        内网访问方式域名。

        :return: The domain_names of this AccessConfigurationDataItems.
        :rtype: list[str]
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        r"""Sets the domain_names of this AccessConfigurationDataItems.

        内网访问方式域名。

        :param domain_names: The domain_names of this AccessConfigurationDataItems.
        :type domain_names: list[str]
        """
        self._domain_names = domain_names

    @property
    def access_control(self):
        r"""Gets the access_control of this AccessConfigurationDataItems.

        :return: The access_control of this AccessConfigurationDataItems.
        :rtype: :class:`huaweicloudsdkcae.v1.AccessControl`
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        r"""Sets the access_control of this AccessConfigurationDataItems.

        :param access_control: The access_control of this AccessConfigurationDataItems.
        :type access_control: :class:`huaweicloudsdkcae.v1.AccessControl`
        """
        self._access_control = access_control

    @property
    def ports(self):
        r"""Gets the ports of this AccessConfigurationDataItems.

        访问方式配置端口、协议、证书、URL路径等信息列表。

        :return: The ports of this AccessConfigurationDataItems.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationPort`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this AccessConfigurationDataItems.

        访问方式配置端口、协议、证书、URL路径等信息列表。

        :param ports: The ports of this AccessConfigurationDataItems.
        :type ports: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationPort`]
        """
        self._ports = ports

    @property
    def elb_id(self):
        r"""Gets the elb_id of this AccessConfigurationDataItems.

        用户选择的elb的ID。

        :return: The elb_id of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this AccessConfigurationDataItems.

        用户选择的elb的ID。

        :param elb_id: The elb_id of this AccessConfigurationDataItems.
        :type elb_id: str
        """
        self._elb_id = elb_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AccessConfigurationDataItems.

        响应体参数，用户选择的elb的公网ip。

        :return: The public_ip of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AccessConfigurationDataItems.

        响应体参数，用户选择的elb的公网ip。

        :param public_ip: The public_ip of this AccessConfigurationDataItems.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AccessConfigurationDataItems.

        响应体参数，用户选择的elb的私网ip。

        :return: The private_ip of this AccessConfigurationDataItems.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AccessConfigurationDataItems.

        响应体参数，用户选择的elb的私网ip。

        :param private_ip: The private_ip of this AccessConfigurationDataItems.
        :type private_ip: str
        """
        self._private_ip = private_ip

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
        if not isinstance(other, AccessConfigurationDataItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
