# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSendSmsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "BatchSendSmsRequestBody"

    sensitive_list = []

    openapi_types = {
        '_from': 'str',
        'to': 'str',
        'template_id': 'str',
        'template_paras': 'str',
        'status_callback': 'str',
        'extend': 'str',
        'signature': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'template_id': 'templateId',
        'template_paras': 'templateParas',
        'status_callback': 'statusCallback',
        'extend': 'extend',
        'signature': 'signature'
    }

    def __init__(self, _from=None, to=None, template_id=None, template_paras=None, status_callback=None, extend=None, signature=None):
        r"""BatchSendSmsRequestBody

        The model defined in huaweicloud sdk

        :param _from: 短信发送方的号码
        :type _from: str
        :param to: 短信接收方的号码
        :type to: str
        :param template_id: 短信模板ID
        :type template_id: str
        :param template_paras: 短信模板的变量值
        :type template_paras: str
        :param status_callback: SP的回调地址
        :type status_callback: str
        :param extend: 扩展参数，在状态报告中会原样返回。
        :type extend: str
        :param signature: 短信签名
        :type signature: str
        """
        
        

        self.__from = None
        self._to = None
        self._template_id = None
        self._template_paras = None
        self._status_callback = None
        self._extend = None
        self._signature = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if template_id is not None:
            self.template_id = template_id
        if template_paras is not None:
            self.template_paras = template_paras
        if status_callback is not None:
            self.status_callback = status_callback
        if extend is not None:
            self.extend = extend
        if signature is not None:
            self.signature = signature

    @property
    def _from(self):
        r"""Gets the _from of this BatchSendSmsRequestBody.

        短信发送方的号码

        :return: The _from of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this BatchSendSmsRequestBody.

        短信发送方的号码

        :param _from: The _from of this BatchSendSmsRequestBody.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this BatchSendSmsRequestBody.

        短信接收方的号码

        :return: The to of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this BatchSendSmsRequestBody.

        短信接收方的号码

        :param to: The to of this BatchSendSmsRequestBody.
        :type to: str
        """
        self._to = to

    @property
    def template_id(self):
        r"""Gets the template_id of this BatchSendSmsRequestBody.

        短信模板ID

        :return: The template_id of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this BatchSendSmsRequestBody.

        短信模板ID

        :param template_id: The template_id of this BatchSendSmsRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_paras(self):
        r"""Gets the template_paras of this BatchSendSmsRequestBody.

        短信模板的变量值

        :return: The template_paras of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._template_paras

    @template_paras.setter
    def template_paras(self, template_paras):
        r"""Sets the template_paras of this BatchSendSmsRequestBody.

        短信模板的变量值

        :param template_paras: The template_paras of this BatchSendSmsRequestBody.
        :type template_paras: str
        """
        self._template_paras = template_paras

    @property
    def status_callback(self):
        r"""Gets the status_callback of this BatchSendSmsRequestBody.

        SP的回调地址

        :return: The status_callback of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._status_callback

    @status_callback.setter
    def status_callback(self, status_callback):
        r"""Sets the status_callback of this BatchSendSmsRequestBody.

        SP的回调地址

        :param status_callback: The status_callback of this BatchSendSmsRequestBody.
        :type status_callback: str
        """
        self._status_callback = status_callback

    @property
    def extend(self):
        r"""Gets the extend of this BatchSendSmsRequestBody.

        扩展参数，在状态报告中会原样返回。

        :return: The extend of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this BatchSendSmsRequestBody.

        扩展参数，在状态报告中会原样返回。

        :param extend: The extend of this BatchSendSmsRequestBody.
        :type extend: str
        """
        self._extend = extend

    @property
    def signature(self):
        r"""Gets the signature of this BatchSendSmsRequestBody.

        短信签名

        :return: The signature of this BatchSendSmsRequestBody.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        r"""Sets the signature of this BatchSendSmsRequestBody.

        短信签名

        :param signature: The signature of this BatchSendSmsRequestBody.
        :type signature: str
        """
        self._signature = signature

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
        if not isinstance(other, BatchSendSmsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
