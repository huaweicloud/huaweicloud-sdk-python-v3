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
        'repackage_mode': 'str',
        'delete_mode': 'str',
        'add_subtitles': 'list[AddSubtitle]',
        'delete_subtitles': 'list[DeleteSubtitle]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'default_language': 'default_language',
        'repackage_mode': 'repackage_mode',
        'delete_mode': 'delete_mode',
        'add_subtitles': 'add_subtitles',
        'delete_subtitles': 'delete_subtitles'
    }

    def __init__(self, asset_id=None, default_language=None, repackage_mode=None, delete_mode=None, add_subtitles=None, delete_subtitles=None):
        r"""SubtitleModifyReq

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID
        :type asset_id: str
        :param default_language: 字幕默认语言(字幕必须存在)
        :type default_language: str
        :param repackage_mode: 外挂模式，不传默认取值为0  取值如下： -0：表示添加的字幕会外挂上历史产物 -1：表示添加的字幕不会外挂上历史产物
        :type repackage_mode: str
        :param delete_mode: 删除模式，不传默认取值为0  取值如下： -0：表示删除字幕会清除历史产物携带的字幕信息 -1：表示删除字幕不清除历史产物携带的字幕信息
        :type delete_mode: str
        :param add_subtitles: 需新增或修改的字幕
        :type add_subtitles: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        :param delete_subtitles: 需删除的字幕，language不能与add_subtitles重复
        :type delete_subtitles: list[:class:`huaweicloudsdkvod.v1.DeleteSubtitle`]
        """
        
        

        self._asset_id = None
        self._default_language = None
        self._repackage_mode = None
        self._delete_mode = None
        self._add_subtitles = None
        self._delete_subtitles = None
        self.discriminator = None

        self.asset_id = asset_id
        if default_language is not None:
            self.default_language = default_language
        if repackage_mode is not None:
            self.repackage_mode = repackage_mode
        if delete_mode is not None:
            self.delete_mode = delete_mode
        if add_subtitles is not None:
            self.add_subtitles = add_subtitles
        if delete_subtitles is not None:
            self.delete_subtitles = delete_subtitles

    @property
    def asset_id(self):
        r"""Gets the asset_id of this SubtitleModifyReq.

        媒资ID

        :return: The asset_id of this SubtitleModifyReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this SubtitleModifyReq.

        媒资ID

        :param asset_id: The asset_id of this SubtitleModifyReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def default_language(self):
        r"""Gets the default_language of this SubtitleModifyReq.

        字幕默认语言(字幕必须存在)

        :return: The default_language of this SubtitleModifyReq.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        r"""Sets the default_language of this SubtitleModifyReq.

        字幕默认语言(字幕必须存在)

        :param default_language: The default_language of this SubtitleModifyReq.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def repackage_mode(self):
        r"""Gets the repackage_mode of this SubtitleModifyReq.

        外挂模式，不传默认取值为0  取值如下： -0：表示添加的字幕会外挂上历史产物 -1：表示添加的字幕不会外挂上历史产物

        :return: The repackage_mode of this SubtitleModifyReq.
        :rtype: str
        """
        return self._repackage_mode

    @repackage_mode.setter
    def repackage_mode(self, repackage_mode):
        r"""Sets the repackage_mode of this SubtitleModifyReq.

        外挂模式，不传默认取值为0  取值如下： -0：表示添加的字幕会外挂上历史产物 -1：表示添加的字幕不会外挂上历史产物

        :param repackage_mode: The repackage_mode of this SubtitleModifyReq.
        :type repackage_mode: str
        """
        self._repackage_mode = repackage_mode

    @property
    def delete_mode(self):
        r"""Gets the delete_mode of this SubtitleModifyReq.

        删除模式，不传默认取值为0  取值如下： -0：表示删除字幕会清除历史产物携带的字幕信息 -1：表示删除字幕不清除历史产物携带的字幕信息

        :return: The delete_mode of this SubtitleModifyReq.
        :rtype: str
        """
        return self._delete_mode

    @delete_mode.setter
    def delete_mode(self, delete_mode):
        r"""Sets the delete_mode of this SubtitleModifyReq.

        删除模式，不传默认取值为0  取值如下： -0：表示删除字幕会清除历史产物携带的字幕信息 -1：表示删除字幕不清除历史产物携带的字幕信息

        :param delete_mode: The delete_mode of this SubtitleModifyReq.
        :type delete_mode: str
        """
        self._delete_mode = delete_mode

    @property
    def add_subtitles(self):
        r"""Gets the add_subtitles of this SubtitleModifyReq.

        需新增或修改的字幕

        :return: The add_subtitles of this SubtitleModifyReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        """
        return self._add_subtitles

    @add_subtitles.setter
    def add_subtitles(self, add_subtitles):
        r"""Sets the add_subtitles of this SubtitleModifyReq.

        需新增或修改的字幕

        :param add_subtitles: The add_subtitles of this SubtitleModifyReq.
        :type add_subtitles: list[:class:`huaweicloudsdkvod.v1.AddSubtitle`]
        """
        self._add_subtitles = add_subtitles

    @property
    def delete_subtitles(self):
        r"""Gets the delete_subtitles of this SubtitleModifyReq.

        需删除的字幕，language不能与add_subtitles重复

        :return: The delete_subtitles of this SubtitleModifyReq.
        :rtype: list[:class:`huaweicloudsdkvod.v1.DeleteSubtitle`]
        """
        return self._delete_subtitles

    @delete_subtitles.setter
    def delete_subtitles(self, delete_subtitles):
        r"""Sets the delete_subtitles of this SubtitleModifyReq.

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
