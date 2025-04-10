# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_more': 'bool',
        'end_offset': 'str',
        'start_offset': 'str',
        'log': 'str',
        'location': 'str',
        'step_run_id': 'str'
    }

    attribute_map = {
        'has_more': 'has_more',
        'end_offset': 'end_offset',
        'start_offset': 'start_offset',
        'log': 'log',
        'location': 'location',
        'step_run_id': 'step_run_id'
    }

    def __init__(self, has_more=None, end_offset=None, start_offset=None, log=None, location=None, step_run_id=None):
        r"""ShowPipelineLogResponse

        The model defined in huaweicloud sdk

        :param has_more: 是否有更多日志
        :type has_more: bool
        :param end_offset: 查询日志结束偏移。填入请求体end_offset字段，用于查询下一页日志。
        :type end_offset: str
        :param start_offset: 查询日志起始偏移。填入请求体start_offset字段，用于查询下一页日志。
        :type start_offset: str
        :param log: 日志内容
        :type log: str
        :param location: 日志存储位置
        :type location: str
        :param step_run_id: 所属步骤ID
        :type step_run_id: str
        """
        
        super(ShowPipelineLogResponse, self).__init__()

        self._has_more = None
        self._end_offset = None
        self._start_offset = None
        self._log = None
        self._location = None
        self._step_run_id = None
        self.discriminator = None

        if has_more is not None:
            self.has_more = has_more
        if end_offset is not None:
            self.end_offset = end_offset
        if start_offset is not None:
            self.start_offset = start_offset
        if log is not None:
            self.log = log
        if location is not None:
            self.location = location
        if step_run_id is not None:
            self.step_run_id = step_run_id

    @property
    def has_more(self):
        r"""Gets the has_more of this ShowPipelineLogResponse.

        是否有更多日志

        :return: The has_more of this ShowPipelineLogResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this ShowPipelineLogResponse.

        是否有更多日志

        :param has_more: The has_more of this ShowPipelineLogResponse.
        :type has_more: bool
        """
        self._has_more = has_more

    @property
    def end_offset(self):
        r"""Gets the end_offset of this ShowPipelineLogResponse.

        查询日志结束偏移。填入请求体end_offset字段，用于查询下一页日志。

        :return: The end_offset of this ShowPipelineLogResponse.
        :rtype: str
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this ShowPipelineLogResponse.

        查询日志结束偏移。填入请求体end_offset字段，用于查询下一页日志。

        :param end_offset: The end_offset of this ShowPipelineLogResponse.
        :type end_offset: str
        """
        self._end_offset = end_offset

    @property
    def start_offset(self):
        r"""Gets the start_offset of this ShowPipelineLogResponse.

        查询日志起始偏移。填入请求体start_offset字段，用于查询下一页日志。

        :return: The start_offset of this ShowPipelineLogResponse.
        :rtype: str
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        r"""Sets the start_offset of this ShowPipelineLogResponse.

        查询日志起始偏移。填入请求体start_offset字段，用于查询下一页日志。

        :param start_offset: The start_offset of this ShowPipelineLogResponse.
        :type start_offset: str
        """
        self._start_offset = start_offset

    @property
    def log(self):
        r"""Gets the log of this ShowPipelineLogResponse.

        日志内容

        :return: The log of this ShowPipelineLogResponse.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this ShowPipelineLogResponse.

        日志内容

        :param log: The log of this ShowPipelineLogResponse.
        :type log: str
        """
        self._log = log

    @property
    def location(self):
        r"""Gets the location of this ShowPipelineLogResponse.

        日志存储位置

        :return: The location of this ShowPipelineLogResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowPipelineLogResponse.

        日志存储位置

        :param location: The location of this ShowPipelineLogResponse.
        :type location: str
        """
        self._location = location

    @property
    def step_run_id(self):
        r"""Gets the step_run_id of this ShowPipelineLogResponse.

        所属步骤ID

        :return: The step_run_id of this ShowPipelineLogResponse.
        :rtype: str
        """
        return self._step_run_id

    @step_run_id.setter
    def step_run_id(self, step_run_id):
        r"""Sets the step_run_id of this ShowPipelineLogResponse.

        所属步骤ID

        :param step_run_id: The step_run_id of this ShowPipelineLogResponse.
        :type step_run_id: str
        """
        self._step_run_id = step_run_id

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
        if not isinstance(other, ShowPipelineLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
