# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandleUnionMemberQuitListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'operation_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'operation_id': 'operation_id'
    }

    def __init__(self, result=None, operation_id=None):
        """HandleUnionMemberQuitListResponse

        The model defined in huaweicloud sdk

        :param result: 请求结果
        :type result: str
        :param operation_id: 操作记录ID
        :type operation_id: str
        """
        
        super(HandleUnionMemberQuitListResponse, self).__init__()

        self._result = None
        self._operation_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def result(self):
        """Gets the result of this HandleUnionMemberQuitListResponse.

        请求结果

        :return: The result of this HandleUnionMemberQuitListResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this HandleUnionMemberQuitListResponse.

        请求结果

        :param result: The result of this HandleUnionMemberQuitListResponse.
        :type result: str
        """
        self._result = result

    @property
    def operation_id(self):
        """Gets the operation_id of this HandleUnionMemberQuitListResponse.

        操作记录ID

        :return: The operation_id of this HandleUnionMemberQuitListResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this HandleUnionMemberQuitListResponse.

        操作记录ID

        :param operation_id: The operation_id of this HandleUnionMemberQuitListResponse.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, HandleUnionMemberQuitListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
