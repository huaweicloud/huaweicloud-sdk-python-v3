# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutResourceGroupReq:

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
        'tags': 'list[ResourceGroupTagRelation]',
        'enterprise_project_id_and_tags': 'list[EnterpriseProjectIdAndTags]',
        'extend_relation_ids': 'list[str]',
        'instances': 'list[Instance]',
        'product_names': 'str',
        'comb_relation': 'CombRelation'
    }

    attribute_map = {
        'group_name': 'group_name',
        'tags': 'tags',
        'enterprise_project_id_and_tags': 'enterprise_project_id_and_tags',
        'extend_relation_ids': 'extend_relation_ids',
        'instances': 'instances',
        'product_names': 'product_names',
        'comb_relation': 'comb_relation'
    }

    def __init__(self, group_name=None, tags=None, enterprise_project_id_and_tags=None, extend_relation_ids=None, instances=None, product_names=None, comb_relation=None):
        r"""PutResourceGroupReq

        The model defined in huaweicloud sdk

        :param group_name: 资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128
        :type group_name: str
        :param tags: 标签动态匹配时的关联标签,type为TAG时该字段不为空
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        :param enterprise_project_id_and_tags: 资源匹配规则为组合匹配时传入的参数
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        :param extend_relation_ids: 智能添加时企业项目匹配传入参数
        :type extend_relation_ids: list[str]
        :param instances: 实例名称匹配参数
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        :param product_names: 修改资源层级为云产品时的云产品的取值，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;。多个云产品则用“;”隔开，如\&quot;SERVICE.BMS,instance_id;SYS.ECS,instance_id\&quot;。
        :type product_names: str
        :param comb_relation: 
        :type comb_relation: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        
        

        self._group_name = None
        self._tags = None
        self._enterprise_project_id_and_tags = None
        self._extend_relation_ids = None
        self._instances = None
        self._product_names = None
        self._comb_relation = None
        self.discriminator = None

        self.group_name = group_name
        if tags is not None:
            self.tags = tags
        if enterprise_project_id_and_tags is not None:
            self.enterprise_project_id_and_tags = enterprise_project_id_and_tags
        if extend_relation_ids is not None:
            self.extend_relation_ids = extend_relation_ids
        if instances is not None:
            self.instances = instances
        if product_names is not None:
            self.product_names = product_names
        if comb_relation is not None:
            self.comb_relation = comb_relation

    @property
    def group_name(self):
        r"""Gets the group_name of this PutResourceGroupReq.

        资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128

        :return: The group_name of this PutResourceGroupReq.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this PutResourceGroupReq.

        资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128

        :param group_name: The group_name of this PutResourceGroupReq.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def tags(self):
        r"""Gets the tags of this PutResourceGroupReq.

        标签动态匹配时的关联标签,type为TAG时该字段不为空

        :return: The tags of this PutResourceGroupReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PutResourceGroupReq.

        标签动态匹配时的关联标签,type为TAG时该字段不为空

        :param tags: The tags of this PutResourceGroupReq.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        self._tags = tags

    @property
    def enterprise_project_id_and_tags(self):
        r"""Gets the enterprise_project_id_and_tags of this PutResourceGroupReq.

        资源匹配规则为组合匹配时传入的参数

        :return: The enterprise_project_id_and_tags of this PutResourceGroupReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        return self._enterprise_project_id_and_tags

    @enterprise_project_id_and_tags.setter
    def enterprise_project_id_and_tags(self, enterprise_project_id_and_tags):
        r"""Sets the enterprise_project_id_and_tags of this PutResourceGroupReq.

        资源匹配规则为组合匹配时传入的参数

        :param enterprise_project_id_and_tags: The enterprise_project_id_and_tags of this PutResourceGroupReq.
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        self._enterprise_project_id_and_tags = enterprise_project_id_and_tags

    @property
    def extend_relation_ids(self):
        r"""Gets the extend_relation_ids of this PutResourceGroupReq.

        智能添加时企业项目匹配传入参数

        :return: The extend_relation_ids of this PutResourceGroupReq.
        :rtype: list[str]
        """
        return self._extend_relation_ids

    @extend_relation_ids.setter
    def extend_relation_ids(self, extend_relation_ids):
        r"""Sets the extend_relation_ids of this PutResourceGroupReq.

        智能添加时企业项目匹配传入参数

        :param extend_relation_ids: The extend_relation_ids of this PutResourceGroupReq.
        :type extend_relation_ids: list[str]
        """
        self._extend_relation_ids = extend_relation_ids

    @property
    def instances(self):
        r"""Gets the instances of this PutResourceGroupReq.

        实例名称匹配参数

        :return: The instances of this PutResourceGroupReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this PutResourceGroupReq.

        实例名称匹配参数

        :param instances: The instances of this PutResourceGroupReq.
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        self._instances = instances

    @property
    def product_names(self):
        r"""Gets the product_names of this PutResourceGroupReq.

        修改资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :return: The product_names of this PutResourceGroupReq.
        :rtype: str
        """
        return self._product_names

    @product_names.setter
    def product_names(self, product_names):
        r"""Sets the product_names of this PutResourceGroupReq.

        修改资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :param product_names: The product_names of this PutResourceGroupReq.
        :type product_names: str
        """
        self._product_names = product_names

    @property
    def comb_relation(self):
        r"""Gets the comb_relation of this PutResourceGroupReq.

        :return: The comb_relation of this PutResourceGroupReq.
        :rtype: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        return self._comb_relation

    @comb_relation.setter
    def comb_relation(self, comb_relation):
        r"""Sets the comb_relation of this PutResourceGroupReq.

        :param comb_relation: The comb_relation of this PutResourceGroupReq.
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
        if not isinstance(other, PutResourceGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
