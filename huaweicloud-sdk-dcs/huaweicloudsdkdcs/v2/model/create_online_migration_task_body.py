# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOnlineMigrationTaskBody:

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
        'description': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, name=None, description=None, vpc_id=None, subnet_id=None, security_group_id=None):
        """CreateOnlineMigrationTaskBody

        The model defined in huaweicloud sdk

        :param name: 在线迁移任务名称。
        :type name: str
        :param description: 在线迁移任务描述。
        :type description: str
        :param vpc_id: 虚拟私有云ID。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 
        :type vpc_id: str
        :param subnet_id: 子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组。 安全组用来实现安全组内和组间虚拟机的访问控制，加强虚拟机的安全保护。您可以在安全组中定义各种访问规则，当虚拟机加入该安全组后，即受到这些访问规则的保护。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，访问控制安全组选项下可以对安全组进行创建和配置,并获取安全组ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0012.html)。 
        :type security_group_id: str
        """
        
        

        self._name = None
        self._description = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id

    @property
    def name(self):
        """Gets the name of this CreateOnlineMigrationTaskBody.

        在线迁移任务名称。

        :return: The name of this CreateOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOnlineMigrationTaskBody.

        在线迁移任务名称。

        :param name: The name of this CreateOnlineMigrationTaskBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateOnlineMigrationTaskBody.

        在线迁移任务描述。

        :return: The description of this CreateOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOnlineMigrationTaskBody.

        在线迁移任务描述。

        :param description: The description of this CreateOnlineMigrationTaskBody.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateOnlineMigrationTaskBody.

        虚拟私有云ID。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 

        :return: The vpc_id of this CreateOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateOnlineMigrationTaskBody.

        虚拟私有云ID。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 

        :param vpc_id: The vpc_id of this CreateOnlineMigrationTaskBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateOnlineMigrationTaskBody.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 

        :return: The subnet_id of this CreateOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateOnlineMigrationTaskBody.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 

        :param subnet_id: The subnet_id of this CreateOnlineMigrationTaskBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateOnlineMigrationTaskBody.

        指定实例所属的安全组。 安全组用来实现安全组内和组间虚拟机的访问控制，加强虚拟机的安全保护。您可以在安全组中定义各种访问规则，当虚拟机加入该安全组后，即受到这些访问规则的保护。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，访问控制安全组选项下可以对安全组进行创建和配置,并获取安全组ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0012.html)。 

        :return: The security_group_id of this CreateOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateOnlineMigrationTaskBody.

        指定实例所属的安全组。 安全组用来实现安全组内和组间虚拟机的访问控制，加强虚拟机的安全保护。您可以在安全组中定义各种访问规则，当虚拟机加入该安全组后，即受到这些访问规则的保护。   获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，访问控制安全组选项下可以对安全组进行创建和配置,并获取安全组ID。  - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询安全组列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0012.html)。 

        :param security_group_id: The security_group_id of this CreateOnlineMigrationTaskBody.
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
        if not isinstance(other, CreateOnlineMigrationTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
