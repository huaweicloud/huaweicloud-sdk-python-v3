# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoverageSiteResp:

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
        'demands': 'list[DemandResp]',
        'i18n_site': 'str'
    }

    attribute_map = {
        'site': 'site',
        'demands': 'demands',
        'i18n_site': 'i18n_site'
    }

    def __init__(self, site=None, demands=None, i18n_site=None):
        """CoverageSiteResp

        The model defined in huaweicloud sdk

        :param site: 站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。
        :type site: str
        :param demands: 租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。
        :type demands: list[:class:`huaweicloudsdkiec.v1.DemandResp`]
        :param i18n_site: 覆盖区域的国际化信息。
        :type i18n_site: str
        """
        
        

        self._site = None
        self._demands = None
        self._i18n_site = None
        self.discriminator = None

        self.site = site
        self.demands = demands
        if i18n_site is not None:
            self.i18n_site = i18n_site

    @property
    def site(self):
        """Gets the site of this CoverageSiteResp.

        站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。

        :return: The site of this CoverageSiteResp.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this CoverageSiteResp.

        站点名称。 具体信息可通过调用“查询边缘站点列表”来查询(注意：本字段区分大小写)。

        :param site: The site of this CoverageSiteResp.
        :type site: str
        """
        self._site = site

    @property
    def demands(self):
        """Gets the demands of this CoverageSiteResp.

        租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。

        :return: The demands of this CoverageSiteResp.
        :rtype: list[:class:`huaweicloudsdkiec.v1.DemandResp`]
        """
        return self._demands

    @demands.setter
    def demands(self, demands):
        """Sets the demands of this CoverageSiteResp.

        租户需求数量列表。表示租户发放资源站点的运营商和发放的资源组的数量。

        :param demands: The demands of this CoverageSiteResp.
        :type demands: list[:class:`huaweicloudsdkiec.v1.DemandResp`]
        """
        self._demands = demands

    @property
    def i18n_site(self):
        """Gets the i18n_site of this CoverageSiteResp.

        覆盖区域的国际化信息。

        :return: The i18n_site of this CoverageSiteResp.
        :rtype: str
        """
        return self._i18n_site

    @i18n_site.setter
    def i18n_site(self, i18n_site):
        """Sets the i18n_site of this CoverageSiteResp.

        覆盖区域的国际化信息。

        :param i18n_site: The i18n_site of this CoverageSiteResp.
        :type i18n_site: str
        """
        self._i18n_site = i18n_site

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
        if not isinstance(other, CoverageSiteResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
