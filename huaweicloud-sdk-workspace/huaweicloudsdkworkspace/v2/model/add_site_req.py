# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSiteReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_configs': 'list[SiteConfigsRequest]'
    }

    attribute_map = {
        'site_configs': 'site_configs'
    }

    def __init__(self, site_configs=None):
        r"""AddSiteReq

        The model defined in huaweicloud sdk

        :param site_configs: 站点配置信息。
        :type site_configs: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        """
        
        

        self._site_configs = None
        self.discriminator = None

        self.site_configs = site_configs

    @property
    def site_configs(self):
        r"""Gets the site_configs of this AddSiteReq.

        站点配置信息。

        :return: The site_configs of this AddSiteReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        """
        return self._site_configs

    @site_configs.setter
    def site_configs(self, site_configs):
        r"""Sets the site_configs of this AddSiteReq.

        站点配置信息。

        :param site_configs: The site_configs of this AddSiteReq.
        :type site_configs: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        """
        self._site_configs = site_configs

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
        if not isinstance(other, AddSiteReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
