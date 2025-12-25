# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterClusterSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_group_id': 'str',
        'category': 'str',
        'type': 'str',
        'provider': 'str',
        'country': 'str',
        'city': 'str',
        'region': 'str',
        'project_id': 'str',
        'manage_type': 'str'
    }

    attribute_map = {
        'cluster_group_id': 'clusterGroupID',
        'category': 'category',
        'type': 'type',
        'provider': 'provider',
        'country': 'country',
        'city': 'city',
        'region': 'region',
        'project_id': 'projectID',
        'manage_type': 'manageType'
    }

    def __init__(self, cluster_group_id=None, category=None, type=None, provider=None, country=None, city=None, region=None, project_id=None, manage_type=None):
        r"""RegisterClusterSpec

        The model defined in huaweicloud sdk

        :param cluster_group_id: 容器舰队ID信息。
        :type cluster_group_id: str
        :param category: 集群类别，填写需要与provider和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 
        :type category: str
        :param type: 集群类型，填写需要与category和provider对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 
        :type type: str
        :param provider: 供应商，填写需要与category和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 
        :type provider: str
        :param country: 所在国家代码，具体代码请参见[国家码](ucs_api_0022.xml)。
        :type country: str
        :param city: 所在城市代码，具体代码请参见[城市码](ucs_api_0023.xml)。仅支持中国城市，其他国家无需填写。
        :type city: str
        :param region: 地域信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的region字段获取。
        :type region: str
        :param project_id: 项目ID信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的projectID字段获取。
        :type project_id: str
        :param manage_type: 集群管理类型信息。 取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群
        :type manage_type: str
        """
        
        

        self._cluster_group_id = None
        self._category = None
        self._type = None
        self._provider = None
        self._country = None
        self._city = None
        self._region = None
        self._project_id = None
        self._manage_type = None
        self.discriminator = None

        if cluster_group_id is not None:
            self.cluster_group_id = cluster_group_id
        self.category = category
        self.type = type
        self.provider = provider
        self.country = country
        self.city = city
        if region is not None:
            self.region = region
        if project_id is not None:
            self.project_id = project_id
        self.manage_type = manage_type

    @property
    def cluster_group_id(self):
        r"""Gets the cluster_group_id of this RegisterClusterSpec.

        容器舰队ID信息。

        :return: The cluster_group_id of this RegisterClusterSpec.
        :rtype: str
        """
        return self._cluster_group_id

    @cluster_group_id.setter
    def cluster_group_id(self, cluster_group_id):
        r"""Sets the cluster_group_id of this RegisterClusterSpec.

        容器舰队ID信息。

        :param cluster_group_id: The cluster_group_id of this RegisterClusterSpec.
        :type cluster_group_id: str
        """
        self._cluster_group_id = cluster_group_id

    @property
    def category(self):
        r"""Gets the category of this RegisterClusterSpec.

        集群类别，填写需要与provider和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :return: The category of this RegisterClusterSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RegisterClusterSpec.

        集群类别，填写需要与provider和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :param category: The category of this RegisterClusterSpec.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        r"""Gets the type of this RegisterClusterSpec.

        集群类型，填写需要与category和provider对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :return: The type of this RegisterClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RegisterClusterSpec.

        集群类型，填写需要与category和provider对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :param type: The type of this RegisterClusterSpec.
        :type type: str
        """
        self._type = type

    @property
    def provider(self):
        r"""Gets the provider of this RegisterClusterSpec.

        供应商，填写需要与category和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :return: The provider of this RegisterClusterSpec.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this RegisterClusterSpec.

        供应商，填写需要与category和type对应，具体请参见[集群类别与类型说明](ucs_api_0024.xml)。 

        :param provider: The provider of this RegisterClusterSpec.
        :type provider: str
        """
        self._provider = provider

    @property
    def country(self):
        r"""Gets the country of this RegisterClusterSpec.

        所在国家代码，具体代码请参见[国家码](ucs_api_0022.xml)。

        :return: The country of this RegisterClusterSpec.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this RegisterClusterSpec.

        所在国家代码，具体代码请参见[国家码](ucs_api_0022.xml)。

        :param country: The country of this RegisterClusterSpec.
        :type country: str
        """
        self._country = country

    @property
    def city(self):
        r"""Gets the city of this RegisterClusterSpec.

        所在城市代码，具体代码请参见[城市码](ucs_api_0023.xml)。仅支持中国城市，其他国家无需填写。

        :return: The city of this RegisterClusterSpec.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this RegisterClusterSpec.

        所在城市代码，具体代码请参见[城市码](ucs_api_0023.xml)。仅支持中国城市，其他国家无需填写。

        :param city: The city of this RegisterClusterSpec.
        :type city: str
        """
        self._city = city

    @property
    def region(self):
        r"""Gets the region of this RegisterClusterSpec.

        地域信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的region字段获取。

        :return: The region of this RegisterClusterSpec.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RegisterClusterSpec.

        地域信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的region字段获取。

        :param region: The region of this RegisterClusterSpec.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        r"""Gets the project_id of this RegisterClusterSpec.

        项目ID信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的projectID字段获取。

        :return: The project_id of this RegisterClusterSpec.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RegisterClusterSpec.

        项目ID信息。仅在CCE导入集群注册时使用。可通过[获取未注册到UCS的CCE集群](ListManagedClusters.xml)接口的projectID字段获取。

        :param project_id: The project_id of this RegisterClusterSpec.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def manage_type(self):
        r"""Gets the manage_type of this RegisterClusterSpec.

        集群管理类型信息。 取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群

        :return: The manage_type of this RegisterClusterSpec.
        :rtype: str
        """
        return self._manage_type

    @manage_type.setter
    def manage_type(self, manage_type):
        r"""Sets the manage_type of this RegisterClusterSpec.

        集群管理类型信息。 取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群

        :param manage_type: The manage_type of this RegisterClusterSpec.
        :type manage_type: str
        """
        self._manage_type = manage_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegisterClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
