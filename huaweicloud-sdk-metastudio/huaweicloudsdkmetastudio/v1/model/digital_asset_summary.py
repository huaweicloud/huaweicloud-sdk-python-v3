# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DigitalAssetSummary:

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
        'asset_name': 'str',
        'asset_state': 'str',
        'asset_type': 'str',
        'cover_url': 'str',
        'thumbnail_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'asset_state': 'asset_state',
        'asset_type': 'asset_type',
        'cover_url': 'cover_url',
        'thumbnail_url': 'thumbnail_url'
    }

    def __init__(self, asset_id=None, asset_name=None, asset_state=None, asset_type=None, cover_url=None, thumbnail_url=None):
        r"""DigitalAssetSummary

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_state: 资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线
        :type asset_state: str
        :param asset_type: 资产类型。 公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板
        :type asset_type: str
        :param cover_url: 封面图片路径。
        :type cover_url: str
        :param thumbnail_url: 缩略图路径。
        :type thumbnail_url: str
        """
        
        

        self._asset_id = None
        self._asset_name = None
        self._asset_state = None
        self._asset_type = None
        self._cover_url = None
        self._thumbnail_url = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_state is not None:
            self.asset_state = asset_state
        if asset_type is not None:
            self.asset_type = asset_type
        if cover_url is not None:
            self.cover_url = cover_url
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DigitalAssetSummary.

        资产ID。

        :return: The asset_id of this DigitalAssetSummary.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DigitalAssetSummary.

        资产ID。

        :param asset_id: The asset_id of this DigitalAssetSummary.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this DigitalAssetSummary.

        资产名称。

        :return: The asset_name of this DigitalAssetSummary.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this DigitalAssetSummary.

        资产名称。

        :param asset_name: The asset_name of this DigitalAssetSummary.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_state(self):
        r"""Gets the asset_state of this DigitalAssetSummary.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线

        :return: The asset_state of this DigitalAssetSummary.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this DigitalAssetSummary.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。 * WAITING_DELETE：资产将被下线

        :param asset_state: The asset_state of this DigitalAssetSummary.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def asset_type(self):
        r"""Gets the asset_type of this DigitalAssetSummary.

        资产类型。 公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板

        :return: The asset_type of this DigitalAssetSummary.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this DigitalAssetSummary.

        资产类型。 公共资产类型： * VOICE_MODEL：音色模型（仅系统管理员可上传，普通租户仅可查询） * VIDEO：视频文件 * IMAGE：图片文件 * PPT：幻灯片文件 * MUSIC: 音乐 * AUDIO: 音频 * COMMON_FILE：通用文件  分身数字人资产： * HUMAN_MODEL_2D: 分身数字人模型 * BUSINESS_CARD_TEMPLET: 数字人名片模板

        :param asset_type: The asset_type of this DigitalAssetSummary.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def cover_url(self):
        r"""Gets the cover_url of this DigitalAssetSummary.

        封面图片路径。

        :return: The cover_url of this DigitalAssetSummary.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this DigitalAssetSummary.

        封面图片路径。

        :param cover_url: The cover_url of this DigitalAssetSummary.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def thumbnail_url(self):
        r"""Gets the thumbnail_url of this DigitalAssetSummary.

        缩略图路径。

        :return: The thumbnail_url of this DigitalAssetSummary.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        r"""Sets the thumbnail_url of this DigitalAssetSummary.

        缩略图路径。

        :param thumbnail_url: The thumbnail_url of this DigitalAssetSummary.
        :type thumbnail_url: str
        """
        self._thumbnail_url = thumbnail_url

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
        if not isinstance(other, DigitalAssetSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
