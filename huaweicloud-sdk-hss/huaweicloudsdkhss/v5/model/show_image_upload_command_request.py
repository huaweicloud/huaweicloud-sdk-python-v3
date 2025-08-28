# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageUploadCommandRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'registry_addr': 'str',
        'namespace': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'registry_addr': 'registry_addr',
        'namespace': 'namespace',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, registry_addr=None, namespace=None, username=None, password=None):
        r"""ShowImageUploadCommandRequest

        The model defined in huaweicloud sdk

        :param registry_addr: **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type registry_addr: str
        :param namespace: **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type namespace: str
        :param username: **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type username: str
        :param password: **参数解释**： 用于登录镜像仓的密码。仅用于生成命令，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type password: str
        """
        
        

        self._registry_addr = None
        self._namespace = None
        self._username = None
        self._password = None
        self.discriminator = None

        self.registry_addr = registry_addr
        self.namespace = namespace
        self.username = username
        self.password = password

    @property
    def registry_addr(self):
        r"""Gets the registry_addr of this ShowImageUploadCommandRequest.

        **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The registry_addr of this ShowImageUploadCommandRequest.
        :rtype: str
        """
        return self._registry_addr

    @registry_addr.setter
    def registry_addr(self, registry_addr):
        r"""Sets the registry_addr of this ShowImageUploadCommandRequest.

        **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param registry_addr: The registry_addr of this ShowImageUploadCommandRequest.
        :type registry_addr: str
        """
        self._registry_addr = registry_addr

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowImageUploadCommandRequest.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The namespace of this ShowImageUploadCommandRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowImageUploadCommandRequest.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param namespace: The namespace of this ShowImageUploadCommandRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def username(self):
        r"""Gets the username of this ShowImageUploadCommandRequest.

        **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The username of this ShowImageUploadCommandRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ShowImageUploadCommandRequest.

        **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param username: The username of this ShowImageUploadCommandRequest.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this ShowImageUploadCommandRequest.

        **参数解释**： 用于登录镜像仓的密码。仅用于生成命令，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The password of this ShowImageUploadCommandRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ShowImageUploadCommandRequest.

        **参数解释**： 用于登录镜像仓的密码。仅用于生成命令，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param password: The password of this ShowImageUploadCommandRequest.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, ShowImageUploadCommandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
