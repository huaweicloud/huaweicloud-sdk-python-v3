# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleExtraMetaAdditionalProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'icon': 'str',
        'label': 'dict(str, str)',
        'use_alg_file': 'bool',
        'algorithm_classify_tag': 'dict(str, str)',
        'model_body_style': 'str',
        'mc_asset': 'EngineAssetInfo',
        'ue_asset': 'EngineAssetInfo'
    }

    attribute_map = {
        'icon': 'icon',
        'label': 'label',
        'use_alg_file': 'use_alg_file',
        'algorithm_classify_tag': 'algorithm_classify_tag',
        'model_body_style': 'model_body_style',
        'mc_asset': 'mc_asset',
        'ue_asset': 'ue_asset'
    }

    def __init__(self, icon=None, label=None, use_alg_file=None, algorithm_classify_tag=None, model_body_style=None, mc_asset=None, ue_asset=None):
        """StyleExtraMetaAdditionalProperties

        The model defined in huaweicloud sdk

        :param icon: 图标url
        :type icon: str
        :param label: 展示标签 {\&quot;cn\&quot;: \&quot;xxxxx\&quot;,\&quot;en\&quot;:\&quot;xxxxx\&quot;}
        :type label: dict(str, str)
        :param use_alg_file: 是否使用算法输出文件，针对生成算法
        :type use_alg_file: bool
        :param algorithm_classify_tag: 所属算法标签属性值，针对分类算法
        :type algorithm_classify_tag: dict(str, str)
        :param model_body_style: 当前使用的身体骨骼
        :type model_body_style: str
        :param mc_asset: 
        :type mc_asset: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        :param ue_asset: 
        :type ue_asset: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        """
        
        

        self._icon = None
        self._label = None
        self._use_alg_file = None
        self._algorithm_classify_tag = None
        self._model_body_style = None
        self._mc_asset = None
        self._ue_asset = None
        self.discriminator = None

        if icon is not None:
            self.icon = icon
        if label is not None:
            self.label = label
        if use_alg_file is not None:
            self.use_alg_file = use_alg_file
        if algorithm_classify_tag is not None:
            self.algorithm_classify_tag = algorithm_classify_tag
        if model_body_style is not None:
            self.model_body_style = model_body_style
        if mc_asset is not None:
            self.mc_asset = mc_asset
        if ue_asset is not None:
            self.ue_asset = ue_asset

    @property
    def icon(self):
        """Gets the icon of this StyleExtraMetaAdditionalProperties.

        图标url

        :return: The icon of this StyleExtraMetaAdditionalProperties.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this StyleExtraMetaAdditionalProperties.

        图标url

        :param icon: The icon of this StyleExtraMetaAdditionalProperties.
        :type icon: str
        """
        self._icon = icon

    @property
    def label(self):
        """Gets the label of this StyleExtraMetaAdditionalProperties.

        展示标签 {\"cn\": \"xxxxx\",\"en\":\"xxxxx\"}

        :return: The label of this StyleExtraMetaAdditionalProperties.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this StyleExtraMetaAdditionalProperties.

        展示标签 {\"cn\": \"xxxxx\",\"en\":\"xxxxx\"}

        :param label: The label of this StyleExtraMetaAdditionalProperties.
        :type label: dict(str, str)
        """
        self._label = label

    @property
    def use_alg_file(self):
        """Gets the use_alg_file of this StyleExtraMetaAdditionalProperties.

        是否使用算法输出文件，针对生成算法

        :return: The use_alg_file of this StyleExtraMetaAdditionalProperties.
        :rtype: bool
        """
        return self._use_alg_file

    @use_alg_file.setter
    def use_alg_file(self, use_alg_file):
        """Sets the use_alg_file of this StyleExtraMetaAdditionalProperties.

        是否使用算法输出文件，针对生成算法

        :param use_alg_file: The use_alg_file of this StyleExtraMetaAdditionalProperties.
        :type use_alg_file: bool
        """
        self._use_alg_file = use_alg_file

    @property
    def algorithm_classify_tag(self):
        """Gets the algorithm_classify_tag of this StyleExtraMetaAdditionalProperties.

        所属算法标签属性值，针对分类算法

        :return: The algorithm_classify_tag of this StyleExtraMetaAdditionalProperties.
        :rtype: dict(str, str)
        """
        return self._algorithm_classify_tag

    @algorithm_classify_tag.setter
    def algorithm_classify_tag(self, algorithm_classify_tag):
        """Sets the algorithm_classify_tag of this StyleExtraMetaAdditionalProperties.

        所属算法标签属性值，针对分类算法

        :param algorithm_classify_tag: The algorithm_classify_tag of this StyleExtraMetaAdditionalProperties.
        :type algorithm_classify_tag: dict(str, str)
        """
        self._algorithm_classify_tag = algorithm_classify_tag

    @property
    def model_body_style(self):
        """Gets the model_body_style of this StyleExtraMetaAdditionalProperties.

        当前使用的身体骨骼

        :return: The model_body_style of this StyleExtraMetaAdditionalProperties.
        :rtype: str
        """
        return self._model_body_style

    @model_body_style.setter
    def model_body_style(self, model_body_style):
        """Sets the model_body_style of this StyleExtraMetaAdditionalProperties.

        当前使用的身体骨骼

        :param model_body_style: The model_body_style of this StyleExtraMetaAdditionalProperties.
        :type model_body_style: str
        """
        self._model_body_style = model_body_style

    @property
    def mc_asset(self):
        """Gets the mc_asset of this StyleExtraMetaAdditionalProperties.

        :return: The mc_asset of this StyleExtraMetaAdditionalProperties.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        """
        return self._mc_asset

    @mc_asset.setter
    def mc_asset(self, mc_asset):
        """Sets the mc_asset of this StyleExtraMetaAdditionalProperties.

        :param mc_asset: The mc_asset of this StyleExtraMetaAdditionalProperties.
        :type mc_asset: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        """
        self._mc_asset = mc_asset

    @property
    def ue_asset(self):
        """Gets the ue_asset of this StyleExtraMetaAdditionalProperties.

        :return: The ue_asset of this StyleExtraMetaAdditionalProperties.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        """
        return self._ue_asset

    @ue_asset.setter
    def ue_asset(self, ue_asset):
        """Sets the ue_asset of this StyleExtraMetaAdditionalProperties.

        :param ue_asset: The ue_asset of this StyleExtraMetaAdditionalProperties.
        :type ue_asset: :class:`huaweicloudsdkmetastudio.v1.EngineAssetInfo`
        """
        self._ue_asset = ue_asset

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
        if not isinstance(other, StyleExtraMetaAdditionalProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
