# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSkillBindingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'skill_ids': 'list[str]',
        'versions': 'list[str]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'skill_ids': 'skill_ids',
        'versions': 'versions',
        'tags': 'tags'
    }

    def __init__(self, instance_ids=None, skill_ids=None, versions=None, tags=None):
        r"""CreateSkillBindingReq

        The model defined in huaweicloud sdk

        :param instance_ids: 实例 ID 列表。
        :type instance_ids: list[str]
        :param skill_ids: 技能 ID 列表。
        :type skill_ids: list[str]
        :param versions: 技能版本列表，与 skill_ids 一一对应。不传或对应位置为空时使用技能当前版本。
        :type versions: list[str]
        :param tags: 标签列表，格式为 key:value，通过标签查询 tbl_desktop_tags 表获取关联实例ID，与 instance_ids 合并后去重。
        :type tags: list[str]
        """
        
        

        self._instance_ids = None
        self._skill_ids = None
        self._versions = None
        self._tags = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.skill_ids = skill_ids
        if versions is not None:
            self.versions = versions
        if tags is not None:
            self.tags = tags

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this CreateSkillBindingReq.

        实例 ID 列表。

        :return: The instance_ids of this CreateSkillBindingReq.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this CreateSkillBindingReq.

        实例 ID 列表。

        :param instance_ids: The instance_ids of this CreateSkillBindingReq.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def skill_ids(self):
        r"""Gets the skill_ids of this CreateSkillBindingReq.

        技能 ID 列表。

        :return: The skill_ids of this CreateSkillBindingReq.
        :rtype: list[str]
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids):
        r"""Sets the skill_ids of this CreateSkillBindingReq.

        技能 ID 列表。

        :param skill_ids: The skill_ids of this CreateSkillBindingReq.
        :type skill_ids: list[str]
        """
        self._skill_ids = skill_ids

    @property
    def versions(self):
        r"""Gets the versions of this CreateSkillBindingReq.

        技能版本列表，与 skill_ids 一一对应。不传或对应位置为空时使用技能当前版本。

        :return: The versions of this CreateSkillBindingReq.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this CreateSkillBindingReq.

        技能版本列表，与 skill_ids 一一对应。不传或对应位置为空时使用技能当前版本。

        :param versions: The versions of this CreateSkillBindingReq.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def tags(self):
        r"""Gets the tags of this CreateSkillBindingReq.

        标签列表，格式为 key:value，通过标签查询 tbl_desktop_tags 表获取关联实例ID，与 instance_ids 合并后去重。

        :return: The tags of this CreateSkillBindingReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateSkillBindingReq.

        标签列表，格式为 key:value，通过标签查询 tbl_desktop_tags 表获取关联实例ID，与 instance_ids 合并后去重。

        :param tags: The tags of this CreateSkillBindingReq.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateSkillBindingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
