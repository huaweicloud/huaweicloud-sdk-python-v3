# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHandshakesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'handshakes': 'list[HandshakeDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'handshakes': 'handshakes',
        'page_info': 'page_info'
    }

    def __init__(self, handshakes=None, page_info=None):
        r"""ListHandshakesResponse

        The model defined in huaweicloud sdk

        :param handshakes: 邀请（握手）对象的列表，其中包含与指定账号关联的每个邀请（握手）的详细信息。
        :type handshakes: list[:class:`huaweicloudsdkorganizations.v1.HandshakeDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListHandshakesResponse, self).__init__()

        self._handshakes = None
        self._page_info = None
        self.discriminator = None

        if handshakes is not None:
            self.handshakes = handshakes
        if page_info is not None:
            self.page_info = page_info

    @property
    def handshakes(self):
        r"""Gets the handshakes of this ListHandshakesResponse.

        邀请（握手）对象的列表，其中包含与指定账号关联的每个邀请（握手）的详细信息。

        :return: The handshakes of this ListHandshakesResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.HandshakeDto`]
        """
        return self._handshakes

    @handshakes.setter
    def handshakes(self, handshakes):
        r"""Sets the handshakes of this ListHandshakesResponse.

        邀请（握手）对象的列表，其中包含与指定账号关联的每个邀请（握手）的详细信息。

        :param handshakes: The handshakes of this ListHandshakesResponse.
        :type handshakes: list[:class:`huaweicloudsdkorganizations.v1.HandshakeDto`]
        """
        self._handshakes = handshakes

    @property
    def page_info(self):
        r"""Gets the page_info of this ListHandshakesResponse.

        :return: The page_info of this ListHandshakesResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListHandshakesResponse.

        :param page_info: The page_info of this ListHandshakesResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
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
        if not isinstance(other, ListHandshakesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
