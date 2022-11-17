# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateElasticResourcePoolInfo:

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
        'tags': 'list[TmsTag]'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'description': 'description',
        'cidr_in_vpc': 'cidr_in_vpc',
        'max_cu': 'max_cu',
        'charging_mode': 'charging_mode',
        'min_cu': 'min_cu',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, elastic_resource_pool_name=None, description=None, cidr_in_vpc=None, max_cu=None, charging_mode=None, min_cu=None, enterprise_project_id=None, tags=None):
        """CreateElasticResourcePoolInfo

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。
        :type elastic_resource_pool_name: str
        :param description: 描述信息。长度限制：256个字符以内。
        :type description: str
        :param cidr_in_vpc: 虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12
        :type cidr_in_vpc: str
        :param max_cu: 最大CU大于等于该资源池下任意一个队列的最大CU之和且大于min_cu。最小值为64
        :type max_cu: int
        :param charging_mode: 计费类型 1、按需计费
        :type charging_mode: int
        :param min_cu: 最小CU大于等于该资源池下所有队列最小CU之和,最小值为64
        :type min_cu: int
        :param enterprise_project_id: 企业ID，不填默认为“0”
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTag`]
        """
        
        

        self._elastic_resource_pool_name = None
        self._description = None
        self._cidr_in_vpc = None
        self._max_cu = None
        self._charging_mode = None
        self._min_cu = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        if description is not None:
            self.description = description
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        self.max_cu = max_cu
        self.charging_mode = charging_mode
        self.min_cu = min_cu
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def elastic_resource_pool_name(self):
        """Gets the elastic_resource_pool_name of this CreateElasticResourcePoolInfo.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :return: The elastic_resource_pool_name of this CreateElasticResourcePoolInfo.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        """Sets the elastic_resource_pool_name of this CreateElasticResourcePoolInfo.

        新建的弹性资源池名称，名称只能包含数字、小写英文字母和下划线，但不能是纯数字，且不能以下划线开头。长度限制：1~128个字符。

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this CreateElasticResourcePoolInfo.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def description(self):
        """Gets the description of this CreateElasticResourcePoolInfo.

        描述信息。长度限制：256个字符以内。

        :return: The description of this CreateElasticResourcePoolInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateElasticResourcePoolInfo.

        描述信息。长度限制：256个字符以内。

        :param description: The description of this CreateElasticResourcePoolInfo.
        :type description: str
        """
        self._description = description

    @property
    def cidr_in_vpc(self):
        """Gets the cidr_in_vpc of this CreateElasticResourcePoolInfo.

        虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12

        :return: The cidr_in_vpc of this CreateElasticResourcePoolInfo.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        """Sets the cidr_in_vpc of this CreateElasticResourcePoolInfo.

        虚拟集群关联的vpc cidr.如果不填，默认值为172.16.0.0//12

        :param cidr_in_vpc: The cidr_in_vpc of this CreateElasticResourcePoolInfo.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def max_cu(self):
        """Gets the max_cu of this CreateElasticResourcePoolInfo.

        最大CU大于等于该资源池下任意一个队列的最大CU之和且大于min_cu。最小值为64

        :return: The max_cu of this CreateElasticResourcePoolInfo.
        :rtype: int
        """
        return self._max_cu

    @max_cu.setter
    def max_cu(self, max_cu):
        """Sets the max_cu of this CreateElasticResourcePoolInfo.

        最大CU大于等于该资源池下任意一个队列的最大CU之和且大于min_cu。最小值为64

        :param max_cu: The max_cu of this CreateElasticResourcePoolInfo.
        :type max_cu: int
        """
        self._max_cu = max_cu

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateElasticResourcePoolInfo.

        计费类型 1、按需计费

        :return: The charging_mode of this CreateElasticResourcePoolInfo.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateElasticResourcePoolInfo.

        计费类型 1、按需计费

        :param charging_mode: The charging_mode of this CreateElasticResourcePoolInfo.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def min_cu(self):
        """Gets the min_cu of this CreateElasticResourcePoolInfo.

        最小CU大于等于该资源池下所有队列最小CU之和,最小值为64

        :return: The min_cu of this CreateElasticResourcePoolInfo.
        :rtype: int
        """
        return self._min_cu

    @min_cu.setter
    def min_cu(self, min_cu):
        """Sets the min_cu of this CreateElasticResourcePoolInfo.

        最小CU大于等于该资源池下所有队列最小CU之和,最小值为64

        :param min_cu: The min_cu of this CreateElasticResourcePoolInfo.
        :type min_cu: int
        """
        self._min_cu = min_cu

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateElasticResourcePoolInfo.

        企业ID，不填默认为“0”

        :return: The enterprise_project_id of this CreateElasticResourcePoolInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateElasticResourcePoolInfo.

        企业ID，不填默认为“0”

        :param enterprise_project_id: The enterprise_project_id of this CreateElasticResourcePoolInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateElasticResourcePoolInfo.

        标签

        :return: The tags of this CreateElasticResourcePoolInfo.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateElasticResourcePoolInfo.

        标签

        :param tags: The tags of this CreateElasticResourcePoolInfo.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateElasticResourcePoolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
