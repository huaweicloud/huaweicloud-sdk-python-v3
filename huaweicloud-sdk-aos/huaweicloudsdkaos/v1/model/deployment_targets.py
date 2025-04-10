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
        'domain_ids_uri': 'str',
        'organizational_unit_ids': 'list[str]',
        'domain_id_filter_type': 'str'
    }

    attribute_map = {
        'regions': 'regions',
        'domain_ids': 'domain_ids',
        'domain_ids_uri': 'domain_ids_uri',
        'organizational_unit_ids': 'organizational_unit_ids',
        'domain_id_filter_type': 'domain_id_filter_type'
    }

    def __init__(self, regions=None, domain_ids=None, domain_ids_uri=None, organizational_unit_ids=None, domain_id_filter_type=None):
        r"""DeploymentTargets

        The model defined in huaweicloud sdk

        :param regions: 用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*
        :type regions: list[str]
        :param domain_ids: 当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。
        :type domain_ids: list[str]
        :param domain_ids_uri: 当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分隔，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。链接文件内容用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri有且仅有一个存在。
        :type domain_ids_uri: str
        :param organizational_unit_ids: 组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*
        :type organizational_unit_ids: list[str]
        :param domain_id_filter_type: 租户ID筛选类型，仅支持资源栈集权限模型是SERVICE_MANAGED时指定该参数。默认为NONE  用户可以指定不同的筛选类型，通过domain_ids或domain_ids_uri 指定或排除部署的用户信息，以增加或限制部署目标用户范围，实现不同的部署策略。     * &#x60;INTERSECTION&#x60; - 从所提供的 OUs 中选择指定用户进行部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * &#x60;DIFFERENCE&#x60; - 从所提供的 OUs 中排除指定用户部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * &#x60;UNION&#x60; - 除了部署到提供的 OUs 外，还将部署到指定的账号中。用户可以通过同时指定organizational_unit_ids 和 domain_ids/domain_ids_uri 以实现在同一请求中部署整个OU和来自不同OU的特定个人账号。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。创建资源栈实例（CreateStackInstances）除外，该API 不允许指定使用该类型。    * &#x60;NONE&#x60; - 只部署在指定 OUs 中的所有账号。该类型下domain_ids和domain_ids_uri字段必须为空。
        :type domain_id_filter_type: str
        """
        
        

        self._regions = None
        self._domain_ids = None
        self._domain_ids_uri = None
        self._organizational_unit_ids = None
        self._domain_id_filter_type = None
        self.discriminator = None

        self.regions = regions
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if domain_ids_uri is not None:
            self.domain_ids_uri = domain_ids_uri
        if organizational_unit_ids is not None:
            self.organizational_unit_ids = organizational_unit_ids
        if domain_id_filter_type is not None:
            self.domain_id_filter_type = domain_id_filter_type

    @property
    def regions(self):
        r"""Gets the regions of this DeploymentTargets.

        用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*

        :return: The regions of this DeploymentTargets.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this DeploymentTargets.

        用户指定资源栈集操作所涉及的区域。  *在DeployStackSet API中，根据用户输入regions和domain_ids列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的region，则会报错。*

        :param regions: The regions of this DeploymentTargets.
        :type regions: list[str]
        """
        self._regions = regions

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this DeploymentTargets.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。

        :return: The domain_ids of this DeploymentTargets.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this DeploymentTargets.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids列表和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果指定了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri 有且仅有一个存在。

        :param domain_ids: The domain_ids of this DeploymentTargets.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def domain_ids_uri(self):
        r"""Gets the domain_ids_uri of this DeploymentTargets.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分隔，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。链接文件内容用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri有且仅有一个存在。

        :return: The domain_ids_uri of this DeploymentTargets.
        :rtype: str
        """
        return self._domain_ids_uri

    @domain_ids_uri.setter
    def domain_ids_uri(self, domain_ids_uri):
        r"""Sets the domain_ids_uri of this DeploymentTargets.

        当资源栈集权限模型是SELF_MANAGED时，用户指定包含本次操作涉及到的租户ID内容文件的OBS地址。  内容格式要求每个租户ID以逗号（,）分隔，支持换行。当前仅支持csv文件，且文件的编码格式须为UTF-8。文件内容大小不超过100KB。  上传的csv文件应尽量避免Excel操作，以防出现读取内容不一致的问题。推荐使用记事本打开确认内容是否符合预期。  *在DeployStackSet API中，如果指定该参数，根据用户输入的domain_ids_uri文件内容和regions列表，以笛卡尔积的形式选择资源栈集中存在的资源栈实例进行部署。如果内容包含了没有被资源栈集所管理的domain_id，则会报错。*  当资源栈集权限模型是SERVICE_MANAGED时，该参数需结合domain_id_filter_type使用。链接文件内容用于指定资源栈集操作涉及到的，从所提供的OU中指定或排除部署的租户ID信息，或除提供的OU外，还进行额外部署的租户ID信息。  domain_ids和domain_ids_uri有且仅有一个存在。

        :param domain_ids_uri: The domain_ids_uri of this DeploymentTargets.
        :type domain_ids_uri: str
        """
        self._domain_ids_uri = domain_ids_uri

    @property
    def organizational_unit_ids(self):
        r"""Gets the organizational_unit_ids of this DeploymentTargets.

        组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*

        :return: The organizational_unit_ids of this DeploymentTargets.
        :rtype: list[str]
        """
        return self._organizational_unit_ids

    @organizational_unit_ids.setter
    def organizational_unit_ids(self, organizational_unit_ids):
        r"""Sets the organizational_unit_ids of this DeploymentTargets.

        组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*

        :param organizational_unit_ids: The organizational_unit_ids of this DeploymentTargets.
        :type organizational_unit_ids: list[str]
        """
        self._organizational_unit_ids = organizational_unit_ids

    @property
    def domain_id_filter_type(self):
        r"""Gets the domain_id_filter_type of this DeploymentTargets.

        租户ID筛选类型，仅支持资源栈集权限模型是SERVICE_MANAGED时指定该参数。默认为NONE  用户可以指定不同的筛选类型，通过domain_ids或domain_ids_uri 指定或排除部署的用户信息，以增加或限制部署目标用户范围，实现不同的部署策略。     * `INTERSECTION` - 从所提供的 OUs 中选择指定用户进行部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * `DIFFERENCE` - 从所提供的 OUs 中排除指定用户部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * `UNION` - 除了部署到提供的 OUs 外，还将部署到指定的账号中。用户可以通过同时指定organizational_unit_ids 和 domain_ids/domain_ids_uri 以实现在同一请求中部署整个OU和来自不同OU的特定个人账号。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。创建资源栈实例（CreateStackInstances）除外，该API 不允许指定使用该类型。    * `NONE` - 只部署在指定 OUs 中的所有账号。该类型下domain_ids和domain_ids_uri字段必须为空。

        :return: The domain_id_filter_type of this DeploymentTargets.
        :rtype: str
        """
        return self._domain_id_filter_type

    @domain_id_filter_type.setter
    def domain_id_filter_type(self, domain_id_filter_type):
        r"""Sets the domain_id_filter_type of this DeploymentTargets.

        租户ID筛选类型，仅支持资源栈集权限模型是SERVICE_MANAGED时指定该参数。默认为NONE  用户可以指定不同的筛选类型，通过domain_ids或domain_ids_uri 指定或排除部署的用户信息，以增加或限制部署目标用户范围，实现不同的部署策略。     * `INTERSECTION` - 从所提供的 OUs 中选择指定用户进行部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * `DIFFERENCE` - 从所提供的 OUs 中排除指定用户部署。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。    * `UNION` - 除了部署到提供的 OUs 外，还将部署到指定的账号中。用户可以通过同时指定organizational_unit_ids 和 domain_ids/domain_ids_uri 以实现在同一请求中部署整个OU和来自不同OU的特定个人账号。指定该类型时，domain_ids和domain_ids_uri 有且仅能有一个存在。创建资源栈实例（CreateStackInstances）除外，该API 不允许指定使用该类型。    * `NONE` - 只部署在指定 OUs 中的所有账号。该类型下domain_ids和domain_ids_uri字段必须为空。

        :param domain_id_filter_type: The domain_id_filter_type of this DeploymentTargets.
        :type domain_id_filter_type: str
        """
        self._domain_id_filter_type = domain_id_filter_type

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
