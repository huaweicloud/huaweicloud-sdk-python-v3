# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicipOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'ip_version': 'int',
        'alias': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'ip_version': 'ip_version',
        'alias': 'alias'
    }

    def __init__(self, port_id=None, ip_version=None, alias=None):
        """UpdatePublicipOption

        The model defined in huaweicloud sdk

        :param port_id: 功能说明：端口id  约束：必须是存在的端口id，如果不带该参数或者值为空时为解除绑定弹性公网IP，如果该端口不存在或端口已绑定弹性公网IP则会提示出错。  和ip_version字段互斥，不能同时更新。
        :type port_id: str
        :param ip_version: 功能说明：IP版本信息  取值范围：4和6  4：IPv4  6：IPv6  约束：必须是系统支持的IP版本类型，和port_id互斥，不能同时更新。
        :type ip_version: int
        :param alias: 功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type alias: str
        """
        
        

        self._port_id = None
        self._ip_version = None
        self._alias = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if ip_version is not None:
            self.ip_version = ip_version
        if alias is not None:
            self.alias = alias

    @property
    def port_id(self):
        """Gets the port_id of this UpdatePublicipOption.

        功能说明：端口id  约束：必须是存在的端口id，如果不带该参数或者值为空时为解除绑定弹性公网IP，如果该端口不存在或端口已绑定弹性公网IP则会提示出错。  和ip_version字段互斥，不能同时更新。

        :return: The port_id of this UpdatePublicipOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this UpdatePublicipOption.

        功能说明：端口id  约束：必须是存在的端口id，如果不带该参数或者值为空时为解除绑定弹性公网IP，如果该端口不存在或端口已绑定弹性公网IP则会提示出错。  和ip_version字段互斥，不能同时更新。

        :param port_id: The port_id of this UpdatePublicipOption.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def ip_version(self):
        """Gets the ip_version of this UpdatePublicipOption.

        功能说明：IP版本信息  取值范围：4和6  4：IPv4  6：IPv6  约束：必须是系统支持的IP版本类型，和port_id互斥，不能同时更新。

        :return: The ip_version of this UpdatePublicipOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this UpdatePublicipOption.

        功能说明：IP版本信息  取值范围：4和6  4：IPv4  6：IPv6  约束：必须是系统支持的IP版本类型，和port_id互斥，不能同时更新。

        :param ip_version: The ip_version of this UpdatePublicipOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def alias(self):
        """Gets the alias of this UpdatePublicipOption.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The alias of this UpdatePublicipOption.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UpdatePublicipOption.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param alias: The alias of this UpdatePublicipOption.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, UpdatePublicipOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
