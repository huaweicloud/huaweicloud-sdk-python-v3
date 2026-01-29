# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionListViewV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'build_version': 'str',
        'files_count': 'int'
    }

    attribute_map = {
        'category': 'category',
        'build_version': 'build_version',
        'files_count': 'files_count'
    }

    def __init__(self, category=None, build_version=None, files_count=None):
        r"""VersionListViewV5

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 发布库版本的状态。 **取值范围**： - test：测试包。 - prod：发布包。
        :type category: str
        :param build_version: **参数解释**： 发布库版本的名称。 **取值范围**： 不涉及。
        :type build_version: str
        :param files_count: **参数解释**： 版本下的文件个数。 **取值范围**： 不涉及。
        :type files_count: int
        """
        
        

        self._category = None
        self._build_version = None
        self._files_count = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if build_version is not None:
            self.build_version = build_version
        if files_count is not None:
            self.files_count = files_count

    @property
    def category(self):
        r"""Gets the category of this VersionListViewV5.

        **参数解释**： 发布库版本的状态。 **取值范围**： - test：测试包。 - prod：发布包。

        :return: The category of this VersionListViewV5.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this VersionListViewV5.

        **参数解释**： 发布库版本的状态。 **取值范围**： - test：测试包。 - prod：发布包。

        :param category: The category of this VersionListViewV5.
        :type category: str
        """
        self._category = category

    @property
    def build_version(self):
        r"""Gets the build_version of this VersionListViewV5.

        **参数解释**： 发布库版本的名称。 **取值范围**： 不涉及。

        :return: The build_version of this VersionListViewV5.
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        r"""Sets the build_version of this VersionListViewV5.

        **参数解释**： 发布库版本的名称。 **取值范围**： 不涉及。

        :param build_version: The build_version of this VersionListViewV5.
        :type build_version: str
        """
        self._build_version = build_version

    @property
    def files_count(self):
        r"""Gets the files_count of this VersionListViewV5.

        **参数解释**： 版本下的文件个数。 **取值范围**： 不涉及。

        :return: The files_count of this VersionListViewV5.
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        r"""Sets the files_count of this VersionListViewV5.

        **参数解释**： 版本下的文件个数。 **取值范围**： 不涉及。

        :param files_count: The files_count of this VersionListViewV5.
        :type files_count: int
        """
        self._files_count = files_count

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
        if not isinstance(other, VersionListViewV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
