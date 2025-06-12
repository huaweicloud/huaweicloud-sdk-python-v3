# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeystoreSearchResponseBodyResultPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'setting': 'bool',
        'delete': 'bool',
        'modify': 'bool',
        'usage': 'bool'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'setting': 'setting',
        'delete': 'delete',
        'modify': 'modify',
        'usage': 'usage'
    }

    def __init__(self, keystore_id=None, setting=None, delete=None, modify=None, usage=None):
        r"""ListKeystoreSearchResponseBodyResultPermission

        The model defined in huaweicloud sdk

        :param keystore_id: 文件ID
        :type keystore_id: str
        :param setting: 是否有设置权限
        :type setting: bool
        :param delete: 是否有删除权限
        :type delete: bool
        :param modify: 是否有修改权限
        :type modify: bool
        :param usage: 是否有使用权限
        :type usage: bool
        """
        
        

        self._keystore_id = None
        self._setting = None
        self._delete = None
        self._modify = None
        self._usage = None
        self.discriminator = None

        if keystore_id is not None:
            self.keystore_id = keystore_id
        if setting is not None:
            self.setting = setting
        if delete is not None:
            self.delete = delete
        if modify is not None:
            self.modify = modify
        if usage is not None:
            self.usage = usage

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this ListKeystoreSearchResponseBodyResultPermission.

        文件ID

        :return: The keystore_id of this ListKeystoreSearchResponseBodyResultPermission.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this ListKeystoreSearchResponseBodyResultPermission.

        文件ID

        :param keystore_id: The keystore_id of this ListKeystoreSearchResponseBodyResultPermission.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def setting(self):
        r"""Gets the setting of this ListKeystoreSearchResponseBodyResultPermission.

        是否有设置权限

        :return: The setting of this ListKeystoreSearchResponseBodyResultPermission.
        :rtype: bool
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        r"""Sets the setting of this ListKeystoreSearchResponseBodyResultPermission.

        是否有设置权限

        :param setting: The setting of this ListKeystoreSearchResponseBodyResultPermission.
        :type setting: bool
        """
        self._setting = setting

    @property
    def delete(self):
        r"""Gets the delete of this ListKeystoreSearchResponseBodyResultPermission.

        是否有删除权限

        :return: The delete of this ListKeystoreSearchResponseBodyResultPermission.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this ListKeystoreSearchResponseBodyResultPermission.

        是否有删除权限

        :param delete: The delete of this ListKeystoreSearchResponseBodyResultPermission.
        :type delete: bool
        """
        self._delete = delete

    @property
    def modify(self):
        r"""Gets the modify of this ListKeystoreSearchResponseBodyResultPermission.

        是否有修改权限

        :return: The modify of this ListKeystoreSearchResponseBodyResultPermission.
        :rtype: bool
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        r"""Sets the modify of this ListKeystoreSearchResponseBodyResultPermission.

        是否有修改权限

        :param modify: The modify of this ListKeystoreSearchResponseBodyResultPermission.
        :type modify: bool
        """
        self._modify = modify

    @property
    def usage(self):
        r"""Gets the usage of this ListKeystoreSearchResponseBodyResultPermission.

        是否有使用权限

        :return: The usage of this ListKeystoreSearchResponseBodyResultPermission.
        :rtype: bool
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ListKeystoreSearchResponseBodyResultPermission.

        是否有使用权限

        :param usage: The usage of this ListKeystoreSearchResponseBodyResultPermission.
        :type usage: bool
        """
        self._usage = usage

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
        if not isinstance(other, ListKeystoreSearchResponseBodyResultPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
