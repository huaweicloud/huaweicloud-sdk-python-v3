# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePeriodToOnDemandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_details': 'list[ErrorDetail]'
    }

    attribute_map = {
        'error_details': 'error_details'
    }

    def __init__(self, error_details=None):
        """UpdatePeriodToOnDemandResponse

        The model defined in huaweicloud sdk

        :param error_details: HTTP 200的时候返回该字段；部分失败时仅返回失败的记录；如果全部成功，则该记录为空，具体参见表1。
        :type error_details: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        """
        
        super(UpdatePeriodToOnDemandResponse, self).__init__()

        self._error_details = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details

    @property
    def error_details(self):
        """Gets the error_details of this UpdatePeriodToOnDemandResponse.

        HTTP 200的时候返回该字段；部分失败时仅返回失败的记录；如果全部成功，则该记录为空，具体参见表1。

        :return: The error_details of this UpdatePeriodToOnDemandResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this UpdatePeriodToOnDemandResponse.

        HTTP 200的时候返回该字段；部分失败时仅返回失败的记录；如果全部成功，则该记录为空，具体参见表1。

        :param error_details: The error_details of this UpdatePeriodToOnDemandResponse.
        :type error_details: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        """
        self._error_details = error_details

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
        if not isinstance(other, UpdatePeriodToOnDemandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
