# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateFilePushPermissionBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[FilePushPermissionUpdateDto]'
    }

    attribute_map = {
        'permissions': 'permissions'
    }

    def __init__(self, permissions=None):
        r"""BatchUpdateFilePushPermissionBodyDto

        The model defined in huaweicloud sdk

        :param permissions: **参数解释：** 文件推送权限更新列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type permissions: list[:class:`huaweicloudsdkcodehub.v4.FilePushPermissionUpdateDto`]
        """
        
        

        self._permissions = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions

    @property
    def permissions(self):
        r"""Gets the permissions of this BatchUpdateFilePushPermissionBodyDto.

        **参数解释：** 文件推送权限更新列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The permissions of this BatchUpdateFilePushPermissionBodyDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.FilePushPermissionUpdateDto`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this BatchUpdateFilePushPermissionBodyDto.

        **参数解释：** 文件推送权限更新列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param permissions: The permissions of this BatchUpdateFilePushPermissionBodyDto.
        :type permissions: list[:class:`huaweicloudsdkcodehub.v4.FilePushPermissionUpdateDto`]
        """
        self._permissions = permissions

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
        if not isinstance(other, BatchUpdateFilePushPermissionBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
