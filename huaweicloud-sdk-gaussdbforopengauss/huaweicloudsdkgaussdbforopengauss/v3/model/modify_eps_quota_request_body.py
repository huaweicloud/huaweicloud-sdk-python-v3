# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyEpsQuotaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_quotas': 'list[EpsQuotasOption]'
    }

    attribute_map = {
        'eps_quotas': 'eps_quotas'
    }

    def __init__(self, eps_quotas=None):
        r"""ModifyEpsQuotaRequestBody

        The model defined in huaweicloud sdk

        :param eps_quotas: 需要修改的企业配额列表。
        :type eps_quotas: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsQuotasOption`]
        """
        
        

        self._eps_quotas = None
        self.discriminator = None

        self.eps_quotas = eps_quotas

    @property
    def eps_quotas(self):
        r"""Gets the eps_quotas of this ModifyEpsQuotaRequestBody.

        需要修改的企业配额列表。

        :return: The eps_quotas of this ModifyEpsQuotaRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsQuotasOption`]
        """
        return self._eps_quotas

    @eps_quotas.setter
    def eps_quotas(self, eps_quotas):
        r"""Sets the eps_quotas of this ModifyEpsQuotaRequestBody.

        需要修改的企业配额列表。

        :param eps_quotas: The eps_quotas of this ModifyEpsQuotaRequestBody.
        :type eps_quotas: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsQuotasOption`]
        """
        self._eps_quotas = eps_quotas

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
        if not isinstance(other, ModifyEpsQuotaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
