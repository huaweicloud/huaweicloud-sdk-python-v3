# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSqlCreateBackupRequestBody:

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
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, name=None, description=None):
        """NoSqlCreateBackupRequestBody

        The model defined in huaweicloud sdk

        :param name: 手动备份名称。  取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。
        :type name: str
        :param description: 手动备份描述。  取值范围：长度不超过256位，且不能包含&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符。
        :type description: str
        """
        
        

        self._name = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.description = description

    @property
    def name(self):
        """Gets the name of this NoSqlCreateBackupRequestBody.

        手动备份名称。  取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :return: The name of this NoSqlCreateBackupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NoSqlCreateBackupRequestBody.

        手动备份名称。  取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :param name: The name of this NoSqlCreateBackupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NoSqlCreateBackupRequestBody.

        手动备份描述。  取值范围：长度不超过256位，且不能包含>!<\"&'=特殊字符。

        :return: The description of this NoSqlCreateBackupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NoSqlCreateBackupRequestBody.

        手动备份描述。  取值范围：长度不超过256位，且不能包含>!<\"&'=特殊字符。

        :param description: The description of this NoSqlCreateBackupRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, NoSqlCreateBackupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
