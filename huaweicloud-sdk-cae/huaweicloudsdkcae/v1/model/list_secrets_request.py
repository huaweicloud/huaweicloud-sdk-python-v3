# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID'
    }

    def __init__(self, x_enterprise_project_id=None):
        r"""ListSecretsRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。
        :type x_enterprise_project_id: str
        """
        
        

        self._x_enterprise_project_id = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this ListSecretsRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :return: The x_enterprise_project_id of this ListSecretsRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this ListSecretsRequest.

        企业项目ID。  - 创建环境时，环境会绑定企业项目ID。      - 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。     - 该字段不传（或传为字符串“0”）时，则查询默认企业项目下的资源。  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。

        :param x_enterprise_project_id: The x_enterprise_project_id of this ListSecretsRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

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
        if not isinstance(other, ListSecretsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
