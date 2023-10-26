# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagedAgencyNamePrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_agency_name': 'str'
    }

    attribute_map = {
        'managed_agency_name': 'managed_agency_name'
    }

    def __init__(self, managed_agency_name=None):
        """ManagedAgencyNamePrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param managed_agency_name: 被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type managed_agency_name: str
        """
        
        

        self._managed_agency_name = None
        self.discriminator = None

        if managed_agency_name is not None:
            self.managed_agency_name = managed_agency_name

    @property
    def managed_agency_name(self):
        """Gets the managed_agency_name of this ManagedAgencyNamePrimitiveTypeHolder.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The managed_agency_name of this ManagedAgencyNamePrimitiveTypeHolder.
        :rtype: str
        """
        return self._managed_agency_name

    @managed_agency_name.setter
    def managed_agency_name(self, managed_agency_name):
        """Sets the managed_agency_name of this ManagedAgencyNamePrimitiveTypeHolder.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :param managed_agency_name: The managed_agency_name of this ManagedAgencyNamePrimitiveTypeHolder.
        :type managed_agency_name: str
        """
        self._managed_agency_name = managed_agency_name

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
        if not isinstance(other, ManagedAgencyNamePrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
