# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimTemplateMaterialsResponse(SdkResponse):

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
        'message': 'str',
        'data': 'ListAimTemplateMaterialsResponseMode'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, status=None, message=None, data=None):
        r"""ListAimTemplateMaterialsResponse

        The model defined in huaweicloud sdk

        :param status: 状态码。
        :type status: str
        :param message: 响应信息。
        :type message: str
        :param data: 
        :type data: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateMaterialsResponseMode`
        """
        
        super(ListAimTemplateMaterialsResponse, self).__init__()

        self._status = None
        self._message = None
        self._data = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data

    @property
    def status(self):
        r"""Gets the status of this ListAimTemplateMaterialsResponse.

        状态码。

        :return: The status of this ListAimTemplateMaterialsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAimTemplateMaterialsResponse.

        状态码。

        :param status: The status of this ListAimTemplateMaterialsResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ListAimTemplateMaterialsResponse.

        响应信息。

        :return: The message of this ListAimTemplateMaterialsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListAimTemplateMaterialsResponse.

        响应信息。

        :param message: The message of this ListAimTemplateMaterialsResponse.
        :type message: str
        """
        self._message = message

    @property
    def data(self):
        r"""Gets the data of this ListAimTemplateMaterialsResponse.

        :return: The data of this ListAimTemplateMaterialsResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateMaterialsResponseMode`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAimTemplateMaterialsResponse.

        :param data: The data of this ListAimTemplateMaterialsResponse.
        :type data: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateMaterialsResponseMode`
        """
        self._data = data

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
        if not isinstance(other, ListAimTemplateMaterialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
