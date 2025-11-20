# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[str]',
        'freeze_type': 'list[int]'
    }

    attribute_map = {
        'tags': 'tags',
        'freeze_type': 'freeze_type'
    }

    def __init__(self, tags=None, freeze_type=None):
        r"""InstanceConfig

        The model defined in huaweicloud sdk

        :param tags: 实例级别标签
        :type tags: list[str]
        :param freeze_type: 冻结类型
        :type freeze_type: list[int]
        """
        
        

        self._tags = None
        self._freeze_type = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if freeze_type is not None:
            self.freeze_type = freeze_type

    @property
    def tags(self):
        r"""Gets the tags of this InstanceConfig.

        实例级别标签

        :return: The tags of this InstanceConfig.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this InstanceConfig.

        实例级别标签

        :param tags: The tags of this InstanceConfig.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def freeze_type(self):
        r"""Gets the freeze_type of this InstanceConfig.

        冻结类型

        :return: The freeze_type of this InstanceConfig.
        :rtype: list[int]
        """
        return self._freeze_type

    @freeze_type.setter
    def freeze_type(self, freeze_type):
        r"""Sets the freeze_type of this InstanceConfig.

        冻结类型

        :param freeze_type: The freeze_type of this InstanceConfig.
        :type freeze_type: list[int]
        """
        self._freeze_type = freeze_type

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
        if not isinstance(other, InstanceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
