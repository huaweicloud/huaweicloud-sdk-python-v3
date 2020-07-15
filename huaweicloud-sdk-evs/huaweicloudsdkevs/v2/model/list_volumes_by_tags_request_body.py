# coding: utf-8

import pprint
import re

import six





class ListVolumesByTagsRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'limit': 'int',
        'matches': 'list[Match]',
        'offset': 'int',
        'tags': 'list[TagsForListVolumes]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'matches': 'matches',
        'offset': 'offset',
        'tags': 'tags'
    }

    def __init__(self, action='filter', limit=1000, matches=None, offset=0, tags=None):
        """ListVolumesByTagsRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._limit = None
        self._matches = None
        self._offset = None
        self._tags = None
        self.discriminator = None

        self.action = action
        if limit is not None:
            self.limit = limit
        if matches is not None:
            self.matches = matches
        if offset is not None:
            self.offset = offset
        self.tags = tags

    @property
    def action(self):
        """Gets the action of this ListVolumesByTagsRequestBody.

        操作标识。  根据标签查询云硬盘实例详情时使用“filter”。

        :return: The action of this ListVolumesByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListVolumesByTagsRequestBody.

        操作标识。  根据标签查询云硬盘实例详情时使用“filter”。

        :param action: The action of this ListVolumesByTagsRequestBody.
        :type: str
        """
        self._action = action

    @property
    def limit(self):
        """Gets the limit of this ListVolumesByTagsRequestBody.

        查询记录数。最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值

        :return: The limit of this ListVolumesByTagsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVolumesByTagsRequestBody.

        查询记录数。最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值

        :param limit: The limit of this ListVolumesByTagsRequestBody.
        :type: int
        """
        self._limit = limit

    @property
    def matches(self):
        """Gets the matches of this ListVolumesByTagsRequestBody.

        资源本身支持的查询条件。标签列表中的标签key值不允许重复。

        :return: The matches of this ListVolumesByTagsRequestBody.
        :rtype: list[Match]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListVolumesByTagsRequestBody.

        资源本身支持的查询条件。标签列表中的标签key值不允许重复。

        :param matches: The matches of this ListVolumesByTagsRequestBody.
        :type: list[Match]
        """
        self._matches = matches

    @property
    def offset(self):
        """Gets the offset of this ListVolumesByTagsRequestBody.

        索引位置。最小值0，默认为0。返回的结果中第一条记录为符合查询条件的第“offset值+1”条记录

        :return: The offset of this ListVolumesByTagsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVolumesByTagsRequestBody.

        索引位置。最小值0，默认为0。返回的结果中第一条记录为符合查询条件的第“offset值+1”条记录

        :param offset: The offset of this ListVolumesByTagsRequestBody.
        :type: int
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListVolumesByTagsRequestBody.

        标签的键值对。标签列表中最多包含10个key 。标签列表中的标签key值不允许重复。标签列表中多个key之间是“与”的关系，云硬盘必须满足请求中所有key才会匹配出来。

        :return: The tags of this ListVolumesByTagsRequestBody.
        :rtype: list[TagsForListVolumes]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListVolumesByTagsRequestBody.

        标签的键值对。标签列表中最多包含10个key 。标签列表中的标签key值不允许重复。标签列表中多个key之间是“与”的关系，云硬盘必须满足请求中所有key才会匹配出来。

        :param tags: The tags of this ListVolumesByTagsRequestBody.
        :type: list[TagsForListVolumes]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListVolumesByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
