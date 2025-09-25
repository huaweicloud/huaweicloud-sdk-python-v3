# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlStartRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'save_days': 'int',
        'storage_mode': 'str',
        'is_exclude_sys_user': 'bool',
        'lts_config': 'LtsInfoOption',
        'sql_type_range': 'list[SqlTypeConfigOption]'
    }

    attribute_map = {
        'save_days': 'save_days',
        'storage_mode': 'storage_mode',
        'is_exclude_sys_user': 'is_exclude_sys_user',
        'lts_config': 'lts_config',
        'sql_type_range': 'sql_type_range'
    }

    def __init__(self, save_days=None, storage_mode=None, is_exclude_sys_user=None, lts_config=None, sql_type_range=None):
        r"""FullSqlStartRequestBody

        The model defined in huaweicloud sdk

        :param save_days: **参数解释**: 全量SQL采集数据最大保留天数。 **约束限制**: 不涉及。 **取值范围**: [1, 30] **默认取值**: 不涉及。
        :type save_days: int
        :param storage_mode: **参数解释**: 存储类型。 **约束限制**: 公有云场景，只支持LTS云日志服务存储。 **取值范围**: - LTS：LTS云日志服务。  **默认取值**: 不涉及。
        :type storage_mode: str
        :param is_exclude_sys_user: **参数解释**: 是否过滤系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：过滤系统用户。 - false：不过滤系统用户。  **默认取值**: 不涉及。
        :type is_exclude_sys_user: bool
        :param lts_config: 
        :type lts_config: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsInfoOption`
        :param sql_type_range: **参数解释**: SQL采集类型列表。默认取值[]，表示采集所有SQL语句。 **约束限制**: 不涉及。
        :type sql_type_range: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeConfigOption`]
        """
        
        

        self._save_days = None
        self._storage_mode = None
        self._is_exclude_sys_user = None
        self._lts_config = None
        self._sql_type_range = None
        self.discriminator = None

        self.save_days = save_days
        self.storage_mode = storage_mode
        if is_exclude_sys_user is not None:
            self.is_exclude_sys_user = is_exclude_sys_user
        self.lts_config = lts_config
        if sql_type_range is not None:
            self.sql_type_range = sql_type_range

    @property
    def save_days(self):
        r"""Gets the save_days of this FullSqlStartRequestBody.

        **参数解释**: 全量SQL采集数据最大保留天数。 **约束限制**: 不涉及。 **取值范围**: [1, 30] **默认取值**: 不涉及。

        :return: The save_days of this FullSqlStartRequestBody.
        :rtype: int
        """
        return self._save_days

    @save_days.setter
    def save_days(self, save_days):
        r"""Sets the save_days of this FullSqlStartRequestBody.

        **参数解释**: 全量SQL采集数据最大保留天数。 **约束限制**: 不涉及。 **取值范围**: [1, 30] **默认取值**: 不涉及。

        :param save_days: The save_days of this FullSqlStartRequestBody.
        :type save_days: int
        """
        self._save_days = save_days

    @property
    def storage_mode(self):
        r"""Gets the storage_mode of this FullSqlStartRequestBody.

        **参数解释**: 存储类型。 **约束限制**: 公有云场景，只支持LTS云日志服务存储。 **取值范围**: - LTS：LTS云日志服务。  **默认取值**: 不涉及。

        :return: The storage_mode of this FullSqlStartRequestBody.
        :rtype: str
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        r"""Sets the storage_mode of this FullSqlStartRequestBody.

        **参数解释**: 存储类型。 **约束限制**: 公有云场景，只支持LTS云日志服务存储。 **取值范围**: - LTS：LTS云日志服务。  **默认取值**: 不涉及。

        :param storage_mode: The storage_mode of this FullSqlStartRequestBody.
        :type storage_mode: str
        """
        self._storage_mode = storage_mode

    @property
    def is_exclude_sys_user(self):
        r"""Gets the is_exclude_sys_user of this FullSqlStartRequestBody.

        **参数解释**: 是否过滤系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：过滤系统用户。 - false：不过滤系统用户。  **默认取值**: 不涉及。

        :return: The is_exclude_sys_user of this FullSqlStartRequestBody.
        :rtype: bool
        """
        return self._is_exclude_sys_user

    @is_exclude_sys_user.setter
    def is_exclude_sys_user(self, is_exclude_sys_user):
        r"""Sets the is_exclude_sys_user of this FullSqlStartRequestBody.

        **参数解释**: 是否过滤系统用户。 **约束限制**: 不涉及。 **取值范围**: - true：过滤系统用户。 - false：不过滤系统用户。  **默认取值**: 不涉及。

        :param is_exclude_sys_user: The is_exclude_sys_user of this FullSqlStartRequestBody.
        :type is_exclude_sys_user: bool
        """
        self._is_exclude_sys_user = is_exclude_sys_user

    @property
    def lts_config(self):
        r"""Gets the lts_config of this FullSqlStartRequestBody.

        :return: The lts_config of this FullSqlStartRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsInfoOption`
        """
        return self._lts_config

    @lts_config.setter
    def lts_config(self, lts_config):
        r"""Sets the lts_config of this FullSqlStartRequestBody.

        :param lts_config: The lts_config of this FullSqlStartRequestBody.
        :type lts_config: :class:`huaweicloudsdkgaussdbforopengauss.v3.LtsInfoOption`
        """
        self._lts_config = lts_config

    @property
    def sql_type_range(self):
        r"""Gets the sql_type_range of this FullSqlStartRequestBody.

        **参数解释**: SQL采集类型列表。默认取值[]，表示采集所有SQL语句。 **约束限制**: 不涉及。

        :return: The sql_type_range of this FullSqlStartRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeConfigOption`]
        """
        return self._sql_type_range

    @sql_type_range.setter
    def sql_type_range(self, sql_type_range):
        r"""Sets the sql_type_range of this FullSqlStartRequestBody.

        **参数解释**: SQL采集类型列表。默认取值[]，表示采集所有SQL语句。 **约束限制**: 不涉及。

        :param sql_type_range: The sql_type_range of this FullSqlStartRequestBody.
        :type sql_type_range: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlTypeConfigOption`]
        """
        self._sql_type_range = sql_type_range

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
        if not isinstance(other, FullSqlStartRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
