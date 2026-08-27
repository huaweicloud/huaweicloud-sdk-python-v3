# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelConfigItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, group_id=None, resource_id=None, resource_type=None):
        r"""ModelConfigItem

        The model defined in huaweicloud sdk

        :param group_id: 模型分组ID。
        :type group_id: str
        :param resource_id: 资源ID（Agent实例ID或桌面标签key:value）。
        :type resource_id: str
        :param resource_type: 资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。
        :type resource_type: str
        """
        
        

        self._group_id = None
        self._resource_id = None
        self._resource_type = None
        self.discriminator = None

        self.group_id = group_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    @property
    def group_id(self):
        r"""Gets the group_id of this ModelConfigItem.

        模型分组ID。

        :return: The group_id of this ModelConfigItem.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ModelConfigItem.

        模型分组ID。

        :param group_id: The group_id of this ModelConfigItem.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ModelConfigItem.

        资源ID（Agent实例ID或桌面标签key:value）。

        :return: The resource_id of this ModelConfigItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ModelConfigItem.

        资源ID（Agent实例ID或桌面标签key:value）。

        :param resource_id: The resource_id of this ModelConfigItem.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ModelConfigItem.

        资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。

        :return: The resource_type of this ModelConfigItem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ModelConfigItem.

        资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。

        :param resource_type: The resource_type of this ModelConfigItem.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ModelConfigItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
