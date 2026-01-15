# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkipPreCheckInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skipped_precheck_list': 'list[str]',
        'skip_reason': 'str'
    }

    attribute_map = {
        'skipped_precheck_list': 'skipped_precheck_list',
        'skip_reason': 'skip_reason'
    }

    def __init__(self, skipped_precheck_list=None, skip_reason=None):
        r"""SkipPreCheckInfo

        The model defined in huaweicloud sdk

        :param skipped_precheck_list: 跳过的预检查项。 dstDbDiskSize：目标端磁盘可用大小是否支持 MysqlForeignKeyReferentialActionCheck：源端存在不支持的外键引用操作 MysqlSourceMaxAllowedPacketActionChecker：源库的max_allowed_packet参数值过小，可能会导致数据迁移失败 checkJobDbObjectInfo：对象选择信息检查 checkRecycleBinConsistent：回收站一致性检查 dbClockConsistency：时钟一致性校验 dbGroupConcatMaxLenConsistency：数据库参数group_concat_max_len一致性检查 dbIsolationLevelConsistency：事务隔离级别一致性校验 dbParamConsistency：结构迁移参数一致性校验 dbServerUuidConsistency：SERVER_UUID的一致性检查 dbTimeZoneConsistency：TIME_ZONE的一致性检查 dstMaxAllowedPacketCheck：增加预校验项检查目标库的max_allowed_packet参数 gtidFormatCheck：mysql源预检查GTID格式校验 innodbStrictModeConsistency：数据库参数INNODB_STRICT_MODE的一致性检查 isUserRequireSslLink：用户是否需要SSL mappedNameCheck：目标库对象命名约束检查 mysqlBlockEncryptionModeInconsistency：源库与目标库的参数block_encryption_mode不一致 rdsCreateDefaultPrimaryKeyConsistency：主备库是否开启隐式主键检查 sourceCheckDynamicMasking：源库脱敏检查 sourceEncryptTableActionChecker：源库加密表检查 sqlModeConsistency：数据库参数SQL_MODE的一致性检查 sqlModeNoEngine：目标库SQL_MODE中NO_ENGINE值检查 srcBinlogFormatCheck：源数据库binlog格式检查 srcBinlogRowImageCheck：源数据库参数binlog_row_image检查 srcDbBinlogExpireLogsDays：源库ExpireLogsDays参数检查 srcDbBinlogIsOff：源数据库二进制日志是否开启 srcDbExistUnsupportEngineTable：源数据库是否存在使用不支持的存储引擎的表 srcDbIndexKeyLength：原库索引列长度检查 srcDbIsStandbyTaurus：源库为Taurus备库检查 srcDbNameContainsUnsupportedSymbols：源数据库的库名是否合法 srcDbServerIdCheck：源数据库参数server_id的检查 srcDstTableNameCaseSensitiveCheck：源数据库和目标数据库表名大小写敏感性检查 srcGtidStatusCheck：源数据库GTID状态检查 srcHasLargeColumnTypeCheck：同步对象中是否存在包含longtext,longblob类型字段的表 srcIdentifierWithBreakCheck：源端表结构是否存在换行 srcTableNameContainsNonAscii：源数据库中有包含非ASCII字符的表名 srcTriggerAndEventCheck：识别到源端是否存在触发器/事件 srclogSlaveUpdatesCheck：源数据库参数slave_updates_check检查 targetCheckDynamicMasking：目标库脱敏检查 targetGtidStatusCheck：目标数据库GTID状态检查 tenantDbActionCheck：多租特性检查 userSelectObjectsCheck：选择对象预检查 dstStatusCheck：目标库实例状态是否正常 dstDbPrivilegesIsEnough：目标数据库用户权限是否足够 dstDbVersionSupport：目标数据库版本是否支持 srcDbVersionSupport：源数据库版本是否支持 dstDbConnection：目标数据库连接是否成功 srcDbConnection：源数据库连接是否成功 checkEmptyDstDb：目标库空库检查 srcDbPrivilegesIsEnoughForIncre：增量迁移,源数据库用户权限是否足够 srcHasNoPkTableWhenTgtHasInvisiblePk：源迁移库无主键表检查 userPrivilegeIsEnoughForDefiner：definer迁移权限检查
        :type skipped_precheck_list: list[str]
        :param skip_reason: 跳过预检查原因。
        :type skip_reason: str
        """
        
        

        self._skipped_precheck_list = None
        self._skip_reason = None
        self.discriminator = None

        self.skipped_precheck_list = skipped_precheck_list
        self.skip_reason = skip_reason

    @property
    def skipped_precheck_list(self):
        r"""Gets the skipped_precheck_list of this SkipPreCheckInfo.

        跳过的预检查项。 dstDbDiskSize：目标端磁盘可用大小是否支持 MysqlForeignKeyReferentialActionCheck：源端存在不支持的外键引用操作 MysqlSourceMaxAllowedPacketActionChecker：源库的max_allowed_packet参数值过小，可能会导致数据迁移失败 checkJobDbObjectInfo：对象选择信息检查 checkRecycleBinConsistent：回收站一致性检查 dbClockConsistency：时钟一致性校验 dbGroupConcatMaxLenConsistency：数据库参数group_concat_max_len一致性检查 dbIsolationLevelConsistency：事务隔离级别一致性校验 dbParamConsistency：结构迁移参数一致性校验 dbServerUuidConsistency：SERVER_UUID的一致性检查 dbTimeZoneConsistency：TIME_ZONE的一致性检查 dstMaxAllowedPacketCheck：增加预校验项检查目标库的max_allowed_packet参数 gtidFormatCheck：mysql源预检查GTID格式校验 innodbStrictModeConsistency：数据库参数INNODB_STRICT_MODE的一致性检查 isUserRequireSslLink：用户是否需要SSL mappedNameCheck：目标库对象命名约束检查 mysqlBlockEncryptionModeInconsistency：源库与目标库的参数block_encryption_mode不一致 rdsCreateDefaultPrimaryKeyConsistency：主备库是否开启隐式主键检查 sourceCheckDynamicMasking：源库脱敏检查 sourceEncryptTableActionChecker：源库加密表检查 sqlModeConsistency：数据库参数SQL_MODE的一致性检查 sqlModeNoEngine：目标库SQL_MODE中NO_ENGINE值检查 srcBinlogFormatCheck：源数据库binlog格式检查 srcBinlogRowImageCheck：源数据库参数binlog_row_image检查 srcDbBinlogExpireLogsDays：源库ExpireLogsDays参数检查 srcDbBinlogIsOff：源数据库二进制日志是否开启 srcDbExistUnsupportEngineTable：源数据库是否存在使用不支持的存储引擎的表 srcDbIndexKeyLength：原库索引列长度检查 srcDbIsStandbyTaurus：源库为Taurus备库检查 srcDbNameContainsUnsupportedSymbols：源数据库的库名是否合法 srcDbServerIdCheck：源数据库参数server_id的检查 srcDstTableNameCaseSensitiveCheck：源数据库和目标数据库表名大小写敏感性检查 srcGtidStatusCheck：源数据库GTID状态检查 srcHasLargeColumnTypeCheck：同步对象中是否存在包含longtext,longblob类型字段的表 srcIdentifierWithBreakCheck：源端表结构是否存在换行 srcTableNameContainsNonAscii：源数据库中有包含非ASCII字符的表名 srcTriggerAndEventCheck：识别到源端是否存在触发器/事件 srclogSlaveUpdatesCheck：源数据库参数slave_updates_check检查 targetCheckDynamicMasking：目标库脱敏检查 targetGtidStatusCheck：目标数据库GTID状态检查 tenantDbActionCheck：多租特性检查 userSelectObjectsCheck：选择对象预检查 dstStatusCheck：目标库实例状态是否正常 dstDbPrivilegesIsEnough：目标数据库用户权限是否足够 dstDbVersionSupport：目标数据库版本是否支持 srcDbVersionSupport：源数据库版本是否支持 dstDbConnection：目标数据库连接是否成功 srcDbConnection：源数据库连接是否成功 checkEmptyDstDb：目标库空库检查 srcDbPrivilegesIsEnoughForIncre：增量迁移,源数据库用户权限是否足够 srcHasNoPkTableWhenTgtHasInvisiblePk：源迁移库无主键表检查 userPrivilegeIsEnoughForDefiner：definer迁移权限检查

        :return: The skipped_precheck_list of this SkipPreCheckInfo.
        :rtype: list[str]
        """
        return self._skipped_precheck_list

    @skipped_precheck_list.setter
    def skipped_precheck_list(self, skipped_precheck_list):
        r"""Sets the skipped_precheck_list of this SkipPreCheckInfo.

        跳过的预检查项。 dstDbDiskSize：目标端磁盘可用大小是否支持 MysqlForeignKeyReferentialActionCheck：源端存在不支持的外键引用操作 MysqlSourceMaxAllowedPacketActionChecker：源库的max_allowed_packet参数值过小，可能会导致数据迁移失败 checkJobDbObjectInfo：对象选择信息检查 checkRecycleBinConsistent：回收站一致性检查 dbClockConsistency：时钟一致性校验 dbGroupConcatMaxLenConsistency：数据库参数group_concat_max_len一致性检查 dbIsolationLevelConsistency：事务隔离级别一致性校验 dbParamConsistency：结构迁移参数一致性校验 dbServerUuidConsistency：SERVER_UUID的一致性检查 dbTimeZoneConsistency：TIME_ZONE的一致性检查 dstMaxAllowedPacketCheck：增加预校验项检查目标库的max_allowed_packet参数 gtidFormatCheck：mysql源预检查GTID格式校验 innodbStrictModeConsistency：数据库参数INNODB_STRICT_MODE的一致性检查 isUserRequireSslLink：用户是否需要SSL mappedNameCheck：目标库对象命名约束检查 mysqlBlockEncryptionModeInconsistency：源库与目标库的参数block_encryption_mode不一致 rdsCreateDefaultPrimaryKeyConsistency：主备库是否开启隐式主键检查 sourceCheckDynamicMasking：源库脱敏检查 sourceEncryptTableActionChecker：源库加密表检查 sqlModeConsistency：数据库参数SQL_MODE的一致性检查 sqlModeNoEngine：目标库SQL_MODE中NO_ENGINE值检查 srcBinlogFormatCheck：源数据库binlog格式检查 srcBinlogRowImageCheck：源数据库参数binlog_row_image检查 srcDbBinlogExpireLogsDays：源库ExpireLogsDays参数检查 srcDbBinlogIsOff：源数据库二进制日志是否开启 srcDbExistUnsupportEngineTable：源数据库是否存在使用不支持的存储引擎的表 srcDbIndexKeyLength：原库索引列长度检查 srcDbIsStandbyTaurus：源库为Taurus备库检查 srcDbNameContainsUnsupportedSymbols：源数据库的库名是否合法 srcDbServerIdCheck：源数据库参数server_id的检查 srcDstTableNameCaseSensitiveCheck：源数据库和目标数据库表名大小写敏感性检查 srcGtidStatusCheck：源数据库GTID状态检查 srcHasLargeColumnTypeCheck：同步对象中是否存在包含longtext,longblob类型字段的表 srcIdentifierWithBreakCheck：源端表结构是否存在换行 srcTableNameContainsNonAscii：源数据库中有包含非ASCII字符的表名 srcTriggerAndEventCheck：识别到源端是否存在触发器/事件 srclogSlaveUpdatesCheck：源数据库参数slave_updates_check检查 targetCheckDynamicMasking：目标库脱敏检查 targetGtidStatusCheck：目标数据库GTID状态检查 tenantDbActionCheck：多租特性检查 userSelectObjectsCheck：选择对象预检查 dstStatusCheck：目标库实例状态是否正常 dstDbPrivilegesIsEnough：目标数据库用户权限是否足够 dstDbVersionSupport：目标数据库版本是否支持 srcDbVersionSupport：源数据库版本是否支持 dstDbConnection：目标数据库连接是否成功 srcDbConnection：源数据库连接是否成功 checkEmptyDstDb：目标库空库检查 srcDbPrivilegesIsEnoughForIncre：增量迁移,源数据库用户权限是否足够 srcHasNoPkTableWhenTgtHasInvisiblePk：源迁移库无主键表检查 userPrivilegeIsEnoughForDefiner：definer迁移权限检查

        :param skipped_precheck_list: The skipped_precheck_list of this SkipPreCheckInfo.
        :type skipped_precheck_list: list[str]
        """
        self._skipped_precheck_list = skipped_precheck_list

    @property
    def skip_reason(self):
        r"""Gets the skip_reason of this SkipPreCheckInfo.

        跳过预检查原因。

        :return: The skip_reason of this SkipPreCheckInfo.
        :rtype: str
        """
        return self._skip_reason

    @skip_reason.setter
    def skip_reason(self, skip_reason):
        r"""Sets the skip_reason of this SkipPreCheckInfo.

        跳过预检查原因。

        :param skip_reason: The skip_reason of this SkipPreCheckInfo.
        :type skip_reason: str
        """
        self._skip_reason = skip_reason

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SkipPreCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
