# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalManifest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manifest_name_modifier': 'str',
        'selected_outputs': 'list[str]'
    }

    attribute_map = {
        'manifest_name_modifier': 'manifest_name_modifier',
        'selected_outputs': 'selected_outputs'
    }

    def __init__(self, manifest_name_modifier=None, selected_outputs=None):
        r"""AdditionalManifest

        The model defined in huaweicloud sdk

        :param manifest_name_modifier: 索引后缀名，后缀名仅支持数字，字母、下划线、中划线。
        :type manifest_name_modifier: str
        :param selected_outputs: 选择流名列表，最多支持9路流。
        :type selected_outputs: list[str]
        """
        
        

        self._manifest_name_modifier = None
        self._selected_outputs = None
        self.discriminator = None

        self.manifest_name_modifier = manifest_name_modifier
        self.selected_outputs = selected_outputs

    @property
    def manifest_name_modifier(self):
        r"""Gets the manifest_name_modifier of this AdditionalManifest.

        索引后缀名，后缀名仅支持数字，字母、下划线、中划线。

        :return: The manifest_name_modifier of this AdditionalManifest.
        :rtype: str
        """
        return self._manifest_name_modifier

    @manifest_name_modifier.setter
    def manifest_name_modifier(self, manifest_name_modifier):
        r"""Sets the manifest_name_modifier of this AdditionalManifest.

        索引后缀名，后缀名仅支持数字，字母、下划线、中划线。

        :param manifest_name_modifier: The manifest_name_modifier of this AdditionalManifest.
        :type manifest_name_modifier: str
        """
        self._manifest_name_modifier = manifest_name_modifier

    @property
    def selected_outputs(self):
        r"""Gets the selected_outputs of this AdditionalManifest.

        选择流名列表，最多支持9路流。

        :return: The selected_outputs of this AdditionalManifest.
        :rtype: list[str]
        """
        return self._selected_outputs

    @selected_outputs.setter
    def selected_outputs(self, selected_outputs):
        r"""Sets the selected_outputs of this AdditionalManifest.

        选择流名列表，最多支持9路流。

        :param selected_outputs: The selected_outputs of this AdditionalManifest.
        :type selected_outputs: list[str]
        """
        self._selected_outputs = selected_outputs

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
        if not isinstance(other, AdditionalManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
