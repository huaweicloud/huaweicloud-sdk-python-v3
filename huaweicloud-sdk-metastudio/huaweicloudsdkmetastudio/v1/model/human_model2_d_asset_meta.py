# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HumanModel2DAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_action_editable': 'bool',
        'is_live_copy': 'bool',
        'is_real_background': 'bool',
        'support_live': 'bool',
        'model_version': 'str',
        'model_resolution': 'str',
        'device_names': 'list[str]',
        'is_with_action_library': 'bool',
        'action_tag_map': 'list[ActionTagInfo]',
        'is_flexus': 'bool',
        'voice_asset_id': 'str'
    }

    attribute_map = {
        'is_action_editable': 'is_action_editable',
        'is_live_copy': 'is_live_copy',
        'is_real_background': 'is_real_background',
        'support_live': 'support_live',
        'model_version': 'model_version',
        'model_resolution': 'model_resolution',
        'device_names': 'device_names',
        'is_with_action_library': 'is_with_action_library',
        'action_tag_map': 'action_tag_map',
        'is_flexus': 'is_flexus',
        'voice_asset_id': 'voice_asset_id'
    }

    def __init__(self, is_action_editable=None, is_live_copy=None, is_real_background=None, support_live=None, model_version=None, model_resolution=None, device_names=None, is_with_action_library=None, action_tag_map=None, is_flexus=None, voice_asset_id=None):
        r"""HumanModel2DAssetMeta

        The model defined in huaweicloud sdk

        :param is_action_editable: **参数解释**： 分身数字人的动作是否可编辑 **约束限制**： 不涉及 **取值范围**： * true: 动作可编辑 * false: 动作不可编辑
        :type is_action_editable: bool
        :param is_live_copy: **参数解释**： 是否是直播间复刻任务 **约束限制**： 不涉及 **取值范围**： * true: 是直播间复刻任务 * false: 不是直播间复刻任务
        :type is_live_copy: bool
        :param is_real_background: **参数解释**： 是否是实景分身数字人 **约束限制**： 实景分身数字人不做背景替换。 **取值范围**： * true: 实景分身数字人 * false: 普通分身数字人，不带背景。
        :type is_real_background: bool
        :param support_live: **参数解释**： 是否支持直播 **约束限制**： 不涉及 **取值范围**： * true: 支持直播 * false: 不支持直播。
        :type support_live: bool
        :param model_version: **参数解释**： 分身数字人模型版本 **约束限制**： 不涉及 **取值范围**： * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型 * V3_3：V3.3版本模型
        :type model_version: str
        :param model_resolution: **参数解释**： 分身数字人模型分辨率。 **约束限制**： 不涉及 **取值范围**： * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。
        :type model_resolution: str
        :param device_names: **参数解释**： 已执行编译任务设备类型列表。 **约束限制**： 支持走动的数字人，当前仅用于视频制作，不能用于直播和智能交互 **取值范围**： 设备名称列表最多16个。 设备名称字符长度1-64位。 **默认取值**： false
        :type device_names: list[str]
        :param is_with_action_library: 分身数字人是否带原子动作库。 &gt; * 带原子动作库的分身数字人可做动作编排。
        :type is_with_action_library: bool
        :param action_tag_map: 动作标签映射。
        :type action_tag_map: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        :param is_flexus: 是否是Flexus版本分身数字人。
        :type is_flexus: bool
        :param voice_asset_id: 形象关联的声音资产ID。
        :type voice_asset_id: str
        """
        
        

        self._is_action_editable = None
        self._is_live_copy = None
        self._is_real_background = None
        self._support_live = None
        self._model_version = None
        self._model_resolution = None
        self._device_names = None
        self._is_with_action_library = None
        self._action_tag_map = None
        self._is_flexus = None
        self._voice_asset_id = None
        self.discriminator = None

        if is_action_editable is not None:
            self.is_action_editable = is_action_editable
        if is_live_copy is not None:
            self.is_live_copy = is_live_copy
        if is_real_background is not None:
            self.is_real_background = is_real_background
        if support_live is not None:
            self.support_live = support_live
        if model_version is not None:
            self.model_version = model_version
        if model_resolution is not None:
            self.model_resolution = model_resolution
        if device_names is not None:
            self.device_names = device_names
        if is_with_action_library is not None:
            self.is_with_action_library = is_with_action_library
        if action_tag_map is not None:
            self.action_tag_map = action_tag_map
        if is_flexus is not None:
            self.is_flexus = is_flexus
        if voice_asset_id is not None:
            self.voice_asset_id = voice_asset_id

    @property
    def is_action_editable(self):
        r"""Gets the is_action_editable of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人的动作是否可编辑 **约束限制**： 不涉及 **取值范围**： * true: 动作可编辑 * false: 动作不可编辑

        :return: The is_action_editable of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_action_editable

    @is_action_editable.setter
    def is_action_editable(self, is_action_editable):
        r"""Sets the is_action_editable of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人的动作是否可编辑 **约束限制**： 不涉及 **取值范围**： * true: 动作可编辑 * false: 动作不可编辑

        :param is_action_editable: The is_action_editable of this HumanModel2DAssetMeta.
        :type is_action_editable: bool
        """
        self._is_action_editable = is_action_editable

    @property
    def is_live_copy(self):
        r"""Gets the is_live_copy of this HumanModel2DAssetMeta.

        **参数解释**： 是否是直播间复刻任务 **约束限制**： 不涉及 **取值范围**： * true: 是直播间复刻任务 * false: 不是直播间复刻任务

        :return: The is_live_copy of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_live_copy

    @is_live_copy.setter
    def is_live_copy(self, is_live_copy):
        r"""Sets the is_live_copy of this HumanModel2DAssetMeta.

        **参数解释**： 是否是直播间复刻任务 **约束限制**： 不涉及 **取值范围**： * true: 是直播间复刻任务 * false: 不是直播间复刻任务

        :param is_live_copy: The is_live_copy of this HumanModel2DAssetMeta.
        :type is_live_copy: bool
        """
        self._is_live_copy = is_live_copy

    @property
    def is_real_background(self):
        r"""Gets the is_real_background of this HumanModel2DAssetMeta.

        **参数解释**： 是否是实景分身数字人 **约束限制**： 实景分身数字人不做背景替换。 **取值范围**： * true: 实景分身数字人 * false: 普通分身数字人，不带背景。

        :return: The is_real_background of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_real_background

    @is_real_background.setter
    def is_real_background(self, is_real_background):
        r"""Sets the is_real_background of this HumanModel2DAssetMeta.

        **参数解释**： 是否是实景分身数字人 **约束限制**： 实景分身数字人不做背景替换。 **取值范围**： * true: 实景分身数字人 * false: 普通分身数字人，不带背景。

        :param is_real_background: The is_real_background of this HumanModel2DAssetMeta.
        :type is_real_background: bool
        """
        self._is_real_background = is_real_background

    @property
    def support_live(self):
        r"""Gets the support_live of this HumanModel2DAssetMeta.

        **参数解释**： 是否支持直播 **约束限制**： 不涉及 **取值范围**： * true: 支持直播 * false: 不支持直播。

        :return: The support_live of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._support_live

    @support_live.setter
    def support_live(self, support_live):
        r"""Sets the support_live of this HumanModel2DAssetMeta.

        **参数解释**： 是否支持直播 **约束限制**： 不涉及 **取值范围**： * true: 支持直播 * false: 不支持直播。

        :param support_live: The support_live of this HumanModel2DAssetMeta.
        :type support_live: bool
        """
        self._support_live = support_live

    @property
    def model_version(self):
        r"""Gets the model_version of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人模型版本 **约束限制**： 不涉及 **取值范围**： * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型 * V3_3：V3.3版本模型

        :return: The model_version of this HumanModel2DAssetMeta.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        r"""Sets the model_version of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人模型版本 **约束限制**： 不涉及 **取值范围**： * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型 * V3_3：V3.3版本模型

        :param model_version: The model_version of this HumanModel2DAssetMeta.
        :type model_version: str
        """
        self._model_version = model_version

    @property
    def model_resolution(self):
        r"""Gets the model_resolution of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人模型分辨率。 **约束限制**： 不涉及 **取值范围**： * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :return: The model_resolution of this HumanModel2DAssetMeta.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        r"""Sets the model_resolution of this HumanModel2DAssetMeta.

        **参数解释**： 分身数字人模型分辨率。 **约束限制**： 不涉及 **取值范围**： * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :param model_resolution: The model_resolution of this HumanModel2DAssetMeta.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def device_names(self):
        r"""Gets the device_names of this HumanModel2DAssetMeta.

        **参数解释**： 已执行编译任务设备类型列表。 **约束限制**： 支持走动的数字人，当前仅用于视频制作，不能用于直播和智能交互 **取值范围**： 设备名称列表最多16个。 设备名称字符长度1-64位。 **默认取值**： false

        :return: The device_names of this HumanModel2DAssetMeta.
        :rtype: list[str]
        """
        return self._device_names

    @device_names.setter
    def device_names(self, device_names):
        r"""Sets the device_names of this HumanModel2DAssetMeta.

        **参数解释**： 已执行编译任务设备类型列表。 **约束限制**： 支持走动的数字人，当前仅用于视频制作，不能用于直播和智能交互 **取值范围**： 设备名称列表最多16个。 设备名称字符长度1-64位。 **默认取值**： false

        :param device_names: The device_names of this HumanModel2DAssetMeta.
        :type device_names: list[str]
        """
        self._device_names = device_names

    @property
    def is_with_action_library(self):
        r"""Gets the is_with_action_library of this HumanModel2DAssetMeta.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :return: The is_with_action_library of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_with_action_library

    @is_with_action_library.setter
    def is_with_action_library(self, is_with_action_library):
        r"""Sets the is_with_action_library of this HumanModel2DAssetMeta.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :param is_with_action_library: The is_with_action_library of this HumanModel2DAssetMeta.
        :type is_with_action_library: bool
        """
        self._is_with_action_library = is_with_action_library

    @property
    def action_tag_map(self):
        r"""Gets the action_tag_map of this HumanModel2DAssetMeta.

        动作标签映射。

        :return: The action_tag_map of this HumanModel2DAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        """
        return self._action_tag_map

    @action_tag_map.setter
    def action_tag_map(self, action_tag_map):
        r"""Sets the action_tag_map of this HumanModel2DAssetMeta.

        动作标签映射。

        :param action_tag_map: The action_tag_map of this HumanModel2DAssetMeta.
        :type action_tag_map: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        """
        self._action_tag_map = action_tag_map

    @property
    def is_flexus(self):
        r"""Gets the is_flexus of this HumanModel2DAssetMeta.

        是否是Flexus版本分身数字人。

        :return: The is_flexus of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        r"""Sets the is_flexus of this HumanModel2DAssetMeta.

        是否是Flexus版本分身数字人。

        :param is_flexus: The is_flexus of this HumanModel2DAssetMeta.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this HumanModel2DAssetMeta.

        形象关联的声音资产ID。

        :return: The voice_asset_id of this HumanModel2DAssetMeta.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this HumanModel2DAssetMeta.

        形象关联的声音资产ID。

        :param voice_asset_id: The voice_asset_id of this HumanModel2DAssetMeta.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

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
        if not isinstance(other, HumanModel2DAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
