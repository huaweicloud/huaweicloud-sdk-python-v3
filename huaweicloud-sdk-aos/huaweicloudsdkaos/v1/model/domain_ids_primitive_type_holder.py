# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainIdsPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_ids': 'list[str]'
    }

    attribute_map = {
        'domain_ids': 'domain_ids'
    }

    def __init__(self, domain_ids=None):
        r"""DomainIdsPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param domain_ids: 当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。
        :type domain_ids: list[str]
        """
        
        

        self._domain_ids = None
        self.discriminator = None

        if domain_ids is not None:
            self.domain_ids = domain_ids

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this DomainIdsPrimitiveTypeHolder.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。

        :return: The domain_ids of this DomainIdsPrimitiveTypeHolder.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this DomainIdsPrimitiveTypeHolder.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。

        :param domain_ids: The domain_ids of this DomainIdsPrimitiveTypeHolder.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

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
        if not isinstance(other, DomainIdsPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
