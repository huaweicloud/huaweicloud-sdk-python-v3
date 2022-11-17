# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentEdgecloud:

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
        'stacks': 'Stack',
        'description': 'str',
        'coverage': 'Coverage'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stacks': 'stacks',
        'description': 'description',
        'coverage': 'coverage'
    }

    def __init__(self, id=None, name=None, stacks=None, description=None, coverage=None):
        """DeploymentEdgecloud

        The model defined in huaweicloud sdk

        :param id: 边缘业务ID。
        :type id: str
        :param name: 边缘业务名称。
        :type name: str
        :param stacks: 
        :type stacks: :class:`huaweicloudsdkiec.v1.Stack`
        :param description: 边缘业务描述，最大支持255字节。
        :type description: str
        :param coverage: 
        :type coverage: :class:`huaweicloudsdkiec.v1.Coverage`
        """
        
        

        self._id = None
        self._name = None
        self._stacks = None
        self._description = None
        self._coverage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if stacks is not None:
            self.stacks = stacks
        if description is not None:
            self.description = description
        if coverage is not None:
            self.coverage = coverage

    @property
    def id(self):
        """Gets the id of this DeploymentEdgecloud.

        边缘业务ID。

        :return: The id of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentEdgecloud.

        边缘业务ID。

        :param id: The id of this DeploymentEdgecloud.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeploymentEdgecloud.

        边缘业务名称。

        :return: The name of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentEdgecloud.

        边缘业务名称。

        :param name: The name of this DeploymentEdgecloud.
        :type name: str
        """
        self._name = name

    @property
    def stacks(self):
        """Gets the stacks of this DeploymentEdgecloud.

        :return: The stacks of this DeploymentEdgecloud.
        :rtype: :class:`huaweicloudsdkiec.v1.Stack`
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        """Sets the stacks of this DeploymentEdgecloud.

        :param stacks: The stacks of this DeploymentEdgecloud.
        :type stacks: :class:`huaweicloudsdkiec.v1.Stack`
        """
        self._stacks = stacks

    @property
    def description(self):
        """Gets the description of this DeploymentEdgecloud.

        边缘业务描述，最大支持255字节。

        :return: The description of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentEdgecloud.

        边缘业务描述，最大支持255字节。

        :param description: The description of this DeploymentEdgecloud.
        :type description: str
        """
        self._description = description

    @property
    def coverage(self):
        """Gets the coverage of this DeploymentEdgecloud.

        :return: The coverage of this DeploymentEdgecloud.
        :rtype: :class:`huaweicloudsdkiec.v1.Coverage`
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this DeploymentEdgecloud.

        :param coverage: The coverage of this DeploymentEdgecloud.
        :type coverage: :class:`huaweicloudsdkiec.v1.Coverage`
        """
        self._coverage = coverage

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
        if not isinstance(other, DeploymentEdgecloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
