# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'quotas': 'QuotaList'
    }

    attribute_map = {
        'is_success': 'is_success',
        'quotas': 'quotas'
    }

    def __init__(self, is_success=None, quotas=None):
        r"""ShowQuotaResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功
        :type is_success: bool
        :param quotas: 
        :type quotas: :class:`huaweicloudsdkdli.v1.QuotaList`
        """
        
        super(ShowQuotaResponse, self).__init__()

        self._is_success = None
        self._quotas = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if quotas is not None:
            self.quotas = quotas

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowQuotaResponse.

        是否成功

        :return: The is_success of this ShowQuotaResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowQuotaResponse.

        是否成功

        :param is_success: The is_success of this ShowQuotaResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def quotas(self):
        r"""Gets the quotas of this ShowQuotaResponse.

        :return: The quotas of this ShowQuotaResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.QuotaList`
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        r"""Sets the quotas of this ShowQuotaResponse.

        :param quotas: The quotas of this ShowQuotaResponse.
        :type quotas: :class:`huaweicloudsdkdli.v1.QuotaList`
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
        if not isinstance(other, ShowQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
