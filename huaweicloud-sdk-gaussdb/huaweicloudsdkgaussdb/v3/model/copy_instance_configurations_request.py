# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyInstanceConfigurationsRequest:

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
        'configuration_id': 'str',
        'body': 'CopyInstanceConfigurationsRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'configuration_id': 'configuration_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, configuration_id=None, body=None):
        """CopyInstanceConfigurationsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param configuration_id: 参数组ID。  通过调用[查询实例详情信息](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlInstanceInfo.html)接口获取。  请求响应成功后在响应消息体中包含的“configuration_id”的值即为configuration_id值。
        :type configuration_id: str
        :param body: Body of the CopyInstanceConfigurationsRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.CopyInstanceConfigurationsRequestBody`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._configuration_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.configuration_id = configuration_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this CopyInstanceConfigurationsRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this CopyInstanceConfigurationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CopyInstanceConfigurationsRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this CopyInstanceConfigurationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this CopyInstanceConfigurationsRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this CopyInstanceConfigurationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CopyInstanceConfigurationsRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this CopyInstanceConfigurationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def configuration_id(self):
        """Gets the configuration_id of this CopyInstanceConfigurationsRequest.

        参数组ID。  通过调用[查询实例详情信息](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlInstanceInfo.html)接口获取。  请求响应成功后在响应消息体中包含的“configuration_id”的值即为configuration_id值。

        :return: The configuration_id of this CopyInstanceConfigurationsRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this CopyInstanceConfigurationsRequest.

        参数组ID。  通过调用[查询实例详情信息](https://support.huaweicloud.com/api-gaussdbformysql/ShowGaussMySqlInstanceInfo.html)接口获取。  请求响应成功后在响应消息体中包含的“configuration_id”的值即为configuration_id值。

        :param configuration_id: The configuration_id of this CopyInstanceConfigurationsRequest.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def body(self):
        """Gets the body of this CopyInstanceConfigurationsRequest.

        :return: The body of this CopyInstanceConfigurationsRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CopyInstanceConfigurationsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CopyInstanceConfigurationsRequest.

        :param body: The body of this CopyInstanceConfigurationsRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.CopyInstanceConfigurationsRequestBody`
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
        if not isinstance(other, CopyInstanceConfigurationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
