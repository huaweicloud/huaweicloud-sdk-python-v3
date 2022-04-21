# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetRomaAppSecretResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'id': 'id',
        'secret': 'secret'
    }

    def __init__(self, id=None, secret=None):
        """ResetRomaAppSecretResponse

        The model defined in huaweicloud sdk

        :param id: 应用ID
        :type id: str
        :param secret: 应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、&#x3D;、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做
        :type secret: str
        """
        
        super(ResetRomaAppSecretResponse, self).__init__()

        self._id = None
        self._secret = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if secret is not None:
            self.secret = secret

    @property
    def id(self):
        """Gets the id of this ResetRomaAppSecretResponse.

        应用ID

        :return: The id of this ResetRomaAppSecretResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResetRomaAppSecretResponse.

        应用ID

        :param id: The id of this ResetRomaAppSecretResponse.
        :type id: str
        """
        self._id = id

    @property
    def secret(self):
        """Gets the secret of this ResetRomaAppSecretResponse.

        应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、=、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做

        :return: The secret of this ResetRomaAppSecretResponse.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ResetRomaAppSecretResponse.

        应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、=、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做

        :param secret: The secret of this ResetRomaAppSecretResponse.
        :type secret: str
        """
        self._secret = secret

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
        if not isinstance(other, ResetRomaAppSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
