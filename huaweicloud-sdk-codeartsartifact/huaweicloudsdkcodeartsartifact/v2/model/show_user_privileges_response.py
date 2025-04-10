# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserPrivilegesResponse(SdkResponse):

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
        'result': 'PrivilegesResponseResult'
    }

    attribute_map = {
        'status': 'status',
        'trace_id': 'traceId',
        'result': 'result'
    }

    def __init__(self, status=None, trace_id=None, result=None):
        r"""ShowUserPrivilegesResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**:  请求成功、失败状态。 **取值范围**: success: 请求成功。 error: 请求失败。 
        :type status: str
        :param trace_id: **参数解释**:  请求id，当前请求唯一标识。 **取值范围**: 数字及中划线(-)组成的字符串。 
        :type trace_id: str
        :param result: 
        :type result: :class:`huaweicloudsdkcodeartsartifact.v2.PrivilegesResponseResult`
        """
        
        super(ShowUserPrivilegesResponse, self).__init__()

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
        r"""Gets the status of this ShowUserPrivilegesResponse.

        **参数解释**:  请求成功、失败状态。 **取值范围**: success: 请求成功。 error: 请求失败。 

        :return: The status of this ShowUserPrivilegesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowUserPrivilegesResponse.

        **参数解释**:  请求成功、失败状态。 **取值范围**: success: 请求成功。 error: 请求失败。 

        :param status: The status of this ShowUserPrivilegesResponse.
        :type status: str
        """
        self._status = status

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ShowUserPrivilegesResponse.

        **参数解释**:  请求id，当前请求唯一标识。 **取值范围**: 数字及中划线(-)组成的字符串。 

        :return: The trace_id of this ShowUserPrivilegesResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ShowUserPrivilegesResponse.

        **参数解释**:  请求id，当前请求唯一标识。 **取值范围**: 数字及中划线(-)组成的字符串。 

        :param trace_id: The trace_id of this ShowUserPrivilegesResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def result(self):
        r"""Gets the result of this ShowUserPrivilegesResponse.

        :return: The result of this ShowUserPrivilegesResponse.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.PrivilegesResponseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowUserPrivilegesResponse.

        :param result: The result of this ShowUserPrivilegesResponse.
        :type result: :class:`huaweicloudsdkcodeartsartifact.v2.PrivilegesResponseResult`
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
        if not isinstance(other, ShowUserPrivilegesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
