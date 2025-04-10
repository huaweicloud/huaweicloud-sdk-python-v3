# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'resources': 'list[str]'
    }

    attribute_map = {
        'region': 'region',
        'resources': 'resources'
    }

    def __init__(self, region=None, resources=None):
        r"""AgencyUsage

        The model defined in huaweicloud sdk

        :param region: 区域名称。
        :type region: str
        :param resources: 统一资源名称列表。
        :type resources: list[str]
        """
        
        

        self._region = None
        self._resources = None
        self.discriminator = None

        self.region = region
        self.resources = resources

    @property
    def region(self):
        r"""Gets the region of this AgencyUsage.

        区域名称。

        :return: The region of this AgencyUsage.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AgencyUsage.

        区域名称。

        :param region: The region of this AgencyUsage.
        :type region: str
        """
        self._region = region

    @property
    def resources(self):
        r"""Gets the resources of this AgencyUsage.

        统一资源名称列表。

        :return: The resources of this AgencyUsage.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this AgencyUsage.

        统一资源名称列表。

        :param resources: The resources of this AgencyUsage.
        :type resources: list[str]
        """
        self._resources = resources

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
        if not isinstance(other, AgencyUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
