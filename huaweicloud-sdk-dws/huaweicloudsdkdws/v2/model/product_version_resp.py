# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductVersionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_cn': 'int',
        'max_cn': 'int',
        'version_type': 'str',
        'datastore_version': 'str'
    }

    attribute_map = {
        'min_cn': 'min_cn',
        'max_cn': 'max_cn',
        'version_type': 'version_type',
        'datastore_version': 'datastore_version'
    }

    def __init__(self, min_cn=None, max_cn=None, version_type=None, datastore_version=None):
        r"""ProductVersionResp

        The model defined in huaweicloud sdk

        :param min_cn: **参数解释**： 产品规格在该版本支持的最小CN数量。 **取值范围**： 不涉及。
        :type min_cn: int
        :param max_cn: **参数解释**： 产品规格在该版本支持的最大CN数量。 **取值范围**： 不涉及。
        :type max_cn: int
        :param version_type: **参数解释**： 产品规格该版本支持的类型。 **取值范围**： 1：稳定版； 0：最新版本。
        :type version_type: str
        :param datastore_version: **参数解释**： 产品规格版本号名称。 **取值范围**： 不涉及。
        :type datastore_version: str
        """
        
        

        self._min_cn = None
        self._max_cn = None
        self._version_type = None
        self._datastore_version = None
        self.discriminator = None

        if min_cn is not None:
            self.min_cn = min_cn
        if max_cn is not None:
            self.max_cn = max_cn
        if version_type is not None:
            self.version_type = version_type
        if datastore_version is not None:
            self.datastore_version = datastore_version

    @property
    def min_cn(self):
        r"""Gets the min_cn of this ProductVersionResp.

        **参数解释**： 产品规格在该版本支持的最小CN数量。 **取值范围**： 不涉及。

        :return: The min_cn of this ProductVersionResp.
        :rtype: int
        """
        return self._min_cn

    @min_cn.setter
    def min_cn(self, min_cn):
        r"""Sets the min_cn of this ProductVersionResp.

        **参数解释**： 产品规格在该版本支持的最小CN数量。 **取值范围**： 不涉及。

        :param min_cn: The min_cn of this ProductVersionResp.
        :type min_cn: int
        """
        self._min_cn = min_cn

    @property
    def max_cn(self):
        r"""Gets the max_cn of this ProductVersionResp.

        **参数解释**： 产品规格在该版本支持的最大CN数量。 **取值范围**： 不涉及。

        :return: The max_cn of this ProductVersionResp.
        :rtype: int
        """
        return self._max_cn

    @max_cn.setter
    def max_cn(self, max_cn):
        r"""Sets the max_cn of this ProductVersionResp.

        **参数解释**： 产品规格在该版本支持的最大CN数量。 **取值范围**： 不涉及。

        :param max_cn: The max_cn of this ProductVersionResp.
        :type max_cn: int
        """
        self._max_cn = max_cn

    @property
    def version_type(self):
        r"""Gets the version_type of this ProductVersionResp.

        **参数解释**： 产品规格该版本支持的类型。 **取值范围**： 1：稳定版； 0：最新版本。

        :return: The version_type of this ProductVersionResp.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ProductVersionResp.

        **参数解释**： 产品规格该版本支持的类型。 **取值范围**： 1：稳定版； 0：最新版本。

        :param version_type: The version_type of this ProductVersionResp.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ProductVersionResp.

        **参数解释**： 产品规格版本号名称。 **取值范围**： 不涉及。

        :return: The datastore_version of this ProductVersionResp.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ProductVersionResp.

        **参数解释**： 产品规格版本号名称。 **取值范围**： 不涉及。

        :param datastore_version: The datastore_version of this ProductVersionResp.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

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
        if not isinstance(other, ProductVersionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
