# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'network_config': 'NetworkConfigReq',
        'access_config': 'AccessConfigReq'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'network_config': 'network_config',
        'access_config': 'access_config'
    }

    def __init__(self, availability_zone=None, network_config=None, access_config=None):
        r"""SiteConfigsRequest

        The model defined in huaweicloud sdk

        :param availability_zone: 开通服务资源使用的可用分区。
        :type availability_zone: str
        :param network_config: 
        :type network_config: :class:`huaweicloudsdkworkspace.v2.NetworkConfigReq`
        :param access_config: 
        :type access_config: :class:`huaweicloudsdkworkspace.v2.AccessConfigReq`
        """
        
        

        self._availability_zone = None
        self._network_config = None
        self._access_config = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.network_config = network_config
        self.access_config = access_config

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this SiteConfigsRequest.

        开通服务资源使用的可用分区。

        :return: The availability_zone of this SiteConfigsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this SiteConfigsRequest.

        开通服务资源使用的可用分区。

        :param availability_zone: The availability_zone of this SiteConfigsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def network_config(self):
        r"""Gets the network_config of this SiteConfigsRequest.

        :return: The network_config of this SiteConfigsRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.NetworkConfigReq`
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        r"""Sets the network_config of this SiteConfigsRequest.

        :param network_config: The network_config of this SiteConfigsRequest.
        :type network_config: :class:`huaweicloudsdkworkspace.v2.NetworkConfigReq`
        """
        self._network_config = network_config

    @property
    def access_config(self):
        r"""Gets the access_config of this SiteConfigsRequest.

        :return: The access_config of this SiteConfigsRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AccessConfigReq`
        """
        return self._access_config

    @access_config.setter
    def access_config(self, access_config):
        r"""Sets the access_config of this SiteConfigsRequest.

        :param access_config: The access_config of this SiteConfigsRequest.
        :type access_config: :class:`huaweicloudsdkworkspace.v2.AccessConfigReq`
        """
        self._access_config = access_config

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
        if not isinstance(other, SiteConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
