# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationModify:

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
        'enterprise_project_id': 'str',
        'description': 'str',
        'labels': 'list[EnvironmentCreateLabels]'
    }

    attribute_map = {
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, name=None, enterprise_project_id=None, description=None, labels=None):
        """ApplicationModify

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param enterprise_project_id: 
        :type enterprise_project_id: str
        :param description: 
        :type description: str
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentCreateLabels`]
        """
        
        

        self._name = None
        self._enterprise_project_id = None
        self._description = None
        self._labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """Gets the name of this ApplicationModify.

        :return: The name of this ApplicationModify.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationModify.

        :param name: The name of this ApplicationModify.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ApplicationModify.

        :return: The enterprise_project_id of this ApplicationModify.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ApplicationModify.

        :param enterprise_project_id: The enterprise_project_id of this ApplicationModify.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        """Gets the description of this ApplicationModify.

        :return: The description of this ApplicationModify.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationModify.

        :param description: The description of this ApplicationModify.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ApplicationModify.

        :return: The labels of this ApplicationModify.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentCreateLabels`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ApplicationModify.

        :param labels: The labels of this ApplicationModify.
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
        if not isinstance(other, ApplicationModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
