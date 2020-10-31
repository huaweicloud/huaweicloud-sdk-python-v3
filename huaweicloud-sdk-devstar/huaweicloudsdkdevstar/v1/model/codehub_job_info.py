# coding: utf-8

import pprint
import re

import six





class CodehubJobInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_name': 'str',
        'privately': 'bool',
        'short_id': 'str',
        'code_url': 'str',
        'region_id': 'str',
        'repo_type': 'int',
        'properties': 'object',
        'repo_info': 'RepositoryInfo'
    }

    attribute_map = {
        'application_name': 'application_name',
        'privately': 'privately',
        'short_id': 'short_id',
        'code_url': 'code_url',
        'region_id': 'region_id',
        'repo_type': 'repo_type',
        'properties': 'properties',
        'repo_info': 'repo_info'
    }

    def __init__(self, application_name=None, privately=True, short_id=None, code_url=None, region_id=None, repo_type=None, properties=None, repo_info=None):
        """CodehubJobInfo - a model defined in huaweicloud sdk"""
        
        

        self._application_name = None
        self._privately = None
        self._short_id = None
        self._code_url = None
        self._region_id = None
        self._repo_type = None
        self._properties = None
        self._repo_info = None
        self.discriminator = None

        self.application_name = application_name
        if privately is not None:
            self.privately = privately
        if short_id is not None:
            self.short_id = short_id
        if code_url is not None:
            self.code_url = code_url
        if region_id is not None:
            self.region_id = region_id
        if repo_type is not None:
            self.repo_type = repo_type
        if properties is not None:
            self.properties = properties
        if repo_info is not None:
            self.repo_info = repo_info

    @property
    def application_name(self):
        """Gets the application_name of this CodehubJobInfo.

        应用名称

        :return: The application_name of this CodehubJobInfo.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this CodehubJobInfo.

        应用名称

        :param application_name: The application_name of this CodehubJobInfo.
        :type: str
        """
        self._application_name = application_name

    @property
    def privately(self):
        """Gets the privately of this CodehubJobInfo.

        仓库是否私有

        :return: The privately of this CodehubJobInfo.
        :rtype: bool
        """
        return self._privately

    @privately.setter
    def privately(self, privately):
        """Sets the privately of this CodehubJobInfo.

        仓库是否私有

        :param privately: The privately of this CodehubJobInfo.
        :type: bool
        """
        self._privately = privately

    @property
    def short_id(self):
        """Gets the short_id of this CodehubJobInfo.

        仓库短id

        :return: The short_id of this CodehubJobInfo.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this CodehubJobInfo.

        仓库短id

        :param short_id: The short_id of this CodehubJobInfo.
        :type: str
        """
        self._short_id = short_id

    @property
    def code_url(self):
        """Gets the code_url of this CodehubJobInfo.

        代码存放的ssh地址

        :return: The code_url of this CodehubJobInfo.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this CodehubJobInfo.

        代码存放的ssh地址

        :param code_url: The code_url of this CodehubJobInfo.
        :type: str
        """
        self._code_url = code_url

    @property
    def region_id(self):
        """Gets the region_id of this CodehubJobInfo.

        区域id

        :return: The region_id of this CodehubJobInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CodehubJobInfo.

        区域id

        :param region_id: The region_id of this CodehubJobInfo.
        :type: str
        """
        self._region_id = region_id

    @property
    def repo_type(self):
        """Gets the repo_type of this CodehubJobInfo.

        应用代码生成后的地址类型，目前支持0：codehub地址; 1：压缩包下载地址

        :return: The repo_type of this CodehubJobInfo.
        :rtype: int
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this CodehubJobInfo.

        应用代码生成后的地址类型，目前支持0：codehub地址; 1：压缩包下载地址

        :param repo_type: The repo_type of this CodehubJobInfo.
        :type: int
        """
        self._repo_type = repo_type

    @property
    def properties(self):
        """Gets the properties of this CodehubJobInfo.

        应用的动态参数json

        :return: The properties of this CodehubJobInfo.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CodehubJobInfo.

        应用的动态参数json

        :param properties: The properties of this CodehubJobInfo.
        :type: object
        """
        self._properties = properties

    @property
    def repo_info(self):
        """Gets the repo_info of this CodehubJobInfo.


        :return: The repo_info of this CodehubJobInfo.
        :rtype: RepositoryInfo
        """
        return self._repo_info

    @repo_info.setter
    def repo_info(self, repo_info):
        """Sets the repo_info of this CodehubJobInfo.


        :param repo_info: The repo_info of this CodehubJobInfo.
        :type: RepositoryInfo
        """
        self._repo_info = repo_info

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
        if not isinstance(other, CodehubJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
