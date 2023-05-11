# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomPage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_code': 'str',
        'content_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'status_code': 'status_code',
        'content_type': 'content_type',
        'content': 'content'
    }

    def __init__(self, status_code=None, content_type=None, content=None):
        """CustomPage

        The model defined in huaweicloud sdk

        :param status_code: 返回状态码
        :type status_code: str
        :param content_type: “自定义”告警页面内容类型，可选择text/html、text/xml和application/json三种类型
        :type content_type: str
        :param content: 根据选择的“页面类型”配置对应的页面内容，具体示例可以参考“Web应用防火墙 WAF”用户手册
        :type content: str
        """
        
        

        self._status_code = None
        self._content_type = None
        self._content = None
        self.discriminator = None

        self.status_code = status_code
        self.content_type = content_type
        self.content = content

    @property
    def status_code(self):
        """Gets the status_code of this CustomPage.

        返回状态码

        :return: The status_code of this CustomPage.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CustomPage.

        返回状态码

        :param status_code: The status_code of this CustomPage.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def content_type(self):
        """Gets the content_type of this CustomPage.

        “自定义”告警页面内容类型，可选择text/html、text/xml和application/json三种类型

        :return: The content_type of this CustomPage.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CustomPage.

        “自定义”告警页面内容类型，可选择text/html、text/xml和application/json三种类型

        :param content_type: The content_type of this CustomPage.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this CustomPage.

        根据选择的“页面类型”配置对应的页面内容，具体示例可以参考“Web应用防火墙 WAF”用户手册

        :return: The content of this CustomPage.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CustomPage.

        根据选择的“页面类型”配置对应的页面内容，具体示例可以参考“Web应用防火墙 WAF”用户手册

        :param content: The content of this CustomPage.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, CustomPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
