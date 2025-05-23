# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkSqlJobTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'template_list': 'FlinkSqlJobTemplateList'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'template_list': 'template_list'
    }

    def __init__(self, is_success=None, message=None, template_list=None):
        r"""ListFlinkSqlJobTemplatesResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求是否成功
        :type is_success: bool
        :param message: 消息内容。
        :type message: str
        :param template_list: 
        :type template_list: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateList`
        """
        
        super(ListFlinkSqlJobTemplatesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._template_list = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if template_list is not None:
            self.template_list = template_list

    @property
    def is_success(self):
        r"""Gets the is_success of this ListFlinkSqlJobTemplatesResponse.

        请求是否成功

        :return: The is_success of this ListFlinkSqlJobTemplatesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListFlinkSqlJobTemplatesResponse.

        请求是否成功

        :param is_success: The is_success of this ListFlinkSqlJobTemplatesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListFlinkSqlJobTemplatesResponse.

        消息内容。

        :return: The message of this ListFlinkSqlJobTemplatesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListFlinkSqlJobTemplatesResponse.

        消息内容。

        :param message: The message of this ListFlinkSqlJobTemplatesResponse.
        :type message: str
        """
        self._message = message

    @property
    def template_list(self):
        r"""Gets the template_list of this ListFlinkSqlJobTemplatesResponse.

        :return: The template_list of this ListFlinkSqlJobTemplatesResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateList`
        """
        return self._template_list

    @template_list.setter
    def template_list(self, template_list):
        r"""Sets the template_list of this ListFlinkSqlJobTemplatesResponse.

        :param template_list: The template_list of this ListFlinkSqlJobTemplatesResponse.
        :type template_list: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateList`
        """
        self._template_list = template_list

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
        if not isinstance(other, ListFlinkSqlJobTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
