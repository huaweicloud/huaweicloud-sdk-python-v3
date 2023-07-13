# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManualBackupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'name': 'str',
        'description': 'str',
        'databases': 'list[BackupDatabase]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'description': 'description',
        'databases': 'databases'
    }

    def __init__(self, instance_id=None, name=None, description=None, databases=None):
        """CreateManualBackupRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param name: 备份名称，4~64个字符，必须以英文字母开头，区分大小写，可以包含英文字母、数字、中划线或者下划线，不能包含其他特殊字符。
        :type name: str
        :param description: 备份描述，不能包含&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符，不大于256个字符。
        :type description: str
        :param databases: 只支持Microsoft SQL Server，局部备份的用户自建数据库名列表，当有此参数时以局部备份为准。
        :type databases: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        """
        
        

        self._instance_id = None
        self._name = None
        self._description = None
        self._databases = None
        self.discriminator = None

        self.instance_id = instance_id
        self.name = name
        if description is not None:
            self.description = description
        if databases is not None:
            self.databases = databases

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateManualBackupRequestBody.

        实例ID。

        :return: The instance_id of this CreateManualBackupRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateManualBackupRequestBody.

        实例ID。

        :param instance_id: The instance_id of this CreateManualBackupRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this CreateManualBackupRequestBody.

        备份名称，4~64个字符，必须以英文字母开头，区分大小写，可以包含英文字母、数字、中划线或者下划线，不能包含其他特殊字符。

        :return: The name of this CreateManualBackupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateManualBackupRequestBody.

        备份名称，4~64个字符，必须以英文字母开头，区分大小写，可以包含英文字母、数字、中划线或者下划线，不能包含其他特殊字符。

        :param name: The name of this CreateManualBackupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateManualBackupRequestBody.

        备份描述，不能包含>!<\"&'=特殊字符，不大于256个字符。

        :return: The description of this CreateManualBackupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateManualBackupRequestBody.

        备份描述，不能包含>!<\"&'=特殊字符，不大于256个字符。

        :param description: The description of this CreateManualBackupRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def databases(self):
        """Gets the databases of this CreateManualBackupRequestBody.

        只支持Microsoft SQL Server，局部备份的用户自建数据库名列表，当有此参数时以局部备份为准。

        :return: The databases of this CreateManualBackupRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this CreateManualBackupRequestBody.

        只支持Microsoft SQL Server，局部备份的用户自建数据库名列表，当有此参数时以局部备份为准。

        :param databases: The databases of this CreateManualBackupRequestBody.
        :type databases: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        """
        self._databases = databases

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
        if not isinstance(other, CreateManualBackupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
