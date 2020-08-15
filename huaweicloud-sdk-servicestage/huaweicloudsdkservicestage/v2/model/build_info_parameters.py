# coding: utf-8

import pprint
import re

import six





class BuildInfoParameters:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'build_cmd': 'str',
        'dockerfile_path': 'str',
        'artifact_namespace': 'str'
    }

    attribute_map = {
        'build_cmd': 'build_cmd',
        'dockerfile_path': 'dockerfile_path',
        'artifact_namespace': 'artifact_namespace'
    }

    def __init__(self, build_cmd=None, dockerfile_path=None, artifact_namespace=None):
        """BuildInfoParameters - a model defined in huaweicloud sdk"""
        
        

        self._build_cmd = None
        self._dockerfile_path = None
        self._artifact_namespace = None
        self.discriminator = None

        if build_cmd is not None:
            self.build_cmd = build_cmd
        if dockerfile_path is not None:
            self.dockerfile_path = dockerfile_path
        if artifact_namespace is not None:
            self.artifact_namespace = artifact_namespace

    @property
    def build_cmd(self):
        """Gets the build_cmd of this BuildInfoParameters.

        编译命令。默认：  1、根目录存在build.sh：./build.sh  2、根据运行系统，示例如下：  Java和Tomcat：mvn clean package  Nodejs: npm build 

        :return: The build_cmd of this BuildInfoParameters.
        :rtype: str
        """
        return self._build_cmd

    @build_cmd.setter
    def build_cmd(self, build_cmd):
        """Sets the build_cmd of this BuildInfoParameters.

        编译命令。默认：  1、根目录存在build.sh：./build.sh  2、根据运行系统，示例如下：  Java和Tomcat：mvn clean package  Nodejs: npm build 

        :param build_cmd: The build_cmd of this BuildInfoParameters.
        :type: str
        """
        self._build_cmd = build_cmd

    @property
    def dockerfile_path(self):
        """Gets the dockerfile_path of this BuildInfoParameters.

        dockerfile地址。默认是根目录./。

        :return: The dockerfile_path of this BuildInfoParameters.
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        """Sets the dockerfile_path of this BuildInfoParameters.

        dockerfile地址。默认是根目录./。

        :param dockerfile_path: The dockerfile_path of this BuildInfoParameters.
        :type: str
        """
        self._dockerfile_path = dockerfile_path

    @property
    def artifact_namespace(self):
        """Gets the artifact_namespace of this BuildInfoParameters.

        构建归档组织，默认cas_{project_id}。

        :return: The artifact_namespace of this BuildInfoParameters.
        :rtype: str
        """
        return self._artifact_namespace

    @artifact_namespace.setter
    def artifact_namespace(self, artifact_namespace):
        """Sets the artifact_namespace of this BuildInfoParameters.

        构建归档组织，默认cas_{project_id}。

        :param artifact_namespace: The artifact_namespace of this BuildInfoParameters.
        :type: str
        """
        self._artifact_namespace = artifact_namespace

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
        if not isinstance(other, BuildInfoParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
