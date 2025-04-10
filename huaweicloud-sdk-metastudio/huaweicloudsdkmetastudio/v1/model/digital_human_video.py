# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DigitalHumanVideo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'state': 'str',
        'job_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'duration': 'float',
        'output_asset_config': 'OutputAssetInfo',
        'error_info': 'ErrorResponse',
        'create_time': 'str',
        'lastupdate_time': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'job_type': 'job_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration',
        'output_asset_config': 'output_asset_config',
        'error_info': 'error_info',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time'
    }

    def __init__(self, job_id=None, state=None, job_type=None, start_time=None, end_time=None, duration=None, output_asset_config=None, error_info=None, create_time=None, lastupdate_time=None):
        r"""DigitalHumanVideo

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消 * BLOCK: 冻结
        :type state: str
        :param job_type: 任务类型。 * 2D_DIGITAL_HUMAN_VIDEO: 分身数字人视频制作任务 * DIGITAL_HUMAN_PHOTO_VIDEO: 照片数字人视频制作任务
        :type job_type: str
        :param start_time: 数字人视频制作开始时间。
        :type start_time: str
        :param end_time: 数字人视频制作结束时间。
        :type end_time: str
        :param duration: **参数解释**： 数字人视频内容时长。
        :type duration: float
        :param output_asset_config: 
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param create_time: 任务创建时间。
        :type create_time: str
        :param lastupdate_time: 任务更新时间。
        :type lastupdate_time: str
        """
        
        

        self._job_id = None
        self._state = None
        self._job_type = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._output_asset_config = None
        self._error_info = None
        self._create_time = None
        self._lastupdate_time = None
        self.discriminator = None

        self.job_id = job_id
        self.state = state
        if job_type is not None:
            self.job_type = job_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if output_asset_config is not None:
            self.output_asset_config = output_asset_config
        if error_info is not None:
            self.error_info = error_info
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time

    @property
    def job_id(self):
        r"""Gets the job_id of this DigitalHumanVideo.

        任务ID。

        :return: The job_id of this DigitalHumanVideo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DigitalHumanVideo.

        任务ID。

        :param job_id: The job_id of this DigitalHumanVideo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this DigitalHumanVideo.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消 * BLOCK: 冻结

        :return: The state of this DigitalHumanVideo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this DigitalHumanVideo.

        任务的状态。 * WAITING：等待 * PROCESSING：处理中 * SUCCEED：成功 * FAILED：失败 * CANCELED：取消 * BLOCK: 冻结

        :param state: The state of this DigitalHumanVideo.
        :type state: str
        """
        self._state = state

    @property
    def job_type(self):
        r"""Gets the job_type of this DigitalHumanVideo.

        任务类型。 * 2D_DIGITAL_HUMAN_VIDEO: 分身数字人视频制作任务 * DIGITAL_HUMAN_PHOTO_VIDEO: 照片数字人视频制作任务

        :return: The job_type of this DigitalHumanVideo.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this DigitalHumanVideo.

        任务类型。 * 2D_DIGITAL_HUMAN_VIDEO: 分身数字人视频制作任务 * DIGITAL_HUMAN_PHOTO_VIDEO: 照片数字人视频制作任务

        :param job_type: The job_type of this DigitalHumanVideo.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def start_time(self):
        r"""Gets the start_time of this DigitalHumanVideo.

        数字人视频制作开始时间。

        :return: The start_time of this DigitalHumanVideo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DigitalHumanVideo.

        数字人视频制作开始时间。

        :param start_time: The start_time of this DigitalHumanVideo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DigitalHumanVideo.

        数字人视频制作结束时间。

        :return: The end_time of this DigitalHumanVideo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DigitalHumanVideo.

        数字人视频制作结束时间。

        :param end_time: The end_time of this DigitalHumanVideo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def duration(self):
        r"""Gets the duration of this DigitalHumanVideo.

        **参数解释**： 数字人视频内容时长。

        :return: The duration of this DigitalHumanVideo.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this DigitalHumanVideo.

        **参数解释**： 数字人视频内容时长。

        :param duration: The duration of this DigitalHumanVideo.
        :type duration: float
        """
        self._duration = duration

    @property
    def output_asset_config(self):
        r"""Gets the output_asset_config of this DigitalHumanVideo.

        :return: The output_asset_config of this DigitalHumanVideo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        return self._output_asset_config

    @output_asset_config.setter
    def output_asset_config(self, output_asset_config):
        r"""Sets the output_asset_config of this DigitalHumanVideo.

        :param output_asset_config: The output_asset_config of this DigitalHumanVideo.
        :type output_asset_config: :class:`huaweicloudsdkmetastudio.v1.OutputAssetInfo`
        """
        self._output_asset_config = output_asset_config

    @property
    def error_info(self):
        r"""Gets the error_info of this DigitalHumanVideo.

        :return: The error_info of this DigitalHumanVideo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this DigitalHumanVideo.

        :param error_info: The error_info of this DigitalHumanVideo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def create_time(self):
        r"""Gets the create_time of this DigitalHumanVideo.

        任务创建时间。

        :return: The create_time of this DigitalHumanVideo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DigitalHumanVideo.

        任务创建时间。

        :param create_time: The create_time of this DigitalHumanVideo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        r"""Gets the lastupdate_time of this DigitalHumanVideo.

        任务更新时间。

        :return: The lastupdate_time of this DigitalHumanVideo.
        :rtype: str
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        r"""Sets the lastupdate_time of this DigitalHumanVideo.

        任务更新时间。

        :param lastupdate_time: The lastupdate_time of this DigitalHumanVideo.
        :type lastupdate_time: str
        """
        self._lastupdate_time = lastupdate_time

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
        if not isinstance(other, DigitalHumanVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
