# coding: utf-8

import pprint
import re

import six





class MetaDataInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'op_svc_userid': 'str',
        'admin_pass': 'str',
        'byol': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'op_svc_userid': 'op_svc_userid',
        'admin_pass': 'admin_pass',
        'byol': 'BYOL',
        'agency_name': 'agency_name'
    }

    def __init__(self, op_svc_userid=None, admin_pass=None, byol=None, agency_name=None):
        """MetaDataInfo - a model defined in huaweicloud sdk"""
        
        

        self._op_svc_userid = None
        self._admin_pass = None
        self._byol = None
        self._agency_name = None
        self.discriminator = None

        self.op_svc_userid = op_svc_userid
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if byol is not None:
            self.byol = byol
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def op_svc_userid(self):
        """Gets the op_svc_userid of this MetaDataInfo.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）。

        :return: The op_svc_userid of this MetaDataInfo.
        :rtype: str
        """
        return self._op_svc_userid

    @op_svc_userid.setter
    def op_svc_userid(self, op_svc_userid):
        """Sets the op_svc_userid of this MetaDataInfo.

        用户ID（登录管理控制台，进入我的凭证，即可看到“用户ID”）。

        :param op_svc_userid: The op_svc_userid of this MetaDataInfo.
        :type: str
        """
        self._op_svc_userid = op_svc_userid

    @property
    def admin_pass(self):
        """Gets the admin_pass of this MetaDataInfo.

        以Windows镜像创建的裸金属服务器Administrator用户的密码，示例：cloud.1234。密码复杂度要求：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :return: The admin_pass of this MetaDataInfo.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this MetaDataInfo.

        以Windows镜像创建的裸金属服务器Administrator用户的密码，示例：cloud.1234。密码复杂度要求：长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。

        :param admin_pass: The admin_pass of this MetaDataInfo.
        :type: str
        """
        self._admin_pass = admin_pass

    @property
    def byol(self):
        """Gets the byol of this MetaDataInfo.

        否自带许可，取值“true”或“false”。

        :return: The byol of this MetaDataInfo.
        :rtype: str
        """
        return self._byol

    @byol.setter
    def byol(self, byol):
        """Sets the byol of this MetaDataInfo.

        否自带许可，取值“true”或“false”。

        :param byol: The byol of this MetaDataInfo.
        :type: str
        """
        self._byol = byol

    @property
    def agency_name(self):
        """Gets the agency_name of this MetaDataInfo.

        委托的名称。委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以作为其他租户访问此裸金属服务器的临时凭证。 说明:委托获取、更新请参考如下步骤：使用IAM服务提供的查询委托列表，获取有效可用的委托名称。使用更新裸金属服务器元数据接口，更新metadata中agency_name字段为新的委托名称。

        :return: The agency_name of this MetaDataInfo.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this MetaDataInfo.

        委托的名称。委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以作为其他租户访问此裸金属服务器的临时凭证。 说明:委托获取、更新请参考如下步骤：使用IAM服务提供的查询委托列表，获取有效可用的委托名称。使用更新裸金属服务器元数据接口，更新metadata中agency_name字段为新的委托名称。

        :param agency_name: The agency_name of this MetaDataInfo.
        :type: str
        """
        self._agency_name = agency_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetaDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
