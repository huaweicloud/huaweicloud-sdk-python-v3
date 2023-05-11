# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityGroupOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'vpc_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, vpc_id=None, enterprise_project_id=None):
        """CreateSecurityGroupOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param vpc_id: 功能说明：安全组所在的vpc的资源标识
        :type vpc_id: str
        :param enterprise_project_id: 功能说明：企业项目ID。创建安全组时，给安全组绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 默认值：“0”
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateSecurityGroupOption.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecurityGroupOption.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateSecurityGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateSecurityGroupOption.

        功能说明：安全组所在的vpc的资源标识

        :return: The vpc_id of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateSecurityGroupOption.

        功能说明：安全组所在的vpc的资源标识

        :param vpc_id: The vpc_id of this CreateSecurityGroupOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSecurityGroupOption.

        功能说明：企业项目ID。创建安全组时，给安全组绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 默认值：“0”

        :return: The enterprise_project_id of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSecurityGroupOption.

        功能说明：企业项目ID。创建安全组时，给安全组绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 默认值：“0”

        :param enterprise_project_id: The enterprise_project_id of this CreateSecurityGroupOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateSecurityGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
