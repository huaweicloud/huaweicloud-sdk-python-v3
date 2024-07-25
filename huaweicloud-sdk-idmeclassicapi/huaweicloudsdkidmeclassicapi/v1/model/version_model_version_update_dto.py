# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelVersionUpdateDTO:

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
        'iteration': 'int',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iteration': 'iteration',
        'version': 'version'
    }

    def __init__(self, id=None, iteration=None, version=None):
        """VersionModelVersionUpdateDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param iteration: **参数解释：**  迭代版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type iteration: int
        :param version: **参数解释：**  版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type version: str
        """
        
        

        self._id = None
        self._iteration = None
        self._version = None
        self.discriminator = None

        self.id = id
        if iteration is not None:
            self.iteration = iteration
        self.version = version

    @property
    def id(self):
        """Gets the id of this VersionModelVersionUpdateDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this VersionModelVersionUpdateDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionModelVersionUpdateDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this VersionModelVersionUpdateDTO.
        :type id: str
        """
        self._id = id

    @property
    def iteration(self):
        """Gets the iteration of this VersionModelVersionUpdateDTO.

        **参数解释：**  迭代版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The iteration of this VersionModelVersionUpdateDTO.
        :rtype: int
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this VersionModelVersionUpdateDTO.

        **参数解释：**  迭代版本。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param iteration: The iteration of this VersionModelVersionUpdateDTO.
        :type iteration: int
        """
        self._iteration = iteration

    @property
    def version(self):
        """Gets the version of this VersionModelVersionUpdateDTO.

        **参数解释：**  版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The version of this VersionModelVersionUpdateDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionModelVersionUpdateDTO.

        **参数解释：**  版本号。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param version: The version of this VersionModelVersionUpdateDTO.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, VersionModelVersionUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
