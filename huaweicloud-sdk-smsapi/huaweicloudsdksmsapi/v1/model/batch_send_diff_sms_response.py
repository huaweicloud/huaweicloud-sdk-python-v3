# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSendDiffSmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "BatchSendDiffSmsResponse"

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'description': 'str',
        'result': 'list[SmsID]'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'result': 'result'
    }

    def __init__(self, code=None, description=None, result=None):
        """BatchSendDiffSmsResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param description: 错误描述
        :type description: str
        :param result: 短信状态
        :type result: list[:class:`huaweicloudsdksmsapi.v1.SmsID`]
        """
        
        super(BatchSendDiffSmsResponse, self).__init__()

        self._code = None
        self._description = None
        self._result = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if result is not None:
            self.result = result

    @property
    def code(self):
        """Gets the code of this BatchSendDiffSmsResponse.

        错误码

        :return: The code of this BatchSendDiffSmsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BatchSendDiffSmsResponse.

        错误码

        :param code: The code of this BatchSendDiffSmsResponse.
        :type code: str
        """
        self._code = code

    @property
    def description(self):
        """Gets the description of this BatchSendDiffSmsResponse.

        错误描述

        :return: The description of this BatchSendDiffSmsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchSendDiffSmsResponse.

        错误描述

        :param description: The description of this BatchSendDiffSmsResponse.
        :type description: str
        """
        self._description = description

    @property
    def result(self):
        """Gets the result of this BatchSendDiffSmsResponse.

        短信状态

        :return: The result of this BatchSendDiffSmsResponse.
        :rtype: list[:class:`huaweicloudsdksmsapi.v1.SmsID`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BatchSendDiffSmsResponse.

        短信状态

        :param result: The result of this BatchSendDiffSmsResponse.
        :type result: list[:class:`huaweicloudsdksmsapi.v1.SmsID`]
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
        if not isinstance(other, BatchSendDiffSmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
