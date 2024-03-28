# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFlinkSqlJobTemplateResponse(SdkResponse):

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
        'template': 'FlinkSqlJobTemplateId'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'template': 'template'
    }

    def __init__(self, is_success=None, message=None, template=None):
        """DeleteFlinkSqlJobTemplateResponse

        The model defined in huaweicloud sdk

        :param is_success: 响应正确与否的标志，true表示成功。
        :type is_success: bool
        :param message: 消息内容。
        :type message: str
        :param template: 
        :type template: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateId`
        """
        
        super(DeleteFlinkSqlJobTemplateResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._template = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if template is not None:
            self.template = template

    @property
    def is_success(self):
        """Gets the is_success of this DeleteFlinkSqlJobTemplateResponse.

        响应正确与否的标志，true表示成功。

        :return: The is_success of this DeleteFlinkSqlJobTemplateResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DeleteFlinkSqlJobTemplateResponse.

        响应正确与否的标志，true表示成功。

        :param is_success: The is_success of this DeleteFlinkSqlJobTemplateResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DeleteFlinkSqlJobTemplateResponse.

        消息内容。

        :return: The message of this DeleteFlinkSqlJobTemplateResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeleteFlinkSqlJobTemplateResponse.

        消息内容。

        :param message: The message of this DeleteFlinkSqlJobTemplateResponse.
        :type message: str
        """
        self._message = message

    @property
    def template(self):
        """Gets the template of this DeleteFlinkSqlJobTemplateResponse.

        :return: The template of this DeleteFlinkSqlJobTemplateResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateId`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this DeleteFlinkSqlJobTemplateResponse.

        :param template: The template of this DeleteFlinkSqlJobTemplateResponse.
        :type template: :class:`huaweicloudsdkdli.v1.FlinkSqlJobTemplateId`
        """
        self._template = template

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
        if not isinstance(other, DeleteFlinkSqlJobTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
