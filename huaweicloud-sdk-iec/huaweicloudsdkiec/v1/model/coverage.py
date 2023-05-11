# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Coverage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coverage_policy': 'str',
        'coverage_level': 'str',
        'coverage_sites': 'list[CoverageSite]'
    }

    attribute_map = {
        'coverage_policy': 'coverage_policy',
        'coverage_level': 'coverage_level',
        'coverage_sites': 'coverage_sites'
    }

    def __init__(self, coverage_policy=None, coverage_level=None, coverage_sites=None):
        """Coverage

        The model defined in huaweicloud sdk

        :param coverage_policy: 区域调度策略，只支持centralize/discrete。  - centralize：代表城市集中策略，指定该策略，边缘业务创建时会保证将所有实例都发放在同一个站点。 - discrete：代表城市分散，指定该策略，边缘业务创建时，尽量保证所有实例都分散发放在不同站点。
        :type coverage_policy: str
        :param coverage_level: 区域分布层级，只支持area/prov/city/site。  - area:大区，用户的资源会在指定大区下发放。 - prov:省份，用户的资源会在指定省份下发放。 - city:城市，用户的资源会在指定城市下发放。 - site:站点级别。  约束：  站点层级，coverage_policy上仅支持&#39;centralize&#39;，coverage_sites中&#39;site&#39;字段仅支持使用ID(站点ID，通过“查询边缘站点列表”获取)，不支持name。
        :type coverage_level: str
        :param coverage_sites: 区域及购买数量列表。
        :type coverage_sites: list[:class:`huaweicloudsdkiec.v1.CoverageSite`]
        """
        
        

        self._coverage_policy = None
        self._coverage_level = None
        self._coverage_sites = None
        self.discriminator = None

        self.coverage_policy = coverage_policy
        self.coverage_level = coverage_level
        self.coverage_sites = coverage_sites

    @property
    def coverage_policy(self):
        """Gets the coverage_policy of this Coverage.

        区域调度策略，只支持centralize/discrete。  - centralize：代表城市集中策略，指定该策略，边缘业务创建时会保证将所有实例都发放在同一个站点。 - discrete：代表城市分散，指定该策略，边缘业务创建时，尽量保证所有实例都分散发放在不同站点。

        :return: The coverage_policy of this Coverage.
        :rtype: str
        """
        return self._coverage_policy

    @coverage_policy.setter
    def coverage_policy(self, coverage_policy):
        """Sets the coverage_policy of this Coverage.

        区域调度策略，只支持centralize/discrete。  - centralize：代表城市集中策略，指定该策略，边缘业务创建时会保证将所有实例都发放在同一个站点。 - discrete：代表城市分散，指定该策略，边缘业务创建时，尽量保证所有实例都分散发放在不同站点。

        :param coverage_policy: The coverage_policy of this Coverage.
        :type coverage_policy: str
        """
        self._coverage_policy = coverage_policy

    @property
    def coverage_level(self):
        """Gets the coverage_level of this Coverage.

        区域分布层级，只支持area/prov/city/site。  - area:大区，用户的资源会在指定大区下发放。 - prov:省份，用户的资源会在指定省份下发放。 - city:城市，用户的资源会在指定城市下发放。 - site:站点级别。  约束：  站点层级，coverage_policy上仅支持'centralize'，coverage_sites中'site'字段仅支持使用ID(站点ID，通过“查询边缘站点列表”获取)，不支持name。

        :return: The coverage_level of this Coverage.
        :rtype: str
        """
        return self._coverage_level

    @coverage_level.setter
    def coverage_level(self, coverage_level):
        """Sets the coverage_level of this Coverage.

        区域分布层级，只支持area/prov/city/site。  - area:大区，用户的资源会在指定大区下发放。 - prov:省份，用户的资源会在指定省份下发放。 - city:城市，用户的资源会在指定城市下发放。 - site:站点级别。  约束：  站点层级，coverage_policy上仅支持'centralize'，coverage_sites中'site'字段仅支持使用ID(站点ID，通过“查询边缘站点列表”获取)，不支持name。

        :param coverage_level: The coverage_level of this Coverage.
        :type coverage_level: str
        """
        self._coverage_level = coverage_level

    @property
    def coverage_sites(self):
        """Gets the coverage_sites of this Coverage.

        区域及购买数量列表。

        :return: The coverage_sites of this Coverage.
        :rtype: list[:class:`huaweicloudsdkiec.v1.CoverageSite`]
        """
        return self._coverage_sites

    @coverage_sites.setter
    def coverage_sites(self, coverage_sites):
        """Sets the coverage_sites of this Coverage.

        区域及购买数量列表。

        :param coverage_sites: The coverage_sites of this Coverage.
        :type coverage_sites: list[:class:`huaweicloudsdkiec.v1.CoverageSite`]
        """
        self._coverage_sites = coverage_sites

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
        if not isinstance(other, Coverage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
