# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListSkillPackageItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skill_id': 'str',
        'current_package': 'CurrentPackageInfo'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'current_package': 'current_package'
    }

    def __init__(self, skill_id=None, current_package=None):
        r"""BatchListSkillPackageItem

        The model defined in huaweicloud sdk

        :param skill_id: 技能 ID。
        :type skill_id: str
        :param current_package: 
        :type current_package: :class:`huaweicloudsdkworkspace.v2.CurrentPackageInfo`
        """
        
        

        self._skill_id = None
        self._current_package = None
        self.discriminator = None

        if skill_id is not None:
            self.skill_id = skill_id
        if current_package is not None:
            self.current_package = current_package

    @property
    def skill_id(self):
        r"""Gets the skill_id of this BatchListSkillPackageItem.

        技能 ID。

        :return: The skill_id of this BatchListSkillPackageItem.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this BatchListSkillPackageItem.

        技能 ID。

        :param skill_id: The skill_id of this BatchListSkillPackageItem.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def current_package(self):
        r"""Gets the current_package of this BatchListSkillPackageItem.

        :return: The current_package of this BatchListSkillPackageItem.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CurrentPackageInfo`
        """
        return self._current_package

    @current_package.setter
    def current_package(self, current_package):
        r"""Sets the current_package of this BatchListSkillPackageItem.

        :param current_package: The current_package of this BatchListSkillPackageItem.
        :type current_package: :class:`huaweicloudsdkworkspace.v2.CurrentPackageInfo`
        """
        self._current_package = current_package

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
        if not isinstance(other, BatchListSkillPackageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
