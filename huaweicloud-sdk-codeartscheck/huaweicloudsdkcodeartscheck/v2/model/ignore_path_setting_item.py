# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IgnorePathSettingItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'checkbox_status': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'checkbox_status': 'checkbox_status'
    }

    def __init__(self, file_path=None, checkbox_status=None):
        r"""IgnorePathSettingItem

        The model defined in huaweicloud sdk

        :param file_path: **参数解释：** 需要屏蔽的目录或文件路径。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type file_path: str
        :param checkbox_status: **参数解释：** 屏蔽状态。 **约束限制：** 不涉及。 **取值范围：** - unchecked：取消屏蔽 - all：全部屏蔽 - half：半屏蔽，用于目录，表示目录下部分子目录、文件需要屏蔽 **默认取值：** 不涉及。
        :type checkbox_status: str
        """
        
        

        self._file_path = None
        self._checkbox_status = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if checkbox_status is not None:
            self.checkbox_status = checkbox_status

    @property
    def file_path(self):
        r"""Gets the file_path of this IgnorePathSettingItem.

        **参数解释：** 需要屏蔽的目录或文件路径。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The file_path of this IgnorePathSettingItem.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this IgnorePathSettingItem.

        **参数解释：** 需要屏蔽的目录或文件路径。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param file_path: The file_path of this IgnorePathSettingItem.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def checkbox_status(self):
        r"""Gets the checkbox_status of this IgnorePathSettingItem.

        **参数解释：** 屏蔽状态。 **约束限制：** 不涉及。 **取值范围：** - unchecked：取消屏蔽 - all：全部屏蔽 - half：半屏蔽，用于目录，表示目录下部分子目录、文件需要屏蔽 **默认取值：** 不涉及。

        :return: The checkbox_status of this IgnorePathSettingItem.
        :rtype: str
        """
        return self._checkbox_status

    @checkbox_status.setter
    def checkbox_status(self, checkbox_status):
        r"""Sets the checkbox_status of this IgnorePathSettingItem.

        **参数解释：** 屏蔽状态。 **约束限制：** 不涉及。 **取值范围：** - unchecked：取消屏蔽 - all：全部屏蔽 - half：半屏蔽，用于目录，表示目录下部分子目录、文件需要屏蔽 **默认取值：** 不涉及。

        :param checkbox_status: The checkbox_status of this IgnorePathSettingItem.
        :type checkbox_status: str
        """
        self._checkbox_status = checkbox_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IgnorePathSettingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
