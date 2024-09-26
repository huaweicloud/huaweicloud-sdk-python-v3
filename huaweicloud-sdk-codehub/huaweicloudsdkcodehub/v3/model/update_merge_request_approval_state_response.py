# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestApprovalStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'ApproverBasicDto',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, result=None, status=None):
        """UpdateMergeRequestApprovalStateResponse

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkcodehub.v3.ApproverBasicDto`
        :param status: 响应状态
        :type status: str
        """
        
        super(UpdateMergeRequestApprovalStateResponse, self).__init__()

        self._result = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def result(self):
        """Gets the result of this UpdateMergeRequestApprovalStateResponse.

        :return: The result of this UpdateMergeRequestApprovalStateResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v3.ApproverBasicDto`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UpdateMergeRequestApprovalStateResponse.

        :param result: The result of this UpdateMergeRequestApprovalStateResponse.
        :type result: :class:`huaweicloudsdkcodehub.v3.ApproverBasicDto`
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this UpdateMergeRequestApprovalStateResponse.

        响应状态

        :return: The status of this UpdateMergeRequestApprovalStateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateMergeRequestApprovalStateResponse.

        响应状态

        :param status: The status of this UpdateMergeRequestApprovalStateResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateMergeRequestApprovalStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
