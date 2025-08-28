# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulBackupStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_info_id': 'str',
        'backup_host_num': 'int',
        'unable_backup_host_num': 'int'
    }

    attribute_map = {
        'backup_info_id': 'backup_info_id',
        'backup_host_num': 'backup_host_num',
        'unable_backup_host_num': 'unable_backup_host_num'
    }

    def __init__(self, backup_info_id=None, backup_host_num=None, unable_backup_host_num=None):
        r"""ShowVulBackupStatisticsResponse

        The model defined in huaweicloud sdk

        :param backup_info_id: **参数解释**: 本次漏洞处理的备份信息id **取值范围**: 字符长度1-128位 
        :type backup_info_id: str
        :param backup_host_num: **参数解释**: 本次漏洞处理可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 
        :type backup_host_num: int
        :param unable_backup_host_num: **参数解释**: 本次漏洞处理不可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 
        :type unable_backup_host_num: int
        """
        
        super(ShowVulBackupStatisticsResponse, self).__init__()

        self._backup_info_id = None
        self._backup_host_num = None
        self._unable_backup_host_num = None
        self.discriminator = None

        if backup_info_id is not None:
            self.backup_info_id = backup_info_id
        if backup_host_num is not None:
            self.backup_host_num = backup_host_num
        if unable_backup_host_num is not None:
            self.unable_backup_host_num = unable_backup_host_num

    @property
    def backup_info_id(self):
        r"""Gets the backup_info_id of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理的备份信息id **取值范围**: 字符长度1-128位 

        :return: The backup_info_id of this ShowVulBackupStatisticsResponse.
        :rtype: str
        """
        return self._backup_info_id

    @backup_info_id.setter
    def backup_info_id(self, backup_info_id):
        r"""Sets the backup_info_id of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理的备份信息id **取值范围**: 字符长度1-128位 

        :param backup_info_id: The backup_info_id of this ShowVulBackupStatisticsResponse.
        :type backup_info_id: str
        """
        self._backup_info_id = backup_info_id

    @property
    def backup_host_num(self):
        r"""Gets the backup_host_num of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 

        :return: The backup_host_num of this ShowVulBackupStatisticsResponse.
        :rtype: int
        """
        return self._backup_host_num

    @backup_host_num.setter
    def backup_host_num(self, backup_host_num):
        r"""Sets the backup_host_num of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 

        :param backup_host_num: The backup_host_num of this ShowVulBackupStatisticsResponse.
        :type backup_host_num: int
        """
        self._backup_host_num = backup_host_num

    @property
    def unable_backup_host_num(self):
        r"""Gets the unable_backup_host_num of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理不可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 

        :return: The unable_backup_host_num of this ShowVulBackupStatisticsResponse.
        :rtype: int
        """
        return self._unable_backup_host_num

    @unable_backup_host_num.setter
    def unable_backup_host_num(self, unable_backup_host_num):
        r"""Sets the unable_backup_host_num of this ShowVulBackupStatisticsResponse.

        **参数解释**: 本次漏洞处理不可进行备份的主机数量 **取值范围**: 字符长度0-1000000位 

        :param unable_backup_host_num: The unable_backup_host_num of this ShowVulBackupStatisticsResponse.
        :type unable_backup_host_num: int
        """
        self._unable_backup_host_num = unable_backup_host_num

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
        if not isinstance(other, ShowVulBackupStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
