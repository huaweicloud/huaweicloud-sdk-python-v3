# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DdlAlarmResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'seqno': 'int',
        'checkpoint': 'str',
        'status': 'int',
        'ddl_timestamp': 'int',
        'ddl_text': 'str',
        'exe_result': 'bool',
        'record_time': 'int',
        'clean_time': 'int'
    }

    attribute_map = {
        'seqno': 'seqno',
        'checkpoint': 'checkpoint',
        'status': 'status',
        'ddl_timestamp': 'ddl_timestamp',
        'ddl_text': 'ddl_text',
        'exe_result': 'exe_result',
        'record_time': 'record_time',
        'clean_time': 'clean_time'
    }

    def __init__(self, seqno=None, checkpoint=None, status=None, ddl_timestamp=None, ddl_text=None, exe_result=None, record_time=None, clean_time=None):
        r"""DdlAlarmResp

        The model defined in huaweicloud sdk

        :param seqno: 记录唯一序号。
        :type seqno: int
        :param checkpoint: 数据源库位点。
        :type checkpoint: str
        :param status: DDL告警状态。0无告警，1告警中。
        :type status: int
        :param ddl_timestamp: DDL在源库执行时间。
        :type ddl_timestamp: int
        :param ddl_text: DDL内容。
        :type ddl_text: str
        :param exe_result: DDL执行结果。false执行失败，true执行成功。
        :type exe_result: bool
        :param record_time: 数据记录时间。
        :type record_time: int
        :param clean_time: DDL告警清理时间。
        :type clean_time: int
        """
        
        

        self._seqno = None
        self._checkpoint = None
        self._status = None
        self._ddl_timestamp = None
        self._ddl_text = None
        self._exe_result = None
        self._record_time = None
        self._clean_time = None
        self.discriminator = None

        self.seqno = seqno
        self.checkpoint = checkpoint
        self.status = status
        self.ddl_timestamp = ddl_timestamp
        self.ddl_text = ddl_text
        self.exe_result = exe_result
        self.record_time = record_time
        if clean_time is not None:
            self.clean_time = clean_time

    @property
    def seqno(self):
        r"""Gets the seqno of this DdlAlarmResp.

        记录唯一序号。

        :return: The seqno of this DdlAlarmResp.
        :rtype: int
        """
        return self._seqno

    @seqno.setter
    def seqno(self, seqno):
        r"""Sets the seqno of this DdlAlarmResp.

        记录唯一序号。

        :param seqno: The seqno of this DdlAlarmResp.
        :type seqno: int
        """
        self._seqno = seqno

    @property
    def checkpoint(self):
        r"""Gets the checkpoint of this DdlAlarmResp.

        数据源库位点。

        :return: The checkpoint of this DdlAlarmResp.
        :rtype: str
        """
        return self._checkpoint

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        r"""Sets the checkpoint of this DdlAlarmResp.

        数据源库位点。

        :param checkpoint: The checkpoint of this DdlAlarmResp.
        :type checkpoint: str
        """
        self._checkpoint = checkpoint

    @property
    def status(self):
        r"""Gets the status of this DdlAlarmResp.

        DDL告警状态。0无告警，1告警中。

        :return: The status of this DdlAlarmResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DdlAlarmResp.

        DDL告警状态。0无告警，1告警中。

        :param status: The status of this DdlAlarmResp.
        :type status: int
        """
        self._status = status

    @property
    def ddl_timestamp(self):
        r"""Gets the ddl_timestamp of this DdlAlarmResp.

        DDL在源库执行时间。

        :return: The ddl_timestamp of this DdlAlarmResp.
        :rtype: int
        """
        return self._ddl_timestamp

    @ddl_timestamp.setter
    def ddl_timestamp(self, ddl_timestamp):
        r"""Sets the ddl_timestamp of this DdlAlarmResp.

        DDL在源库执行时间。

        :param ddl_timestamp: The ddl_timestamp of this DdlAlarmResp.
        :type ddl_timestamp: int
        """
        self._ddl_timestamp = ddl_timestamp

    @property
    def ddl_text(self):
        r"""Gets the ddl_text of this DdlAlarmResp.

        DDL内容。

        :return: The ddl_text of this DdlAlarmResp.
        :rtype: str
        """
        return self._ddl_text

    @ddl_text.setter
    def ddl_text(self, ddl_text):
        r"""Sets the ddl_text of this DdlAlarmResp.

        DDL内容。

        :param ddl_text: The ddl_text of this DdlAlarmResp.
        :type ddl_text: str
        """
        self._ddl_text = ddl_text

    @property
    def exe_result(self):
        r"""Gets the exe_result of this DdlAlarmResp.

        DDL执行结果。false执行失败，true执行成功。

        :return: The exe_result of this DdlAlarmResp.
        :rtype: bool
        """
        return self._exe_result

    @exe_result.setter
    def exe_result(self, exe_result):
        r"""Sets the exe_result of this DdlAlarmResp.

        DDL执行结果。false执行失败，true执行成功。

        :param exe_result: The exe_result of this DdlAlarmResp.
        :type exe_result: bool
        """
        self._exe_result = exe_result

    @property
    def record_time(self):
        r"""Gets the record_time of this DdlAlarmResp.

        数据记录时间。

        :return: The record_time of this DdlAlarmResp.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this DdlAlarmResp.

        数据记录时间。

        :param record_time: The record_time of this DdlAlarmResp.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def clean_time(self):
        r"""Gets the clean_time of this DdlAlarmResp.

        DDL告警清理时间。

        :return: The clean_time of this DdlAlarmResp.
        :rtype: int
        """
        return self._clean_time

    @clean_time.setter
    def clean_time(self, clean_time):
        r"""Sets the clean_time of this DdlAlarmResp.

        DDL告警清理时间。

        :param clean_time: The clean_time of this DdlAlarmResp.
        :type clean_time: int
        """
        self._clean_time = clean_time

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
        if not isinstance(other, DdlAlarmResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
