# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverTestResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'switchover_test_record': 'SwitchoverTestRecord'
    }

    attribute_map = {
        'request_id': 'request_id',
        'switchover_test_record': 'switchover_test_record'
    }

    def __init__(self, request_id=None, switchover_test_record=None):
        """SwitchoverTestResponse

        The model defined in huaweicloud sdk

        :param request_id: 操作请求ID
        :type request_id: str
        :param switchover_test_record: 
        :type switchover_test_record: :class:`huaweicloudsdkdc.v3.SwitchoverTestRecord`
        """
        
        super(SwitchoverTestResponse, self).__init__()

        self._request_id = None
        self._switchover_test_record = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if switchover_test_record is not None:
            self.switchover_test_record = switchover_test_record

    @property
    def request_id(self):
        """Gets the request_id of this SwitchoverTestResponse.

        操作请求ID

        :return: The request_id of this SwitchoverTestResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SwitchoverTestResponse.

        操作请求ID

        :param request_id: The request_id of this SwitchoverTestResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def switchover_test_record(self):
        """Gets the switchover_test_record of this SwitchoverTestResponse.

        :return: The switchover_test_record of this SwitchoverTestResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.SwitchoverTestRecord`
        """
        return self._switchover_test_record

    @switchover_test_record.setter
    def switchover_test_record(self, switchover_test_record):
        """Sets the switchover_test_record of this SwitchoverTestResponse.

        :param switchover_test_record: The switchover_test_record of this SwitchoverTestResponse.
        :type switchover_test_record: :class:`huaweicloudsdkdc.v3.SwitchoverTestRecord`
        """
        self._switchover_test_record = switchover_test_record

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
        if not isinstance(other, SwitchoverTestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
