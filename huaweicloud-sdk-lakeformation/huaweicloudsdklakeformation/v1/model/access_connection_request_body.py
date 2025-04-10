# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpcep_id': 'str',
        'vpcep_service_name': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'vpcep_id': 'vpcep_id',
        'vpcep_service_name': 'vpcep_service_name',
        'domain': 'domain'
    }

    def __init__(self, vpcep_id=None, vpcep_service_name=None, domain=None):
        r"""AccessConnectionRequestBody

        The model defined in huaweicloud sdk

        :param vpcep_id: 虚拟私有云终端节点ID。在 接入管理-创建客户端-前往VPC创建-VPC终端节点 创建和查看。
        :type vpcep_id: str
        :param vpcep_service_name: 终端节点服务名称。最大长度为64个字符。
        :type vpcep_service_name: str
        :param domain: 接入域名，通过IP接入访问Lakeformation API时，需在请求头中添加HOST参数并传入该域名。
        :type domain: str
        """
        
        

        self._vpcep_id = None
        self._vpcep_service_name = None
        self._domain = None
        self.discriminator = None

        if vpcep_id is not None:
            self.vpcep_id = vpcep_id
        if vpcep_service_name is not None:
            self.vpcep_service_name = vpcep_service_name
        if domain is not None:
            self.domain = domain

    @property
    def vpcep_id(self):
        r"""Gets the vpcep_id of this AccessConnectionRequestBody.

        虚拟私有云终端节点ID。在 接入管理-创建客户端-前往VPC创建-VPC终端节点 创建和查看。

        :return: The vpcep_id of this AccessConnectionRequestBody.
        :rtype: str
        """
        return self._vpcep_id

    @vpcep_id.setter
    def vpcep_id(self, vpcep_id):
        r"""Sets the vpcep_id of this AccessConnectionRequestBody.

        虚拟私有云终端节点ID。在 接入管理-创建客户端-前往VPC创建-VPC终端节点 创建和查看。

        :param vpcep_id: The vpcep_id of this AccessConnectionRequestBody.
        :type vpcep_id: str
        """
        self._vpcep_id = vpcep_id

    @property
    def vpcep_service_name(self):
        r"""Gets the vpcep_service_name of this AccessConnectionRequestBody.

        终端节点服务名称。最大长度为64个字符。

        :return: The vpcep_service_name of this AccessConnectionRequestBody.
        :rtype: str
        """
        return self._vpcep_service_name

    @vpcep_service_name.setter
    def vpcep_service_name(self, vpcep_service_name):
        r"""Sets the vpcep_service_name of this AccessConnectionRequestBody.

        终端节点服务名称。最大长度为64个字符。

        :param vpcep_service_name: The vpcep_service_name of this AccessConnectionRequestBody.
        :type vpcep_service_name: str
        """
        self._vpcep_service_name = vpcep_service_name

    @property
    def domain(self):
        r"""Gets the domain of this AccessConnectionRequestBody.

        接入域名，通过IP接入访问Lakeformation API时，需在请求头中添加HOST参数并传入该域名。

        :return: The domain of this AccessConnectionRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AccessConnectionRequestBody.

        接入域名，通过IP接入访问Lakeformation API时，需在请求头中添加HOST参数并传入该域名。

        :param domain: The domain of this AccessConnectionRequestBody.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, AccessConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
