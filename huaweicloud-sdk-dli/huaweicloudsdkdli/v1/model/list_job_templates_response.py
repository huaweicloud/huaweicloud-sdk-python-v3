# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobTemplatesResponse(SdkResponse):

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
        'count': 'int',
        'templates': 'list[JobTemplateInfo]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'count': 'count',
        'templates': 'templates'
    }

    def __init__(self, is_success=None, message=None, count=None, templates=None):
        """ListJobTemplatesResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param count: 返回的模板个数
        :type count: int
        :param templates: 模板信息列表。
        :type templates: list[:class:`huaweicloudsdkdli.v1.JobTemplateInfo`]
        """
        
        super(ListJobTemplatesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._count = None
        self._templates = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if count is not None:
            self.count = count
        if templates is not None:
            self.templates = templates

    @property
    def is_success(self):
        """Gets the is_success of this ListJobTemplatesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListJobTemplatesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListJobTemplatesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListJobTemplatesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListJobTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListJobTemplatesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListJobTemplatesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListJobTemplatesResponse.
        :type message: str
        """
        self._message = message

    @property
    def count(self):
        """Gets the count of this ListJobTemplatesResponse.

        返回的模板个数

        :return: The count of this ListJobTemplatesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListJobTemplatesResponse.

        返回的模板个数

        :param count: The count of this ListJobTemplatesResponse.
        :type count: int
        """
        self._count = count

    @property
    def templates(self):
        """Gets the templates of this ListJobTemplatesResponse.

        模板信息列表。

        :return: The templates of this ListJobTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.JobTemplateInfo`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListJobTemplatesResponse.

        模板信息列表。

        :param templates: The templates of this ListJobTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkdli.v1.JobTemplateInfo`]
        """
        self._templates = templates

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
        if not isinstance(other, ListJobTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
