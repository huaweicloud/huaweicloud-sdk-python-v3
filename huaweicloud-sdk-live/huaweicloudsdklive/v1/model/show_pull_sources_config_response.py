# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPullSourcesConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'source_type': 'str',
        'sources': 'list[str]',
        'sources_ip': 'list[str]',
        'source_port': 'int',
        'scheme': 'str',
        'additional_args': 'dict(str, str)'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'source_type': 'source_type',
        'sources': 'sources',
        'sources_ip': 'sources_ip',
        'source_port': 'source_port',
        'scheme': 'scheme',
        'additional_args': 'additional_args'
    }

    def __init__(self, play_domain=None, source_type=None, sources=None, sources_ip=None, source_port=None, scheme=None, additional_args=None):
        r"""ShowPullSourcesConfigResponse

        The model defined in huaweicloud sdk

        :param play_domain: 播放域名
        :type play_domain: str
        :param source_type: 回源方式。 - domain: 回源客户源站，源站地址是域名格式。回源域名，可配置多个，如果回源失败，将按照配置顺序进行轮循。 - ipaddr: 回源客户源站，源站地址是IP格式。回源IP，可配置多个，如果回源失败，将按照配置顺序进行轮循。同时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl字段填该域名，否则按当前IP作为HOST。 - huawei: 回源华为源站，域名创建后的默认值。
        :type source_type: str
        :param sources: 回源域名列表，最多可配置10个。 - 当回源方式是“domain”时，此参数必选，域名配置多个时，如果回源失败，将按照配置顺序进行轮循。 - 当回源方式是“ipaddr”时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl 字段填该域名，否则按当前IP作为HOST。
        :type sources: list[str]
        :param sources_ip: 回源IP地址列表，最多可配置10个。当回源方式是“ipaddr”时，此参数必选，IP配置多个时，如果回源失败，将按照配置顺序进行轮循。
        :type sources_ip: list[str]
        :param source_port: 回源端口。 
        :type source_port: int
        :param scheme: 回源协议，回源方式非“huawei”时必选。
        :type scheme: str
        :param additional_args: 回源客户源站时在URL携带的参数。
        :type additional_args: dict(str, str)
        """
        
        super(ShowPullSourcesConfigResponse, self).__init__()

        self._play_domain = None
        self._source_type = None
        self._sources = None
        self._sources_ip = None
        self._source_port = None
        self._scheme = None
        self._additional_args = None
        self.discriminator = None

        if play_domain is not None:
            self.play_domain = play_domain
        if source_type is not None:
            self.source_type = source_type
        if sources is not None:
            self.sources = sources
        if sources_ip is not None:
            self.sources_ip = sources_ip
        if source_port is not None:
            self.source_port = source_port
        if scheme is not None:
            self.scheme = scheme
        if additional_args is not None:
            self.additional_args = additional_args

    @property
    def play_domain(self):
        r"""Gets the play_domain of this ShowPullSourcesConfigResponse.

        播放域名

        :return: The play_domain of this ShowPullSourcesConfigResponse.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this ShowPullSourcesConfigResponse.

        播放域名

        :param play_domain: The play_domain of this ShowPullSourcesConfigResponse.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def source_type(self):
        r"""Gets the source_type of this ShowPullSourcesConfigResponse.

        回源方式。 - domain: 回源客户源站，源站地址是域名格式。回源域名，可配置多个，如果回源失败，将按照配置顺序进行轮循。 - ipaddr: 回源客户源站，源站地址是IP格式。回源IP，可配置多个，如果回源失败，将按照配置顺序进行轮循。同时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl字段填该域名，否则按当前IP作为HOST。 - huawei: 回源华为源站，域名创建后的默认值。

        :return: The source_type of this ShowPullSourcesConfigResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ShowPullSourcesConfigResponse.

        回源方式。 - domain: 回源客户源站，源站地址是域名格式。回源域名，可配置多个，如果回源失败，将按照配置顺序进行轮循。 - ipaddr: 回源客户源站，源站地址是IP格式。回源IP，可配置多个，如果回源失败，将按照配置顺序进行轮循。同时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl字段填该域名，否则按当前IP作为HOST。 - huawei: 回源华为源站，域名创建后的默认值。

        :param source_type: The source_type of this ShowPullSourcesConfigResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def sources(self):
        r"""Gets the sources of this ShowPullSourcesConfigResponse.

        回源域名列表，最多可配置10个。 - 当回源方式是“domain”时，此参数必选，域名配置多个时，如果回源失败，将按照配置顺序进行轮循。 - 当回源方式是“ipaddr”时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl 字段填该域名，否则按当前IP作为HOST。

        :return: The sources of this ShowPullSourcesConfigResponse.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this ShowPullSourcesConfigResponse.

        回源域名列表，最多可配置10个。 - 当回源方式是“domain”时，此参数必选，域名配置多个时，如果回源失败，将按照配置顺序进行轮循。 - 当回源方式是“ipaddr”时，最多可以配置一个回源域名，如果配置，回源时httpflv HOST头填该域名，RTMP tcurl 字段填该域名，否则按当前IP作为HOST。

        :param sources: The sources of this ShowPullSourcesConfigResponse.
        :type sources: list[str]
        """
        self._sources = sources

    @property
    def sources_ip(self):
        r"""Gets the sources_ip of this ShowPullSourcesConfigResponse.

        回源IP地址列表，最多可配置10个。当回源方式是“ipaddr”时，此参数必选，IP配置多个时，如果回源失败，将按照配置顺序进行轮循。

        :return: The sources_ip of this ShowPullSourcesConfigResponse.
        :rtype: list[str]
        """
        return self._sources_ip

    @sources_ip.setter
    def sources_ip(self, sources_ip):
        r"""Sets the sources_ip of this ShowPullSourcesConfigResponse.

        回源IP地址列表，最多可配置10个。当回源方式是“ipaddr”时，此参数必选，IP配置多个时，如果回源失败，将按照配置顺序进行轮循。

        :param sources_ip: The sources_ip of this ShowPullSourcesConfigResponse.
        :type sources_ip: list[str]
        """
        self._sources_ip = sources_ip

    @property
    def source_port(self):
        r"""Gets the source_port of this ShowPullSourcesConfigResponse.

        回源端口。 

        :return: The source_port of this ShowPullSourcesConfigResponse.
        :rtype: int
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this ShowPullSourcesConfigResponse.

        回源端口。 

        :param source_port: The source_port of this ShowPullSourcesConfigResponse.
        :type source_port: int
        """
        self._source_port = source_port

    @property
    def scheme(self):
        r"""Gets the scheme of this ShowPullSourcesConfigResponse.

        回源协议，回源方式非“huawei”时必选。

        :return: The scheme of this ShowPullSourcesConfigResponse.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        r"""Sets the scheme of this ShowPullSourcesConfigResponse.

        回源协议，回源方式非“huawei”时必选。

        :param scheme: The scheme of this ShowPullSourcesConfigResponse.
        :type scheme: str
        """
        self._scheme = scheme

    @property
    def additional_args(self):
        r"""Gets the additional_args of this ShowPullSourcesConfigResponse.

        回源客户源站时在URL携带的参数。

        :return: The additional_args of this ShowPullSourcesConfigResponse.
        :rtype: dict(str, str)
        """
        return self._additional_args

    @additional_args.setter
    def additional_args(self, additional_args):
        r"""Sets the additional_args of this ShowPullSourcesConfigResponse.

        回源客户源站时在URL携带的参数。

        :param additional_args: The additional_args of this ShowPullSourcesConfigResponse.
        :type additional_args: dict(str, str)
        """
        self._additional_args = additional_args

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
        if not isinstance(other, ShowPullSourcesConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
