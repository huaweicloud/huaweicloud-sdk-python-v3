# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetOnlineMigrationTaskBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'migration_method': 'str',
        'resume_mode': 'str',
        'bandwidth_limit_mb': 'str',
        'source_instance': 'ConfigMigrationInstanceBody',
        'target_instance': 'ConfigMigrationInstanceBody'
    }

    attribute_map = {
        'migration_method': 'migration_method',
        'resume_mode': 'resume_mode',
        'bandwidth_limit_mb': 'bandwidth_limit_mb',
        'source_instance': 'source_instance',
        'target_instance': 'target_instance'
    }

    def __init__(self, migration_method=None, resume_mode=None, bandwidth_limit_mb=None, source_instance=None, target_instance=None):
        """SetOnlineMigrationTaskBody

        The model defined in huaweicloud sdk

        :param migration_method: 迁移方式，包括全量迁移和增量迁移两种类型。 - 全量迁移：该模式为Redis的一次性迁移，适用于可中断业务的迁移场景。   全量迁移过程中，如果源Redis有数据更新，这部分更新数据不会被迁移到目标Redis。 - 增量迁移：该模式为Redis的持续性迁移，适用于对业务中断敏感的迁移场景。   增量迁移阶段通过解析日志等技术， 持续保持源Redis和目标端Redis的数据一致。 取值范围： - full_amount_migration：表示全量迁移。 - incremental_migration：表示增量迁移。 
        :type migration_method: str
        :param resume_mode: 自动重连，根据参数决定是否自动重连。 自动重连模式在遇到网络等异常情况时，会无限自动重试。 自动重连模式在无法进行增量同步时，会触发全量同步，增加带宽占用，请谨慎选择。 取值范围： - auto：自动重连。 - manual：手动重连。 
        :type resume_mode: str
        :param bandwidth_limit_mb: 带宽限制，当迁移方式为增量迁移时，为保证业务正常运行，您可以启用带宽限制功能，当数据同步速度达到带宽限制时，将限制同步速度的继续增长。 -限制为MB/s -取值范围：1-10,241(大于0小于10,241的整数)
        :type bandwidth_limit_mb: str
        :param source_instance: 
        :type source_instance: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        :param target_instance: 
        :type target_instance: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        """
        
        

        self._migration_method = None
        self._resume_mode = None
        self._bandwidth_limit_mb = None
        self._source_instance = None
        self._target_instance = None
        self.discriminator = None

        self.migration_method = migration_method
        self.resume_mode = resume_mode
        if bandwidth_limit_mb is not None:
            self.bandwidth_limit_mb = bandwidth_limit_mb
        self.source_instance = source_instance
        self.target_instance = target_instance

    @property
    def migration_method(self):
        """Gets the migration_method of this SetOnlineMigrationTaskBody.

        迁移方式，包括全量迁移和增量迁移两种类型。 - 全量迁移：该模式为Redis的一次性迁移，适用于可中断业务的迁移场景。   全量迁移过程中，如果源Redis有数据更新，这部分更新数据不会被迁移到目标Redis。 - 增量迁移：该模式为Redis的持续性迁移，适用于对业务中断敏感的迁移场景。   增量迁移阶段通过解析日志等技术， 持续保持源Redis和目标端Redis的数据一致。 取值范围： - full_amount_migration：表示全量迁移。 - incremental_migration：表示增量迁移。 

        :return: The migration_method of this SetOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._migration_method

    @migration_method.setter
    def migration_method(self, migration_method):
        """Sets the migration_method of this SetOnlineMigrationTaskBody.

        迁移方式，包括全量迁移和增量迁移两种类型。 - 全量迁移：该模式为Redis的一次性迁移，适用于可中断业务的迁移场景。   全量迁移过程中，如果源Redis有数据更新，这部分更新数据不会被迁移到目标Redis。 - 增量迁移：该模式为Redis的持续性迁移，适用于对业务中断敏感的迁移场景。   增量迁移阶段通过解析日志等技术， 持续保持源Redis和目标端Redis的数据一致。 取值范围： - full_amount_migration：表示全量迁移。 - incremental_migration：表示增量迁移。 

        :param migration_method: The migration_method of this SetOnlineMigrationTaskBody.
        :type migration_method: str
        """
        self._migration_method = migration_method

    @property
    def resume_mode(self):
        """Gets the resume_mode of this SetOnlineMigrationTaskBody.

        自动重连，根据参数决定是否自动重连。 自动重连模式在遇到网络等异常情况时，会无限自动重试。 自动重连模式在无法进行增量同步时，会触发全量同步，增加带宽占用，请谨慎选择。 取值范围： - auto：自动重连。 - manual：手动重连。 

        :return: The resume_mode of this SetOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._resume_mode

    @resume_mode.setter
    def resume_mode(self, resume_mode):
        """Sets the resume_mode of this SetOnlineMigrationTaskBody.

        自动重连，根据参数决定是否自动重连。 自动重连模式在遇到网络等异常情况时，会无限自动重试。 自动重连模式在无法进行增量同步时，会触发全量同步，增加带宽占用，请谨慎选择。 取值范围： - auto：自动重连。 - manual：手动重连。 

        :param resume_mode: The resume_mode of this SetOnlineMigrationTaskBody.
        :type resume_mode: str
        """
        self._resume_mode = resume_mode

    @property
    def bandwidth_limit_mb(self):
        """Gets the bandwidth_limit_mb of this SetOnlineMigrationTaskBody.

        带宽限制，当迁移方式为增量迁移时，为保证业务正常运行，您可以启用带宽限制功能，当数据同步速度达到带宽限制时，将限制同步速度的继续增长。 -限制为MB/s -取值范围：1-10,241(大于0小于10,241的整数)

        :return: The bandwidth_limit_mb of this SetOnlineMigrationTaskBody.
        :rtype: str
        """
        return self._bandwidth_limit_mb

    @bandwidth_limit_mb.setter
    def bandwidth_limit_mb(self, bandwidth_limit_mb):
        """Sets the bandwidth_limit_mb of this SetOnlineMigrationTaskBody.

        带宽限制，当迁移方式为增量迁移时，为保证业务正常运行，您可以启用带宽限制功能，当数据同步速度达到带宽限制时，将限制同步速度的继续增长。 -限制为MB/s -取值范围：1-10,241(大于0小于10,241的整数)

        :param bandwidth_limit_mb: The bandwidth_limit_mb of this SetOnlineMigrationTaskBody.
        :type bandwidth_limit_mb: str
        """
        self._bandwidth_limit_mb = bandwidth_limit_mb

    @property
    def source_instance(self):
        """Gets the source_instance of this SetOnlineMigrationTaskBody.


        :return: The source_instance of this SetOnlineMigrationTaskBody.
        :rtype: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        """
        return self._source_instance

    @source_instance.setter
    def source_instance(self, source_instance):
        """Sets the source_instance of this SetOnlineMigrationTaskBody.


        :param source_instance: The source_instance of this SetOnlineMigrationTaskBody.
        :type source_instance: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        """
        self._source_instance = source_instance

    @property
    def target_instance(self):
        """Gets the target_instance of this SetOnlineMigrationTaskBody.


        :return: The target_instance of this SetOnlineMigrationTaskBody.
        :rtype: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        """
        return self._target_instance

    @target_instance.setter
    def target_instance(self, target_instance):
        """Sets the target_instance of this SetOnlineMigrationTaskBody.


        :param target_instance: The target_instance of this SetOnlineMigrationTaskBody.
        :type target_instance: :class:`huaweicloudsdkdcs.v2.ConfigMigrationInstanceBody`
        """
        self._target_instance = target_instance

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
        if not isinstance(other, SetOnlineMigrationTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
