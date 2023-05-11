# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobNodeVpcInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'custom_node_ip': 'str',
        'security_group_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'custom_node_ip': 'custom_node_ip',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, vpc_id=None, subnet_id=None, custom_node_ip=None, security_group_id=None):
        """JobNodeVpcInfo

        The model defined in huaweicloud sdk

        :param vpc_id: 任务实例所在虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 任务实例所在子网ID。
        :type subnet_id: str
        :param custom_node_ip: 指定创建任务实例IP地址，多个IP端口之间请用“,”英文逗号分隔，目前仅支持设置IPv4地址，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP 。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询私有IP列表，选择“device_owner”为空的私有IP。 示例： \&quot;192.168.0.10,192.168.0.11\&quot;
        :type custom_node_ip: str
        :param security_group_id: 任务实例所在的安全组ID。
        :type security_group_id: str
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._custom_node_ip = None
        self._security_group_id = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if custom_node_ip is not None:
            self.custom_node_ip = custom_node_ip
        if security_group_id is not None:
            self.security_group_id = security_group_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this JobNodeVpcInfo.

        任务实例所在虚拟私有云ID。

        :return: The vpc_id of this JobNodeVpcInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this JobNodeVpcInfo.

        任务实例所在虚拟私有云ID。

        :param vpc_id: The vpc_id of this JobNodeVpcInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this JobNodeVpcInfo.

        任务实例所在子网ID。

        :return: The subnet_id of this JobNodeVpcInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this JobNodeVpcInfo.

        任务实例所在子网ID。

        :param subnet_id: The subnet_id of this JobNodeVpcInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def custom_node_ip(self):
        """Gets the custom_node_ip of this JobNodeVpcInfo.

        指定创建任务实例IP地址，多个IP端口之间请用“,”英文逗号分隔，目前仅支持设置IPv4地址，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP 。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询私有IP列表，选择“device_owner”为空的私有IP。 示例： \"192.168.0.10,192.168.0.11\"

        :return: The custom_node_ip of this JobNodeVpcInfo.
        :rtype: str
        """
        return self._custom_node_ip

    @custom_node_ip.setter
    def custom_node_ip(self, custom_node_ip):
        """Sets the custom_node_ip of this JobNodeVpcInfo.

        指定创建任务实例IP地址，多个IP端口之间请用“,”英文逗号分隔，目前仅支持设置IPv4地址，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找子网的网段，选择未被占用的IP 。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询私有IP列表，选择“device_owner”为空的私有IP。 示例： \"192.168.0.10,192.168.0.11\"

        :param custom_node_ip: The custom_node_ip of this JobNodeVpcInfo.
        :type custom_node_ip: str
        """
        self._custom_node_ip = custom_node_ip

    @property
    def security_group_id(self):
        """Gets the security_group_id of this JobNodeVpcInfo.

        任务实例所在的安全组ID。

        :return: The security_group_id of this JobNodeVpcInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this JobNodeVpcInfo.

        任务实例所在的安全组ID。

        :param security_group_id: The security_group_id of this JobNodeVpcInfo.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, JobNodeVpcInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
