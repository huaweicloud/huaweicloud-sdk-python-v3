# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdditionalManifests:

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
        r"""AdditionalManifests

        The model defined in huaweicloud sdk

        :param manifest_name_modifier: 定制的索引后缀名 
        :type manifest_name_modifier: str
        :param selected_outputs: 选择的流名称
        :type selected_outputs: list[str]
        """
        
        

        self._manifest_name_modifier = None
        self._selected_outputs = None
        self.discriminator = None

        if manifest_name_modifier is not None:
            self.manifest_name_modifier = manifest_name_modifier
        if selected_outputs is not None:
            self.selected_outputs = selected_outputs

    @property
    def manifest_name_modifier(self):
        r"""Gets the manifest_name_modifier of this AdditionalManifests.

        定制的索引后缀名 

        :return: The manifest_name_modifier of this AdditionalManifests.
        :rtype: str
        """
        return self._manifest_name_modifier

    @manifest_name_modifier.setter
    def manifest_name_modifier(self, manifest_name_modifier):
        r"""Sets the manifest_name_modifier of this AdditionalManifests.

        定制的索引后缀名 

        :param manifest_name_modifier: The manifest_name_modifier of this AdditionalManifests.
        :type manifest_name_modifier: str
        """
        self._manifest_name_modifier = manifest_name_modifier

    @property
    def selected_outputs(self):
        r"""Gets the selected_outputs of this AdditionalManifests.

        选择的流名称

        :return: The selected_outputs of this AdditionalManifests.
        :rtype: list[str]
        """
        return self._selected_outputs

    @selected_outputs.setter
    def selected_outputs(self, selected_outputs):
        r"""Sets the selected_outputs of this AdditionalManifests.

        选择的流名称

        :param selected_outputs: The selected_outputs of this AdditionalManifests.
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
        if not isinstance(other, AdditionalManifests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
