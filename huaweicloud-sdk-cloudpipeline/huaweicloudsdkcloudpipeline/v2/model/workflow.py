# coding: utf-8

import pprint
import re

import six





class Workflow:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'parameter': 'PipelineParam',
        'source': 'Source',
        'name': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'parameter': 'parameter',
        'source': 'source',
        'name': 'name',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, parameter=None, source=None, name=None, project_id=None, project_name=None):
        """Workflow - a model defined in huaweicloud sdk"""
        
        

        self._parameter = None
        self._source = None
        self._name = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        self.parameter = parameter
        self.source = source
        self.name = name
        self.project_id = project_id
        self.project_name = project_name

    @property
    def parameter(self):
        """Gets the parameter of this Workflow.


        :return: The parameter of this Workflow.
        :rtype: PipelineParam
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this Workflow.


        :param parameter: The parameter of this Workflow.
        :type: PipelineParam
        """
        self._parameter = parameter

    @property
    def source(self):
        """Gets the source of this Workflow.


        :return: The source of this Workflow.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Workflow.


        :param source: The source of this Workflow.
        :type: Source
        """
        self._source = source

    @property
    def name(self):
        """Gets the name of this Workflow.

        流水线名字

        :return: The name of this Workflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workflow.

        流水线名字

        :param name: The name of this Workflow.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Workflow.

        项目ID

        :return: The project_id of this Workflow.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Workflow.

        项目ID

        :param project_id: The project_id of this Workflow.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this Workflow.

        项目名字

        :return: The project_name of this Workflow.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Workflow.

        项目名字

        :param project_name: The project_name of this Workflow.
        :type: str
        """
        self._project_name = project_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
