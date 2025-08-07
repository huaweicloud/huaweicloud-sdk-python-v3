# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmPolicyAntileakageMapResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'leakagemap': 'AntileakageMapResponseBodyLeakagemap',
        'locale': 'AntileakageMapResponseBodyLocale'
    }

    attribute_map = {
        'leakagemap': 'leakagemap',
        'locale': 'locale'
    }

    def __init__(self, leakagemap=None, locale=None):
        r"""ConfirmPolicyAntileakageMapResponse

        The model defined in huaweicloud sdk

        :param leakagemap: 
        :type leakagemap: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLeakagemap`
        :param locale: 
        :type locale: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLocale`
        """
        
        super(ConfirmPolicyAntileakageMapResponse, self).__init__()

        self._leakagemap = None
        self._locale = None
        self.discriminator = None

        if leakagemap is not None:
            self.leakagemap = leakagemap
        if locale is not None:
            self.locale = locale

    @property
    def leakagemap(self):
        r"""Gets the leakagemap of this ConfirmPolicyAntileakageMapResponse.

        :return: The leakagemap of this ConfirmPolicyAntileakageMapResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLeakagemap`
        """
        return self._leakagemap

    @leakagemap.setter
    def leakagemap(self, leakagemap):
        r"""Sets the leakagemap of this ConfirmPolicyAntileakageMapResponse.

        :param leakagemap: The leakagemap of this ConfirmPolicyAntileakageMapResponse.
        :type leakagemap: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLeakagemap`
        """
        self._leakagemap = leakagemap

    @property
    def locale(self):
        r"""Gets the locale of this ConfirmPolicyAntileakageMapResponse.

        :return: The locale of this ConfirmPolicyAntileakageMapResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLocale`
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ConfirmPolicyAntileakageMapResponse.

        :param locale: The locale of this ConfirmPolicyAntileakageMapResponse.
        :type locale: :class:`huaweicloudsdkwaf.v1.AntileakageMapResponseBodyLocale`
        """
        self._locale = locale

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
        if not isinstance(other, ConfirmPolicyAntileakageMapResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
