# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroupDependency:

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
        'enterprise_project_id': 'str',
        'dependency': 'list[Dependency]'
    }

    attribute_map = {
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'dependency': 'dependency'
    }

    def __init__(self, id=None, enterprise_project_id=None, dependency=None):
        r"""AddressGroupDependency

        The model defined in huaweicloud sdk

        :param id: **参数解释**： IP地址组的资源ID。IP地址组创建成功后，会生成一个IP地址组 ID，是IP地址组对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。
        :type id: str
        :param enterprise_project_id: **参数解释**： IP地址组所属的企业项目ID。 **取值范围**： 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。
        :type enterprise_project_id: str
        :param dependency: **参数解释**： IP地址组关联的资源列表。 **取值范围**： 不涉及。
        :type dependency: list[:class:`huaweicloudsdkvpc.v3.Dependency`]
        """
        
        

        self._id = None
        self._enterprise_project_id = None
        self._dependency = None
        self.discriminator = None

        self.id = id
        self.enterprise_project_id = enterprise_project_id
        self.dependency = dependency

    @property
    def id(self):
        r"""Gets the id of this AddressGroupDependency.

        **参数解释**： IP地址组的资源ID。IP地址组创建成功后，会生成一个IP地址组 ID，是IP地址组对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this AddressGroupDependency.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddressGroupDependency.

        **参数解释**： IP地址组的资源ID。IP地址组创建成功后，会生成一个IP地址组 ID，是IP地址组对应的唯一标识。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this AddressGroupDependency.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AddressGroupDependency.

        **参数解释**： IP地址组所属的企业项目ID。 **取值范围**： 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this AddressGroupDependency.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AddressGroupDependency.

        **参数解释**： IP地址组所属的企业项目ID。 **取值范围**： 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this AddressGroupDependency.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dependency(self):
        r"""Gets the dependency of this AddressGroupDependency.

        **参数解释**： IP地址组关联的资源列表。 **取值范围**： 不涉及。

        :return: The dependency of this AddressGroupDependency.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.Dependency`]
        """
        return self._dependency

    @dependency.setter
    def dependency(self, dependency):
        r"""Sets the dependency of this AddressGroupDependency.

        **参数解释**： IP地址组关联的资源列表。 **取值范围**： 不涉及。

        :param dependency: The dependency of this AddressGroupDependency.
        :type dependency: list[:class:`huaweicloudsdkvpc.v3.Dependency`]
        """
        self._dependency = dependency

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
        if not isinstance(other, AddressGroupDependency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
