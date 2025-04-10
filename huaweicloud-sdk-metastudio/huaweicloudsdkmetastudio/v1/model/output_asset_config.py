# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputAssetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_name': 'str'
    }

    attribute_map = {
        'asset_name': 'asset_name'
    }

    def __init__(self, asset_name=None):
        r"""OutputAssetConfig

        The model defined in huaweicloud sdk

        :param asset_name: **参数解释**： 输出视频资产名称。 &gt; * 视频资产名称最大长度支持256；文件名称最大长度支持240（超过长度的会被舍弃）  **约束限制**： 不涉及。 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。
        :type asset_name: str
        """
        
        

        self._asset_name = None
        self.discriminator = None

        self.asset_name = asset_name

    @property
    def asset_name(self):
        r"""Gets the asset_name of this OutputAssetConfig.

        **参数解释**： 输出视频资产名称。 > * 视频资产名称最大长度支持256；文件名称最大长度支持240（超过长度的会被舍弃）  **约束限制**： 不涉及。 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。

        :return: The asset_name of this OutputAssetConfig.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this OutputAssetConfig.

        **参数解释**： 输出视频资产名称。 > * 视频资产名称最大长度支持256；文件名称最大长度支持240（超过长度的会被舍弃）  **约束限制**： 不涉及。 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。

        :param asset_name: The asset_name of this OutputAssetConfig.
        :type asset_name: str
        """
        self._asset_name = asset_name

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
        if not isinstance(other, OutputAssetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
