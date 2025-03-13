# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_id': 'str',
        'x_enterprise_project_id': 'str',
        'body': 'CreateOrUpdateSecretReq'
    }

    attribute_map = {
        'secret_id': 'secret_id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'body': 'body'
    }

    def __init__(self, secret_id=None, x_enterprise_project_id=None, body=None):
        """UpdateSecretRequest

        The model defined in huaweicloud sdk

        :param secret_id: 凭据ID。
        :type secret_id: str
        :param x_enterprise_project_id: 企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。
        :type x_enterprise_project_id: str
        :param body: Body of the UpdateSecretRequest
        :type body: :class:`huaweicloudsdkcae.v1.CreateOrUpdateSecretReq`
        """
        
        

        self._secret_id = None
        self._x_enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.secret_id = secret_id
        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def secret_id(self):
        """Gets the secret_id of this UpdateSecretRequest.

        凭据ID。

        :return: The secret_id of this UpdateSecretRequest.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this UpdateSecretRequest.

        凭据ID。

        :param secret_id: The secret_id of this UpdateSecretRequest.
        :type secret_id: str
        """
        self._secret_id = secret_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this UpdateSecretRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :return: The x_enterprise_project_id of this UpdateSecretRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this UpdateSecretRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :param x_enterprise_project_id: The x_enterprise_project_id of this UpdateSecretRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def body(self):
        """Gets the body of this UpdateSecretRequest.

        :return: The body of this UpdateSecretRequest.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateOrUpdateSecretReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSecretRequest.

        :param body: The body of this UpdateSecretRequest.
        :type body: :class:`huaweicloudsdkcae.v1.CreateOrUpdateSecretReq`
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
        if not isinstance(other, UpdateSecretRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
