# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentTargets:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'regions': 'list[str]',
        'domain_ids': 'list[str]',
        'domain_ids_uri': 'str'
    }

    attribute_map = {
        'regions': 'regions',
        'domain_ids': 'domain_ids',
        'domain_ids_uri': 'domain_ids_uri'
    }

    def __init__(self, regions=None, domain_ids=None, domain_ids_uri=None):
        """DeploymentTargets

        The model defined in huaweicloud sdk

        :param regions: 用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*
        :type regions: list[str]
        :param domain_ids: 权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri 有且仅有一个存在。
        :type domain_ids: list[str]
        :param domain_ids_uri: 权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分割，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri有且仅有一个存在。
        :type domain_ids_uri: str
        """
        
        

        self._regions = None
        self._domain_ids = None
        self._domain_ids_uri = None
        self.discriminator = None

        self.regions = regions
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if domain_ids_uri is not None:
            self.domain_ids_uri = domain_ids_uri

    @property
    def regions(self):
        """Gets the regions of this DeploymentTargets.

        用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*

        :return: The regions of this DeploymentTargets.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this DeploymentTargets.

        用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*

        :param regions: The regions of this DeploymentTargets.
        :type regions: list[str]
        """
        self._regions = regions

    @property
    def domain_ids(self):
        """Gets the domain_ids of this DeploymentTargets.

        权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri 有且仅有一个存在。

        :return: The domain_ids of this DeploymentTargets.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        """Sets the domain_ids of this DeploymentTargets.

        权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri 有且仅有一个存在。

        :param domain_ids: The domain_ids of this DeploymentTargets.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def domain_ids_uri(self):
        """Gets the domain_ids_uri of this DeploymentTargets.

        权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分割，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri有且仅有一个存在。

        :return: The domain_ids_uri of this DeploymentTargets.
        :rtype: str
        """
        return self._domain_ids_uri

    @domain_ids_uri.setter
    def domain_ids_uri(self, domain_ids_uri):
        """Sets the domain_ids_uri of this DeploymentTargets.

        权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分割，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  domain_ids和domain_ids_uri有且仅有一个存在。

        :param domain_ids_uri: The domain_ids_uri of this DeploymentTargets.
        :type domain_ids_uri: str
        """
        self._domain_ids_uri = domain_ids_uri

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
        if not isinstance(other, DeploymentTargets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
