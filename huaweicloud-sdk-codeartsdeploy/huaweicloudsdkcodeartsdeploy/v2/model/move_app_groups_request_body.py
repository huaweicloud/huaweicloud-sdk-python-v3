# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MoveAppGroupsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'movement': 'int'
    }

    attribute_map = {
        'id': 'id',
        'movement': 'movement'
    }

    def __init__(self, id=None, movement=None):
        r"""MoveAppGroupsRequestBody

        The model defined in huaweicloud sdk

        :param id: 分组id
        :type id: str
        :param movement: 移动方向，1为上移，-1为下移
        :type movement: int
        """
        
        

        self._id = None
        self._movement = None
        self.discriminator = None

        self.id = id
        self.movement = movement

    @property
    def id(self):
        r"""Gets the id of this MoveAppGroupsRequestBody.

        分组id

        :return: The id of this MoveAppGroupsRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MoveAppGroupsRequestBody.

        分组id

        :param id: The id of this MoveAppGroupsRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def movement(self):
        r"""Gets the movement of this MoveAppGroupsRequestBody.

        移动方向，1为上移，-1为下移

        :return: The movement of this MoveAppGroupsRequestBody.
        :rtype: int
        """
        return self._movement

    @movement.setter
    def movement(self, movement):
        r"""Sets the movement of this MoveAppGroupsRequestBody.

        移动方向，1为上移，-1为下移

        :param movement: The movement of this MoveAppGroupsRequestBody.
        :type movement: int
        """
        self._movement = movement

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
        if not isinstance(other, MoveAppGroupsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
