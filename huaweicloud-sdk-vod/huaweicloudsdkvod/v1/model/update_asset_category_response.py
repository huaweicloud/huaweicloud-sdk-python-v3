# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateAssetCategoryResponse(SdkResponse):


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
        'parent_id': 'int',
        'id': 'int',
        'level': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id',
        'id': 'id',
        'level': 'level',
        'project_id': 'projectId'
    }

    def __init__(self, name=None, parent_id=None, id=None, level=None, project_id=None):
        """UpdateAssetCategoryResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateAssetCategoryResponse, self).__init__()

        self._name = None
        self._parent_id = None
        self._id = None
        self._level = None
        self._project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if project_id is not None:
            self.project_id = project_id

    @property
    def name(self):
        """Gets the name of this UpdateAssetCategoryResponse.

        视频分类名称<br/> 

        :return: The name of this UpdateAssetCategoryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAssetCategoryResponse.

        视频分类名称<br/> 

        :param name: The name of this UpdateAssetCategoryResponse.
        :type: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this UpdateAssetCategoryResponse.

        父分类ID<br/> 

        :return: The parent_id of this UpdateAssetCategoryResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this UpdateAssetCategoryResponse.

        父分类ID<br/> 

        :param parent_id: The parent_id of this UpdateAssetCategoryResponse.
        :type: int
        """
        self._parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this UpdateAssetCategoryResponse.

        视频分类ID<br/> 

        :return: The id of this UpdateAssetCategoryResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAssetCategoryResponse.

        视频分类ID<br/> 

        :param id: The id of this UpdateAssetCategoryResponse.
        :type: int
        """
        self._id = id

    @property
    def level(self):
        """Gets the level of this UpdateAssetCategoryResponse.

        视频分类层级<br/> 

        :return: The level of this UpdateAssetCategoryResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdateAssetCategoryResponse.

        视频分类层级<br/> 

        :param level: The level of this UpdateAssetCategoryResponse.
        :type: int
        """
        self._level = level

    @property
    def project_id(self):
        """Gets the project_id of this UpdateAssetCategoryResponse.


        :return: The project_id of this UpdateAssetCategoryResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateAssetCategoryResponse.


        :param project_id: The project_id of this UpdateAssetCategoryResponse.
        :type: str
        """
        self._project_id = project_id

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
        if not isinstance(other, UpdateAssetCategoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other