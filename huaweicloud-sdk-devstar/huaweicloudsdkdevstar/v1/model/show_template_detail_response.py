# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowTemplateDetailResponse(SdkResponse):


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
        'title': 'str',
        'description': 'str',
        'region_id': 'str',
        'repostory_id': 'str',
        'code_url': 'str',
        'ssh_url': 'str',
        'project_uuid': 'str',
        'status': 'int',
        'properties': 'list[PropertiesInfo]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'region_id': 'region_id',
        'repostory_id': 'repostory_id',
        'code_url': 'code_url',
        'ssh_url': 'ssh_url',
        'project_uuid': 'project_uuid',
        'status': 'status',
        'properties': 'properties'
    }

    def __init__(self, id=None, title=None, description=None, region_id=None, repostory_id=None, code_url=None, ssh_url=None, project_uuid=None, status=None, properties=None):
        """ShowTemplateDetailResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._id = None
        self._title = None
        self._description = None
        self._region_id = None
        self._repostory_id = None
        self._code_url = None
        self._ssh_url = None
        self._project_uuid = None
        self._status = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if region_id is not None:
            self.region_id = region_id
        if repostory_id is not None:
            self.repostory_id = repostory_id
        if code_url is not None:
            self.code_url = code_url
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if status is not None:
            self.status = status
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this ShowTemplateDetailResponse.

        模板的id

        :return: The id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowTemplateDetailResponse.

        模板的id

        :param id: The id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._id = id

    @property
    def title(self):
        """Gets the title of this ShowTemplateDetailResponse.

        模板的名称

        :return: The title of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowTemplateDetailResponse.

        模板的名称

        :param title: The title of this ShowTemplateDetailResponse.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this ShowTemplateDetailResponse.

        模板的描述信息

        :return: The description of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowTemplateDetailResponse.

        模板的描述信息

        :param description: The description of this ShowTemplateDetailResponse.
        :type: str
        """
        self._description = description

    @property
    def region_id(self):
        """Gets the region_id of this ShowTemplateDetailResponse.

        模板关联的region host id

        :return: The region_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowTemplateDetailResponse.

        模板关联的region host id

        :param region_id: The region_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._region_id = region_id

    @property
    def repostory_id(self):
        """Gets the repostory_id of this ShowTemplateDetailResponse.

        模板关联的repo id

        :return: The repostory_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._repostory_id

    @repostory_id.setter
    def repostory_id(self, repostory_id):
        """Sets the repostory_id of this ShowTemplateDetailResponse.

        模板关联的repo id

        :param repostory_id: The repostory_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._repostory_id = repostory_id

    @property
    def code_url(self):
        """Gets the code_url of this ShowTemplateDetailResponse.

        模板https下载路径

        :return: The code_url of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this ShowTemplateDetailResponse.

        模板https下载路径

        :param code_url: The code_url of this ShowTemplateDetailResponse.
        :type: str
        """
        self._code_url = code_url

    @property
    def ssh_url(self):
        """Gets the ssh_url of this ShowTemplateDetailResponse.

        模板ssh下载路径

        :return: The ssh_url of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this ShowTemplateDetailResponse.

        模板ssh下载路径

        :param ssh_url: The ssh_url of this ShowTemplateDetailResponse.
        :type: str
        """
        self._ssh_url = ssh_url

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ShowTemplateDetailResponse.

        项目id

        :return: The project_uuid of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ShowTemplateDetailResponse.

        项目id

        :param project_uuid: The project_uuid of this ShowTemplateDetailResponse.
        :type: str
        """
        self._project_uuid = project_uuid

    @property
    def status(self):
        """Gets the status of this ShowTemplateDetailResponse.

        模板状态

        :return: The status of this ShowTemplateDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowTemplateDetailResponse.

        模板状态

        :param status: The status of this ShowTemplateDetailResponse.
        :type: int
        """
        self._status = status

    @property
    def properties(self):
        """Gets the properties of this ShowTemplateDetailResponse.


        :return: The properties of this ShowTemplateDetailResponse.
        :rtype: list[PropertiesInfo]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShowTemplateDetailResponse.


        :param properties: The properties of this ShowTemplateDetailResponse.
        :type: list[PropertiesInfo]
        """
        self._properties = properties

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
        if not isinstance(other, ShowTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
