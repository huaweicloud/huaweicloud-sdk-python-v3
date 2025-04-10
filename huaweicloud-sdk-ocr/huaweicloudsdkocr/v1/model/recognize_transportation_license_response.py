# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeTransportationLicenseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'TransportationLicenseResult',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, result=None, x_request_id=None):
        r"""RecognizeTransportationLicenseResponse

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkocr.v1.TransportationLicenseResult`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(RecognizeTransportationLicenseResponse, self).__init__()

        self._result = None
        self._x_request_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result(self):
        r"""Gets the result of this RecognizeTransportationLicenseResponse.

        :return: The result of this RecognizeTransportationLicenseResponse.
        :rtype: :class:`huaweicloudsdkocr.v1.TransportationLicenseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this RecognizeTransportationLicenseResponse.

        :param result: The result of this RecognizeTransportationLicenseResponse.
        :type result: :class:`huaweicloudsdkocr.v1.TransportationLicenseResult`
        """
        self._result = result

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this RecognizeTransportationLicenseResponse.

        :return: The x_request_id of this RecognizeTransportationLicenseResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this RecognizeTransportationLicenseResponse.

        :param x_request_id: The x_request_id of this RecognizeTransportationLicenseResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, RecognizeTransportationLicenseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
