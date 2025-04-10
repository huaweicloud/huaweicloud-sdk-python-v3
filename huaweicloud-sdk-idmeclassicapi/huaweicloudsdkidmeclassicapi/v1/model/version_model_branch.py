# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelBranch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'creator': 'str',
        'id': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'need_set_null_attrs': 'list[str]',
        'rdm_extension_type': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'creator': 'creator',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'need_set_null_attrs': 'needSetNullAttrs',
        'rdm_extension_type': 'rdmExtensionType'
    }

    def __init__(self, create_time=None, creator=None, id=None, last_update_time=None, modifier=None, need_set_null_attrs=None, rdm_extension_type=None):
        r"""VersionModelBranch

        The model defined in huaweicloud sdk

        :param create_time: **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param creator: **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param id: **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param last_update_time: **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param modifier: **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param need_set_null_attrs: **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type need_set_null_attrs: list[str]
        :param rdm_extension_type: **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        """
        
        

        self._create_time = None
        self._creator = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._need_set_null_attrs = None
        self._rdm_extension_type = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if need_set_null_attrs is not None:
            self.need_set_null_attrs = need_set_null_attrs
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type

    @property
    def create_time(self):
        r"""Gets the create_time of this VersionModelBranch.

        **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this VersionModelBranch.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this VersionModelBranch.

        **参数解释：**  创建时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this VersionModelBranch.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this VersionModelBranch.

        **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this VersionModelBranch.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this VersionModelBranch.

        **参数解释：**  创建者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this VersionModelBranch.
        :type creator: str
        """
        self._creator = creator

    @property
    def id(self):
        r"""Gets the id of this VersionModelBranch.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this VersionModelBranch.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VersionModelBranch.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this VersionModelBranch.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this VersionModelBranch.

        **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this VersionModelBranch.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this VersionModelBranch.

        **参数解释：**  最后更新时间。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this VersionModelBranch.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        r"""Gets the modifier of this VersionModelBranch.

        **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this VersionModelBranch.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this VersionModelBranch.

        **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this VersionModelBranch.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def need_set_null_attrs(self):
        r"""Gets the need_set_null_attrs of this VersionModelBranch.

        **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The need_set_null_attrs of this VersionModelBranch.
        :rtype: list[str]
        """
        return self._need_set_null_attrs

    @need_set_null_attrs.setter
    def need_set_null_attrs(self, need_set_null_attrs):
        r"""Sets the need_set_null_attrs of this VersionModelBranch.

        **参数解释：**  将自定义属性（包括基本属性、扩展属性和分类属性）设置为空值，其长度不能超过1000个字符。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param need_set_null_attrs: The need_set_null_attrs of this VersionModelBranch.
        :type need_set_null_attrs: list[str]
        """
        self._need_set_null_attrs = need_set_null_attrs

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this VersionModelBranch.

        **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this VersionModelBranch.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this VersionModelBranch.

        **参数解释：**  扩展类型。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this VersionModelBranch.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

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
        if not isinstance(other, VersionModelBranch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
