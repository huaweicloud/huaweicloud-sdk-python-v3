# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSendDiffSmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "BatchSendDiffSmsRequestBody"

    sensitive_list = []

    openapi_types = {
        '_from': 'str',
        'status_callback': 'str',
        'sms_content': 'list[SmsContent]',
        'extend': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'status_callback': 'statusCallback',
        'sms_content': 'smsContent',
        'extend': 'extend'
    }

    def __init__(self, _from=None, status_callback=None, sms_content=None, extend=None):
        r"""BatchSendDiffSmsRequestBody

        The model defined in huaweicloud sdk

        :param _from: 短信发送方的号码
        :type _from: str
        :param status_callback: SP的回调地址，用于单条接收短信状态报告
        :type status_callback: str
        :param sms_content: 短信内容
        :type sms_content: list[:class:`huaweicloudsdksmsapi.v1.SmsContent`]
        :param extend: 扩展参数
        :type extend: str
        """
        
        

        self.__from = None
        self._status_callback = None
        self._sms_content = None
        self._extend = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if status_callback is not None:
            self.status_callback = status_callback
        if sms_content is not None:
            self.sms_content = sms_content
        if extend is not None:
            self.extend = extend

    @property
    def _from(self):
        r"""Gets the _from of this BatchSendDiffSmsRequestBody.

        短信发送方的号码

        :return: The _from of this BatchSendDiffSmsRequestBody.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this BatchSendDiffSmsRequestBody.

        短信发送方的号码

        :param _from: The _from of this BatchSendDiffSmsRequestBody.
        :type _from: str
        """
        self.__from = _from

    @property
    def status_callback(self):
        r"""Gets the status_callback of this BatchSendDiffSmsRequestBody.

        SP的回调地址，用于单条接收短信状态报告

        :return: The status_callback of this BatchSendDiffSmsRequestBody.
        :rtype: str
        """
        return self._status_callback

    @status_callback.setter
    def status_callback(self, status_callback):
        r"""Sets the status_callback of this BatchSendDiffSmsRequestBody.

        SP的回调地址，用于单条接收短信状态报告

        :param status_callback: The status_callback of this BatchSendDiffSmsRequestBody.
        :type status_callback: str
        """
        self._status_callback = status_callback

    @property
    def sms_content(self):
        r"""Gets the sms_content of this BatchSendDiffSmsRequestBody.

        短信内容

        :return: The sms_content of this BatchSendDiffSmsRequestBody.
        :rtype: list[:class:`huaweicloudsdksmsapi.v1.SmsContent`]
        """
        return self._sms_content

    @sms_content.setter
    def sms_content(self, sms_content):
        r"""Sets the sms_content of this BatchSendDiffSmsRequestBody.

        短信内容

        :param sms_content: The sms_content of this BatchSendDiffSmsRequestBody.
        :type sms_content: list[:class:`huaweicloudsdksmsapi.v1.SmsContent`]
        """
        self._sms_content = sms_content

    @property
    def extend(self):
        r"""Gets the extend of this BatchSendDiffSmsRequestBody.

        扩展参数

        :return: The extend of this BatchSendDiffSmsRequestBody.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this BatchSendDiffSmsRequestBody.

        扩展参数

        :param extend: The extend of this BatchSendDiffSmsRequestBody.
        :type extend: str
        """
        self._extend = extend

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
        if not isinstance(other, BatchSendDiffSmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
