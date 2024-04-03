# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnsubscribeCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unsubscribe_results': 'str'
    }

    attribute_map = {
        'unsubscribe_results': 'unsubscribe_results'
    }

    def __init__(self, unsubscribe_results=None):
        """UnsubscribeCertificateResponse

        The model defined in huaweicloud sdk

        :param unsubscribe_results: 退订结果。
        :type unsubscribe_results: str
        """
        
        super(UnsubscribeCertificateResponse, self).__init__()

        self._unsubscribe_results = None
        self.discriminator = None

        if unsubscribe_results is not None:
            self.unsubscribe_results = unsubscribe_results

    @property
    def unsubscribe_results(self):
        """Gets the unsubscribe_results of this UnsubscribeCertificateResponse.

        退订结果。

        :return: The unsubscribe_results of this UnsubscribeCertificateResponse.
        :rtype: str
        """
        return self._unsubscribe_results

    @unsubscribe_results.setter
    def unsubscribe_results(self, unsubscribe_results):
        """Sets the unsubscribe_results of this UnsubscribeCertificateResponse.

        退订结果。

        :param unsubscribe_results: The unsubscribe_results of this UnsubscribeCertificateResponse.
        :type unsubscribe_results: str
        """
        self._unsubscribe_results = unsubscribe_results

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
        if not isinstance(other, UnsubscribeCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
