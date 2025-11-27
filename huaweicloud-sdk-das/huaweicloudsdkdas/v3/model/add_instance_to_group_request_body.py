# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddInstanceToGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, group_id=None, instance_ids=None):
        r"""AddInstanceToGroupRequestBody

        The model defined in huaweicloud sdk

        :param group_id: 实例组ID
        :type group_id: int
        :param instance_ids: 实例ID列表
        :type instance_ids: list[str]
        """
        
        

        self._group_id = None
        self._instance_ids = None
        self.discriminator = None

        self.group_id = group_id
        self.instance_ids = instance_ids

    @property
    def group_id(self):
        r"""Gets the group_id of this AddInstanceToGroupRequestBody.

        实例组ID

        :return: The group_id of this AddInstanceToGroupRequestBody.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AddInstanceToGroupRequestBody.

        实例组ID

        :param group_id: The group_id of this AddInstanceToGroupRequestBody.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this AddInstanceToGroupRequestBody.

        实例ID列表

        :return: The instance_ids of this AddInstanceToGroupRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this AddInstanceToGroupRequestBody.

        实例ID列表

        :param instance_ids: The instance_ids of this AddInstanceToGroupRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, AddInstanceToGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
