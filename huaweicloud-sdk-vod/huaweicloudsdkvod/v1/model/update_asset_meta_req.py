# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'tags': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'title': 'title',
        'description': 'description',
        'category_id': 'category_id',
        'tags': 'tags'
    }

    def __init__(self, asset_id=None, title=None, description=None, category_id=None, tags=None):
        """UpdateAssetMetaReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param title: 媒资标题，长度不超过128个字节，UTF-8编码。
        :type title: str
        :param description: 媒资描述，长度不超过1024个字节。
        :type description: str
        :param category_id: 媒资分类id。
        :type category_id: int
        :param tags: 媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF-8编码。
        :type tags: str
        """
        
        

        self._asset_id = None
        self._title = None
        self._description = None
        self._category_id = None
        self._tags = None
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

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateAssetMetaReq.

        媒资ID。

        :return: The asset_id of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateAssetMetaReq.

        媒资ID。

        :param asset_id: The asset_id of this UpdateAssetMetaReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def title(self):
        """Gets the title of this UpdateAssetMetaReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :return: The title of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateAssetMetaReq.

        媒资标题，长度不超过128个字节，UTF-8编码。

        :param title: The title of this UpdateAssetMetaReq.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateAssetMetaReq.

        媒资描述，长度不超过1024个字节。

        :return: The description of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAssetMetaReq.

        媒资描述，长度不超过1024个字节。

        :param description: The description of this UpdateAssetMetaReq.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this UpdateAssetMetaReq.

        媒资分类id。

        :return: The category_id of this UpdateAssetMetaReq.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this UpdateAssetMetaReq.

        媒资分类id。

        :param category_id: The category_id of this UpdateAssetMetaReq.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this UpdateAssetMetaReq.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF-8编码。

        :return: The tags of this UpdateAssetMetaReq.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateAssetMetaReq.

        媒资标签。  单个标签不超过16个字节，最多不超过16个标签。  多个用逗号分隔，UTF-8编码。

        :param tags: The tags of this UpdateAssetMetaReq.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, UpdateAssetMetaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
