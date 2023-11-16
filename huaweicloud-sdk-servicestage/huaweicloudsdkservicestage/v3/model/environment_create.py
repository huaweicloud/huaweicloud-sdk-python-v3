# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentCreate:

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
        'description': 'str',
        'enterprise_project_id': 'str',
        'vpc_id': 'str',
        'deploy_mode': 'str',
        'labels': 'list[EnvironmentCreateLabels]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'vpc_id': 'vpc_id',
        'deploy_mode': 'deploy_mode',
        'labels': 'labels'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None, vpc_id=None, deploy_mode=None, labels=None):
        """EnvironmentCreate

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param enterprise_project_id: 
        :type enterprise_project_id: str
        :param vpc_id: 
        :type vpc_id: str
        :param deploy_mode: 
        :type deploy_mode: str
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentCreateLabels`]
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._vpc_id = None
        self._deploy_mode = None
        self._labels = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.vpc_id = vpc_id
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """Gets the name of this EnvironmentCreate.

        :return: The name of this EnvironmentCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentCreate.

        :param name: The name of this EnvironmentCreate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EnvironmentCreate.

        :return: The description of this EnvironmentCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvironmentCreate.

        :param description: The description of this EnvironmentCreate.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EnvironmentCreate.

        :return: The enterprise_project_id of this EnvironmentCreate.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EnvironmentCreate.

        :param enterprise_project_id: The enterprise_project_id of this EnvironmentCreate.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EnvironmentCreate.

        :return: The vpc_id of this EnvironmentCreate.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EnvironmentCreate.

        :param vpc_id: The vpc_id of this EnvironmentCreate.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def deploy_mode(self):
        """Gets the deploy_mode of this EnvironmentCreate.

        :return: The deploy_mode of this EnvironmentCreate.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        """Sets the deploy_mode of this EnvironmentCreate.

        :param deploy_mode: The deploy_mode of this EnvironmentCreate.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def labels(self):
        """Gets the labels of this EnvironmentCreate.

        :return: The labels of this EnvironmentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentCreateLabels`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this EnvironmentCreate.

        :param labels: The labels of this EnvironmentCreate.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentCreateLabels`]
        """
        self._labels = labels

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
        if not isinstance(other, EnvironmentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
