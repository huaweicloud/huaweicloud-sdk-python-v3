# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'name': 'str',
        'deploy_type': 'int',
        'os': 'str',
        'description': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'deploy_type': 'deploy_type',
        'os': 'os',
        'description': 'description'
    }

    def __init__(self, project_id=None, name=None, deploy_type=None, os=None, description=None):
        r"""EnvironmentRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param name: 环境名称
        :type name: str
        :param deploy_type: 部署类型：0表示主机, 1表示kubernetes
        :type deploy_type: int
        :param os: 操作系统：windows|linux，需要和主机集群保持一致
        :type os: str
        :param description: 环境描述
        :type description: str
        """
        
        

        self._project_id = None
        self._name = None
        self._deploy_type = None
        self._os = None
        self._description = None
        self.discriminator = None

        self.project_id = project_id
        self.name = name
        self.deploy_type = deploy_type
        self.os = os
        if description is not None:
            self.description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this EnvironmentRequestBody.

        项目id

        :return: The project_id of this EnvironmentRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EnvironmentRequestBody.

        项目id

        :param project_id: The project_id of this EnvironmentRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this EnvironmentRequestBody.

        环境名称

        :return: The name of this EnvironmentRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvironmentRequestBody.

        环境名称

        :param name: The name of this EnvironmentRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this EnvironmentRequestBody.

        部署类型：0表示主机, 1表示kubernetes

        :return: The deploy_type of this EnvironmentRequestBody.
        :rtype: int
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this EnvironmentRequestBody.

        部署类型：0表示主机, 1表示kubernetes

        :param deploy_type: The deploy_type of this EnvironmentRequestBody.
        :type deploy_type: int
        """
        self._deploy_type = deploy_type

    @property
    def os(self):
        r"""Gets the os of this EnvironmentRequestBody.

        操作系统：windows|linux，需要和主机集群保持一致

        :return: The os of this EnvironmentRequestBody.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this EnvironmentRequestBody.

        操作系统：windows|linux，需要和主机集群保持一致

        :param os: The os of this EnvironmentRequestBody.
        :type os: str
        """
        self._os = os

    @property
    def description(self):
        r"""Gets the description of this EnvironmentRequestBody.

        环境描述

        :return: The description of this EnvironmentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EnvironmentRequestBody.

        环境描述

        :param description: The description of this EnvironmentRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, EnvironmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
