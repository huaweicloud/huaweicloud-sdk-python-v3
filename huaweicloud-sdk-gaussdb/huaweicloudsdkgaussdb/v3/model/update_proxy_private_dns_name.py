# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProxyPrivateDnsName:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_dns_name': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'new_dns_name': 'new_dns_name',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, new_dns_name=None, vpc_id=None):
        r"""UpdateProxyPrivateDnsName

        The model defined in huaweicloud sdk

        :param new_dns_name: **参数解释**：  新的dns名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type new_dns_name: str
        :param vpc_id: **参数解释**：            虚拟私有云ID，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type vpc_id: str
        """
        
        

        self._new_dns_name = None
        self._vpc_id = None
        self.discriminator = None

        self.new_dns_name = new_dns_name
        self.vpc_id = vpc_id

    @property
    def new_dns_name(self):
        r"""Gets the new_dns_name of this UpdateProxyPrivateDnsName.

        **参数解释**：  新的dns名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The new_dns_name of this UpdateProxyPrivateDnsName.
        :rtype: str
        """
        return self._new_dns_name

    @new_dns_name.setter
    def new_dns_name(self, new_dns_name):
        r"""Sets the new_dns_name of this UpdateProxyPrivateDnsName.

        **参数解释**：  新的dns名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param new_dns_name: The new_dns_name of this UpdateProxyPrivateDnsName.
        :type new_dns_name: str
        """
        self._new_dns_name = new_dns_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateProxyPrivateDnsName.

        **参数解释**：            虚拟私有云ID，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The vpc_id of this UpdateProxyPrivateDnsName.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateProxyPrivateDnsName.

        **参数解释**：            虚拟私有云ID，获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html)。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param vpc_id: The vpc_id of this UpdateProxyPrivateDnsName.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, UpdateProxyPrivateDnsName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
