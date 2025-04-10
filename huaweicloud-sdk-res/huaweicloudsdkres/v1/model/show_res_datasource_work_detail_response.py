# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResDatasourceWorkDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_count': 'ErrorCount',
        'data_struct': 'DataStruct',
        'error_samples': 'list[ErrorSample]',
        'inspect_result': 'list[InspectResult]',
        'is_success': 'bool',
        'message': 'str',
        'legal_rate': 'float',
        'inspect_rst_generated_time': 'str',
        'final_report': 'FinalReport'
    }

    attribute_map = {
        'error_count': 'error_count',
        'data_struct': 'data_struct',
        'error_samples': 'error_samples',
        'inspect_result': 'inspect_result',
        'is_success': 'is_success',
        'message': 'message',
        'legal_rate': 'legal_rate',
        'inspect_rst_generated_time': 'inspect_rst_generated_time',
        'final_report': 'final_report'
    }

    def __init__(self, error_count=None, data_struct=None, error_samples=None, inspect_result=None, is_success=None, message=None, legal_rate=None, inspect_rst_generated_time=None, final_report=None):
        r"""ShowResDatasourceWorkDetailResponse

        The model defined in huaweicloud sdk

        :param error_count: 
        :type error_count: :class:`huaweicloudsdkres.v1.ErrorCount`
        :param data_struct: 
        :type data_struct: :class:`huaweicloudsdkres.v1.DataStruct`
        :param error_samples: 错误样例(请求类型为DATA_INSPECTION时返回)。
        :type error_samples: list[:class:`huaweicloudsdkres.v1.ErrorSample`]
        :param inspect_result: 数据检测结果(请求类型为DATA_INSPECTION时返回)。
        :type inspect_result: list[:class:`huaweicloudsdkres.v1.InspectResult`]
        :param is_success: 是否成功。
        :type is_success: bool
        :param message: 返回消息。
        :type message: str
        :param legal_rate: 合法率(请求类型为DATA_INSPECTION时返回)。
        :type legal_rate: float
        :param inspect_rst_generated_time: 检测结果生成时间(请求类型为DATA_INSPECTION时返回)。
        :type inspect_rst_generated_time: str
        :param final_report: 
        :type final_report: :class:`huaweicloudsdkres.v1.FinalReport`
        """
        
        super(ShowResDatasourceWorkDetailResponse, self).__init__()

        self._error_count = None
        self._data_struct = None
        self._error_samples = None
        self._inspect_result = None
        self._is_success = None
        self._message = None
        self._legal_rate = None
        self._inspect_rst_generated_time = None
        self._final_report = None
        self.discriminator = None

        if error_count is not None:
            self.error_count = error_count
        if data_struct is not None:
            self.data_struct = data_struct
        if error_samples is not None:
            self.error_samples = error_samples
        if inspect_result is not None:
            self.inspect_result = inspect_result
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if legal_rate is not None:
            self.legal_rate = legal_rate
        if inspect_rst_generated_time is not None:
            self.inspect_rst_generated_time = inspect_rst_generated_time
        if final_report is not None:
            self.final_report = final_report

    @property
    def error_count(self):
        r"""Gets the error_count of this ShowResDatasourceWorkDetailResponse.

        :return: The error_count of this ShowResDatasourceWorkDetailResponse.
        :rtype: :class:`huaweicloudsdkres.v1.ErrorCount`
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        r"""Sets the error_count of this ShowResDatasourceWorkDetailResponse.

        :param error_count: The error_count of this ShowResDatasourceWorkDetailResponse.
        :type error_count: :class:`huaweicloudsdkres.v1.ErrorCount`
        """
        self._error_count = error_count

    @property
    def data_struct(self):
        r"""Gets the data_struct of this ShowResDatasourceWorkDetailResponse.

        :return: The data_struct of this ShowResDatasourceWorkDetailResponse.
        :rtype: :class:`huaweicloudsdkres.v1.DataStruct`
        """
        return self._data_struct

    @data_struct.setter
    def data_struct(self, data_struct):
        r"""Sets the data_struct of this ShowResDatasourceWorkDetailResponse.

        :param data_struct: The data_struct of this ShowResDatasourceWorkDetailResponse.
        :type data_struct: :class:`huaweicloudsdkres.v1.DataStruct`
        """
        self._data_struct = data_struct

    @property
    def error_samples(self):
        r"""Gets the error_samples of this ShowResDatasourceWorkDetailResponse.

        错误样例(请求类型为DATA_INSPECTION时返回)。

        :return: The error_samples of this ShowResDatasourceWorkDetailResponse.
        :rtype: list[:class:`huaweicloudsdkres.v1.ErrorSample`]
        """
        return self._error_samples

    @error_samples.setter
    def error_samples(self, error_samples):
        r"""Sets the error_samples of this ShowResDatasourceWorkDetailResponse.

        错误样例(请求类型为DATA_INSPECTION时返回)。

        :param error_samples: The error_samples of this ShowResDatasourceWorkDetailResponse.
        :type error_samples: list[:class:`huaweicloudsdkres.v1.ErrorSample`]
        """
        self._error_samples = error_samples

    @property
    def inspect_result(self):
        r"""Gets the inspect_result of this ShowResDatasourceWorkDetailResponse.

        数据检测结果(请求类型为DATA_INSPECTION时返回)。

        :return: The inspect_result of this ShowResDatasourceWorkDetailResponse.
        :rtype: list[:class:`huaweicloudsdkres.v1.InspectResult`]
        """
        return self._inspect_result

    @inspect_result.setter
    def inspect_result(self, inspect_result):
        r"""Sets the inspect_result of this ShowResDatasourceWorkDetailResponse.

        数据检测结果(请求类型为DATA_INSPECTION时返回)。

        :param inspect_result: The inspect_result of this ShowResDatasourceWorkDetailResponse.
        :type inspect_result: list[:class:`huaweicloudsdkres.v1.InspectResult`]
        """
        self._inspect_result = inspect_result

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowResDatasourceWorkDetailResponse.

        是否成功。

        :return: The is_success of this ShowResDatasourceWorkDetailResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowResDatasourceWorkDetailResponse.

        是否成功。

        :param is_success: The is_success of this ShowResDatasourceWorkDetailResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowResDatasourceWorkDetailResponse.

        返回消息。

        :return: The message of this ShowResDatasourceWorkDetailResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowResDatasourceWorkDetailResponse.

        返回消息。

        :param message: The message of this ShowResDatasourceWorkDetailResponse.
        :type message: str
        """
        self._message = message

    @property
    def legal_rate(self):
        r"""Gets the legal_rate of this ShowResDatasourceWorkDetailResponse.

        合法率(请求类型为DATA_INSPECTION时返回)。

        :return: The legal_rate of this ShowResDatasourceWorkDetailResponse.
        :rtype: float
        """
        return self._legal_rate

    @legal_rate.setter
    def legal_rate(self, legal_rate):
        r"""Sets the legal_rate of this ShowResDatasourceWorkDetailResponse.

        合法率(请求类型为DATA_INSPECTION时返回)。

        :param legal_rate: The legal_rate of this ShowResDatasourceWorkDetailResponse.
        :type legal_rate: float
        """
        self._legal_rate = legal_rate

    @property
    def inspect_rst_generated_time(self):
        r"""Gets the inspect_rst_generated_time of this ShowResDatasourceWorkDetailResponse.

        检测结果生成时间(请求类型为DATA_INSPECTION时返回)。

        :return: The inspect_rst_generated_time of this ShowResDatasourceWorkDetailResponse.
        :rtype: str
        """
        return self._inspect_rst_generated_time

    @inspect_rst_generated_time.setter
    def inspect_rst_generated_time(self, inspect_rst_generated_time):
        r"""Sets the inspect_rst_generated_time of this ShowResDatasourceWorkDetailResponse.

        检测结果生成时间(请求类型为DATA_INSPECTION时返回)。

        :param inspect_rst_generated_time: The inspect_rst_generated_time of this ShowResDatasourceWorkDetailResponse.
        :type inspect_rst_generated_time: str
        """
        self._inspect_rst_generated_time = inspect_rst_generated_time

    @property
    def final_report(self):
        r"""Gets the final_report of this ShowResDatasourceWorkDetailResponse.

        :return: The final_report of this ShowResDatasourceWorkDetailResponse.
        :rtype: :class:`huaweicloudsdkres.v1.FinalReport`
        """
        return self._final_report

    @final_report.setter
    def final_report(self, final_report):
        r"""Sets the final_report of this ShowResDatasourceWorkDetailResponse.

        :param final_report: The final_report of this ShowResDatasourceWorkDetailResponse.
        :type final_report: :class:`huaweicloudsdkres.v1.FinalReport`
        """
        self._final_report = final_report

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
        if not isinstance(other, ShowResDatasourceWorkDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
