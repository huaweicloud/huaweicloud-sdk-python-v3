# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceLevelBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_type': 'str',
        'resource_ids': 'list[str]',
        'resource_level_id': 'str'
    }

    attribute_map = {
        'change_type': 'change_type',
        'resource_ids': 'resource_ids',
        'resource_level_id': 'resource_level_id'
    }

    def __init__(self, change_type=None, resource_ids=None, resource_level_id=None):
        r"""UpdateResourceLevelBody

        The model defined in huaweicloud sdk

        :param change_type: change和recover两种枚举
        :type change_type: str
        :param resource_ids: resource_id的列表
        :type resource_ids: list[str]
        :param resource_level_id: 资源等级ID
        :type resource_level_id: str
        """
        
        

        self._change_type = None
        self._resource_ids = None
        self._resource_level_id = None
        self.discriminator = None

        self.change_type = change_type
        self.resource_ids = resource_ids
        if resource_level_id is not None:
            self.resource_level_id = resource_level_id

    @property
    def change_type(self):
        r"""Gets the change_type of this UpdateResourceLevelBody.

        change和recover两种枚举

        :return: The change_type of this UpdateResourceLevelBody.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this UpdateResourceLevelBody.

        change和recover两种枚举

        :param change_type: The change_type of this UpdateResourceLevelBody.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this UpdateResourceLevelBody.

        resource_id的列表

        :return: The resource_ids of this UpdateResourceLevelBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this UpdateResourceLevelBody.

        resource_id的列表

        :param resource_ids: The resource_ids of this UpdateResourceLevelBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def resource_level_id(self):
        r"""Gets the resource_level_id of this UpdateResourceLevelBody.

        资源等级ID

        :return: The resource_level_id of this UpdateResourceLevelBody.
        :rtype: str
        """
        return self._resource_level_id

    @resource_level_id.setter
    def resource_level_id(self, resource_level_id):
        r"""Sets the resource_level_id of this UpdateResourceLevelBody.

        资源等级ID

        :param resource_level_id: The resource_level_id of this UpdateResourceLevelBody.
        :type resource_level_id: str
        """
        self._resource_level_id = resource_level_id

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
        if not isinstance(other, UpdateResourceLevelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
