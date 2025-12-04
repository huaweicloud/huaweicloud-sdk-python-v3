# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'cluster_type': 'str',
        'cluster_version': 'list[str]'
    }

    attribute_map = {
        'category': 'category',
        'cluster_type': 'clusterType',
        'cluster_version': 'clusterVersion'
    }

    def __init__(self, category=None, cluster_type=None, cluster_version=None):
        r"""SupportVersion

        The model defined in huaweicloud sdk

        :param category: 支持的集群类型
        :type category: str
        :param cluster_type: 支持的集群类型（BareMetal，VirtualMachine，windows等）
        :type cluster_type: str
        :param cluster_version: 支持的集群版本，支持正则表达式，如\&quot;.*\&quot;匹配所有集群版本
        :type cluster_version: list[str]
        """
        
        

        self._category = None
        self._cluster_type = None
        self._cluster_version = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_version is not None:
            self.cluster_version = cluster_version

    @property
    def category(self):
        r"""Gets the category of this SupportVersion.

        支持的集群类型

        :return: The category of this SupportVersion.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SupportVersion.

        支持的集群类型

        :param category: The category of this SupportVersion.
        :type category: str
        """
        self._category = category

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this SupportVersion.

        支持的集群类型（BareMetal，VirtualMachine，windows等）

        :return: The cluster_type of this SupportVersion.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this SupportVersion.

        支持的集群类型（BareMetal，VirtualMachine，windows等）

        :param cluster_type: The cluster_type of this SupportVersion.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this SupportVersion.

        支持的集群版本，支持正则表达式，如\".*\"匹配所有集群版本

        :return: The cluster_version of this SupportVersion.
        :rtype: list[str]
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this SupportVersion.

        支持的集群版本，支持正则表达式，如\".*\"匹配所有集群版本

        :param cluster_version: The cluster_version of this SupportVersion.
        :type cluster_version: list[str]
        """
        self._cluster_version = cluster_version

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupportVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
