# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMessageTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'message_template_count': 'int',
        'message_templates': 'list[MessageTemplate]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'message_template_count': 'message_template_count',
        'message_templates': 'message_templates'
    }

    def __init__(self, request_id=None, message_template_count=None, message_templates=None):
        r"""ListMessageTemplatesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param message_template_count: 返回的模板个数。
        :type message_template_count: int
        :param message_templates: Message_template结构体数组。
        :type message_templates: list[:class:`huaweicloudsdksmn.v2.MessageTemplate`]
        """
        
        super(ListMessageTemplatesResponse, self).__init__()

        self._request_id = None
        self._message_template_count = None
        self._message_templates = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if message_template_count is not None:
            self.message_template_count = message_template_count
        if message_templates is not None:
            self.message_templates = message_templates

    @property
    def request_id(self):
        r"""Gets the request_id of this ListMessageTemplatesResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListMessageTemplatesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListMessageTemplatesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListMessageTemplatesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def message_template_count(self):
        r"""Gets the message_template_count of this ListMessageTemplatesResponse.

        返回的模板个数。

        :return: The message_template_count of this ListMessageTemplatesResponse.
        :rtype: int
        """
        return self._message_template_count

    @message_template_count.setter
    def message_template_count(self, message_template_count):
        r"""Sets the message_template_count of this ListMessageTemplatesResponse.

        返回的模板个数。

        :param message_template_count: The message_template_count of this ListMessageTemplatesResponse.
        :type message_template_count: int
        """
        self._message_template_count = message_template_count

    @property
    def message_templates(self):
        r"""Gets the message_templates of this ListMessageTemplatesResponse.

        Message_template结构体数组。

        :return: The message_templates of this ListMessageTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.MessageTemplate`]
        """
        return self._message_templates

    @message_templates.setter
    def message_templates(self, message_templates):
        r"""Sets the message_templates of this ListMessageTemplatesResponse.

        Message_template结构体数组。

        :param message_templates: The message_templates of this ListMessageTemplatesResponse.
        :type message_templates: list[:class:`huaweicloudsdksmn.v2.MessageTemplate`]
        """
        self._message_templates = message_templates

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
        if not isinstance(other, ListMessageTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
