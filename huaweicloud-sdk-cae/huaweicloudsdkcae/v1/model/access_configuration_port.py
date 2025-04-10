# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigurationPort:

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
        'target_port': 'int',
        'port': 'int',
        'protocol': 'str',
        'default_certificate': 'str',
        'certificate': 'str',
        'policy': 'str',
        'paths': 'list[AccessConfigurationHttpPath]',
        'elb_id': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'uid': 'uid',
        'target_port': 'target_port',
        'port': 'port',
        'protocol': 'protocol',
        'default_certificate': 'default_certificate',
        'certificate': 'certificate',
        'policy': 'policy',
        'paths': 'paths',
        'elb_id': 'elb_id'
    }

    def __init__(self, operator=None, uid=None, target_port=None, port=None, protocol=None, default_certificate=None, certificate=None, policy=None, paths=None, elb_id=None):
        r"""AccessConfigurationPort

        The model defined in huaweicloud sdk

        :param operator: 配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\&quot;add\&quot;,\&quot;copy\&quot;,\&quot;modify\&quot;,\&quot;delete\&quot;，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\&quot;copy\&quot;,\&quot;modify\&quot;,\&quot;delete\&quot;时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\&quot;copy\&quot;,\&quot;modify\&quot;时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 
        :type operator: str
        :param uid: 端口配置的uid。
        :type uid: str
        :param target_port: 监听端口。
        :type target_port: int
        :param port: 访问端口。
        :type port: int
        :param protocol: 协议，负载均衡支持TCP，负载均衡与路由配置支持HTTP、HTTPS。
        :type protocol: str
        :param default_certificate: 默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。
        :type default_certificate: str
        :param certificate: 证书。
        :type certificate: str
        :param policy: 安全策略。
        :type policy: str
        :param paths: 
        :type paths: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        :param elb_id: 用户选择的elb的ID。
        :type elb_id: str
        """
        
        

        self._operator = None
        self._uid = None
        self._target_port = None
        self._port = None
        self._protocol = None
        self._default_certificate = None
        self._certificate = None
        self._policy = None
        self._paths = None
        self._elb_id = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        if uid is not None:
            self.uid = uid
        if target_port is not None:
            self.target_port = target_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if default_certificate is not None:
            self.default_certificate = default_certificate
        if certificate is not None:
            self.certificate = certificate
        if policy is not None:
            self.policy = policy
        if paths is not None:
            self.paths = paths
        if elb_id is not None:
            self.elb_id = elb_id

    @property
    def operator(self):
        r"""Gets the operator of this AccessConfigurationPort.

        配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\"add\",\"copy\",\"modify\",\"delete\"，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\"copy\",\"modify\",\"delete\"时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\"copy\",\"modify\"时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 

        :return: The operator of this AccessConfigurationPort.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this AccessConfigurationPort.

        配置模式。 - 如果operator值为空，则表示使用全量覆盖模式进行配置，否则表示使用增删改模式进行配置。且此级列表的所有元素的operator值必须同时全为空或者非空。 - 当使用增删改模式时，operator取值支持\"add\",\"copy\",\"modify\",\"delete\"，分别表示新增，复制指定uid的元素修改后新增，修改指定uid的元素，删除指定uid的元素。 - 当operator取值为\"copy\",\"modify\",\"delete\"时，uid的值必须为非空，且存在于最后一次生效的配置中。 - 当operator取值为\"copy\",\"modify\"时，与operator同级别的字段中除uid外的所有字段如不写，置空或者为空列表，则表示保留在最后一次生效配置中指定uid的元素的同一字段的值。 

        :param operator: The operator of this AccessConfigurationPort.
        :type operator: str
        """
        self._operator = operator

    @property
    def uid(self):
        r"""Gets the uid of this AccessConfigurationPort.

        端口配置的uid。

        :return: The uid of this AccessConfigurationPort.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this AccessConfigurationPort.

        端口配置的uid。

        :param uid: The uid of this AccessConfigurationPort.
        :type uid: str
        """
        self._uid = uid

    @property
    def target_port(self):
        r"""Gets the target_port of this AccessConfigurationPort.

        监听端口。

        :return: The target_port of this AccessConfigurationPort.
        :rtype: int
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        r"""Sets the target_port of this AccessConfigurationPort.

        监听端口。

        :param target_port: The target_port of this AccessConfigurationPort.
        :type target_port: int
        """
        self._target_port = target_port

    @property
    def port(self):
        r"""Gets the port of this AccessConfigurationPort.

        访问端口。

        :return: The port of this AccessConfigurationPort.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AccessConfigurationPort.

        访问端口。

        :param port: The port of this AccessConfigurationPort.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this AccessConfigurationPort.

        协议，负载均衡支持TCP，负载均衡与路由配置支持HTTP、HTTPS。

        :return: The protocol of this AccessConfigurationPort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AccessConfigurationPort.

        协议，负载均衡支持TCP，负载均衡与路由配置支持HTTP、HTTPS。

        :param protocol: The protocol of this AccessConfigurationPort.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def default_certificate(self):
        r"""Gets the default_certificate of this AccessConfigurationPort.

        默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。

        :return: The default_certificate of this AccessConfigurationPort.
        :rtype: str
        """
        return self._default_certificate

    @default_certificate.setter
    def default_certificate(self, default_certificate):
        r"""Sets the default_certificate of this AccessConfigurationPort.

        默认证书，访问方式配置为转发策略且协议为HTTPS时配置，未配置域名证书对时使用默认证书。

        :param default_certificate: The default_certificate of this AccessConfigurationPort.
        :type default_certificate: str
        """
        self._default_certificate = default_certificate

    @property
    def certificate(self):
        r"""Gets the certificate of this AccessConfigurationPort.

        证书。

        :return: The certificate of this AccessConfigurationPort.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this AccessConfigurationPort.

        证书。

        :param certificate: The certificate of this AccessConfigurationPort.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def policy(self):
        r"""Gets the policy of this AccessConfigurationPort.

        安全策略。

        :return: The policy of this AccessConfigurationPort.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this AccessConfigurationPort.

        安全策略。

        :param policy: The policy of this AccessConfigurationPort.
        :type policy: str
        """
        self._policy = policy

    @property
    def paths(self):
        r"""Gets the paths of this AccessConfigurationPort.

        :return: The paths of this AccessConfigurationPort.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        r"""Sets the paths of this AccessConfigurationPort.

        :param paths: The paths of this AccessConfigurationPort.
        :type paths: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationHttpPath`]
        """
        self._paths = paths

    @property
    def elb_id(self):
        r"""Gets the elb_id of this AccessConfigurationPort.

        用户选择的elb的ID。

        :return: The elb_id of this AccessConfigurationPort.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this AccessConfigurationPort.

        用户选择的elb的ID。

        :param elb_id: The elb_id of this AccessConfigurationPort.
        :type elb_id: str
        """
        self._elb_id = elb_id

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
        if not isinstance(other, AccessConfigurationPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
