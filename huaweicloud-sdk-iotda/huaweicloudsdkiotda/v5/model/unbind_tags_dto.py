# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindTagsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str',
        'tag_keys': 'list[str]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'tag_keys': 'tag_keys'
    }

    def __init__(self, resource_type=None, resource_id=None, tag_keys=None):
        """UnbindTagsDTO

        The model defined in huaweicloud sdk

        :param resource_type: **参数说明**：要绑定标签的资源类型。 **取值范围**： - device：设备。
        :type resource_type: str
        :param resource_id: **参数说明**：要绑定标签的资源id。例如，资源类型为device，那么对应的资源id就是device_id。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type resource_id: str
        :param tag_keys: **参数说明**：指定资源要解绑的标签键列表，标签键列表中各项之间不允许重复，不能填写不存在的标签键值 **取值范围**：标签键长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。
        :type tag_keys: list[str]
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._tag_keys = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_keys = tag_keys

    @property
    def resource_type(self):
        """Gets the resource_type of this UnbindTagsDTO.

        **参数说明**：要绑定标签的资源类型。 **取值范围**： - device：设备。

        :return: The resource_type of this UnbindTagsDTO.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UnbindTagsDTO.

        **参数说明**：要绑定标签的资源类型。 **取值范围**： - device：设备。

        :param resource_type: The resource_type of this UnbindTagsDTO.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this UnbindTagsDTO.

        **参数说明**：要绑定标签的资源id。例如，资源类型为device，那么对应的资源id就是device_id。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The resource_id of this UnbindTagsDTO.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UnbindTagsDTO.

        **参数说明**：要绑定标签的资源id。例如，资源类型为device，那么对应的资源id就是device_id。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param resource_id: The resource_id of this UnbindTagsDTO.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def tag_keys(self):
        """Gets the tag_keys of this UnbindTagsDTO.

        **参数说明**：指定资源要解绑的标签键列表，标签键列表中各项之间不允许重复，不能填写不存在的标签键值 **取值范围**：标签键长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The tag_keys of this UnbindTagsDTO.
        :rtype: list[str]
        """
        return self._tag_keys

    @tag_keys.setter
    def tag_keys(self, tag_keys):
        """Sets the tag_keys of this UnbindTagsDTO.

        **参数说明**：指定资源要解绑的标签键列表，标签键列表中各项之间不允许重复，不能填写不存在的标签键值 **取值范围**：标签键长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。

        :param tag_keys: The tag_keys of this UnbindTagsDTO.
        :type tag_keys: list[str]
        """
        self._tag_keys = tag_keys

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
        if not isinstance(other, UnbindTagsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
