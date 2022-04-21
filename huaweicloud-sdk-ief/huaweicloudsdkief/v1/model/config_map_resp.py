# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigMapResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'configs': 'dict(str, str)',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'configs': 'configs',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, configs=None, project_id=None, created_at=None, updated_at=None):
        """ConfigMapResp

        The model defined in huaweicloud sdk

        :param id: 配置项ID
        :type id: str
        :param name: 配置项名称
        :type name: str
        :param description: 配置项描述
        :type description: str
        :param configs: 配置项键列表
        :type configs: dict(str, str)
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._configs = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.configs = configs
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ConfigMapResp.

        配置项ID

        :return: The id of this ConfigMapResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigMapResp.

        配置项ID

        :param id: The id of this ConfigMapResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigMapResp.

        配置项名称

        :return: The name of this ConfigMapResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigMapResp.

        配置项名称

        :param name: The name of this ConfigMapResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConfigMapResp.

        配置项描述

        :return: The description of this ConfigMapResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigMapResp.

        配置项描述

        :param description: The description of this ConfigMapResp.
        :type description: str
        """
        self._description = description

    @property
    def configs(self):
        """Gets the configs of this ConfigMapResp.

        配置项键列表

        :return: The configs of this ConfigMapResp.
        :rtype: dict(str, str)
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ConfigMapResp.

        配置项键列表

        :param configs: The configs of this ConfigMapResp.
        :type configs: dict(str, str)
        """
        self._configs = configs

    @property
    def project_id(self):
        """Gets the project_id of this ConfigMapResp.

        项目ID

        :return: The project_id of this ConfigMapResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ConfigMapResp.

        项目ID

        :param project_id: The project_id of this ConfigMapResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this ConfigMapResp.

        创建时间

        :return: The created_at of this ConfigMapResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConfigMapResp.

        创建时间

        :param created_at: The created_at of this ConfigMapResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ConfigMapResp.

        更新时间

        :return: The updated_at of this ConfigMapResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ConfigMapResp.

        更新时间

        :param updated_at: The updated_at of this ConfigMapResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ConfigMapResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
