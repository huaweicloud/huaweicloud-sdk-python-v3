# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowElbDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_cert_name': 'str',
        'server_cert_id': 'str',
        'cacert_name': 'str',
        'cacert_id': 'str',
        'elb_enable': 'bool',
        'authentication_type': 'str',
        'load_balancer': 'EsLoadBalancerResource',
        'healthmonitors': 'EsHealthmonitorsResource'
    }

    attribute_map = {
        'server_cert_name': 'serverCertName',
        'server_cert_id': 'serverCertId',
        'cacert_name': 'cacertName',
        'cacert_id': 'cacertId',
        'elb_enable': 'elb_enable',
        'authentication_type': 'authentication_type',
        'load_balancer': 'loadBalancer',
        'healthmonitors': 'healthmonitors'
    }

    def __init__(self, server_cert_name=None, server_cert_id=None, cacert_name=None, cacert_id=None, elb_enable=None, authentication_type=None, load_balancer=None, healthmonitors=None):
        r"""ShowElbDetailResponse

        The model defined in huaweicloud sdk

        :param server_cert_name: 服务器证书名称。
        :type server_cert_name: str
        :param server_cert_id: 服务器证书ID。
        :type server_cert_id: str
        :param cacert_name: ca证书名称。
        :type cacert_name: str
        :param cacert_id: ca证书ID。
        :type cacert_id: str
        :param elb_enable: 是否开启elb。 - true: 打开elb - false： 关闭elb
        :type elb_enable: bool
        :param authentication_type: 认证方式。
        :type authentication_type: str
        :param load_balancer: 
        :type load_balancer: :class:`huaweicloudsdkcss.v1.EsLoadBalancerResource`
        :param healthmonitors: 
        :type healthmonitors: :class:`huaweicloudsdkcss.v1.EsHealthmonitorsResource`
        """
        
        super(ShowElbDetailResponse, self).__init__()

        self._server_cert_name = None
        self._server_cert_id = None
        self._cacert_name = None
        self._cacert_id = None
        self._elb_enable = None
        self._authentication_type = None
        self._load_balancer = None
        self._healthmonitors = None
        self.discriminator = None

        if server_cert_name is not None:
            self.server_cert_name = server_cert_name
        if server_cert_id is not None:
            self.server_cert_id = server_cert_id
        if cacert_name is not None:
            self.cacert_name = cacert_name
        if cacert_id is not None:
            self.cacert_id = cacert_id
        if elb_enable is not None:
            self.elb_enable = elb_enable
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if load_balancer is not None:
            self.load_balancer = load_balancer
        if healthmonitors is not None:
            self.healthmonitors = healthmonitors

    @property
    def server_cert_name(self):
        r"""Gets the server_cert_name of this ShowElbDetailResponse.

        服务器证书名称。

        :return: The server_cert_name of this ShowElbDetailResponse.
        :rtype: str
        """
        return self._server_cert_name

    @server_cert_name.setter
    def server_cert_name(self, server_cert_name):
        r"""Sets the server_cert_name of this ShowElbDetailResponse.

        服务器证书名称。

        :param server_cert_name: The server_cert_name of this ShowElbDetailResponse.
        :type server_cert_name: str
        """
        self._server_cert_name = server_cert_name

    @property
    def server_cert_id(self):
        r"""Gets the server_cert_id of this ShowElbDetailResponse.

        服务器证书ID。

        :return: The server_cert_id of this ShowElbDetailResponse.
        :rtype: str
        """
        return self._server_cert_id

    @server_cert_id.setter
    def server_cert_id(self, server_cert_id):
        r"""Sets the server_cert_id of this ShowElbDetailResponse.

        服务器证书ID。

        :param server_cert_id: The server_cert_id of this ShowElbDetailResponse.
        :type server_cert_id: str
        """
        self._server_cert_id = server_cert_id

    @property
    def cacert_name(self):
        r"""Gets the cacert_name of this ShowElbDetailResponse.

        ca证书名称。

        :return: The cacert_name of this ShowElbDetailResponse.
        :rtype: str
        """
        return self._cacert_name

    @cacert_name.setter
    def cacert_name(self, cacert_name):
        r"""Sets the cacert_name of this ShowElbDetailResponse.

        ca证书名称。

        :param cacert_name: The cacert_name of this ShowElbDetailResponse.
        :type cacert_name: str
        """
        self._cacert_name = cacert_name

    @property
    def cacert_id(self):
        r"""Gets the cacert_id of this ShowElbDetailResponse.

        ca证书ID。

        :return: The cacert_id of this ShowElbDetailResponse.
        :rtype: str
        """
        return self._cacert_id

    @cacert_id.setter
    def cacert_id(self, cacert_id):
        r"""Sets the cacert_id of this ShowElbDetailResponse.

        ca证书ID。

        :param cacert_id: The cacert_id of this ShowElbDetailResponse.
        :type cacert_id: str
        """
        self._cacert_id = cacert_id

    @property
    def elb_enable(self):
        r"""Gets the elb_enable of this ShowElbDetailResponse.

        是否开启elb。 - true: 打开elb - false： 关闭elb

        :return: The elb_enable of this ShowElbDetailResponse.
        :rtype: bool
        """
        return self._elb_enable

    @elb_enable.setter
    def elb_enable(self, elb_enable):
        r"""Sets the elb_enable of this ShowElbDetailResponse.

        是否开启elb。 - true: 打开elb - false： 关闭elb

        :param elb_enable: The elb_enable of this ShowElbDetailResponse.
        :type elb_enable: bool
        """
        self._elb_enable = elb_enable

    @property
    def authentication_type(self):
        r"""Gets the authentication_type of this ShowElbDetailResponse.

        认证方式。

        :return: The authentication_type of this ShowElbDetailResponse.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        r"""Sets the authentication_type of this ShowElbDetailResponse.

        认证方式。

        :param authentication_type: The authentication_type of this ShowElbDetailResponse.
        :type authentication_type: str
        """
        self._authentication_type = authentication_type

    @property
    def load_balancer(self):
        r"""Gets the load_balancer of this ShowElbDetailResponse.

        :return: The load_balancer of this ShowElbDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.EsLoadBalancerResource`
        """
        return self._load_balancer

    @load_balancer.setter
    def load_balancer(self, load_balancer):
        r"""Sets the load_balancer of this ShowElbDetailResponse.

        :param load_balancer: The load_balancer of this ShowElbDetailResponse.
        :type load_balancer: :class:`huaweicloudsdkcss.v1.EsLoadBalancerResource`
        """
        self._load_balancer = load_balancer

    @property
    def healthmonitors(self):
        r"""Gets the healthmonitors of this ShowElbDetailResponse.

        :return: The healthmonitors of this ShowElbDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.EsHealthmonitorsResource`
        """
        return self._healthmonitors

    @healthmonitors.setter
    def healthmonitors(self, healthmonitors):
        r"""Sets the healthmonitors of this ShowElbDetailResponse.

        :param healthmonitors: The healthmonitors of this ShowElbDetailResponse.
        :type healthmonitors: :class:`huaweicloudsdkcss.v1.EsHealthmonitorsResource`
        """
        self._healthmonitors = healthmonitors

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
        if not isinstance(other, ShowElbDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
