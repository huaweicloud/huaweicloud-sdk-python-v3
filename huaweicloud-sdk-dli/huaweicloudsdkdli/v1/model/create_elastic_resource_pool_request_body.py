# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateElasticResourcePoolRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'description': 'str',
        'cidr_in_vpc': 'str',
        'max_cu': 'int',
        'charging_mode': 'int',
        'min_cu': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'label': 'dict(str, str)',
        'ipv6_enable': 'bool'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'description': 'description',
        'cidr_in_vpc': 'cidr_in_vpc',
        'max_cu': 'max_cu',
        'charging_mode': 'charging_mode',
        'min_cu': 'min_cu',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'label': 'label',
        'ipv6_enable': 'ipv6_enable'
    }

    def __init__(self, elastic_resource_pool_name=None, description=None, cidr_in_vpc=None, max_cu=None, charging_mode=None, min_cu=None, enterprise_project_id=None, tags=None, label=None, ipv6_enable=None):
        r"""CreateElasticResourcePoolRequestBody

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。
        :type elastic_resource_pool_name: str
        :param description: 描述信息。长度限制：256个字符以内。
        :type description: str
        :param cidr_in_vpc: 虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12
        :type cidr_in_vpc: str
        :param max_cu: max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。
        :type max_cu: int
        :param charging_mode: 计费类型 1、按需计费
        :type charging_mode: int
        :param min_cu: min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。
        :type min_cu: int
        :param enterprise_project_id: 企业ID，不填默认为“0”
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param label: 弹性资源池属性字段。默认为标准版弹性资源池；{\&quot;spec\&quot;:\&quot;basic\&quot;}标识基础版弹性资源池；{\&quot;billing_spec_code\&quot;:\&quot;developer\&quot;}标识开发者弹性资源池。目前不支持其它属性设置。
        :type label: dict(str, str)
        :param ipv6_enable: 是否启用IPv6。开启IPv6后，将自动为资源池分配IPv6网段，暂不支持自定义IPv6网段。该功能一旦开启，将不能关闭。
        :type ipv6_enable: bool
        """
        
        

        self._elastic_resource_pool_name = None
        self._description = None
        self._cidr_in_vpc = None
        self._max_cu = None
        self._charging_mode = None
        self._min_cu = None
        self._enterprise_project_id = None
        self._tags = None
        self._label = None
        self._ipv6_enable = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        if description is not None:
            self.description = description
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        self.max_cu = max_cu
        if charging_mode is not None:
            self.charging_mode = charging_mode
        self.min_cu = min_cu
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if label is not None:
            self.label = label
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable

    @property
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this CreateElasticResourcePoolRequestBody.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :return: The elastic_resource_pool_name of this CreateElasticResourcePoolRequestBody.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this CreateElasticResourcePoolRequestBody.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this CreateElasticResourcePoolRequestBody.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def description(self):
        r"""Gets the description of this CreateElasticResourcePoolRequestBody.

        描述信息。长度限制：256个字符以内。

        :return: The description of this CreateElasticResourcePoolRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateElasticResourcePoolRequestBody.

        描述信息。长度限制：256个字符以内。

        :param description: The description of this CreateElasticResourcePoolRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def cidr_in_vpc(self):
        r"""Gets the cidr_in_vpc of this CreateElasticResourcePoolRequestBody.

        虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12

        :return: The cidr_in_vpc of this CreateElasticResourcePoolRequestBody.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        r"""Sets the cidr_in_vpc of this CreateElasticResourcePoolRequestBody.

        虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12

        :param cidr_in_vpc: The cidr_in_vpc of this CreateElasticResourcePoolRequestBody.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def max_cu(self):
        r"""Gets the max_cu of this CreateElasticResourcePoolRequestBody.

        max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :return: The max_cu of this CreateElasticResourcePoolRequestBody.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        r"""Sets the max_cu of this CreateElasticResourcePoolRequestBody.

        max_cu大于等于该弹性资源池下任意一个队列的最大CU。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :param max_cu: The max_cu of this CreateElasticResourcePoolRequestBody.
        :type max_cu: int
        """
        self._max_cu = max_cu

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateElasticResourcePoolRequestBody.

        计费类型 1、按需计费

        :return: The charging_mode of this CreateElasticResourcePoolRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateElasticResourcePoolRequestBody.

        计费类型 1、按需计费

        :param charging_mode: The charging_mode of this CreateElasticResourcePoolRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def min_cu(self):
        r"""Gets the min_cu of this CreateElasticResourcePoolRequestBody.

        min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :return: The min_cu of this CreateElasticResourcePoolRequestBody.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        r"""Sets the min_cu of this CreateElasticResourcePoolRequestBody.

        min_cu大于等于该弹性资源池下所有队列最小CU之和，且小于等于max_cu。标准版弹性资源池最小值为64，最大值为32000；基础版弹性资源池最小值为16，最大值为64。

        :param min_cu: The min_cu of this CreateElasticResourcePoolRequestBody.
        :type min_cu: int
        """
        self._min_cu = min_cu

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateElasticResourcePoolRequestBody.

        企业ID，不填默认为“0”

        :return: The enterprise_project_id of this CreateElasticResourcePoolRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateElasticResourcePoolRequestBody.

        企业ID，不填默认为“0”

        :param enterprise_project_id: The enterprise_project_id of this CreateElasticResourcePoolRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateElasticResourcePoolRequestBody.

        标签

        :return: The tags of this CreateElasticResourcePoolRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateElasticResourcePoolRequestBody.

        标签

        :param tags: The tags of this CreateElasticResourcePoolRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def label(self):
        r"""Gets the label of this CreateElasticResourcePoolRequestBody.

        弹性资源池属性字段。默认为标准版弹性资源池；{\"spec\":\"basic\"}标识基础版弹性资源池；{\"billing_spec_code\":\"developer\"}标识开发者弹性资源池。目前不支持其它属性设置。

        :return: The label of this CreateElasticResourcePoolRequestBody.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this CreateElasticResourcePoolRequestBody.

        弹性资源池属性字段。默认为标准版弹性资源池；{\"spec\":\"basic\"}标识基础版弹性资源池；{\"billing_spec_code\":\"developer\"}标识开发者弹性资源池。目前不支持其它属性设置。

        :param label: The label of this CreateElasticResourcePoolRequestBody.
        :type label: dict(str, str)
        """
        self._label = label

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this CreateElasticResourcePoolRequestBody.

        是否启用IPv6。开启IPv6后，将自动为资源池分配IPv6网段，暂不支持自定义IPv6网段。该功能一旦开启，将不能关闭。

        :return: The ipv6_enable of this CreateElasticResourcePoolRequestBody.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this CreateElasticResourcePoolRequestBody.

        是否启用IPv6。开启IPv6后，将自动为资源池分配IPv6网段，暂不支持自定义IPv6网段。该功能一旦开启，将不能关闭。

        :param ipv6_enable: The ipv6_enable of this CreateElasticResourcePoolRequestBody.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

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
        if not isinstance(other, CreateElasticResourcePoolRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
