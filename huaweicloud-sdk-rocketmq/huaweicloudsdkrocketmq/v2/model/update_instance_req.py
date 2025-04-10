# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceReq:

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
        'security_group_id': 'str',
        'enable_acl': 'bool',
        'enable_publicip': 'bool',
        'publicip_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'security_group_id': 'security_group_id',
        'enable_acl': 'enable_acl',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id'
    }

    def __init__(self, name=None, description=None, security_group_id=None, enable_acl=None, enable_publicip=None, publicip_id=None):
        r"""UpdateInstanceReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。
        :type name: str
        :param description: 实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\&quot;&gt;\&quot;与\&quot;&lt;\&quot;，字符串首字符不能为\&quot;&#x3D;\&quot;,\&quot;+\&quot;,\&quot;-\&quot;,\&quot;@\&quot;的全角和半角字符。](tag:hcs)  &gt; \\与\&quot;在json报文中属于特殊字符，如果参数值中需要显示\\或者\&quot;字符，请在字符前增加转义字符\\，比如\\\\或者\\\&quot;。
        :type description: str
        :param security_group_id: 安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。
        :type security_group_id: str
        :param enable_acl: ACL访问控制。
        :type enable_acl: bool
        :param enable_publicip: 是否开启公网。
        :type enable_publicip: bool
        :param publicip_id: 实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。
        :type publicip_id: str
        """
        
        

        self._name = None
        self._description = None
        self._security_group_id = None
        self._enable_acl = None
        self._enable_publicip = None
        self._publicip_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if enable_acl is not None:
            self.enable_acl = enable_acl
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id

    @property
    def name(self):
        r"""Gets the name of this UpdateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :return: The name of this UpdateInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInstanceReq.

        实例名称。  由英文字符开头，只能由英文字母、数字、中划线组成，长度为4~64的字符。

        :param name: The name of this UpdateInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs)  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :return: The description of this UpdateInstanceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInstanceReq.

        实例的描述信息。  长度不超过1024的字符串。[且字符串不能包含\">\"与\"<\"，字符串首字符不能为\"=\",\"+\",\"-\",\"@\"的全角和半角字符。](tag:hcs)  > \\与\"在json报文中属于特殊字符，如果参数值中需要显示\\或者\"字符，请在字符前增加转义字符\\，比如\\\\或者\\\"。

        :param description: The description of this UpdateInstanceReq.
        :type description: str
        """
        self._description = description

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this UpdateInstanceReq.

        安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :return: The security_group_id of this UpdateInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this UpdateInstanceReq.

        安全组ID。  获取方法如下：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。

        :param security_group_id: The security_group_id of this UpdateInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def enable_acl(self):
        r"""Gets the enable_acl of this UpdateInstanceReq.

        ACL访问控制。

        :return: The enable_acl of this UpdateInstanceReq.
        :rtype: bool
        """
        return self._enable_acl

    @enable_acl.setter
    def enable_acl(self, enable_acl):
        r"""Sets the enable_acl of this UpdateInstanceReq.

        ACL访问控制。

        :param enable_acl: The enable_acl of this UpdateInstanceReq.
        :type enable_acl: bool
        """
        self._enable_acl = enable_acl

    @property
    def enable_publicip(self):
        r"""Gets the enable_publicip of this UpdateInstanceReq.

        是否开启公网。

        :return: The enable_publicip of this UpdateInstanceReq.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        r"""Sets the enable_publicip of this UpdateInstanceReq.

        是否开启公网。

        :param enable_publicip: The enable_publicip of this UpdateInstanceReq.
        :type enable_publicip: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this UpdateInstanceReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :return: The publicip_id of this UpdateInstanceReq.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this UpdateInstanceReq.

        实例绑定的弹性IP地址的ID。  以英文逗号隔开多个弹性IP地址的ID。  如果开启了公网访问功能（即enable_publicip为true），该字段为必选。

        :param publicip_id: The publicip_id of this UpdateInstanceReq.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

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
        if not isinstance(other, UpdateInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
