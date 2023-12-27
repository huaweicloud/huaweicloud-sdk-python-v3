# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMavenInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'trace_id': 'str',
        'result': 'object'
    }

    attribute_map = {
        'status': 'status',
        'trace_id': 'trace_id',
        'result': 'result'
    }

    def __init__(self, status=None, trace_id=None, result=None):
        """ShowMavenInfoResponse

        The model defined in huaweicloud sdk

        :param status: 结果状态
        :type status: str
        :param trace_id: 请求id
        :type trace_id: str
        :param result: 请求返回结果，接口不同，返回不同
        :type result: object
        """
        
        super(ShowMavenInfoResponse, self).__init__()

        self._status = None
        self._trace_id = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if trace_id is not None:
            self.trace_id = trace_id
        if result is not None:
            self.result = result

    @property
    def status(self):
        """Gets the status of this ShowMavenInfoResponse.

        结果状态

        :return: The status of this ShowMavenInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowMavenInfoResponse.

        结果状态

        :param status: The status of this ShowMavenInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def trace_id(self):
        """Gets the trace_id of this ShowMavenInfoResponse.

        请求id

        :return: The trace_id of this ShowMavenInfoResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ShowMavenInfoResponse.

        请求id

        :param trace_id: The trace_id of this ShowMavenInfoResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def result(self):
        """Gets the result of this ShowMavenInfoResponse.

        请求返回结果，接口不同，返回不同

        :return: The result of this ShowMavenInfoResponse.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowMavenInfoResponse.

        请求返回结果，接口不同，返回不同

        :param result: The result of this ShowMavenInfoResponse.
        :type result: object
        """
        self._result = result

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
        if not isinstance(other, ShowMavenInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
