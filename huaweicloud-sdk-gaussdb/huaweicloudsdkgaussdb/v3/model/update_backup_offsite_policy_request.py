# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBackupOffsitePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'body': 'UpdateBackupOffsitePolicyRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, body=None):
        r"""UpdateBackupOffsitePolicyRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param body: Body of the UpdateBackupOffsitePolicyRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.UpdateBackupOffsitePolicyRequestBody`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateBackupOffsitePolicyRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this UpdateBackupOffsitePolicyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateBackupOffsitePolicyRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this UpdateBackupOffsitePolicyRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateBackupOffsitePolicyRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this UpdateBackupOffsitePolicyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateBackupOffsitePolicyRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this UpdateBackupOffsitePolicyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        r"""Gets the body of this UpdateBackupOffsitePolicyRequest.

        :return: The body of this UpdateBackupOffsitePolicyRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateBackupOffsitePolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateBackupOffsitePolicyRequest.

        :param body: The body of this UpdateBackupOffsitePolicyRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.UpdateBackupOffsitePolicyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateBackupOffsitePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
