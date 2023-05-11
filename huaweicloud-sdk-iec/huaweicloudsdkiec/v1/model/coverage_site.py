# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoverageSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site': 'str',
        'demands': 'list[Demand]'
    }

    attribute_map = {
        'site': 'site',
        'demands': 'demands'
    }

    def __init__(self, site=None, demands=None):
        """CoverageSite

        The model defined in huaweicloud sdk

        :param site: 站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。
        :type site: str
        :param demands: 租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。
        :type demands: list[:class:`huaweicloudsdkiec.v1.Demand`]
        """
        
        

        self._site = None
        self._demands = None
        self.discriminator = None

        self.site = site
        self.demands = demands

    @property
    def site(self):
        """Gets the site of this CoverageSite.

        站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。

        :return: The site of this CoverageSite.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this CoverageSite.

        站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。

        :param site: The site of this CoverageSite.
        :type site: str
        """
        self._site = site

    @property
    def demands(self):
        """Gets the demands of this CoverageSite.

        租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。

        :return: The demands of this CoverageSite.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Demand`]
        """
        return self._demands

    @demands.setter
    def demands(self, demands):
        """Sets the demands of this CoverageSite.

        租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。

        :param demands: The demands of this CoverageSite.
        :type demands: list[:class:`huaweicloudsdkiec.v1.Demand`]
        """
        self._demands = demands

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
        if not isinstance(other, CoverageSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
