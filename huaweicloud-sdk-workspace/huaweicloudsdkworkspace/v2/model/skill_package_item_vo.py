# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkillPackageItemVO:

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
        'version': 'str',
        'revision': 'int',
        'package_hash': 'str',
        'package_size': 'int',
        'package_status': 'PackageStatusEnum',
        'uploaded_by': 'str',
        'uploaded_role': 'str',
        'regions': 'list[SkillPackageRegionItem]',
        'remark': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'revision': 'revision',
        'package_hash': 'package_hash',
        'package_size': 'package_size',
        'package_status': 'package_status',
        'uploaded_by': 'uploaded_by',
        'uploaded_role': 'uploaded_role',
        'regions': 'regions',
        'remark': 'remark',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, version=None, revision=None, package_hash=None, package_size=None, package_status=None, uploaded_by=None, uploaded_role=None, regions=None, remark=None, create_time=None, update_time=None):
        r"""SkillPackageItemVO

        The model defined in huaweicloud sdk

        :param id: 技能包id。
        :type id: str
        :param version: 版本号。
        :type version: str
        :param revision: 版本修订号。
        :type revision: int
        :param package_hash: 技能包 SHA256 哈希值。
        :type package_hash: str
        :param package_size: 技能包大小（字节）。
        :type package_size: int
        :param package_status: 
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        :param uploaded_by: 上传者。
        :type uploaded_by: str
        :param uploaded_role: 上传者角色。
        :type uploaded_role: str
        :param regions: 区域详情列表。
        :type regions: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageRegionItem`]
        :param remark: 备注。
        :type remark: str
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        """
        
        

        self._id = None
        self._version = None
        self._revision = None
        self._package_hash = None
        self._package_size = None
        self._package_status = None
        self._uploaded_by = None
        self._uploaded_role = None
        self._regions = None
        self._remark = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if revision is not None:
            self.revision = revision
        if package_hash is not None:
            self.package_hash = package_hash
        if package_size is not None:
            self.package_size = package_size
        if package_status is not None:
            self.package_status = package_status
        if uploaded_by is not None:
            self.uploaded_by = uploaded_by
        if uploaded_role is not None:
            self.uploaded_role = uploaded_role
        if regions is not None:
            self.regions = regions
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this SkillPackageItemVO.

        技能包id。

        :return: The id of this SkillPackageItemVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SkillPackageItemVO.

        技能包id。

        :param id: The id of this SkillPackageItemVO.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this SkillPackageItemVO.

        版本号。

        :return: The version of this SkillPackageItemVO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SkillPackageItemVO.

        版本号。

        :param version: The version of this SkillPackageItemVO.
        :type version: str
        """
        self._version = version

    @property
    def revision(self):
        r"""Gets the revision of this SkillPackageItemVO.

        版本修订号。

        :return: The revision of this SkillPackageItemVO.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this SkillPackageItemVO.

        版本修订号。

        :param revision: The revision of this SkillPackageItemVO.
        :type revision: int
        """
        self._revision = revision

    @property
    def package_hash(self):
        r"""Gets the package_hash of this SkillPackageItemVO.

        技能包 SHA256 哈希值。

        :return: The package_hash of this SkillPackageItemVO.
        :rtype: str
        """
        return self._package_hash

    @package_hash.setter
    def package_hash(self, package_hash):
        r"""Sets the package_hash of this SkillPackageItemVO.

        技能包 SHA256 哈希值。

        :param package_hash: The package_hash of this SkillPackageItemVO.
        :type package_hash: str
        """
        self._package_hash = package_hash

    @property
    def package_size(self):
        r"""Gets the package_size of this SkillPackageItemVO.

        技能包大小（字节）。

        :return: The package_size of this SkillPackageItemVO.
        :rtype: int
        """
        return self._package_size

    @package_size.setter
    def package_size(self, package_size):
        r"""Sets the package_size of this SkillPackageItemVO.

        技能包大小（字节）。

        :param package_size: The package_size of this SkillPackageItemVO.
        :type package_size: int
        """
        self._package_size = package_size

    @property
    def package_status(self):
        r"""Gets the package_status of this SkillPackageItemVO.

        :return: The package_status of this SkillPackageItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        return self._package_status

    @package_status.setter
    def package_status(self, package_status):
        r"""Sets the package_status of this SkillPackageItemVO.

        :param package_status: The package_status of this SkillPackageItemVO.
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        self._package_status = package_status

    @property
    def uploaded_by(self):
        r"""Gets the uploaded_by of this SkillPackageItemVO.

        上传者。

        :return: The uploaded_by of this SkillPackageItemVO.
        :rtype: str
        """
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        r"""Sets the uploaded_by of this SkillPackageItemVO.

        上传者。

        :param uploaded_by: The uploaded_by of this SkillPackageItemVO.
        :type uploaded_by: str
        """
        self._uploaded_by = uploaded_by

    @property
    def uploaded_role(self):
        r"""Gets the uploaded_role of this SkillPackageItemVO.

        上传者角色。

        :return: The uploaded_role of this SkillPackageItemVO.
        :rtype: str
        """
        return self._uploaded_role

    @uploaded_role.setter
    def uploaded_role(self, uploaded_role):
        r"""Sets the uploaded_role of this SkillPackageItemVO.

        上传者角色。

        :param uploaded_role: The uploaded_role of this SkillPackageItemVO.
        :type uploaded_role: str
        """
        self._uploaded_role = uploaded_role

    @property
    def regions(self):
        r"""Gets the regions of this SkillPackageItemVO.

        区域详情列表。

        :return: The regions of this SkillPackageItemVO.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageRegionItem`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this SkillPackageItemVO.

        区域详情列表。

        :param regions: The regions of this SkillPackageItemVO.
        :type regions: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageRegionItem`]
        """
        self._regions = regions

    @property
    def remark(self):
        r"""Gets the remark of this SkillPackageItemVO.

        备注。

        :return: The remark of this SkillPackageItemVO.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this SkillPackageItemVO.

        备注。

        :param remark: The remark of this SkillPackageItemVO.
        :type remark: str
        """
        self._remark = remark

    @property
    def create_time(self):
        r"""Gets the create_time of this SkillPackageItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this SkillPackageItemVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SkillPackageItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this SkillPackageItemVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SkillPackageItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this SkillPackageItemVO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SkillPackageItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this SkillPackageItemVO.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, SkillPackageItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
