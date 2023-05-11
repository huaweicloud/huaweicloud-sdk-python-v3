# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiMockCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remark': 'str',
        'result_content': 'str',
        'version': 'str',
        'authorizer_id': 'str'
    }

    attribute_map = {
        'remark': 'remark',
        'result_content': 'result_content',
        'version': 'version',
        'authorizer_id': 'authorizer_id'
    }

    def __init__(self, remark=None, result_content=None, version=None, authorizer_id=None):
        """ApiMockCreate

        The model defined in huaweicloud sdk

        :param remark: 描述信息。长度不超过255个字符 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param result_content: 返回结果
        :type result_content: str
        :param version: 版本。字符长度不超过64
        :type version: str
        :param authorizer_id: 后端自定义认证ID
        :type authorizer_id: str
        """
        
        

        self._remark = None
        self._result_content = None
        self._version = None
        self._authorizer_id = None
        self.discriminator = None

        if remark is not None:
            self.remark = remark
        if result_content is not None:
            self.result_content = result_content
        if version is not None:
            self.version = version
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id

    @property
    def remark(self):
        """Gets the remark of this ApiMockCreate.

        描述信息。长度不超过255个字符 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiMockCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiMockCreate.

        描述信息。长度不超过255个字符 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiMockCreate.
        :type remark: str
        """
        self._remark = remark

    @property
    def result_content(self):
        """Gets the result_content of this ApiMockCreate.

        返回结果

        :return: The result_content of this ApiMockCreate.
        :rtype: str
        """
        return self._result_content

    @result_content.setter
    def result_content(self, result_content):
        """Sets the result_content of this ApiMockCreate.

        返回结果

        :param result_content: The result_content of this ApiMockCreate.
        :type result_content: str
        """
        self._result_content = result_content

    @property
    def version(self):
        """Gets the version of this ApiMockCreate.

        版本。字符长度不超过64

        :return: The version of this ApiMockCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiMockCreate.

        版本。字符长度不超过64

        :param version: The version of this ApiMockCreate.
        :type version: str
        """
        self._version = version

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiMockCreate.

        后端自定义认证ID

        :return: The authorizer_id of this ApiMockCreate.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiMockCreate.

        后端自定义认证ID

        :param authorizer_id: The authorizer_id of this ApiMockCreate.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

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
        if not isinstance(other, ApiMockCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
