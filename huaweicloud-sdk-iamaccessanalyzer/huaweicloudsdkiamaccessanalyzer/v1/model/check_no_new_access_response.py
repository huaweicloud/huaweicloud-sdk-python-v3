# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNoNewAccessResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'check_result': 'str',
        'reasons': 'list[CheckNoNewAccessReason]'
    }

    attribute_map = {
        'message': 'message',
        'check_result': 'check_result',
        'reasons': 'reasons'
    }

    def __init__(self, message=None, check_result=None, reasons=None):
        r"""CheckNoNewAccessResponse

        The model defined in huaweicloud sdk

        :param message: 更新后的策略是否允许新访问权限的消息。
        :type message: str
        :param check_result: 检查新访问权限的结果。
        :type check_result: str
        :param reasons: 新增action的statement描述。
        :type reasons: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.CheckNoNewAccessReason`]
        """
        
        super(CheckNoNewAccessResponse, self).__init__()

        self._message = None
        self._check_result = None
        self._reasons = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if check_result is not None:
            self.check_result = check_result
        if reasons is not None:
            self.reasons = reasons

    @property
    def message(self):
        r"""Gets the message of this CheckNoNewAccessResponse.

        更新后的策略是否允许新访问权限的消息。

        :return: The message of this CheckNoNewAccessResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CheckNoNewAccessResponse.

        更新后的策略是否允许新访问权限的消息。

        :param message: The message of this CheckNoNewAccessResponse.
        :type message: str
        """
        self._message = message

    @property
    def check_result(self):
        r"""Gets the check_result of this CheckNoNewAccessResponse.

        检查新访问权限的结果。

        :return: The check_result of this CheckNoNewAccessResponse.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        r"""Sets the check_result of this CheckNoNewAccessResponse.

        检查新访问权限的结果。

        :param check_result: The check_result of this CheckNoNewAccessResponse.
        :type check_result: str
        """
        self._check_result = check_result

    @property
    def reasons(self):
        r"""Gets the reasons of this CheckNoNewAccessResponse.

        新增action的statement描述。

        :return: The reasons of this CheckNoNewAccessResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.CheckNoNewAccessReason`]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        r"""Sets the reasons of this CheckNoNewAccessResponse.

        新增action的statement描述。

        :param reasons: The reasons of this CheckNoNewAccessResponse.
        :type reasons: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.CheckNoNewAccessReason`]
        """
        self._reasons = reasons

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
        if not isinstance(other, CheckNoNewAccessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
