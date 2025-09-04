# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyStarRocksSecurityGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str'
    }

    attribute_map = {
        'security_group_id': 'security_group_id'
    }

    def __init__(self, security_group_id=None):
        r"""ModifyStarRocksSecurityGroupReq

        The model defined in huaweicloud sdk

        :param security_group_id: 安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。获取方法如下：  方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。  方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。
        :type security_group_id: str
        """
        
        

        self._security_group_id = None
        self.discriminator = None

        self.security_group_id = security_group_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ModifyStarRocksSecurityGroupReq.

        安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。获取方法如下：  方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。  方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。

        :return: The security_group_id of this ModifyStarRocksSecurityGroupReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ModifyStarRocksSecurityGroupReq.

        安全组ID。如果实例所选用的子网开启网络ACL进行访问控制，则该参数非必选。如果未开启ACL进行访问控制，则该参数必选。获取方法如下：  方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。  方法2：通过虚拟私有云服务的API接口查询，具体操作可参考查询安全组列表。

        :param security_group_id: The security_group_id of this ModifyStarRocksSecurityGroupReq.
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
        if not isinstance(other, ModifyStarRocksSecurityGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
