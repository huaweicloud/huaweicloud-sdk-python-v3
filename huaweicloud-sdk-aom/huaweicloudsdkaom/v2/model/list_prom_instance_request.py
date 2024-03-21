# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPromInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prom_id': 'str',
        'prom_type': 'str',
        'cce_cluster_enable': 'str',
        'prom_status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'prom_id': 'prom_id',
        'prom_type': 'prom_type',
        'cce_cluster_enable': 'cce_cluster_enable',
        'prom_status': 'prom_status',
        'enterprise_project_id': 'Enterprise-Project-Id'
    }

    def __init__(self, prom_id=None, prom_type=None, cce_cluster_enable=None, prom_status=None, enterprise_project_id=None):
        """ListPromInstanceRequest

        The model defined in huaweicloud sdk

        :param prom_id: Prometheus实例id(prom_id与prom_type同时存在时，仅prom_id生效)。
        :type prom_id: str
        :param prom_type: Prometheus实例类型（暂时不支持VPC、KUBERNETES）。
        :type prom_type: str
        :param cce_cluster_enable: cce集群开关。
        :type cce_cluster_enable: str
        :param prom_status: Prometheus实例状态。
        :type prom_status: str
        :param enterprise_project_id: 企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        """
        
        

        self._prom_id = None
        self._prom_type = None
        self._cce_cluster_enable = None
        self._prom_status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if prom_id is not None:
            self.prom_id = prom_id
        if prom_type is not None:
            self.prom_type = prom_type
        if cce_cluster_enable is not None:
            self.cce_cluster_enable = cce_cluster_enable
        if prom_status is not None:
            self.prom_status = prom_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def prom_id(self):
        """Gets the prom_id of this ListPromInstanceRequest.

        Prometheus实例id(prom_id与prom_type同时存在时，仅prom_id生效)。

        :return: The prom_id of this ListPromInstanceRequest.
        :rtype: str
        """
        return self._prom_id

    @prom_id.setter
    def prom_id(self, prom_id):
        """Sets the prom_id of this ListPromInstanceRequest.

        Prometheus实例id(prom_id与prom_type同时存在时，仅prom_id生效)。

        :param prom_id: The prom_id of this ListPromInstanceRequest.
        :type prom_id: str
        """
        self._prom_id = prom_id

    @property
    def prom_type(self):
        """Gets the prom_type of this ListPromInstanceRequest.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :return: The prom_type of this ListPromInstanceRequest.
        :rtype: str
        """
        return self._prom_type

    @prom_type.setter
    def prom_type(self, prom_type):
        """Sets the prom_type of this ListPromInstanceRequest.

        Prometheus实例类型（暂时不支持VPC、KUBERNETES）。

        :param prom_type: The prom_type of this ListPromInstanceRequest.
        :type prom_type: str
        """
        self._prom_type = prom_type

    @property
    def cce_cluster_enable(self):
        """Gets the cce_cluster_enable of this ListPromInstanceRequest.

        cce集群开关。

        :return: The cce_cluster_enable of this ListPromInstanceRequest.
        :rtype: str
        """
        return self._cce_cluster_enable

    @cce_cluster_enable.setter
    def cce_cluster_enable(self, cce_cluster_enable):
        """Sets the cce_cluster_enable of this ListPromInstanceRequest.

        cce集群开关。

        :param cce_cluster_enable: The cce_cluster_enable of this ListPromInstanceRequest.
        :type cce_cluster_enable: str
        """
        self._cce_cluster_enable = cce_cluster_enable

    @property
    def prom_status(self):
        """Gets the prom_status of this ListPromInstanceRequest.

        Prometheus实例状态。

        :return: The prom_status of this ListPromInstanceRequest.
        :rtype: str
        """
        return self._prom_status

    @prom_status.setter
    def prom_status(self, prom_status):
        """Sets the prom_status of this ListPromInstanceRequest.

        Prometheus实例状态。

        :param prom_status: The prom_status of this ListPromInstanceRequest.
        :type prom_status: str
        """
        self._prom_status = prom_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPromInstanceRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this ListPromInstanceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPromInstanceRequest.

        企业项目id。 - 查询单个企业项目下实例，填写企业项目id。 - 查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this ListPromInstanceRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListPromInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
