# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmClusterEnterpriseProject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'sys_tags': 'list[SysTags]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, cluster_id=None, sys_tags=None):
        r"""CdmClusterEnterpriseProject

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param sys_tags: 企业项目列表
        :type sys_tags: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        """
        
        

        self._cluster_id = None
        self._sys_tags = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CdmClusterEnterpriseProject.

        集群ID

        :return: The cluster_id of this CdmClusterEnterpriseProject.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CdmClusterEnterpriseProject.

        集群ID

        :param cluster_id: The cluster_id of this CdmClusterEnterpriseProject.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this CdmClusterEnterpriseProject.

        企业项目列表

        :return: The sys_tags of this CdmClusterEnterpriseProject.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this CdmClusterEnterpriseProject.

        企业项目列表

        :param sys_tags: The sys_tags of this CdmClusterEnterpriseProject.
        :type sys_tags: list[:class:`huaweicloudsdkcdm.v1.SysTags`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, CdmClusterEnterpriseProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
