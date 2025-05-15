# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSiteInformationPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sites': 'list[CreateSiteInformation]'
    }

    attribute_map = {
        'sites': 'sites'
    }

    def __init__(self, sites=None):
        r"""CreateSiteInformationPair

        The model defined in huaweicloud sdk

        :param sites: 端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。
        :type sites: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        
        

        self._sites = None
        self.discriminator = None

        self.sites = sites

    @property
    def sites(self):
        r"""Gets the sites of this CreateSiteInformationPair.

        端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。

        :return: The sites of this CreateSiteInformationPair.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        r"""Sets the sites of this CreateSiteInformationPair.

        端到端（P2P）类型分支网络连接的两个端点定义，长度固定为2的数组。

        :param sites: The sites of this CreateSiteInformationPair.
        :type sites: list[:class:`huaweicloudsdkcc.v3.CreateSiteInformation`]
        """
        self._sites = sites

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
        if not isinstance(other, CreateSiteInformationPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
