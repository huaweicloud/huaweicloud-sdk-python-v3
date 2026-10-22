# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageSnapshotRequestInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'image_snapshot_size': 'int',
        'reserved_days': 'int'
    }

    attribute_map = {
        'name': 'name',
        'image_snapshot_size': 'image_snapshot_size',
        'reserved_days': 'reserved_days'
    }

    def __init__(self, name=None, image_snapshot_size=None, reserved_days=None):
        r"""CreateImageSnapshotRequestInput

        The model defined in huaweicloud sdk

        :param name: **参数解释**：快照名称（用户指定，用于标识快照用途）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 
        :type name: str
        :param image_snapshot_size: **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不传则基于镜像大小的3倍自动估算。 
        :type image_snapshot_size: int
        :param reserved_days: **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536天。 **默认取值**：0。 
        :type reserved_days: int
        """
        
        

        self._name = None
        self._image_snapshot_size = None
        self._reserved_days = None
        self.discriminator = None

        self.name = name
        if image_snapshot_size is not None:
            self.image_snapshot_size = image_snapshot_size
        if reserved_days is not None:
            self.reserved_days = reserved_days

    @property
    def name(self):
        r"""Gets the name of this CreateImageSnapshotRequestInput.

        **参数解释**：快照名称（用户指定，用于标识快照用途）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 

        :return: The name of this CreateImageSnapshotRequestInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateImageSnapshotRequestInput.

        **参数解释**：快照名称（用户指定，用于标识快照用途）。 **约束限制**：不涉及。 **取值范围**：以小写字母开头，小写字母、数字、中划线（-）组成，小写字母或数字结尾的1到190字符的字符串。 **默认取值**：不涉及。 

        :param name: The name of this CreateImageSnapshotRequestInput.
        :type name: str
        """
        self._name = name

    @property
    def image_snapshot_size(self):
        r"""Gets the image_snapshot_size of this CreateImageSnapshotRequestInput.

        **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不传则基于镜像大小的3倍自动估算。 

        :return: The image_snapshot_size of this CreateImageSnapshotRequestInput.
        :rtype: int
        """
        return self._image_snapshot_size

    @image_snapshot_size.setter
    def image_snapshot_size(self, image_snapshot_size):
        r"""Sets the image_snapshot_size of this CreateImageSnapshotRequestInput.

        **参数解释**：快照大小，单位GiB。 **约束限制**：不涉及。 **取值范围**：20~400。 **默认取值**：不传则基于镜像大小的3倍自动估算。 

        :param image_snapshot_size: The image_snapshot_size of this CreateImageSnapshotRequestInput.
        :type image_snapshot_size: int
        """
        self._image_snapshot_size = image_snapshot_size

    @property
    def reserved_days(self):
        r"""Gets the reserved_days of this CreateImageSnapshotRequestInput.

        **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536天。 **默认取值**：0。 

        :return: The reserved_days of this CreateImageSnapshotRequestInput.
        :rtype: int
        """
        return self._reserved_days

    @reserved_days.setter
    def reserved_days(self, reserved_days):
        r"""Sets the reserved_days of this CreateImageSnapshotRequestInput.

        **参数解释**：镜像快照保留天数。超过保留天数自动失效，0表示永久保留。 **约束限制**：不涉及。 **取值范围**：0~65536天。 **默认取值**：0。 

        :param reserved_days: The reserved_days of this CreateImageSnapshotRequestInput.
        :type reserved_days: int
        """
        self._reserved_days = reserved_days

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
        if not isinstance(other, CreateImageSnapshotRequestInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
