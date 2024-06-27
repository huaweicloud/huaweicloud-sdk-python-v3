# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_tags': 'list[str]',
        'custom_tags': 'list[str]',
        'custom_annotations': 'list[str]'
    }

    attribute_map = {
        'auto_tags': 'auto_tags',
        'custom_tags': 'custom_tags',
        'custom_annotations': 'custom_annotations'
    }

    def __init__(self, auto_tags=None, custom_tags=None, custom_annotations=None):
        """AlarmTags

        The model defined in huaweicloud sdk

        :param auto_tags: 自动标签。
        :type auto_tags: list[str]
        :param custom_tags: 自定义标签。
        :type custom_tags: list[str]
        :param custom_annotations: 告警标注。
        :type custom_annotations: list[str]
        """
        
        

        self._auto_tags = None
        self._custom_tags = None
        self._custom_annotations = None
        self.discriminator = None

        if auto_tags is not None:
            self.auto_tags = auto_tags
        if custom_tags is not None:
            self.custom_tags = custom_tags
        if custom_annotations is not None:
            self.custom_annotations = custom_annotations

    @property
    def auto_tags(self):
        """Gets the auto_tags of this AlarmTags.

        自动标签。

        :return: The auto_tags of this AlarmTags.
        :rtype: list[str]
        """
        return self._auto_tags

    @auto_tags.setter
    def auto_tags(self, auto_tags):
        """Sets the auto_tags of this AlarmTags.

        自动标签。

        :param auto_tags: The auto_tags of this AlarmTags.
        :type auto_tags: list[str]
        """
        self._auto_tags = auto_tags

    @property
    def custom_tags(self):
        """Gets the custom_tags of this AlarmTags.

        自定义标签。

        :return: The custom_tags of this AlarmTags.
        :rtype: list[str]
        """
        return self._custom_tags

    @custom_tags.setter
    def custom_tags(self, custom_tags):
        """Sets the custom_tags of this AlarmTags.

        自定义标签。

        :param custom_tags: The custom_tags of this AlarmTags.
        :type custom_tags: list[str]
        """
        self._custom_tags = custom_tags

    @property
    def custom_annotations(self):
        """Gets the custom_annotations of this AlarmTags.

        告警标注。

        :return: The custom_annotations of this AlarmTags.
        :rtype: list[str]
        """
        return self._custom_annotations

    @custom_annotations.setter
    def custom_annotations(self, custom_annotations):
        """Sets the custom_annotations of this AlarmTags.

        告警标注。

        :param custom_annotations: The custom_annotations of this AlarmTags.
        :type custom_annotations: list[str]
        """
        self._custom_annotations = custom_annotations

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
        if not isinstance(other, AlarmTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
