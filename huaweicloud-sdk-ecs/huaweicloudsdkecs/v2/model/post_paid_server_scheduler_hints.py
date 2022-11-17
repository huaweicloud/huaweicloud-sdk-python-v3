# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerSchedulerHints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group': 'str',
        'dedicated_host_id': 'str',
        'tenancy': 'str'
    }

    attribute_map = {
        'group': 'group',
        'dedicated_host_id': 'dedicated_host_id',
        'tenancy': 'tenancy'
    }

    def __init__(self, group=None, dedicated_host_id=None, tenancy=None):
        """PostPaidServerSchedulerHints

        The model defined in huaweicloud sdk

        :param group: 云服务器组ID，UUID格式。  云服务器组的ID可以从控制台或者参考[查询云服务器组列表](https://support.huaweicloud.com/api-ecs/ecs_03_1402.html)获取。
        :type group: str
        :param dedicated_host_id: 专属主机的ID。专属主机的ID仅在tenancy为dedicated时生效。
        :type dedicated_host_id: str
        :param tenancy: 在指定的专属主机或者共享主机上创建弹性云服务器云主机。参数值为shared或者dedicated。
        :type tenancy: str
        """
        
        

        self._group = None
        self._dedicated_host_id = None
        self._tenancy = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if tenancy is not None:
            self.tenancy = tenancy

    @property
    def group(self):
        """Gets the group of this PostPaidServerSchedulerHints.

        云服务器组ID，UUID格式。  云服务器组的ID可以从控制台或者参考[查询云服务器组列表](https://support.huaweicloud.com/api-ecs/ecs_03_1402.html)获取。

        :return: The group of this PostPaidServerSchedulerHints.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PostPaidServerSchedulerHints.

        云服务器组ID，UUID格式。  云服务器组的ID可以从控制台或者参考[查询云服务器组列表](https://support.huaweicloud.com/api-ecs/ecs_03_1402.html)获取。

        :param group: The group of this PostPaidServerSchedulerHints.
        :type group: str
        """
        self._group = group

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this PostPaidServerSchedulerHints.

        专属主机的ID。专属主机的ID仅在tenancy为dedicated时生效。

        :return: The dedicated_host_id of this PostPaidServerSchedulerHints.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this PostPaidServerSchedulerHints.

        专属主机的ID。专属主机的ID仅在tenancy为dedicated时生效。

        :param dedicated_host_id: The dedicated_host_id of this PostPaidServerSchedulerHints.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def tenancy(self):
        """Gets the tenancy of this PostPaidServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器云主机。参数值为shared或者dedicated。

        :return: The tenancy of this PostPaidServerSchedulerHints.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this PostPaidServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器云主机。参数值为shared或者dedicated。

        :param tenancy: The tenancy of this PostPaidServerSchedulerHints.
        :type tenancy: str
        """
        self._tenancy = tenancy

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
        if not isinstance(other, PostPaidServerSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
