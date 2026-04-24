# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainsNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uos_domain_list': 'list[UosDomainInfo]',
        'domain_infos': 'list[AdDomain]'
    }

    attribute_map = {
        'uos_domain_list': 'uos_domain_list',
        'domain_infos': 'domain_infos'
    }

    def __init__(self, uos_domain_list=None, domain_infos=None):
        r"""ShowDomainsNewResponse

        The model defined in huaweicloud sdk

        :param uos_domain_list: 统信域控列表。
        :type uos_domain_list: list[:class:`huaweicloudsdkworkspace.v2.UosDomainInfo`]
        :param domain_infos: 域信息。
        :type domain_infos: list[:class:`huaweicloudsdkworkspace.v2.AdDomain`]
        """
        
        super().__init__()

        self._uos_domain_list = None
        self._domain_infos = None
        self.discriminator = None

        if uos_domain_list is not None:
            self.uos_domain_list = uos_domain_list
        if domain_infos is not None:
            self.domain_infos = domain_infos

    @property
    def uos_domain_list(self):
        r"""Gets the uos_domain_list of this ShowDomainsNewResponse.

        统信域控列表。

        :return: The uos_domain_list of this ShowDomainsNewResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UosDomainInfo`]
        """
        return self._uos_domain_list

    @uos_domain_list.setter
    def uos_domain_list(self, uos_domain_list):
        r"""Sets the uos_domain_list of this ShowDomainsNewResponse.

        统信域控列表。

        :param uos_domain_list: The uos_domain_list of this ShowDomainsNewResponse.
        :type uos_domain_list: list[:class:`huaweicloudsdkworkspace.v2.UosDomainInfo`]
        """
        self._uos_domain_list = uos_domain_list

    @property
    def domain_infos(self):
        r"""Gets the domain_infos of this ShowDomainsNewResponse.

        域信息。

        :return: The domain_infos of this ShowDomainsNewResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AdDomain`]
        """
        return self._domain_infos

    @domain_infos.setter
    def domain_infos(self, domain_infos):
        r"""Sets the domain_infos of this ShowDomainsNewResponse.

        域信息。

        :param domain_infos: The domain_infos of this ShowDomainsNewResponse.
        :type domain_infos: list[:class:`huaweicloudsdkworkspace.v2.AdDomain`]
        """
        self._domain_infos = domain_infos

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainsNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDomainsNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
