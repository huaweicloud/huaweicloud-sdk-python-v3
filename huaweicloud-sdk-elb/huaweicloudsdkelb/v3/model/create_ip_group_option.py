# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpGroupOption:

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
        'description': 'str',
        'name': 'str',
        'ip_list': 'list[CreateIpGroupIpOption]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'description': 'description',
        'name': 'name',
        'ip_list': 'ip_list',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, project_id=None, description=None, name=None, ip_list=None, enterprise_project_id=None):
        """CreateIpGroupOption

        The model defined in huaweicloud sdk

        :param project_id: IP地址组所在的项目ID。
        :type project_id: str
        :param description: IP地址组的描述。
        :type description: str
        :param name: IP地址组的名称。
        :type name: str
        :param ip_list: IP地址组中包含的IP或网段列表。[]表示任意IP。
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.CreateIpGroupIpOption`]
        :param enterprise_project_id: IP地址组所在的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: str
        """
        
        

        self._project_id = None
        self._description = None
        self._name = None
        self._ip_list = None
        self._enterprise_project_id = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        self.ip_list = ip_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateIpGroupOption.

        IP地址组所在的项目ID。

        :return: The project_id of this CreateIpGroupOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateIpGroupOption.

        IP地址组所在的项目ID。

        :param project_id: The project_id of this CreateIpGroupOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this CreateIpGroupOption.

        IP地址组的描述。

        :return: The description of this CreateIpGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIpGroupOption.

        IP地址组的描述。

        :param description: The description of this CreateIpGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateIpGroupOption.

        IP地址组的名称。

        :return: The name of this CreateIpGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIpGroupOption.

        IP地址组的名称。

        :param name: The name of this CreateIpGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def ip_list(self):
        """Gets the ip_list of this CreateIpGroupOption.

        IP地址组中包含的IP或网段列表。[]表示任意IP。

        :return: The ip_list of this CreateIpGroupOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CreateIpGroupIpOption`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this CreateIpGroupOption.

        IP地址组中包含的IP或网段列表。[]表示任意IP。

        :param ip_list: The ip_list of this CreateIpGroupOption.
        :type ip_list: list[:class:`huaweicloudsdkelb.v3.CreateIpGroupIpOption`]
        """
        self._ip_list = ip_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateIpGroupOption.

        IP地址组所在的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this CreateIpGroupOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateIpGroupOption.

        IP地址组所在的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this CreateIpGroupOption.
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
        if not isinstance(other, CreateIpGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
