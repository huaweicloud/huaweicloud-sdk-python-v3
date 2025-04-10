# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInformationSpecHostNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group': 'str'
    }

    attribute_map = {
        'security_group': 'SecurityGroup'
    }

    def __init__(self, security_group=None):
        r"""ClusterInformationSpecHostNetwork

        The model defined in huaweicloud sdk

        :param security_group: 集群默认Node节点安全组需要放通部分端口来保证正常通信，[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 修改后的安全组只作用于新创建的节点和新纳管的节点，存量节点的安全组需手动修改。 
        :type security_group: str
        """
        
        

        self._security_group = None
        self.discriminator = None

        if security_group is not None:
            self.security_group = security_group

    @property
    def security_group(self):
        r"""Gets the security_group of this ClusterInformationSpecHostNetwork.

        集群默认Node节点安全组需要放通部分端口来保证正常通信，[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 修改后的安全组只作用于新创建的节点和新纳管的节点，存量节点的安全组需手动修改。 

        :return: The security_group of this ClusterInformationSpecHostNetwork.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this ClusterInformationSpecHostNetwork.

        集群默认Node节点安全组需要放通部分端口来保证正常通信，[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/cce_faq/cce_faq_00265.html)。](tag:hws)[详细设置请参考[集群安全组规则配置](https://support.huaweicloud.com/intl/zh-cn/cce_faq/cce_faq_00265.html)。](tag:hws_hk) 修改后的安全组只作用于新创建的节点和新纳管的节点，存量节点的安全组需手动修改。 

        :param security_group: The security_group of this ClusterInformationSpecHostNetwork.
        :type security_group: str
        """
        self._security_group = security_group

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
        if not isinstance(other, ClusterInformationSpecHostNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
