# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelCompareVersionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_version': 'str',
        'correlation_version': 'str',
        'id': 'str'
    }

    attribute_map = {
        'basic_version': 'basicVersion',
        'correlation_version': 'correlationVersion',
        'id': 'id'
    }

    def __init__(self, basic_version=None, correlation_version=None, id=None):
        r"""VersionModelCompareVersionVO

        The model defined in huaweicloud sdk

        :param basic_version: **参数解释：**  基础版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type basic_version: str
        :param correlation_version: **参数解释：**  对比版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type correlation_version: str
        :param id: **参数解释：**  主对象ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        """
        
        

        self._basic_version = None
        self._correlation_version = None
        self._id = None
        self.discriminator = None

        self.basic_version = basic_version
        self.correlation_version = correlation_version
        self.id = id

    @property
    def basic_version(self):
        r"""Gets the basic_version of this VersionModelCompareVersionVO.

        **参数解释：**  基础版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The basic_version of this VersionModelCompareVersionVO.
        :rtype: str
        """
        return self._basic_version

    @basic_version.setter
    def basic_version(self, basic_version):
        r"""Sets the basic_version of this VersionModelCompareVersionVO.

        **参数解释：**  基础版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param basic_version: The basic_version of this VersionModelCompareVersionVO.
        :type basic_version: str
        """
        self._basic_version = basic_version

    @property
    def correlation_version(self):
        r"""Gets the correlation_version of this VersionModelCompareVersionVO.

        **参数解释：**  对比版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The correlation_version of this VersionModelCompareVersionVO.
        :rtype: str
        """
        return self._correlation_version

    @correlation_version.setter
    def correlation_version(self, correlation_version):
        r"""Sets the correlation_version of this VersionModelCompareVersionVO.

        **参数解释：**  对比版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param correlation_version: The correlation_version of this VersionModelCompareVersionVO.
        :type correlation_version: str
        """
        self._correlation_version = correlation_version

    @property
    def id(self):
        r"""Gets the id of this VersionModelCompareVersionVO.

        **参数解释：**  主对象ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this VersionModelCompareVersionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VersionModelCompareVersionVO.

        **参数解释：**  主对象ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this VersionModelCompareVersionVO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, VersionModelCompareVersionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
