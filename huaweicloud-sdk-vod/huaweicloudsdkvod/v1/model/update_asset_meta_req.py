# coding: utf-8

import pprint
import re

import six





class UpdateAssetMetaReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'title': 'str',
        'description': 'str',
        'category_id': 'int',
        'tags': 'str',
        'folder_name': 'str',
        'custom_metadata': 'dict(str, object)',
        'privilege': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'title': 'title',
        'description': 'description',
        'category_id': 'category_id',
        'tags': 'tags',
        'folder_name': 'folder_name',
        'custom_metadata': 'custom_metadata',
        'privilege': 'privilege'
    }

    def __init__(self, asset_id=None, title=None, description=None, category_id=None, tags=None, folder_name=None, custom_metadata=None, privilege=None):
        """UpdateAssetMetaReq - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._title = None
        self._description = None
        self._category_id = None
        self._tags = None
        self._folder_name = None
        self._custom_metadata = None
        self._privilege = None
        self.discriminator = None

        self.asset_id = asset_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if tags is not None:
            self.tags = tags
        if folder_name is not None:
            self.folder_name = folder_name
        if custom_metadata is not None:
            self.custom_metadata = custom_metadata
        if privilege is not None:
            self.privilege = privilege

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateAssetMetaReq.

        媒体ID<br/> 

        :return: The asset_id of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateAssetMetaReq.

        媒体ID<br/> 

        :param asset_id: The asset_id of this UpdateAssetMetaReq.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def title(self):
        """Gets the title of this UpdateAssetMetaReq.

        媒体标题<br/> 

        :return: The title of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateAssetMetaReq.

        媒体标题<br/> 

        :param title: The title of this UpdateAssetMetaReq.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateAssetMetaReq.

        视频描述<br/> 

        :return: The description of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAssetMetaReq.

        视频描述<br/> 

        :param description: The description of this UpdateAssetMetaReq.
        :type: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this UpdateAssetMetaReq.

        媒资分类id<br/> 

        :return: The category_id of this UpdateAssetMetaReq.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this UpdateAssetMetaReq.

        媒资分类id<br/> 

        :param category_id: The category_id of this UpdateAssetMetaReq.
        :type: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this UpdateAssetMetaReq.

        视频标签<br/> 

        :return: The tags of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateAssetMetaReq.

        视频标签<br/> 

        :param tags: The tags of this UpdateAssetMetaReq.
        :type: str
        """
        self._tags = tags

    @property
    def folder_name(self):
        """Gets the folder_name of this UpdateAssetMetaReq.

        媒资所在文件夹id

        :return: The folder_name of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this UpdateAssetMetaReq.

        媒资所在文件夹id

        :param folder_name: The folder_name of this UpdateAssetMetaReq.
        :type: str
        """
        self._folder_name = folder_name

    @property
    def custom_metadata(self):
        """Gets the custom_metadata of this UpdateAssetMetaReq.

        自定义元数据<br/> 

        :return: The custom_metadata of this UpdateAssetMetaReq.
        :rtype: dict(str, object)
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """Sets the custom_metadata of this UpdateAssetMetaReq.

        自定义元数据<br/> 

        :param custom_metadata: The custom_metadata of this UpdateAssetMetaReq.
        :type: dict(str, object)
        """
        self._custom_metadata = custom_metadata

    @property
    def privilege(self):
        """Gets the privilege of this UpdateAssetMetaReq.

        权限<br/> 

        :return: The privilege of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this UpdateAssetMetaReq.

        权限<br/> 

        :param privilege: The privilege of this UpdateAssetMetaReq.
        :type: str
        """
        self._privilege = privilege

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
        if not isinstance(other, UpdateAssetMetaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
