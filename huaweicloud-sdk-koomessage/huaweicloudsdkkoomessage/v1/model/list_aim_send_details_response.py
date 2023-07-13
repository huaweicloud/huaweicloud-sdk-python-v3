# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimSendDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'send_details': 'list[AIMSendDetail]',
        'page_info': 'Page'
    }

    attribute_map = {
        'send_details': 'send_details',
        'page_info': 'page_info'
    }

    def __init__(self, send_details=None, page_info=None):
        """ListAimSendDetailsResponse

        The model defined in huaweicloud sdk

        :param send_details: 查询发送明细结果集。
        :type send_details: list[:class:`huaweicloudsdkkoomessage.v1.AIMSendDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        super(ListAimSendDetailsResponse, self).__init__()

        self._send_details = None
        self._page_info = None
        self.discriminator = None

        if send_details is not None:
            self.send_details = send_details
        if page_info is not None:
            self.page_info = page_info

    @property
    def send_details(self):
        """Gets the send_details of this ListAimSendDetailsResponse.

        查询发送明细结果集。

        :return: The send_details of this ListAimSendDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AIMSendDetail`]
        """
        return self._send_details

    @send_details.setter
    def send_details(self, send_details):
        """Sets the send_details of this ListAimSendDetailsResponse.

        查询发送明细结果集。

        :param send_details: The send_details of this ListAimSendDetailsResponse.
        :type send_details: list[:class:`huaweicloudsdkkoomessage.v1.AIMSendDetail`]
        """
        self._send_details = send_details

    @property
    def page_info(self):
        """Gets the page_info of this ListAimSendDetailsResponse.

        :return: The page_info of this ListAimSendDetailsResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAimSendDetailsResponse.

        :param page_info: The page_info of this ListAimSendDetailsResponse.
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
        if not isinstance(other, ListAimSendDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
