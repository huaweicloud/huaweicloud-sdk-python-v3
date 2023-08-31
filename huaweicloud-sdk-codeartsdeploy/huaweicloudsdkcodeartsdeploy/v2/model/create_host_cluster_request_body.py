# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHostClusterRequestBody:

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
        'project_id': 'str',
        'os': 'str',
        'slave_cluster_id': 'str',
        'description': 'str',
        'is_proxy_mode': 'int'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'os': 'os',
        'slave_cluster_id': 'slave_cluster_id',
        'description': 'description',
        'is_proxy_mode': 'is_proxy_mode'
    }

    def __init__(self, name=None, project_id=None, os=None, slave_cluster_id=None, description=None, is_proxy_mode=None):
        """CreateHostClusterRequestBody

        The model defined in huaweicloud sdk

        :param name: 主机集群名
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param os: 操作系统：windows|linux
        :type os: str
        :param slave_cluster_id: slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id
        :type slave_cluster_id: str
        :param description: 描述
        :type description: str
        :param is_proxy_mode: 主机集群是否为代理机接入模式， 1：是 0：否
        :type is_proxy_mode: int
        """
        
        

        self._name = None
        self._project_id = None
        self._os = None
        self._slave_cluster_id = None
        self._description = None
        self._is_proxy_mode = None
        self.discriminator = None

        self.name = name
        self.project_id = project_id
        self.os = os
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if description is not None:
            self.description = description
        self.is_proxy_mode = is_proxy_mode

    @property
    def name(self):
        """Gets the name of this CreateHostClusterRequestBody.

        主机集群名

        :return: The name of this CreateHostClusterRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateHostClusterRequestBody.

        主机集群名

        :param name: The name of this CreateHostClusterRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateHostClusterRequestBody.

        项目ID

        :return: The project_id of this CreateHostClusterRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateHostClusterRequestBody.

        项目ID

        :param project_id: The project_id of this CreateHostClusterRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def os(self):
        """Gets the os of this CreateHostClusterRequestBody.

        操作系统：windows|linux

        :return: The os of this CreateHostClusterRequestBody.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this CreateHostClusterRequestBody.

        操作系统：windows|linux

        :param os: The os of this CreateHostClusterRequestBody.
        :type os: str
        """
        self._os = os

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this CreateHostClusterRequestBody.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :return: The slave_cluster_id of this CreateHostClusterRequestBody.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this CreateHostClusterRequestBody.

        slave集群id，默认为null时使用默认slave集群，用户自定义slave时为slave集群id

        :param slave_cluster_id: The slave_cluster_id of this CreateHostClusterRequestBody.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def description(self):
        """Gets the description of this CreateHostClusterRequestBody.

        描述

        :return: The description of this CreateHostClusterRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateHostClusterRequestBody.

        描述

        :param description: The description of this CreateHostClusterRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def is_proxy_mode(self):
        """Gets the is_proxy_mode of this CreateHostClusterRequestBody.

        主机集群是否为代理机接入模式， 1：是 0：否

        :return: The is_proxy_mode of this CreateHostClusterRequestBody.
        :rtype: int
        """
        return self._is_proxy_mode

    @is_proxy_mode.setter
    def is_proxy_mode(self, is_proxy_mode):
        """Sets the is_proxy_mode of this CreateHostClusterRequestBody.

        主机集群是否为代理机接入模式， 1：是 0：否

        :param is_proxy_mode: The is_proxy_mode of this CreateHostClusterRequestBody.
        :type is_proxy_mode: int
        """
        self._is_proxy_mode = is_proxy_mode

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
        if not isinstance(other, CreateHostClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
