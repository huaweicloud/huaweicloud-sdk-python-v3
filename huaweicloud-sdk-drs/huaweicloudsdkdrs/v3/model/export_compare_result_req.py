# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportCompareResultReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_type': 'str',
        'compare_job_id': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'compare_type': 'compare_type',
        'compare_job_id': 'compare_job_id',
        'time_zone': 'time_zone'
    }

    def __init__(self, compare_type=None, compare_job_id=None, time_zone=None):
        r"""ExportCompareResultReq

        The model defined in huaweicloud sdk

        :param compare_type: 对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。
        :type compare_type: str
        :param compare_job_id: 对比任务的ID，内容对比、抽样对比、行数对比场景必填。
        :type compare_job_id: str
        :param time_zone: 时区，如GMT+08:00，用于生成当前时间标识，拼接到文件名称中。
        :type time_zone: str
        """
        
        

        self._compare_type = None
        self._compare_job_id = None
        self._time_zone = None
        self.discriminator = None

        self.compare_type = compare_type
        if compare_job_id is not None:
            self.compare_job_id = compare_job_id
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ExportCompareResultReq.

        对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。

        :return: The compare_type of this ExportCompareResultReq.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ExportCompareResultReq.

        对比任务类型： - contents： 内容对比。 - lines：行数对比。 - random：抽样对比。 - objects_comparison：对象对比。 - repair_data：数据修复。

        :param compare_type: The compare_type of this ExportCompareResultReq.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def compare_job_id(self):
        r"""Gets the compare_job_id of this ExportCompareResultReq.

        对比任务的ID，内容对比、抽样对比、行数对比场景必填。

        :return: The compare_job_id of this ExportCompareResultReq.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        r"""Sets the compare_job_id of this ExportCompareResultReq.

        对比任务的ID，内容对比、抽样对比、行数对比场景必填。

        :param compare_job_id: The compare_job_id of this ExportCompareResultReq.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ExportCompareResultReq.

        时区，如GMT+08:00，用于生成当前时间标识，拼接到文件名称中。

        :return: The time_zone of this ExportCompareResultReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ExportCompareResultReq.

        时区，如GMT+08:00，用于生成当前时间标识，拼接到文件名称中。

        :param time_zone: The time_zone of this ExportCompareResultReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, ExportCompareResultReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
