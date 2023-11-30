# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChartRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'str',
        'content': 'file'
    }

    attribute_map = {
        'parameters': 'parameters',
        'content': 'content'
    }

    def __init__(self, parameters=None, content=None):
        """UpdateChartRequestBody

        The model defined in huaweicloud sdk

        :param parameters: 上传模板的配置参数，示例如下：\&quot;{\\\&quot;override\\\&quot;:true,\\\&quot;skip_lint\\\&quot;:true,\\\&quot;source\\\&quot;:\\\&quot;package\\\&quot;}\&quot; - skip_lint: whether lint uploaded chart - override: whether override existed chart - visible: update chart visible
        :type parameters: str
        :param content: 模板包文件
        :type content: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._parameters = None
        self._content = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        self.content = content

    @property
    def parameters(self):
        """Gets the parameters of this UpdateChartRequestBody.

        上传模板的配置参数，示例如下：\"{\\\"override\\\":true,\\\"skip_lint\\\":true,\\\"source\\\":\\\"package\\\"}\" - skip_lint: whether lint uploaded chart - override: whether override existed chart - visible: update chart visible

        :return: The parameters of this UpdateChartRequestBody.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpdateChartRequestBody.

        上传模板的配置参数，示例如下：\"{\\\"override\\\":true,\\\"skip_lint\\\":true,\\\"source\\\":\\\"package\\\"}\" - skip_lint: whether lint uploaded chart - override: whether override existed chart - visible: update chart visible

        :param parameters: The parameters of this UpdateChartRequestBody.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def content(self):
        """Gets the content of this UpdateChartRequestBody.

        模板包文件

        :return: The content of this UpdateChartRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateChartRequestBody.

        模板包文件

        :param content: The content of this UpdateChartRequestBody.
        :type content: :class:`huaweicloudsdkcore.http.formdata.FormFile`
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
        if not isinstance(other, UpdateChartRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
