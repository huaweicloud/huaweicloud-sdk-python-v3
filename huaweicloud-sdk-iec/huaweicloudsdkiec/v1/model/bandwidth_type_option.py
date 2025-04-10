# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthTypeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'bandwidth_type': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'bandwidth_type': 'bandwidth_type',
        'site_id': 'site_id'
    }

    def __init__(self, name=None, bandwidth_type=None, site_id=None):
        r"""BandwidthTypeOption

        The model defined in huaweicloud sdk

        :param name: 共享带宽类型名称
        :type name: str
        :param bandwidth_type: 共享带宽类型
        :type bandwidth_type: str
        :param site_id: 站点ID
        :type site_id: str
        """
        
        

        self._name = None
        self._bandwidth_type = None
        self._site_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if site_id is not None:
            self.site_id = site_id

    @property
    def name(self):
        r"""Gets the name of this BandwidthTypeOption.

        共享带宽类型名称

        :return: The name of this BandwidthTypeOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BandwidthTypeOption.

        共享带宽类型名称

        :param name: The name of this BandwidthTypeOption.
        :type name: str
        """
        self._name = name

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this BandwidthTypeOption.

        共享带宽类型

        :return: The bandwidth_type of this BandwidthTypeOption.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this BandwidthTypeOption.

        共享带宽类型

        :param bandwidth_type: The bandwidth_type of this BandwidthTypeOption.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def site_id(self):
        r"""Gets the site_id of this BandwidthTypeOption.

        站点ID

        :return: The site_id of this BandwidthTypeOption.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this BandwidthTypeOption.

        站点ID

        :param site_id: The site_id of this BandwidthTypeOption.
        :type site_id: str
        """
        self._site_id = site_id

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
        if not isinstance(other, BandwidthTypeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
