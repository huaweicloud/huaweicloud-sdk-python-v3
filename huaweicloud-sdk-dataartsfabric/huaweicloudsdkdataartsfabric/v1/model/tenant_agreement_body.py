# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantAgreementBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreements': 'list[TenantAgreement]'
    }

    attribute_map = {
        'agreements': 'agreements'
    }

    def __init__(self, agreements=None):
        r"""TenantAgreementBody

        The model defined in huaweicloud sdk

        :param agreements: 租户协议列表
        :type agreements: list[:class:`huaweicloudsdkdataartsfabric.v1.TenantAgreement`]
        """
        
        

        self._agreements = None
        self.discriminator = None

        if agreements is not None:
            self.agreements = agreements

    @property
    def agreements(self):
        r"""Gets the agreements of this TenantAgreementBody.

        租户协议列表

        :return: The agreements of this TenantAgreementBody.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.TenantAgreement`]
        """
        return self._agreements

    @agreements.setter
    def agreements(self, agreements):
        r"""Sets the agreements of this TenantAgreementBody.

        租户协议列表

        :param agreements: The agreements of this TenantAgreementBody.
        :type agreements: list[:class:`huaweicloudsdkdataartsfabric.v1.TenantAgreement`]
        """
        self._agreements = agreements

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
        if not isinstance(other, TenantAgreementBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
