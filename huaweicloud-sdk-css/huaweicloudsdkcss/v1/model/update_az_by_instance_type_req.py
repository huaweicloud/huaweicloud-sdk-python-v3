# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAzByInstanceTypeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_az': 'str',
        'target_az': 'str',
        'migrate_type': 'str',
        'agency': 'str',
        'indices_backup_check': 'bool'
    }

    attribute_map = {
        'source_az': 'source_az',
        'target_az': 'target_az',
        'migrate_type': 'migrate_type',
        'agency': 'agency',
        'indices_backup_check': 'indices_backup_check'
    }

    def __init__(self, source_az=None, target_az=None, migrate_type=None, agency=None, indices_backup_check=None):
        r"""UpdateAzByInstanceTypeReq

        The model defined in huaweicloud sdk

        :param source_az: 节点当前所在AZ。
        :type source_az: str
        :param target_az: 期望节点最终分布AZ。
        :type target_az: str
        :param migrate_type: AZ迁移方式： - multi_az_change：高可用改造。 - az_migrate： AZ平移
        :type migrate_type: str
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param indices_backup_check: 是否进行全量索引快照备份检测。 true：进行全量索引快照备份检测。 false：不进行全量索引快照备份检测。
        :type indices_backup_check: bool
        """
        
        

        self._source_az = None
        self._target_az = None
        self._migrate_type = None
        self._agency = None
        self._indices_backup_check = None
        self.discriminator = None

        self.source_az = source_az
        self.target_az = target_az
        self.migrate_type = migrate_type
        self.agency = agency
        if indices_backup_check is not None:
            self.indices_backup_check = indices_backup_check

    @property
    def source_az(self):
        r"""Gets the source_az of this UpdateAzByInstanceTypeReq.

        节点当前所在AZ。

        :return: The source_az of this UpdateAzByInstanceTypeReq.
        :rtype: str
        """
        return self._source_az

    @source_az.setter
    def source_az(self, source_az):
        r"""Sets the source_az of this UpdateAzByInstanceTypeReq.

        节点当前所在AZ。

        :param source_az: The source_az of this UpdateAzByInstanceTypeReq.
        :type source_az: str
        """
        self._source_az = source_az

    @property
    def target_az(self):
        r"""Gets the target_az of this UpdateAzByInstanceTypeReq.

        期望节点最终分布AZ。

        :return: The target_az of this UpdateAzByInstanceTypeReq.
        :rtype: str
        """
        return self._target_az

    @target_az.setter
    def target_az(self, target_az):
        r"""Sets the target_az of this UpdateAzByInstanceTypeReq.

        期望节点最终分布AZ。

        :param target_az: The target_az of this UpdateAzByInstanceTypeReq.
        :type target_az: str
        """
        self._target_az = target_az

    @property
    def migrate_type(self):
        r"""Gets the migrate_type of this UpdateAzByInstanceTypeReq.

        AZ迁移方式： - multi_az_change：高可用改造。 - az_migrate： AZ平移

        :return: The migrate_type of this UpdateAzByInstanceTypeReq.
        :rtype: str
        """
        return self._migrate_type

    @migrate_type.setter
    def migrate_type(self, migrate_type):
        r"""Sets the migrate_type of this UpdateAzByInstanceTypeReq.

        AZ迁移方式： - multi_az_change：高可用改造。 - az_migrate： AZ平移

        :param migrate_type: The migrate_type of this UpdateAzByInstanceTypeReq.
        :type migrate_type: str
        """
        self._migrate_type = migrate_type

    @property
    def agency(self):
        r"""Gets the agency of this UpdateAzByInstanceTypeReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpdateAzByInstanceTypeReq.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpdateAzByInstanceTypeReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpdateAzByInstanceTypeReq.
        :type agency: str
        """
        self._agency = agency

    @property
    def indices_backup_check(self):
        r"""Gets the indices_backup_check of this UpdateAzByInstanceTypeReq.

        是否进行全量索引快照备份检测。 true：进行全量索引快照备份检测。 false：不进行全量索引快照备份检测。

        :return: The indices_backup_check of this UpdateAzByInstanceTypeReq.
        :rtype: bool
        """
        return self._indices_backup_check

    @indices_backup_check.setter
    def indices_backup_check(self, indices_backup_check):
        r"""Sets the indices_backup_check of this UpdateAzByInstanceTypeReq.

        是否进行全量索引快照备份检测。 true：进行全量索引快照备份检测。 false：不进行全量索引快照备份检测。

        :param indices_backup_check: The indices_backup_check of this UpdateAzByInstanceTypeReq.
        :type indices_backup_check: bool
        """
        self._indices_backup_check = indices_backup_check

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
        if not isinstance(other, UpdateAzByInstanceTypeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
