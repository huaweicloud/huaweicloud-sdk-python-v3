# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateHookVersionDescriptionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_version_description': 'str'
    }

    attribute_map = {
        'hook_version_description': 'hook_version_description'
    }

    def __init__(self, hook_version_description=None):
        """PrivateHookVersionDescriptionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param hook_version_description: 私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。
        :type hook_version_description: str
        """
        
        

        self._hook_version_description = None
        self.discriminator = None

        if hook_version_description is not None:
            self.hook_version_description = hook_version_description

    @property
    def hook_version_description(self):
        """Gets the hook_version_description of this PrivateHookVersionDescriptionPrimitiveTypeHolder.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :return: The hook_version_description of this PrivateHookVersionDescriptionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._hook_version_description

    @hook_version_description.setter
    def hook_version_description(self, hook_version_description):
        """Sets the hook_version_description of this PrivateHookVersionDescriptionPrimitiveTypeHolder.

        私有hook版本的描述。可用于客户识别创建私有hook的版本。注意：hook版本为不可更新（immutable），所以该字段不可更新，如果需要更新，请删除后重建。

        :param hook_version_description: The hook_version_description of this PrivateHookVersionDescriptionPrimitiveTypeHolder.
        :type hook_version_description: str
        """
        self._hook_version_description = hook_version_description

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
        if not isinstance(other, PrivateHookVersionDescriptionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
