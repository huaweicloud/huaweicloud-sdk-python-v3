# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlModiflyEpsQuotasRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quotas': 'list[NoSqlRequestEpsQuota]'
    }

    attribute_map = {
        'quotas': 'quotas'
    }

    def __init__(self, quotas=None):
        """NoSqlModiflyEpsQuotasRequestBody

        The model defined in huaweicloud sdk

        :param quotas: 需要修改的企业项目配额信息列表。
        :type quotas: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlRequestEpsQuota`]
        """
        
        

        self._quotas = None
        self.discriminator = None

        self.quotas = quotas

    @property
    def quotas(self):
        """Gets the quotas of this NoSqlModiflyEpsQuotasRequestBody.

        需要修改的企业项目配额信息列表。

        :return: The quotas of this NoSqlModiflyEpsQuotasRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlRequestEpsQuota`]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this NoSqlModiflyEpsQuotasRequestBody.

        需要修改的企业项目配额信息列表。

        :param quotas: The quotas of this NoSqlModiflyEpsQuotasRequestBody.
        :type quotas: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSqlRequestEpsQuota`]
        """
        self._quotas = quotas

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
        if not isinstance(other, NoSqlModiflyEpsQuotasRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
