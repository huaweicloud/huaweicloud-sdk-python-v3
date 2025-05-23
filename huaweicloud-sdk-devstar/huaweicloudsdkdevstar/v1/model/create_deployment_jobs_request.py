# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeploymentJobsRequest:

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
        'application_id': 'str',
        'environment_tag': 'str',
        'body': 'CreateDeploymentJobsParams'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'application_id': 'application_id',
        'environment_tag': 'environment_tag',
        'body': 'body'
    }

    def __init__(self, x_language=None, application_id=None, environment_tag=None, body=None):
        r"""CreateDeploymentJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param application_id: 应用id
        :type application_id: str
        :param environment_tag: 环境标识，从 [应用详情接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;DevStar&amp;api&#x3D;ShowApplication) 返回报文中的环境信息获取。
        :type environment_tag: str
        :param body: Body of the CreateDeploymentJobsRequest
        :type body: :class:`huaweicloudsdkdevstar.v1.CreateDeploymentJobsParams`
        """
        
        

        self._x_language = None
        self._application_id = None
        self._environment_tag = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.application_id = application_id
        self.environment_tag = environment_tag
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateDeploymentJobsRequest.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this CreateDeploymentJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateDeploymentJobsRequest.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this CreateDeploymentJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def application_id(self):
        r"""Gets the application_id of this CreateDeploymentJobsRequest.

        应用id

        :return: The application_id of this CreateDeploymentJobsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CreateDeploymentJobsRequest.

        应用id

        :param application_id: The application_id of this CreateDeploymentJobsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def environment_tag(self):
        r"""Gets the environment_tag of this CreateDeploymentJobsRequest.

        环境标识，从 [应用详情接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=DevStar&api=ShowApplication) 返回报文中的环境信息获取。

        :return: The environment_tag of this CreateDeploymentJobsRequest.
        :rtype: str
        """
        return self._environment_tag

    @environment_tag.setter
    def environment_tag(self, environment_tag):
        r"""Sets the environment_tag of this CreateDeploymentJobsRequest.

        环境标识，从 [应用详情接口](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=DevStar&api=ShowApplication) 返回报文中的环境信息获取。

        :param environment_tag: The environment_tag of this CreateDeploymentJobsRequest.
        :type environment_tag: str
        """
        self._environment_tag = environment_tag

    @property
    def body(self):
        r"""Gets the body of this CreateDeploymentJobsRequest.

        :return: The body of this CreateDeploymentJobsRequest.
        :rtype: :class:`huaweicloudsdkdevstar.v1.CreateDeploymentJobsParams`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateDeploymentJobsRequest.

        :param body: The body of this CreateDeploymentJobsRequest.
        :type body: :class:`huaweicloudsdkdevstar.v1.CreateDeploymentJobsParams`
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
        if not isinstance(other, CreateDeploymentJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
