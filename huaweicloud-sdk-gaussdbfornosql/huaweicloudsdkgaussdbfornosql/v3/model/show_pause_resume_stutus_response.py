# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPauseResumeStutusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_instance_id': 'str',
        'slave_instance_id': 'str',
        'status': 'str',
        'data_sync_indicators': 'NoSQLDrDateSyncIndicators',
        'rto_and_rpo_indicators': 'list[NoSQLDrRpoAndRto]'
    }

    attribute_map = {
        'master_instance_id': 'master_instance_id',
        'slave_instance_id': 'slave_instance_id',
        'status': 'status',
        'data_sync_indicators': 'data_sync_indicators',
        'rto_and_rpo_indicators': 'rto_and_rpo_indicators'
    }

    def __init__(self, master_instance_id=None, slave_instance_id=None, status=None, data_sync_indicators=None, rto_and_rpo_indicators=None):
        """ShowPauseResumeStutusResponse

        The model defined in huaweicloud sdk

        :param master_instance_id: 主实例id
        :type master_instance_id: str
        :param slave_instance_id: 备实例id
        :type slave_instance_id: str
        :param status: 容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步
        :type status: str
        :param data_sync_indicators: 
        :type data_sync_indicators: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrDateSyncIndicators`
        :param rto_and_rpo_indicators: 切换或倒换RPO和RTO值，仅当请求实例id为主实例时有值
        :type rto_and_rpo_indicators: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrRpoAndRto`]
        """
        
        super(ShowPauseResumeStutusResponse, self).__init__()

        self._master_instance_id = None
        self._slave_instance_id = None
        self._status = None
        self._data_sync_indicators = None
        self._rto_and_rpo_indicators = None
        self.discriminator = None

        if master_instance_id is not None:
            self.master_instance_id = master_instance_id
        if slave_instance_id is not None:
            self.slave_instance_id = slave_instance_id
        if status is not None:
            self.status = status
        if data_sync_indicators is not None:
            self.data_sync_indicators = data_sync_indicators
        if rto_and_rpo_indicators is not None:
            self.rto_and_rpo_indicators = rto_and_rpo_indicators

    @property
    def master_instance_id(self):
        """Gets the master_instance_id of this ShowPauseResumeStutusResponse.

        主实例id

        :return: The master_instance_id of this ShowPauseResumeStutusResponse.
        :rtype: str
        """
        return self._master_instance_id

    @master_instance_id.setter
    def master_instance_id(self, master_instance_id):
        """Sets the master_instance_id of this ShowPauseResumeStutusResponse.

        主实例id

        :param master_instance_id: The master_instance_id of this ShowPauseResumeStutusResponse.
        :type master_instance_id: str
        """
        self._master_instance_id = master_instance_id

    @property
    def slave_instance_id(self):
        """Gets the slave_instance_id of this ShowPauseResumeStutusResponse.

        备实例id

        :return: The slave_instance_id of this ShowPauseResumeStutusResponse.
        :rtype: str
        """
        return self._slave_instance_id

    @slave_instance_id.setter
    def slave_instance_id(self, slave_instance_id):
        """Sets the slave_instance_id of this ShowPauseResumeStutusResponse.

        备实例id

        :param slave_instance_id: The slave_instance_id of this ShowPauseResumeStutusResponse.
        :type slave_instance_id: str
        """
        self._slave_instance_id = slave_instance_id

    @property
    def status(self):
        """Gets the status of this ShowPauseResumeStutusResponse.

        容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步

        :return: The status of this ShowPauseResumeStutusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowPauseResumeStutusResponse.

        容灾实例数据同步状态 - NA：实例尚未搭建容灾关系 - NEW：尚未启动的数据同步状态 - SYNCING：数据同步正常进行中 - SUSPENDING：正在暂停数据同步 - SUSPENDED：数据同步已暂停 - RECOVERYING：正在恢复数据同步

        :param status: The status of this ShowPauseResumeStutusResponse.
        :type status: str
        """
        self._status = status

    @property
    def data_sync_indicators(self):
        """Gets the data_sync_indicators of this ShowPauseResumeStutusResponse.

        :return: The data_sync_indicators of this ShowPauseResumeStutusResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrDateSyncIndicators`
        """
        return self._data_sync_indicators

    @data_sync_indicators.setter
    def data_sync_indicators(self, data_sync_indicators):
        """Sets the data_sync_indicators of this ShowPauseResumeStutusResponse.

        :param data_sync_indicators: The data_sync_indicators of this ShowPauseResumeStutusResponse.
        :type data_sync_indicators: :class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrDateSyncIndicators`
        """
        self._data_sync_indicators = data_sync_indicators

    @property
    def rto_and_rpo_indicators(self):
        """Gets the rto_and_rpo_indicators of this ShowPauseResumeStutusResponse.

        切换或倒换RPO和RTO值，仅当请求实例id为主实例时有值

        :return: The rto_and_rpo_indicators of this ShowPauseResumeStutusResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrRpoAndRto`]
        """
        return self._rto_and_rpo_indicators

    @rto_and_rpo_indicators.setter
    def rto_and_rpo_indicators(self, rto_and_rpo_indicators):
        """Sets the rto_and_rpo_indicators of this ShowPauseResumeStutusResponse.

        切换或倒换RPO和RTO值，仅当请求实例id为主实例时有值

        :param rto_and_rpo_indicators: The rto_and_rpo_indicators of this ShowPauseResumeStutusResponse.
        :type rto_and_rpo_indicators: list[:class:`huaweicloudsdkgaussdbfornosql.v3.NoSQLDrRpoAndRto`]
        """
        self._rto_and_rpo_indicators = rto_and_rpo_indicators

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
        if not isinstance(other, ShowPauseResumeStutusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
