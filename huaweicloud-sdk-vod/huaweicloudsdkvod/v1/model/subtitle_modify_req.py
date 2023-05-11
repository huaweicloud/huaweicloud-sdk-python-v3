# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleModifyReq:

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
        'default_language': 'str',
        'add_subtitles': 'list[AddSubtitle]',
        'delete_subtitles': 'list[DeleteSubtitle]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'default_language': 'default_language',
        'add_subtitles': 'add_subtitles',
        'delete_subtitles': 'delete_subtitles'
    }

    def __init__(self, asset_id=None, default_language=None, add_subtitles=None, delete_subtitles=None):
        """SubtitleModifyReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID
        :type asset_id: str
        :param default_language: 字幕默认语言(字幕必须存在)
        :type default_language: str
        :param add_subtitles: 需新增或修改的字幕
        :type add_subtitles: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        :param delete_subtitles: 需删除的字幕，language不能与add_subtitles重复
        :type delete_subtitles: list[:class:`huaweicloudsdkvod.v1.DeleteSubtitle`]
        """
        
        

        self._asset_id = None
        self._default_language = None
        self._add_subtitles = None
        self._delete_subtitles = None
        self.discriminator = None

        self.asset_id = asset_id
        if default_language is not None:
            self.default_language = default_language
        if add_subtitles is not None:
            self.add_subtitles = add_subtitles
        if delete_subtitles is not None:
            self.delete_subtitles = delete_subtitles

    @property
    def asset_id(self):
        """Gets the asset_id of this SubtitleModifyReq.

        媒资ID

        :return: The asset_id of this SubtitleModifyReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this SubtitleModifyReq.

        媒资ID

        :param asset_id: The asset_id of this SubtitleModifyReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def default_language(self):
        """Gets the default_language of this SubtitleModifyReq.

        字幕默认语言(字幕必须存在)

        :return: The default_language of this SubtitleModifyReq.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """Sets the default_language of this SubtitleModifyReq.

        字幕默认语言(字幕必须存在)

        :param default_language: The default_language of this SubtitleModifyReq.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def add_subtitles(self):
        """Gets the add_subtitles of this SubtitleModifyReq.

        需新增或修改的字幕

        :return: The add_subtitles of this SubtitleModifyReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        """
        return self._add_subtitles

    @add_subtitles.setter
    def add_subtitles(self, add_subtitles):
        """Sets the add_subtitles of this SubtitleModifyReq.

        需新增或修改的字幕

        :param add_subtitles: The add_subtitles of this SubtitleModifyReq.
        :type add_subtitles: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        """
        self._add_subtitles = add_subtitles

    @property
    def delete_subtitles(self):
        """Gets the delete_subtitles of this SubtitleModifyReq.

        需删除的字幕，language不能与add_subtitles重复

        :return: The delete_subtitles of this SubtitleModifyReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.DeleteSubtitle`]
        """
        return self._delete_subtitles

    @delete_subtitles.setter
    def delete_subtitles(self, delete_subtitles):
        """Sets the delete_subtitles of this SubtitleModifyReq.

        需删除的字幕，language不能与add_subtitles重复

        :param delete_subtitles: The delete_subtitles of this SubtitleModifyReq.
        :type delete_subtitles: list[:class:`huaweicloudsdkvod.v1.DeleteSubtitle`]
        """
        self._delete_subtitles = delete_subtitles

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
        if not isinstance(other, SubtitleModifyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
