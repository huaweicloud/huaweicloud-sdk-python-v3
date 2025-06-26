# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisSummaryResponse(SdkResponse):

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
        'status': 'str',
        'region': 'str',
        'start_time': 'int',
        'instance_summary': 'list[DiagnosisSummaryItem]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'status': 'status',
        'region': 'region',
        'start_time': 'start_time',
        'instance_summary': 'instance_summary'
    }

    def __init__(self, error_code=None, error_msg=None, status=None, region=None, start_time=None, instance_summary=None):
        r"""ShowDiagnosisSummaryResponse

        The model defined in huaweicloud sdk

        :param error_code: error_code
        :type error_code: str
        :param error_msg: error_msg
        :type error_msg: str
        :param status: 工单状态
        :type status: str
        :param region: region
        :type region: str
        :param start_time: 开始时间
        :type start_time: int
        :param instance_summary: 被诊断实例的概览信息列表
        :type instance_summary: list[:class:`huaweicloudsdkcoc.v1.DiagnosisSummaryItem`]
        """
        
        super(ShowDiagnosisSummaryResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._status = None
        self._region = None
        self._start_time = None
        self._instance_summary = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if start_time is not None:
            self.start_time = start_time
        if instance_summary is not None:
            self.instance_summary = instance_summary

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowDiagnosisSummaryResponse.

        error_code

        :return: The error_code of this ShowDiagnosisSummaryResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowDiagnosisSummaryResponse.

        error_code

        :param error_code: The error_code of this ShowDiagnosisSummaryResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowDiagnosisSummaryResponse.

        error_msg

        :return: The error_msg of this ShowDiagnosisSummaryResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowDiagnosisSummaryResponse.

        error_msg

        :param error_msg: The error_msg of this ShowDiagnosisSummaryResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def status(self):
        r"""Gets the status of this ShowDiagnosisSummaryResponse.

        工单状态

        :return: The status of this ShowDiagnosisSummaryResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDiagnosisSummaryResponse.

        工单状态

        :param status: The status of this ShowDiagnosisSummaryResponse.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ShowDiagnosisSummaryResponse.

        region

        :return: The region of this ShowDiagnosisSummaryResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowDiagnosisSummaryResponse.

        region

        :param region: The region of this ShowDiagnosisSummaryResponse.
        :type region: str
        """
        self._region = region

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDiagnosisSummaryResponse.

        开始时间

        :return: The start_time of this ShowDiagnosisSummaryResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDiagnosisSummaryResponse.

        开始时间

        :param start_time: The start_time of this ShowDiagnosisSummaryResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def instance_summary(self):
        r"""Gets the instance_summary of this ShowDiagnosisSummaryResponse.

        被诊断实例的概览信息列表

        :return: The instance_summary of this ShowDiagnosisSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.DiagnosisSummaryItem`]
        """
        return self._instance_summary

    @instance_summary.setter
    def instance_summary(self, instance_summary):
        r"""Sets the instance_summary of this ShowDiagnosisSummaryResponse.

        被诊断实例的概览信息列表

        :param instance_summary: The instance_summary of this ShowDiagnosisSummaryResponse.
        :type instance_summary: list[:class:`huaweicloudsdkcoc.v1.DiagnosisSummaryItem`]
        """
        self._instance_summary = instance_summary

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
        if not isinstance(other, ShowDiagnosisSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
