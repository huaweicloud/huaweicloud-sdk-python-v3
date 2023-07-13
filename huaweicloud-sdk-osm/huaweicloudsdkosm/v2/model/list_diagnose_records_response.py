# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnoseRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'total_count': 'int',
        'records': 'list[DiagnoseRecordVo]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'total_count': 'total_count',
        'records': 'records'
    }

    def __init__(self, error_code=None, error_msg=None, total_count=None, records=None):
        """ListDiagnoseRecordsResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param total_count: 总条数
        :type total_count: int
        :param records: 获取的诊断记录列表
        :type records: list[:class:`huaweicloudsdkosm.v2.DiagnoseRecordVo`]
        """
        
        super(ListDiagnoseRecordsResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._total_count = None
        self._records = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if total_count is not None:
            self.total_count = total_count
        if records is not None:
            self.records = records

    @property
    def error_code(self):
        """Gets the error_code of this ListDiagnoseRecordsResponse.

        错误码

        :return: The error_code of this ListDiagnoseRecordsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListDiagnoseRecordsResponse.

        错误码

        :param error_code: The error_code of this ListDiagnoseRecordsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ListDiagnoseRecordsResponse.

        错误描述

        :return: The error_msg of this ListDiagnoseRecordsResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ListDiagnoseRecordsResponse.

        错误描述

        :param error_msg: The error_msg of this ListDiagnoseRecordsResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def total_count(self):
        """Gets the total_count of this ListDiagnoseRecordsResponse.

        总条数

        :return: The total_count of this ListDiagnoseRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListDiagnoseRecordsResponse.

        总条数

        :param total_count: The total_count of this ListDiagnoseRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def records(self):
        """Gets the records of this ListDiagnoseRecordsResponse.

        获取的诊断记录列表

        :return: The records of this ListDiagnoseRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.DiagnoseRecordVo`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ListDiagnoseRecordsResponse.

        获取的诊断记录列表

        :param records: The records of this ListDiagnoseRecordsResponse.
        :type records: list[:class:`huaweicloudsdkosm.v2.DiagnoseRecordVo`]
        """
        self._records = records

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
        if not isinstance(other, ListDiagnoseRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
