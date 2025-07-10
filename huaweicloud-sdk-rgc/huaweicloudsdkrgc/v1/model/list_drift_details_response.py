# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDriftDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'drift_details': 'list[DriftDetail]'
    }

    attribute_map = {
        'drift_details': 'drift_details'
    }

    def __init__(self, drift_details=None):
        r"""ListDriftDetailsResponse

        The model defined in huaweicloud sdk

        :param drift_details: 漂移详细信息。
        :type drift_details: list[:class:`huaweicloudsdkrgc.v1.DriftDetail`]
        """
        
        super(ListDriftDetailsResponse, self).__init__()

        self._drift_details = None
        self.discriminator = None

        if drift_details is not None:
            self.drift_details = drift_details

    @property
    def drift_details(self):
        r"""Gets the drift_details of this ListDriftDetailsResponse.

        漂移详细信息。

        :return: The drift_details of this ListDriftDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.DriftDetail`]
        """
        return self._drift_details

    @drift_details.setter
    def drift_details(self, drift_details):
        r"""Sets the drift_details of this ListDriftDetailsResponse.

        漂移详细信息。

        :param drift_details: The drift_details of this ListDriftDetailsResponse.
        :type drift_details: list[:class:`huaweicloudsdkrgc.v1.DriftDetail`]
        """
        self._drift_details = drift_details

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
        if not isinstance(other, ListDriftDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
