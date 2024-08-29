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
        'is_real_background': 'bool',
        'support_live': 'bool',
        'model_version': 'str',
        'model_resolution': 'str',
        'device_names': 'list[str]',
        'is_with_action_library': 'bool',
        'action_tag_map': 'list[ActionTagInfo]',
        'is_flexus': 'bool'
    }

    attribute_map = {
        'is_action_editable': 'is_action_editable',
        'is_real_background': 'is_real_background',
        'support_live': 'support_live',
        'model_version': 'model_version',
        'model_resolution': 'model_resolution',
        'device_names': 'device_names',
        'is_with_action_library': 'is_with_action_library',
        'action_tag_map': 'action_tag_map',
        'is_flexus': 'is_flexus'
    }

    def __init__(self, is_action_editable=None, is_real_background=None, support_live=None, model_version=None, model_resolution=None, device_names=None, is_with_action_library=None, action_tag_map=None, is_flexus=None):
        """HumanModel2DAssetMeta

        The model defined in huaweicloud sdk

        :param is_action_editable: 分身数字人的动作是否可编辑。默认不可编辑。
        :type is_action_editable: bool
        :param is_real_background: 是否是实景分身数字人。实景分身数字人不做背景替换。
        :type is_real_background: bool
        :param support_live: 是否支持直播
        :type support_live: bool
        :param model_version: 分身数字人模型版本。默认是V2版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型
        :type model_version: str
        :param model_resolution: 分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。
        :type model_resolution: str
        :param device_names: 已执行编译任务
        :type device_names: list[str]
        :param is_with_action_library: 分身数字人是否带原子动作库。 &gt; * 带原子动作库的分身数字人可做动作编排。
        :type is_with_action_library: bool
        :param action_tag_map: 动作标签映射。
        :type action_tag_map: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        :param is_flexus: 是否是Flexus版本分身数字人。
        :type is_flexus: bool
        """
        
        

        self._is_action_editable = None
        self._is_real_background = None
        self._support_live = None
        self._model_version = None
        self._model_resolution = None
        self._device_names = None
        self._is_with_action_library = None
        self._action_tag_map = None
        self._is_flexus = None
        self.discriminator = None

        if is_action_editable is not None:
            self.is_action_editable = is_action_editable
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

    @property
    def is_action_editable(self):
        """Gets the is_action_editable of this HumanModel2DAssetMeta.

        分身数字人的动作是否可编辑。默认不可编辑。

        :return: The is_action_editable of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_action_editable

    @is_action_editable.setter
    def is_action_editable(self, is_action_editable):
        """Sets the is_action_editable of this HumanModel2DAssetMeta.

        分身数字人的动作是否可编辑。默认不可编辑。

        :param is_action_editable: The is_action_editable of this HumanModel2DAssetMeta.
        :type is_action_editable: bool
        """
        self._is_action_editable = is_action_editable

    @property
    def is_real_background(self):
        """Gets the is_real_background of this HumanModel2DAssetMeta.

        是否是实景分身数字人。实景分身数字人不做背景替换。

        :return: The is_real_background of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_real_background

    @is_real_background.setter
    def is_real_background(self, is_real_background):
        """Sets the is_real_background of this HumanModel2DAssetMeta.

        是否是实景分身数字人。实景分身数字人不做背景替换。

        :param is_real_background: The is_real_background of this HumanModel2DAssetMeta.
        :type is_real_background: bool
        """
        self._is_real_background = is_real_background

    @property
    def support_live(self):
        """Gets the support_live of this HumanModel2DAssetMeta.

        是否支持直播

        :return: The support_live of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._support_live

    @support_live.setter
    def support_live(self, support_live):
        """Sets the support_live of this HumanModel2DAssetMeta.

        是否支持直播

        :param support_live: The support_live of this HumanModel2DAssetMeta.
        :type support_live: bool
        """
        self._support_live = support_live

    @property
    def model_version(self):
        """Gets the model_version of this HumanModel2DAssetMeta.

        分身数字人模型版本。默认是V2版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型

        :return: The model_version of this HumanModel2DAssetMeta.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this HumanModel2DAssetMeta.

        分身数字人模型版本。默认是V2版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3_2：V3.2版本模型

        :param model_version: The model_version of this HumanModel2DAssetMeta.
        :type model_version: str
        """
        self._model_version = model_version

    @property
    def model_resolution(self):
        """Gets the model_resolution of this HumanModel2DAssetMeta.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :return: The model_resolution of this HumanModel2DAssetMeta.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        """Sets the model_resolution of this HumanModel2DAssetMeta.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :param model_resolution: The model_resolution of this HumanModel2DAssetMeta.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def device_names(self):
        """Gets the device_names of this HumanModel2DAssetMeta.

        已执行编译任务

        :return: The device_names of this HumanModel2DAssetMeta.
        :rtype: list[str]
        """
        return self._device_names

    @device_names.setter
    def device_names(self, device_names):
        """Sets the device_names of this HumanModel2DAssetMeta.

        已执行编译任务

        :param device_names: The device_names of this HumanModel2DAssetMeta.
        :type device_names: list[str]
        """
        self._device_names = device_names

    @property
    def is_with_action_library(self):
        """Gets the is_with_action_library of this HumanModel2DAssetMeta.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :return: The is_with_action_library of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_with_action_library

    @is_with_action_library.setter
    def is_with_action_library(self, is_with_action_library):
        """Sets the is_with_action_library of this HumanModel2DAssetMeta.

        分身数字人是否带原子动作库。 > * 带原子动作库的分身数字人可做动作编排。

        :param is_with_action_library: The is_with_action_library of this HumanModel2DAssetMeta.
        :type is_with_action_library: bool
        """
        self._is_with_action_library = is_with_action_library

    @property
    def action_tag_map(self):
        """Gets the action_tag_map of this HumanModel2DAssetMeta.

        动作标签映射。

        :return: The action_tag_map of this HumanModel2DAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        """
        return self._action_tag_map

    @action_tag_map.setter
    def action_tag_map(self, action_tag_map):
        """Sets the action_tag_map of this HumanModel2DAssetMeta.

        动作标签映射。

        :param action_tag_map: The action_tag_map of this HumanModel2DAssetMeta.
        :type action_tag_map: list[:class:`huaweicloudsdkmetastudio.v1.ActionTagInfo`]
        """
        self._action_tag_map = action_tag_map

    @property
    def is_flexus(self):
        """Gets the is_flexus of this HumanModel2DAssetMeta.

        是否是Flexus版本分身数字人。

        :return: The is_flexus of this HumanModel2DAssetMeta.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        """Sets the is_flexus of this HumanModel2DAssetMeta.

        是否是Flexus版本分身数字人。

        :param is_flexus: The is_flexus of this HumanModel2DAssetMeta.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

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
