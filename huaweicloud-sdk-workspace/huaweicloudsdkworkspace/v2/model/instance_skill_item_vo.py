# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSkillItemVO:

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
        'display_name': 'str',
        'slug': 'str',
        'alias_name': 'str',
        'description': 'str',
        'owner_type': 'SkillOwnerTypeEnum',
        'install_status': 'InstallStatusEnum',
        'package_id': 'str',
        'version': 'str',
        'installed_at': 'str',
        'cover': 'str'
    }

    attribute_map = {
        'skill_id': 'skill_id',
        'display_name': 'display_name',
        'slug': 'slug',
        'alias_name': 'alias_name',
        'description': 'description',
        'owner_type': 'owner_type',
        'install_status': 'install_status',
        'package_id': 'package_id',
        'version': 'version',
        'installed_at': 'installed_at',
        'cover': 'cover'
    }

    def __init__(self, skill_id=None, display_name=None, slug=None, alias_name=None, description=None, owner_type=None, install_status=None, package_id=None, version=None, installed_at=None, cover=None):
        r"""InstanceSkillItemVO

        The model defined in huaweicloud sdk

        :param skill_id: 技能id。
        :type skill_id: str
        :param display_name: 技能名称。
        :type display_name: str
        :param slug: 技能slug。
        :type slug: str
        :param alias_name: 别名。
        :type alias_name: str
        :param description: 技能描述。
        :type description: str
        :param owner_type: 
        :type owner_type: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        :param install_status: 
        :type install_status: :class:`huaweicloudsdkworkspace.v2.InstallStatusEnum`
        :param package_id: 安装的技能包id。
        :type package_id: str
        :param version: 安装的技能包版本号。
        :type version: str
        :param installed_at: 安装时间（ISO8601格式，UTC时区）。
        :type installed_at: str
        :param cover: 技能封面图 base64 编码。
        :type cover: str
        """
        
        

        self._skill_id = None
        self._display_name = None
        self._slug = None
        self._alias_name = None
        self._description = None
        self._owner_type = None
        self._install_status = None
        self._package_id = None
        self._version = None
        self._installed_at = None
        self._cover = None
        self.discriminator = None

        if skill_id is not None:
            self.skill_id = skill_id
        if display_name is not None:
            self.display_name = display_name
        if slug is not None:
            self.slug = slug
        if alias_name is not None:
            self.alias_name = alias_name
        if description is not None:
            self.description = description
        if owner_type is not None:
            self.owner_type = owner_type
        if install_status is not None:
            self.install_status = install_status
        if package_id is not None:
            self.package_id = package_id
        if version is not None:
            self.version = version
        if installed_at is not None:
            self.installed_at = installed_at
        if cover is not None:
            self.cover = cover

    @property
    def skill_id(self):
        r"""Gets the skill_id of this InstanceSkillItemVO.

        技能id。

        :return: The skill_id of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this InstanceSkillItemVO.

        技能id。

        :param skill_id: The skill_id of this InstanceSkillItemVO.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def display_name(self):
        r"""Gets the display_name of this InstanceSkillItemVO.

        技能名称。

        :return: The display_name of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this InstanceSkillItemVO.

        技能名称。

        :param display_name: The display_name of this InstanceSkillItemVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def slug(self):
        r"""Gets the slug of this InstanceSkillItemVO.

        技能slug。

        :return: The slug of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        r"""Sets the slug of this InstanceSkillItemVO.

        技能slug。

        :param slug: The slug of this InstanceSkillItemVO.
        :type slug: str
        """
        self._slug = slug

    @property
    def alias_name(self):
        r"""Gets the alias_name of this InstanceSkillItemVO.

        别名。

        :return: The alias_name of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this InstanceSkillItemVO.

        别名。

        :param alias_name: The alias_name of this InstanceSkillItemVO.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this InstanceSkillItemVO.

        技能描述。

        :return: The description of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstanceSkillItemVO.

        技能描述。

        :param description: The description of this InstanceSkillItemVO.
        :type description: str
        """
        self._description = description

    @property
    def owner_type(self):
        r"""Gets the owner_type of this InstanceSkillItemVO.

        :return: The owner_type of this InstanceSkillItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this InstanceSkillItemVO.

        :param owner_type: The owner_type of this InstanceSkillItemVO.
        :type owner_type: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        """
        self._owner_type = owner_type

    @property
    def install_status(self):
        r"""Gets the install_status of this InstanceSkillItemVO.

        :return: The install_status of this InstanceSkillItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.InstallStatusEnum`
        """
        return self._install_status

    @install_status.setter
    def install_status(self, install_status):
        r"""Sets the install_status of this InstanceSkillItemVO.

        :param install_status: The install_status of this InstanceSkillItemVO.
        :type install_status: :class:`huaweicloudsdkworkspace.v2.InstallStatusEnum`
        """
        self._install_status = install_status

    @property
    def package_id(self):
        r"""Gets the package_id of this InstanceSkillItemVO.

        安装的技能包id。

        :return: The package_id of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        r"""Sets the package_id of this InstanceSkillItemVO.

        安装的技能包id。

        :param package_id: The package_id of this InstanceSkillItemVO.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def version(self):
        r"""Gets the version of this InstanceSkillItemVO.

        安装的技能包版本号。

        :return: The version of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstanceSkillItemVO.

        安装的技能包版本号。

        :param version: The version of this InstanceSkillItemVO.
        :type version: str
        """
        self._version = version

    @property
    def installed_at(self):
        r"""Gets the installed_at of this InstanceSkillItemVO.

        安装时间（ISO8601格式，UTC时区）。

        :return: The installed_at of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._installed_at

    @installed_at.setter
    def installed_at(self, installed_at):
        r"""Sets the installed_at of this InstanceSkillItemVO.

        安装时间（ISO8601格式，UTC时区）。

        :param installed_at: The installed_at of this InstanceSkillItemVO.
        :type installed_at: str
        """
        self._installed_at = installed_at

    @property
    def cover(self):
        r"""Gets the cover of this InstanceSkillItemVO.

        技能封面图 base64 编码。

        :return: The cover of this InstanceSkillItemVO.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this InstanceSkillItemVO.

        技能封面图 base64 编码。

        :param cover: The cover of this InstanceSkillItemVO.
        :type cover: str
        """
        self._cover = cover

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
        if not isinstance(other, InstanceSkillItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
