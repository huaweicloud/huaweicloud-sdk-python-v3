# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAgentDaemonsetRequest:

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
        'enterprise_project_id': 'str',
        'cluster_id': 'str',
        'invoked_service': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'cluster_id': 'cluster_id',
        'invoked_service': 'invoked_service'
    }

    def __init__(self, region=None, enterprise_project_id=None, cluster_id=None, invoked_service=None):
        """DeleteAgentDaemonsetRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param invoked_service: 调用服务,默认hss，cce集成防护调用场景使用，包括:    - hss： hss服务    - cce： cce服务，cce集成防护调用需要传参cce
        :type invoked_service: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._cluster_id = None
        self._invoked_service = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.cluster_id = cluster_id
        if invoked_service is not None:
            self.invoked_service = invoked_service

    @property
    def region(self):
        """Gets the region of this DeleteAgentDaemonsetRequest.

        Region ID

        :return: The region of this DeleteAgentDaemonsetRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DeleteAgentDaemonsetRequest.

        Region ID

        :param region: The region of this DeleteAgentDaemonsetRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DeleteAgentDaemonsetRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this DeleteAgentDaemonsetRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DeleteAgentDaemonsetRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this DeleteAgentDaemonsetRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteAgentDaemonsetRequest.

        集群id

        :return: The cluster_id of this DeleteAgentDaemonsetRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteAgentDaemonsetRequest.

        集群id

        :param cluster_id: The cluster_id of this DeleteAgentDaemonsetRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def invoked_service(self):
        """Gets the invoked_service of this DeleteAgentDaemonsetRequest.

        调用服务,默认hss，cce集成防护调用场景使用，包括:    - hss： hss服务    - cce： cce服务，cce集成防护调用需要传参cce

        :return: The invoked_service of this DeleteAgentDaemonsetRequest.
        :rtype: str
        """
        return self._invoked_service

    @invoked_service.setter
    def invoked_service(self, invoked_service):
        """Sets the invoked_service of this DeleteAgentDaemonsetRequest.

        调用服务,默认hss，cce集成防护调用场景使用，包括:    - hss： hss服务    - cce： cce服务，cce集成防护调用需要传参cce

        :param invoked_service: The invoked_service of this DeleteAgentDaemonsetRequest.
        :type invoked_service: str
        """
        self._invoked_service = invoked_service

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
        if not isinstance(other, DeleteAgentDaemonsetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
