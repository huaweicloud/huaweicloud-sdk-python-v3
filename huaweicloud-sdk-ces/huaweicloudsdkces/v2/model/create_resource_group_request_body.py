# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'enterprise_project_id': 'str',
        'type': 'str',
        'tags': 'list[ResourceGroupTagRelation]',
        'association_ep_ids': 'list[str]',
        'providers': 'str',
        'enterprise_project_id_and_tags': 'list[EnterpriseProjectIdAndTags]',
        'resources': 'list[Resource]',
        'product_resources': 'list[ProductResource]',
        'instances': 'list[Instance]',
        'product_names': 'str',
        'resource_level': 'str',
        'comb_relation': 'CombRelation'
    }

    attribute_map = {
        'group_name': 'group_name',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'tags': 'tags',
        'association_ep_ids': 'association_ep_ids',
        'providers': 'providers',
        'enterprise_project_id_and_tags': 'enterprise_project_id_and_tags',
        'resources': 'resources',
        'product_resources': 'product_resources',
        'instances': 'instances',
        'product_names': 'product_names',
        'resource_level': 'resource_level',
        'comb_relation': 'comb_relation'
    }

    def __init__(self, group_name=None, enterprise_project_id=None, type=None, tags=None, association_ep_ids=None, providers=None, enterprise_project_id_and_tags=None, resources=None, product_resources=None, instances=None, product_names=None, resource_level=None, comb_relation=None):
        r"""CreateResourceGroupRequestBody

        The model defined in huaweicloud sdk

        :param group_name: 资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128
        :type group_name: str
        :param enterprise_project_id: 资源分组归属企业项目ID
        :type enterprise_project_id: str
        :param type: 资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,NAME（实例名称）,不传为手动添加
        :type type: str
        :param tags: 标签动态匹配时的关联标签,type为TAG时必传
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        :param association_ep_ids: 该资源分组内包含的资源来源的企业项目ID，type为EPS时必传
        :type association_ep_ids: list[str]
        :param providers: 云服务名称,格式为\&quot;dcs,ecs\&quot;,支持的云服务providers请参考《配置审计API参考》中的\&quot;支持的服务和资源类型\&quot;章节
        :type providers: str
        :param enterprise_project_id_and_tags: 匹配企业项目或匹配标签参数
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        :param resources: 手动创建时的资源详情
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        :param product_resources: 手动创建，选择资源层级为云产品时的资源详情
        :type product_resources: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        :param instances: 实例名称匹配参数
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        :param product_names: 创建资源层级为云产品时的云产品的取值，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;。多个云产品则用“;”隔开，如\&quot;SERVICE.BMS,instance_id;SYS.ECS,instance_id\&quot;。
        :type product_names: str
        :param resource_level: 资源层级，资源生效范围。选择云产品，则云产品及其子层级均可进入该资源分组，选择子维度，则只生效具体的子维度 product 云产品 dimension 子维度 
        :type resource_level: str
        :param comb_relation: 
        :type comb_relation: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        
        

        self._group_name = None
        self._enterprise_project_id = None
        self._type = None
        self._tags = None
        self._association_ep_ids = None
        self._providers = None
        self._enterprise_project_id_and_tags = None
        self._resources = None
        self._product_resources = None
        self._instances = None
        self._product_names = None
        self._resource_level = None
        self._comb_relation = None
        self.discriminator = None

        self.group_name = group_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags
        if association_ep_ids is not None:
            self.association_ep_ids = association_ep_ids
        if providers is not None:
            self.providers = providers
        if enterprise_project_id_and_tags is not None:
            self.enterprise_project_id_and_tags = enterprise_project_id_and_tags
        if resources is not None:
            self.resources = resources
        if product_resources is not None:
            self.product_resources = product_resources
        if instances is not None:
            self.instances = instances
        if product_names is not None:
            self.product_names = product_names
        if resource_level is not None:
            self.resource_level = resource_level
        if comb_relation is not None:
            self.comb_relation = comb_relation

    @property
    def group_name(self):
        r"""Gets the group_name of this CreateResourceGroupRequestBody.

        资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128

        :return: The group_name of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this CreateResourceGroupRequestBody.

        资源分组的名称，只能为字母、数字、汉字、-、_，最大长度为128

        :param group_name: The group_name of this CreateResourceGroupRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateResourceGroupRequestBody.

        资源分组归属企业项目ID

        :return: The enterprise_project_id of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateResourceGroupRequestBody.

        资源分组归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateResourceGroupRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this CreateResourceGroupRequestBody.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,NAME（实例名称）,不传为手动添加

        :return: The type of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateResourceGroupRequestBody.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,NAME（实例名称）,不传为手动添加

        :param type: The type of this CreateResourceGroupRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this CreateResourceGroupRequestBody.

        标签动态匹配时的关联标签,type为TAG时必传

        :return: The tags of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateResourceGroupRequestBody.

        标签动态匹配时的关联标签,type为TAG时必传

        :param tags: The tags of this CreateResourceGroupRequestBody.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        self._tags = tags

    @property
    def association_ep_ids(self):
        r"""Gets the association_ep_ids of this CreateResourceGroupRequestBody.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :return: The association_ep_ids of this CreateResourceGroupRequestBody.
        :rtype: list[str]
        """
        return self._association_ep_ids

    @association_ep_ids.setter
    def association_ep_ids(self, association_ep_ids):
        r"""Sets the association_ep_ids of this CreateResourceGroupRequestBody.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :param association_ep_ids: The association_ep_ids of this CreateResourceGroupRequestBody.
        :type association_ep_ids: list[str]
        """
        self._association_ep_ids = association_ep_ids

    @property
    def providers(self):
        r"""Gets the providers of this CreateResourceGroupRequestBody.

        云服务名称,格式为\"dcs,ecs\",支持的云服务providers请参考《配置审计API参考》中的\"支持的服务和资源类型\"章节

        :return: The providers of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this CreateResourceGroupRequestBody.

        云服务名称,格式为\"dcs,ecs\",支持的云服务providers请参考《配置审计API参考》中的\"支持的服务和资源类型\"章节

        :param providers: The providers of this CreateResourceGroupRequestBody.
        :type providers: str
        """
        self._providers = providers

    @property
    def enterprise_project_id_and_tags(self):
        r"""Gets the enterprise_project_id_and_tags of this CreateResourceGroupRequestBody.

        匹配企业项目或匹配标签参数

        :return: The enterprise_project_id_and_tags of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        return self._enterprise_project_id_and_tags

    @enterprise_project_id_and_tags.setter
    def enterprise_project_id_and_tags(self, enterprise_project_id_and_tags):
        r"""Sets the enterprise_project_id_and_tags of this CreateResourceGroupRequestBody.

        匹配企业项目或匹配标签参数

        :param enterprise_project_id_and_tags: The enterprise_project_id_and_tags of this CreateResourceGroupRequestBody.
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        self._enterprise_project_id_and_tags = enterprise_project_id_and_tags

    @property
    def resources(self):
        r"""Gets the resources of this CreateResourceGroupRequestBody.

        手动创建时的资源详情

        :return: The resources of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this CreateResourceGroupRequestBody.

        手动创建时的资源详情

        :param resources: The resources of this CreateResourceGroupRequestBody.
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        self._resources = resources

    @property
    def product_resources(self):
        r"""Gets the product_resources of this CreateResourceGroupRequestBody.

        手动创建，选择资源层级为云产品时的资源详情

        :return: The product_resources of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        """
        return self._product_resources

    @product_resources.setter
    def product_resources(self, product_resources):
        r"""Sets the product_resources of this CreateResourceGroupRequestBody.

        手动创建，选择资源层级为云产品时的资源详情

        :param product_resources: The product_resources of this CreateResourceGroupRequestBody.
        :type product_resources: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        """
        self._product_resources = product_resources

    @property
    def instances(self):
        r"""Gets the instances of this CreateResourceGroupRequestBody.

        实例名称匹配参数

        :return: The instances of this CreateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this CreateResourceGroupRequestBody.

        实例名称匹配参数

        :param instances: The instances of this CreateResourceGroupRequestBody.
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        self._instances = instances

    @property
    def product_names(self):
        r"""Gets the product_names of this CreateResourceGroupRequestBody.

        创建资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :return: The product_names of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._product_names

    @product_names.setter
    def product_names(self, product_names):
        r"""Sets the product_names of this CreateResourceGroupRequestBody.

        创建资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :param product_names: The product_names of this CreateResourceGroupRequestBody.
        :type product_names: str
        """
        self._product_names = product_names

    @property
    def resource_level(self):
        r"""Gets the resource_level of this CreateResourceGroupRequestBody.

        资源层级，资源生效范围。选择云产品，则云产品及其子层级均可进入该资源分组，选择子维度，则只生效具体的子维度 product 云产品 dimension 子维度 

        :return: The resource_level of this CreateResourceGroupRequestBody.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this CreateResourceGroupRequestBody.

        资源层级，资源生效范围。选择云产品，则云产品及其子层级均可进入该资源分组，选择子维度，则只生效具体的子维度 product 云产品 dimension 子维度 

        :param resource_level: The resource_level of this CreateResourceGroupRequestBody.
        :type resource_level: str
        """
        self._resource_level = resource_level

    @property
    def comb_relation(self):
        r"""Gets the comb_relation of this CreateResourceGroupRequestBody.

        :return: The comb_relation of this CreateResourceGroupRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        return self._comb_relation

    @comb_relation.setter
    def comb_relation(self, comb_relation):
        r"""Sets the comb_relation of this CreateResourceGroupRequestBody.

        :param comb_relation: The comb_relation of this CreateResourceGroupRequestBody.
        :type comb_relation: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        self._comb_relation = comb_relation

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
        if not isinstance(other, CreateResourceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
