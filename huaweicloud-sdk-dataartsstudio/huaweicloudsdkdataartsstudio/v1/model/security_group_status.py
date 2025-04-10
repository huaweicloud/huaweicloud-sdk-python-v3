# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupStatus:

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
        'cluster_name': 'str',
        'security_group_name': 'str',
        'group_description': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'security_group_name': 'security_group_name',
        'group_description': 'group_description'
    }

    def __init__(self, cluster_id=None, cluster_name=None, security_group_name=None, group_description=None):
        r"""SecurityGroupStatus

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param security_group_name: 安全组名称
        :type security_group_name: str
        :param group_description: 风险说明
        :type group_description: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._security_group_name = None
        self._group_description = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if group_description is not None:
            self.group_description = group_description

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this SecurityGroupStatus.

        集群id

        :return: The cluster_id of this SecurityGroupStatus.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this SecurityGroupStatus.

        集群id

        :param cluster_id: The cluster_id of this SecurityGroupStatus.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this SecurityGroupStatus.

        集群名称

        :return: The cluster_name of this SecurityGroupStatus.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this SecurityGroupStatus.

        集群名称

        :param cluster_name: The cluster_name of this SecurityGroupStatus.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def security_group_name(self):
        r"""Gets the security_group_name of this SecurityGroupStatus.

        安全组名称

        :return: The security_group_name of this SecurityGroupStatus.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        r"""Sets the security_group_name of this SecurityGroupStatus.

        安全组名称

        :param security_group_name: The security_group_name of this SecurityGroupStatus.
        :type security_group_name: str
        """
        self._security_group_name = security_group_name

    @property
    def group_description(self):
        r"""Gets the group_description of this SecurityGroupStatus.

        风险说明

        :return: The group_description of this SecurityGroupStatus.
        :rtype: str
        """
        return self._group_description

    @group_description.setter
    def group_description(self, group_description):
        r"""Sets the group_description of this SecurityGroupStatus.

        风险说明

        :param group_description: The group_description of this SecurityGroupStatus.
        :type group_description: str
        """
        self._group_description = group_description

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
        if not isinstance(other, SecurityGroupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
