# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptData:

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
        'config': 'list[EncryptDataItem]',
        'project_id': 'str',
        'ief_instance_id': 'str',
        'domain_id': 'str',
        'created_time': 'int',
        'updated_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'config': 'config',
        'project_id': 'project_id',
        'ief_instance_id': 'ief_instance_id',
        'domain_id': 'domain_id',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, description=None, config=None, project_id=None, ief_instance_id=None, domain_id=None, created_time=None, updated_time=None):
        """EncryptData

        The model defined in huaweicloud sdk

        :param id: 加密数据ID
        :type id: str
        :param name: 加密数据名称
        :type name: str
        :param description: 加密数据描述
        :type description: str
        :param config: 加密数据项配置
        :type config: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        :param project_id: 项目ID
        :type project_id: str
        :param ief_instance_id: 铂金版实例ID，专业版实例为default
        :type ief_instance_id: str
        :param domain_id: 租户账户ID
        :type domain_id: str
        :param created_time: 加密数据创建时间
        :type created_time: int
        :param updated_time: 加密数据更新时间
        :type updated_time: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._config = None
        self._project_id = None
        self._ief_instance_id = None
        self._domain_id = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.config = config
        if project_id is not None:
            self.project_id = project_id
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if domain_id is not None:
            self.domain_id = domain_id
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        """Gets the id of this EncryptData.

        加密数据ID

        :return: The id of this EncryptData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EncryptData.

        加密数据ID

        :param id: The id of this EncryptData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EncryptData.

        加密数据名称

        :return: The name of this EncryptData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EncryptData.

        加密数据名称

        :param name: The name of this EncryptData.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EncryptData.

        加密数据描述

        :return: The description of this EncryptData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EncryptData.

        加密数据描述

        :param description: The description of this EncryptData.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        """Gets the config of this EncryptData.

        加密数据项配置

        :return: The config of this EncryptData.
        :rtype: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this EncryptData.

        加密数据项配置

        :param config: The config of this EncryptData.
        :type config: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        """
        self._config = config

    @property
    def project_id(self):
        """Gets the project_id of this EncryptData.

        项目ID

        :return: The project_id of this EncryptData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EncryptData.

        项目ID

        :param project_id: The project_id of this EncryptData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this EncryptData.

        铂金版实例ID，专业版实例为default

        :return: The ief_instance_id of this EncryptData.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this EncryptData.

        铂金版实例ID，专业版实例为default

        :param ief_instance_id: The ief_instance_id of this EncryptData.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def domain_id(self):
        """Gets the domain_id of this EncryptData.

        租户账户ID

        :return: The domain_id of this EncryptData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this EncryptData.

        租户账户ID

        :param domain_id: The domain_id of this EncryptData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def created_time(self):
        """Gets the created_time of this EncryptData.

        加密数据创建时间

        :return: The created_time of this EncryptData.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EncryptData.

        加密数据创建时间

        :param created_time: The created_time of this EncryptData.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this EncryptData.

        加密数据更新时间

        :return: The updated_time of this EncryptData.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this EncryptData.

        加密数据更新时间

        :param updated_time: The updated_time of this EncryptData.
        :type updated_time: int
        """
        self._updated_time = updated_time

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
        if not isinstance(other, EncryptData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
