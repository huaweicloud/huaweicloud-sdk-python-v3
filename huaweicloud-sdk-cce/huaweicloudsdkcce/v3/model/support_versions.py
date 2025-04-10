# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportVersions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str',
        'cluster_version': 'list[str]',
        'category': 'list[str]'
    }

    attribute_map = {
        'cluster_type': 'clusterType',
        'cluster_version': 'clusterVersion',
        'category': 'category'
    }

    def __init__(self, cluster_type=None, cluster_version=None, category=None):
        r"""SupportVersions

        The model defined in huaweicloud sdk

        :param cluster_type: 支持的集群类型
        :type cluster_type: str
        :param cluster_version: 支持的集群版本（正则表达式）
        :type cluster_version: list[str]
        :param category: 作用的集群类型 **取值范围：** - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 - Autopilot：CCE Autopilot集群  **默认取值** 为空时默认为CCE Standard，CCE Turbo集群
        :type category: list[str]
        """
        
        

        self._cluster_type = None
        self._cluster_version = None
        self._category = None
        self.discriminator = None

        self.cluster_type = cluster_type
        self.cluster_version = cluster_version
        if category is not None:
            self.category = category

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this SupportVersions.

        支持的集群类型

        :return: The cluster_type of this SupportVersions.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this SupportVersions.

        支持的集群类型

        :param cluster_type: The cluster_type of this SupportVersions.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this SupportVersions.

        支持的集群版本（正则表达式）

        :return: The cluster_version of this SupportVersions.
        :rtype: list[str]
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this SupportVersions.

        支持的集群版本（正则表达式）

        :param cluster_version: The cluster_version of this SupportVersions.
        :type cluster_version: list[str]
        """
        self._cluster_version = cluster_version

    @property
    def category(self):
        r"""Gets the category of this SupportVersions.

        作用的集群类型 **取值范围：** - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 - Autopilot：CCE Autopilot集群  **默认取值** 为空时默认为CCE Standard，CCE Turbo集群

        :return: The category of this SupportVersions.
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SupportVersions.

        作用的集群类型 **取值范围：** - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 - Autopilot：CCE Autopilot集群  **默认取值** 为空时默认为CCE Standard，CCE Turbo集群

        :param category: The category of this SupportVersions.
        :type category: list[str]
        """
        self._category = category

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
        if not isinstance(other, SupportVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
