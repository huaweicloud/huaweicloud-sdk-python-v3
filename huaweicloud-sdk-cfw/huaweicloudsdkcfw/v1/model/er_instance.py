# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErInstance:

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
        'state': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'enable_ipv6': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'enable_ipv6': 'enable_ipv6'
    }

    def __init__(self, id=None, name=None, state=None, enterprise_project_id=None, project_id=None, enable_ipv6=None):
        """ErInstance

        The model defined in huaweicloud sdk

        :param id: Er实例id
        :type id: str
        :param name: Er名称
        :type name: str
        :param state: Er状态
        :type state: str
        :param enterprise_project_id: 企业租户id
        :type enterprise_project_id: str
        :param project_id: 租户id
        :type project_id: str
        :param enable_ipv6: 是否开启ipv6
        :type enable_ipv6: str
        """
        
        

        self._id = None
        self._name = None
        self._state = None
        self._enterprise_project_id = None
        self._project_id = None
        self._enable_ipv6 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if project_id is not None:
            self.project_id = project_id
        if enable_ipv6 is not None:
            self.enable_ipv6 = enable_ipv6

    @property
    def id(self):
        """Gets the id of this ErInstance.

        Er实例id

        :return: The id of this ErInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErInstance.

        Er实例id

        :param id: The id of this ErInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ErInstance.

        Er名称

        :return: The name of this ErInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ErInstance.

        Er名称

        :param name: The name of this ErInstance.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ErInstance.

        Er状态

        :return: The state of this ErInstance.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ErInstance.

        Er状态

        :param state: The state of this ErInstance.
        :type state: str
        """
        self._state = state

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ErInstance.

        企业租户id

        :return: The enterprise_project_id of this ErInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ErInstance.

        企业租户id

        :param enterprise_project_id: The enterprise_project_id of this ErInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ErInstance.

        租户id

        :return: The project_id of this ErInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ErInstance.

        租户id

        :param project_id: The project_id of this ErInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enable_ipv6(self):
        """Gets the enable_ipv6 of this ErInstance.

        是否开启ipv6

        :return: The enable_ipv6 of this ErInstance.
        :rtype: str
        """
        return self._enable_ipv6

    @enable_ipv6.setter
    def enable_ipv6(self, enable_ipv6):
        """Sets the enable_ipv6 of this ErInstance.

        是否开启ipv6

        :param enable_ipv6: The enable_ipv6 of this ErInstance.
        :type enable_ipv6: str
        """
        self._enable_ipv6 = enable_ipv6

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
        if not isinstance(other, ErInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
