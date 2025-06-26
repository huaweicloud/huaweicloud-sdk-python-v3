# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainNamesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name_infos': 'list[DomainNameInfo]'
    }

    attribute_map = {
        'domain_name_infos': 'domain_name_infos'
    }

    def __init__(self, domain_name_infos=None):
        r"""ListDomainNamesResponse

        The model defined in huaweicloud sdk

        :param domain_name_infos: 域名信息
        :type domain_name_infos: list[:class:`huaweicloudsdkswr.v2.DomainNameInfo`]
        """
        
        super(ListDomainNamesResponse, self).__init__()

        self._domain_name_infos = None
        self.discriminator = None

        if domain_name_infos is not None:
            self.domain_name_infos = domain_name_infos

    @property
    def domain_name_infos(self):
        r"""Gets the domain_name_infos of this ListDomainNamesResponse.

        域名信息

        :return: The domain_name_infos of this ListDomainNamesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.DomainNameInfo`]
        """
        return self._domain_name_infos

    @domain_name_infos.setter
    def domain_name_infos(self, domain_name_infos):
        r"""Sets the domain_name_infos of this ListDomainNamesResponse.

        域名信息

        :param domain_name_infos: The domain_name_infos of this ListDomainNamesResponse.
        :type domain_name_infos: list[:class:`huaweicloudsdkswr.v2.DomainNameInfo`]
        """
        self._domain_name_infos = domain_name_infos

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
        if not isinstance(other, ListDomainNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
