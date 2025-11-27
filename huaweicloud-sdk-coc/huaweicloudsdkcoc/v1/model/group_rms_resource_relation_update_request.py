# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupRmsResourceRelationUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_list': 'list[str]',
        'group_id': 'str'
    }

    attribute_map = {
        'id_list': 'id_list',
        'group_id': 'group_id'
    }

    def __init__(self, id_list=None, group_id=None):
        r"""GroupRmsResourceRelationUpdateRequest

        The model defined in huaweicloud sdk

        :param id_list: **参数解释：** 资源关联uuid列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及
        :type id_list: list[str]
        :param group_id: **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及
        :type group_id: str
        """
        
        

        self._id_list = None
        self._group_id = None
        self.discriminator = None

        self.id_list = id_list
        self.group_id = group_id

    @property
    def id_list(self):
        r"""Gets the id_list of this GroupRmsResourceRelationUpdateRequest.

        **参数解释：** 资源关联uuid列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及

        :return: The id_list of this GroupRmsResourceRelationUpdateRequest.
        :rtype: list[str]
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        r"""Sets the id_list of this GroupRmsResourceRelationUpdateRequest.

        **参数解释：** 资源关联uuid列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及

        :param id_list: The id_list of this GroupRmsResourceRelationUpdateRequest.
        :type id_list: list[str]
        """
        self._id_list = id_list

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupRmsResourceRelationUpdateRequest.

        **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及

        :return: The group_id of this GroupRmsResourceRelationUpdateRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupRmsResourceRelationUpdateRequest.

        **参数解释：** 分组id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及

        :param group_id: The group_id of this GroupRmsResourceRelationUpdateRequest.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, GroupRmsResourceRelationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
