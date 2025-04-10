# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleGroupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'scene_id': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'scene_id': 'scene_id'
    }

    def __init__(self, role_id=None, scene_id=None):
        r"""ScheduleGroupInfo

        The model defined in huaweicloud sdk

        :param role_id: 角色id
        :type role_id: str
        :param scene_id: 场景id
        :type scene_id: str
        """
        
        

        self._role_id = None
        self._scene_id = None
        self.discriminator = None

        self.role_id = role_id
        self.scene_id = scene_id

    @property
    def role_id(self):
        r"""Gets the role_id of this ScheduleGroupInfo.

        角色id

        :return: The role_id of this ScheduleGroupInfo.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ScheduleGroupInfo.

        角色id

        :param role_id: The role_id of this ScheduleGroupInfo.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def scene_id(self):
        r"""Gets the scene_id of this ScheduleGroupInfo.

        场景id

        :return: The scene_id of this ScheduleGroupInfo.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this ScheduleGroupInfo.

        场景id

        :param scene_id: The scene_id of this ScheduleGroupInfo.
        :type scene_id: str
        """
        self._scene_id = scene_id

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
        if not isinstance(other, ScheduleGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
