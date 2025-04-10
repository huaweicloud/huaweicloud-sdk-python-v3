# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreDatabaseInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'int',
        'instance_id': 'str',
        'is_fast_restore': 'bool',
        'databases': 'list[RestoreDatabaseInfo]'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'instance_id': 'instance_id',
        'is_fast_restore': 'is_fast_restore',
        'databases': 'databases'
    }

    def __init__(self, restore_time=None, instance_id=None, is_fast_restore=None, databases=None):
        r"""RestoreDatabaseInstance

        The model defined in huaweicloud sdk

        :param restore_time: 恢复时间
        :type restore_time: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param is_fast_restore: 是否使用极速恢复，可先根据”获取实例是否能使用极速恢复“接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！
        :type is_fast_restore: bool
        :param databases: 库信息
        :type databases: list[:class:`huaweicloudsdkrds.v3.RestoreDatabaseInfo`]
        """
        
        

        self._restore_time = None
        self._instance_id = None
        self._is_fast_restore = None
        self._databases = None
        self.discriminator = None

        self.restore_time = restore_time
        self.instance_id = instance_id
        if is_fast_restore is not None:
            self.is_fast_restore = is_fast_restore
        self.databases = databases

    @property
    def restore_time(self):
        r"""Gets the restore_time of this RestoreDatabaseInstance.

        恢复时间

        :return: The restore_time of this RestoreDatabaseInstance.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this RestoreDatabaseInstance.

        恢复时间

        :param restore_time: The restore_time of this RestoreDatabaseInstance.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RestoreDatabaseInstance.

        实例ID

        :return: The instance_id of this RestoreDatabaseInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RestoreDatabaseInstance.

        实例ID

        :param instance_id: The instance_id of this RestoreDatabaseInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_fast_restore(self):
        r"""Gets the is_fast_restore of this RestoreDatabaseInstance.

        是否使用极速恢复，可先根据”获取实例是否能使用极速恢复“接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！

        :return: The is_fast_restore of this RestoreDatabaseInstance.
        :rtype: bool
        """
        return self._is_fast_restore

    @is_fast_restore.setter
    def is_fast_restore(self, is_fast_restore):
        r"""Sets the is_fast_restore of this RestoreDatabaseInstance.

        是否使用极速恢复，可先根据”获取实例是否能使用极速恢复“接口判断本次恢复是否能使用极速恢复。 如果实例使用了XA事务，采用极速恢复的方式会导致恢复失败！

        :param is_fast_restore: The is_fast_restore of this RestoreDatabaseInstance.
        :type is_fast_restore: bool
        """
        self._is_fast_restore = is_fast_restore

    @property
    def databases(self):
        r"""Gets the databases of this RestoreDatabaseInstance.

        库信息

        :return: The databases of this RestoreDatabaseInstance.
        :rtype: list[:class:`huaweicloudsdkrds.v3.RestoreDatabaseInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this RestoreDatabaseInstance.

        库信息

        :param databases: The databases of this RestoreDatabaseInstance.
        :type databases: list[:class:`huaweicloudsdkrds.v3.RestoreDatabaseInfo`]
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
        if not isinstance(other, RestoreDatabaseInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
