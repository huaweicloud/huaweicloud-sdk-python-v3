# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PictureModelingInfo:

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
        'start_time': 'str',
        'end_time': 'str',
        'error_info': 'ErrorResponse',
        'model_asset_id': 'str',
        'name': 'str',
        'style_id': 'str',
        'model_cover_url': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_info': 'error_info',
        'model_asset_id': 'model_asset_id',
        'name': 'name',
        'style_id': 'style_id',
        'model_cover_url': 'model_cover_url'
    }

    def __init__(self, job_id=None, state=None, start_time=None, end_time=None, error_info=None, model_asset_id=None, name=None, style_id=None, model_cover_url=None):
        """PictureModelingInfo

        The model defined in huaweicloud sdk

        :param job_id: 照片建模任务ID。
        :type job_id: str
        :param state: 任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消
        :type state: str
        :param start_time: 任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type start_time: str
        :param end_time: 任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type end_time: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param model_asset_id: 模型资产ID。
        :type model_asset_id: str
        :param name: 数字人模型名称。
        :type name: str
        :param style_id: 风格ID。
        :type style_id: str
        :param model_cover_url: 模型封面URL。
        :type model_cover_url: str
        """
        
        

        self._job_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._error_info = None
        self._model_asset_id = None
        self._name = None
        self._style_id = None
        self._model_cover_url = None
        self.discriminator = None

        self.job_id = job_id
        self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_info is not None:
            self.error_info = error_info
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if name is not None:
            self.name = name
        if style_id is not None:
            self.style_id = style_id
        if model_cover_url is not None:
            self.model_cover_url = model_cover_url

    @property
    def job_id(self):
        """Gets the job_id of this PictureModelingInfo.

        照片建模任务ID。

        :return: The job_id of this PictureModelingInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this PictureModelingInfo.

        照片建模任务ID。

        :param job_id: The job_id of this PictureModelingInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        """Gets the state of this PictureModelingInfo.

        任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :return: The state of this PictureModelingInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PictureModelingInfo.

        任务的状态。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED：部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :param state: The state of this PictureModelingInfo.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this PictureModelingInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The start_time of this PictureModelingInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PictureModelingInfo.

        任务开始时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param start_time: The start_time of this PictureModelingInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PictureModelingInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The end_time of this PictureModelingInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PictureModelingInfo.

        任务结束时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param end_time: The end_time of this PictureModelingInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_info(self):
        """Gets the error_info of this PictureModelingInfo.

        :return: The error_info of this PictureModelingInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this PictureModelingInfo.

        :param error_info: The error_info of this PictureModelingInfo.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this PictureModelingInfo.

        模型资产ID。

        :return: The model_asset_id of this PictureModelingInfo.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this PictureModelingInfo.

        模型资产ID。

        :param model_asset_id: The model_asset_id of this PictureModelingInfo.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def name(self):
        """Gets the name of this PictureModelingInfo.

        数字人模型名称。

        :return: The name of this PictureModelingInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PictureModelingInfo.

        数字人模型名称。

        :param name: The name of this PictureModelingInfo.
        :type name: str
        """
        self._name = name

    @property
    def style_id(self):
        """Gets the style_id of this PictureModelingInfo.

        风格ID。

        :return: The style_id of this PictureModelingInfo.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this PictureModelingInfo.

        风格ID。

        :param style_id: The style_id of this PictureModelingInfo.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def model_cover_url(self):
        """Gets the model_cover_url of this PictureModelingInfo.

        模型封面URL。

        :return: The model_cover_url of this PictureModelingInfo.
        :rtype: str
        """
        return self._model_cover_url

    @model_cover_url.setter
    def model_cover_url(self, model_cover_url):
        """Sets the model_cover_url of this PictureModelingInfo.

        模型封面URL。

        :param model_cover_url: The model_cover_url of this PictureModelingInfo.
        :type model_cover_url: str
        """
        self._model_cover_url = model_cover_url

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
        if not isinstance(other, PictureModelingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
