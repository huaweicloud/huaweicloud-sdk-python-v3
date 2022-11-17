# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAcceleratorOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'ip_sets': 'list[CreateAcceleratorOptionIpSets]',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ip_sets': 'ip_sets',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, ip_sets=None, enterprise_project_id=None, tags=None):
        """CreateAcceleratorOption

        The model defined in huaweicloud sdk

        :param name: 全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param ip_sets: 全球加速器IP列表。
        :type ip_sets: list[:class:`huaweicloudsdkga.v1.CreateAcceleratorOptionIpSets`]
        :param enterprise_project_id: 租户的企业项目ID，最大长度36个字符，带\&quot;-\&quot;连字符的UUID格式，或者是字符串\&quot;0\&quot;。\&quot;0\&quot;表示默认企业项目。
        :type enterprise_project_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        
        

        self._name = None
        self._description = None
        self._ip_sets = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.ip_sets = ip_sets
        self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateAcceleratorOption.

        全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this CreateAcceleratorOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAcceleratorOption.

        全球加速器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this CreateAcceleratorOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAcceleratorOption.

        全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this CreateAcceleratorOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAcceleratorOption.

        全球加速器描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this CreateAcceleratorOption.
        :type description: str
        """
        self._description = description

    @property
    def ip_sets(self):
        """Gets the ip_sets of this CreateAcceleratorOption.

        全球加速器IP列表。

        :return: The ip_sets of this CreateAcceleratorOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.CreateAcceleratorOptionIpSets`]
        """
        return self._ip_sets

    @ip_sets.setter
    def ip_sets(self, ip_sets):
        """Sets the ip_sets of this CreateAcceleratorOption.

        全球加速器IP列表。

        :param ip_sets: The ip_sets of this CreateAcceleratorOption.
        :type ip_sets: list[:class:`huaweicloudsdkga.v1.CreateAcceleratorOptionIpSets`]
        """
        self._ip_sets = ip_sets

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateAcceleratorOption.

        租户的企业项目ID，最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。

        :return: The enterprise_project_id of this CreateAcceleratorOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateAcceleratorOption.

        租户的企业项目ID，最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateAcceleratorOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateAcceleratorOption.

        标签列表。

        :return: The tags of this CreateAcceleratorOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateAcceleratorOption.

        标签列表。

        :param tags: The tags of this CreateAcceleratorOption.
        :type tags: list[:class:`huaweicloudsdkga.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateAcceleratorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
