# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimMsgSignatureResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[SmsSignatureInfo]',
        'page_info': 'Page'
    }

    attribute_map = {
        'result': 'result',
        'page_info': 'page_info'
    }

    def __init__(self, result=None, page_info=None):
        r"""ListAimMsgSignatureResponse

        The model defined in huaweicloud sdk

        :param result: 查询结果。
        :type result: list[:class:`huaweicloudsdkkoomessage.v1.SmsSignatureInfo`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        super(ListAimMsgSignatureResponse, self).__init__()

        self._result = None
        self._page_info = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if page_info is not None:
            self.page_info = page_info

    @property
    def result(self):
        r"""Gets the result of this ListAimMsgSignatureResponse.

        查询结果。

        :return: The result of this ListAimMsgSignatureResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.SmsSignatureInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListAimMsgSignatureResponse.

        查询结果。

        :param result: The result of this ListAimMsgSignatureResponse.
        :type result: list[:class:`huaweicloudsdkkoomessage.v1.SmsSignatureInfo`]
        """
        self._result = result

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAimMsgSignatureResponse.

        :return: The page_info of this ListAimMsgSignatureResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAimMsgSignatureResponse.

        :param page_info: The page_info of this ListAimMsgSignatureResponse.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAimMsgSignatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
