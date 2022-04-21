# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyCertificateToHostRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cloud_host_ids': 'list[str]',
        'premium_host_ids': 'list[str]'
    }

    attribute_map = {
        'cloud_host_ids': 'cloud_host_ids',
        'premium_host_ids': 'premium_host_ids'
    }

    def __init__(self, cloud_host_ids=None, premium_host_ids=None):
        """ApplyCertificateToHostRequestBody

        The model defined in huaweicloud sdk

        :param cloud_host_ids: 云模式HTTPS域名id，通过查询云模式防护域名列表（ListHost）接口获取
        :type cloud_host_ids: list[str]
        :param premium_host_ids: 独享模式HTTPS域名id，通过独享模式域名列表（ListPremiumHost）接口获取
        :type premium_host_ids: list[str]
        """
        
        

        self._cloud_host_ids = None
        self._premium_host_ids = None
        self.discriminator = None

        if cloud_host_ids is not None:
            self.cloud_host_ids = cloud_host_ids
        if premium_host_ids is not None:
            self.premium_host_ids = premium_host_ids

    @property
    def cloud_host_ids(self):
        """Gets the cloud_host_ids of this ApplyCertificateToHostRequestBody.

        云模式HTTPS域名id，通过查询云模式防护域名列表（ListHost）接口获取

        :return: The cloud_host_ids of this ApplyCertificateToHostRequestBody.
        :rtype: list[str]
        """
        return self._cloud_host_ids

    @cloud_host_ids.setter
    def cloud_host_ids(self, cloud_host_ids):
        """Sets the cloud_host_ids of this ApplyCertificateToHostRequestBody.

        云模式HTTPS域名id，通过查询云模式防护域名列表（ListHost）接口获取

        :param cloud_host_ids: The cloud_host_ids of this ApplyCertificateToHostRequestBody.
        :type cloud_host_ids: list[str]
        """
        self._cloud_host_ids = cloud_host_ids

    @property
    def premium_host_ids(self):
        """Gets the premium_host_ids of this ApplyCertificateToHostRequestBody.

        独享模式HTTPS域名id，通过独享模式域名列表（ListPremiumHost）接口获取

        :return: The premium_host_ids of this ApplyCertificateToHostRequestBody.
        :rtype: list[str]
        """
        return self._premium_host_ids

    @premium_host_ids.setter
    def premium_host_ids(self, premium_host_ids):
        """Sets the premium_host_ids of this ApplyCertificateToHostRequestBody.

        独享模式HTTPS域名id，通过独享模式域名列表（ListPremiumHost）接口获取

        :param premium_host_ids: The premium_host_ids of this ApplyCertificateToHostRequestBody.
        :type premium_host_ids: list[str]
        """
        self._premium_host_ids = premium_host_ids

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
        if not isinstance(other, ApplyCertificateToHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
