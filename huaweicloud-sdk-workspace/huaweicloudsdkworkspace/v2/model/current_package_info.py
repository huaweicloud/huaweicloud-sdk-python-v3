# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CurrentPackageInfo:

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
        'package_status': 'PackageStatusEnum',
        'regions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'revision': 'revision',
        'package_status': 'package_status',
        'regions': 'regions'
    }

    def __init__(self, id=None, version=None, revision=None, package_status=None, regions=None):
        r"""CurrentPackageInfo

        The model defined in huaweicloud sdk

        :param id: 技能包id。
        :type id: str
        :param version: 版本号。
        :type version: str
        :param revision: 版本修订号。
        :type revision: int
        :param package_status: 
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        :param regions: 已部署的区域标识列表。
        :type regions: list[str]
        """
        
        

        self._id = None
        self._version = None
        self._revision = None
        self._package_status = None
        self._regions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if revision is not None:
            self.revision = revision
        if package_status is not None:
            self.package_status = package_status
        if regions is not None:
            self.regions = regions

    @property
    def id(self):
        r"""Gets the id of this CurrentPackageInfo.

        技能包id。

        :return: The id of this CurrentPackageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CurrentPackageInfo.

        技能包id。

        :param id: The id of this CurrentPackageInfo.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this CurrentPackageInfo.

        版本号。

        :return: The version of this CurrentPackageInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CurrentPackageInfo.

        版本号。

        :param version: The version of this CurrentPackageInfo.
        :type version: str
        """
        self._version = version

    @property
    def revision(self):
        r"""Gets the revision of this CurrentPackageInfo.

        版本修订号。

        :return: The revision of this CurrentPackageInfo.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this CurrentPackageInfo.

        版本修订号。

        :param revision: The revision of this CurrentPackageInfo.
        :type revision: int
        """
        self._revision = revision

    @property
    def package_status(self):
        r"""Gets the package_status of this CurrentPackageInfo.

        :return: The package_status of this CurrentPackageInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        return self._package_status

    @package_status.setter
    def package_status(self, package_status):
        r"""Sets the package_status of this CurrentPackageInfo.

        :param package_status: The package_status of this CurrentPackageInfo.
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        self._package_status = package_status

    @property
    def regions(self):
        r"""Gets the regions of this CurrentPackageInfo.

        已部署的区域标识列表。

        :return: The regions of this CurrentPackageInfo.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this CurrentPackageInfo.

        已部署的区域标识列表。

        :param regions: The regions of this CurrentPackageInfo.
        :type regions: list[str]
        """
        self._regions = regions

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
        if not isinstance(other, CurrentPackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
