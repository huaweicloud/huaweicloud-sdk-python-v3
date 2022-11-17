# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'password': 'password'
    }

    def __init__(self, backup_id=None, password=None):
        """RestoreRequestBody

        The model defined in huaweicloud sdk

        :param backup_id: 备份文件名称。根据备份文件恢复到已有的实例。
        :type backup_id: str
        :param password: 实例密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。   - 不传入密码时，恢复后，备份文件中保留的密码将覆盖原有实例的密码。   - 传入密码时，恢复后，将使用该密码覆盖原有实例的密码。
        :type password: str
        """
        
        

        self._backup_id = None
        self._password = None
        self.discriminator = None

        self.backup_id = backup_id
        if password is not None:
            self.password = password

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreRequestBody.

        备份文件名称。根据备份文件恢复到已有的实例。

        :return: The backup_id of this RestoreRequestBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreRequestBody.

        备份文件名称。根据备份文件恢复到已有的实例。

        :param backup_id: The backup_id of this RestoreRequestBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def password(self):
        """Gets the password of this RestoreRequestBody.

        实例密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。   - 不传入密码时，恢复后，备份文件中保留的密码将覆盖原有实例的密码。   - 传入密码时，恢复后，将使用该密码覆盖原有实例的密码。

        :return: The password of this RestoreRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RestoreRequestBody.

        实例密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。   - 不传入密码时，恢复后，备份文件中保留的密码将覆盖原有实例的密码。   - 传入密码时，恢复后，将使用该密码覆盖原有实例的密码。

        :param password: The password of this RestoreRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, RestoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
