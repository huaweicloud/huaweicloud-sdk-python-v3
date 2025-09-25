# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseVersionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'software_version': 'str',
        'hotfixes': 'list[DbHotfixInfoResult]'
    }

    attribute_map = {
        'software_version': 'software_version',
        'hotfixes': 'hotfixes'
    }

    def __init__(self, software_version=None, hotfixes=None):
        r"""DatabaseVersionResult

        The model defined in huaweicloud sdk

        :param software_version: **参数解释**： 数据库三位引擎版本。 **取值范围**： 不涉及。
        :type software_version: str
        :param hotfixes: **参数解释**： 数据库三位引擎版本对应的热补丁信息。 **取值范围**： 不涉及。
        :type hotfixes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DbHotfixInfoResult`]
        """
        
        

        self._software_version = None
        self._hotfixes = None
        self.discriminator = None

        self.software_version = software_version
        self.hotfixes = hotfixes

    @property
    def software_version(self):
        r"""Gets the software_version of this DatabaseVersionResult.

        **参数解释**： 数据库三位引擎版本。 **取值范围**： 不涉及。

        :return: The software_version of this DatabaseVersionResult.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        r"""Sets the software_version of this DatabaseVersionResult.

        **参数解释**： 数据库三位引擎版本。 **取值范围**： 不涉及。

        :param software_version: The software_version of this DatabaseVersionResult.
        :type software_version: str
        """
        self._software_version = software_version

    @property
    def hotfixes(self):
        r"""Gets the hotfixes of this DatabaseVersionResult.

        **参数解释**： 数据库三位引擎版本对应的热补丁信息。 **取值范围**： 不涉及。

        :return: The hotfixes of this DatabaseVersionResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DbHotfixInfoResult`]
        """
        return self._hotfixes

    @hotfixes.setter
    def hotfixes(self, hotfixes):
        r"""Sets the hotfixes of this DatabaseVersionResult.

        **参数解释**： 数据库三位引擎版本对应的热补丁信息。 **取值范围**： 不涉及。

        :param hotfixes: The hotfixes of this DatabaseVersionResult.
        :type hotfixes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DbHotfixInfoResult`]
        """
        self._hotfixes = hotfixes

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
        if not isinstance(other, DatabaseVersionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
