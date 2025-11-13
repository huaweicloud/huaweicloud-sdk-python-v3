# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainDetectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, domain_name=None, type=None, status=None):
        r"""ShowDomainDetectionResponse

        The model defined in huaweicloud sdk

        :param domain_name: 待诊断记录集的名称。
        :type domain_name: str
        :param type: 待诊断记录集的类型。 取值范围：CNAME、TXT、MX。
        :type type: str
        :param status: 域名诊断状态。  取值范围：  OK：解析成功 FAILED：whois查询失败 NOT_REGISTERED：通过whois查询，域名未注册 CANNOT_RESOLVE：通过whois查询，域名无法解析 NOT_HWDNS：未托管在华为云 NO_WEBSITE_RECORD：未配置网站解析记录 NO_EMAIL_RECORD：未配置邮箱解析记录 NO_DEFAULT_VIEW：未配置默认解析 NOT_EFFECT：权威服务器未生效
        :type status: str
        """
        
        super().__init__()

        self._domain_name = None
        self._type = None
        self._status = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainDetectionResponse.

        待诊断记录集的名称。

        :return: The domain_name of this ShowDomainDetectionResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainDetectionResponse.

        待诊断记录集的名称。

        :param domain_name: The domain_name of this ShowDomainDetectionResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def type(self):
        r"""Gets the type of this ShowDomainDetectionResponse.

        待诊断记录集的类型。 取值范围：CNAME、TXT、MX。

        :return: The type of this ShowDomainDetectionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDomainDetectionResponse.

        待诊断记录集的类型。 取值范围：CNAME、TXT、MX。

        :param type: The type of this ShowDomainDetectionResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ShowDomainDetectionResponse.

        域名诊断状态。  取值范围：  OK：解析成功 FAILED：whois查询失败 NOT_REGISTERED：通过whois查询，域名未注册 CANNOT_RESOLVE：通过whois查询，域名无法解析 NOT_HWDNS：未托管在华为云 NO_WEBSITE_RECORD：未配置网站解析记录 NO_EMAIL_RECORD：未配置邮箱解析记录 NO_DEFAULT_VIEW：未配置默认解析 NOT_EFFECT：权威服务器未生效

        :return: The status of this ShowDomainDetectionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDomainDetectionResponse.

        域名诊断状态。  取值范围：  OK：解析成功 FAILED：whois查询失败 NOT_REGISTERED：通过whois查询，域名未注册 CANNOT_RESOLVE：通过whois查询，域名无法解析 NOT_HWDNS：未托管在华为云 NO_WEBSITE_RECORD：未配置网站解析记录 NO_EMAIL_RECORD：未配置邮箱解析记录 NO_DEFAULT_VIEW：未配置默认解析 NOT_EFFECT：权威服务器未生效

        :param status: The status of this ShowDomainDetectionResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainDetectionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDomainDetectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
