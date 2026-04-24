# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDomainNewReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uos_domain_info': 'CreateUosDomainInfo',
        'ad_domain_info': 'AdDomain',
        'auth_type': 'DomainType'
    }

    attribute_map = {
        'uos_domain_info': 'uos_domain_info',
        'ad_domain_info': 'ad_domain_info',
        'auth_type': 'auth_type'
    }

    def __init__(self, uos_domain_info=None, ad_domain_info=None, auth_type=None):
        r"""CreateDomainNewReq

        The model defined in huaweicloud sdk

        :param uos_domain_info: 
        :type uos_domain_info: :class:`huaweicloudsdkworkspace.v2.CreateUosDomainInfo`
        :param ad_domain_info: 
        :type ad_domain_info: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        :param auth_type: 
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        
        

        self._uos_domain_info = None
        self._ad_domain_info = None
        self._auth_type = None
        self.discriminator = None

        if uos_domain_info is not None:
            self.uos_domain_info = uos_domain_info
        if ad_domain_info is not None:
            self.ad_domain_info = ad_domain_info
        if auth_type is not None:
            self.auth_type = auth_type

    @property
    def uos_domain_info(self):
        r"""Gets the uos_domain_info of this CreateDomainNewReq.

        :return: The uos_domain_info of this CreateDomainNewReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateUosDomainInfo`
        """
        return self._uos_domain_info

    @uos_domain_info.setter
    def uos_domain_info(self, uos_domain_info):
        r"""Sets the uos_domain_info of this CreateDomainNewReq.

        :param uos_domain_info: The uos_domain_info of this CreateDomainNewReq.
        :type uos_domain_info: :class:`huaweicloudsdkworkspace.v2.CreateUosDomainInfo`
        """
        self._uos_domain_info = uos_domain_info

    @property
    def ad_domain_info(self):
        r"""Gets the ad_domain_info of this CreateDomainNewReq.

        :return: The ad_domain_info of this CreateDomainNewReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        """
        return self._ad_domain_info

    @ad_domain_info.setter
    def ad_domain_info(self, ad_domain_info):
        r"""Sets the ad_domain_info of this CreateDomainNewReq.

        :param ad_domain_info: The ad_domain_info of this CreateDomainNewReq.
        :type ad_domain_info: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        """
        self._ad_domain_info = ad_domain_info

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CreateDomainNewReq.

        :return: The auth_type of this CreateDomainNewReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CreateDomainNewReq.

        :param auth_type: The auth_type of this CreateDomainNewReq.
        :type auth_type: :class:`huaweicloudsdkworkspace.v2.DomainType`
        """
        self._auth_type = auth_type

    def to_dict(self):
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
        if not isinstance(other, CreateDomainNewReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
