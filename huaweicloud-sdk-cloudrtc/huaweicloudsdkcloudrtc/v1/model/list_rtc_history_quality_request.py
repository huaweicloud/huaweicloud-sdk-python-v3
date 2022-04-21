# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcHistoryQualityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'x_sdk_date': 'str',
        'x_project_id': 'str',
        'project_id': 'str',
        'app': 'str',
        'metric': 'list[str]',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'app': 'app',
        'metric': 'metric',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, app=None, metric=None, start_date=None, end_date=None):
        """ListRtcHistoryQualityRequest

        The model defined in huaweicloud sdk

        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。 
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。 
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 
        :type x_project_id: str
        :param project_id: 项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 
        :type project_id: str
        :param app: 应用标识 
        :type app: str
        :param metric: 查询的数据类型 - JoinSuccessRate：加入房间成功率 - JoinSuccess5SecsRate：5秒加入成功率 - VideoFreezeRate：视频卡顿率 - AudioFreezeRate：音频卡顿率 - FirstVideoRecvTime：首帧视频接收耗时 - FirstAudioRecvTime：首帧音频接收耗时 - PullStreamSuccessRate：拉流成功率 - PushStreamSuccessRate：推流成功率 - VideoUpstreamExcellentTransRate：客户端视频上行优质传输率 - AudioUpstreamExcellentTransRate：客户端音频上行优质传输率 - VideoExcellentTransRate：端到端视频优质传输率 - AudioExcellentTransRate：端到端音频优质传输率 - VideoTransDelay：端到端视频网络时，单位为毫秒，取当天所有用户网络延迟的中位数 - AudioTransDelay：端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数 
        :type metric: list[str]
        :param start_date: 查询起始时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23，不写默认读取过去1天数据数据。 
        :type start_date: str
        :param end_date: 查询结束时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23 
        :type end_date: str
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._app = None
        self._metric = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.project_id = project_id
        self.app = app
        self.metric = metric
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcHistoryQualityRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcHistoryQualityRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcHistoryQualityRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcHistoryQualityRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcHistoryQualityRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcHistoryQualityRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcHistoryQualityRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app(self):
        """Gets the app of this ListRtcHistoryQualityRequest.

        应用标识 

        :return: The app of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcHistoryQualityRequest.

        应用标识 

        :param app: The app of this ListRtcHistoryQualityRequest.
        :type app: str
        """
        self._app = app

    @property
    def metric(self):
        """Gets the metric of this ListRtcHistoryQualityRequest.

        查询的数据类型 - JoinSuccessRate：加入房间成功率 - JoinSuccess5SecsRate：5秒加入成功率 - VideoFreezeRate：视频卡顿率 - AudioFreezeRate：音频卡顿率 - FirstVideoRecvTime：首帧视频接收耗时 - FirstAudioRecvTime：首帧音频接收耗时 - PullStreamSuccessRate：拉流成功率 - PushStreamSuccessRate：推流成功率 - VideoUpstreamExcellentTransRate：客户端视频上行优质传输率 - AudioUpstreamExcellentTransRate：客户端音频上行优质传输率 - VideoExcellentTransRate：端到端视频优质传输率 - AudioExcellentTransRate：端到端音频优质传输率 - VideoTransDelay：端到端视频网络时，单位为毫秒，取当天所有用户网络延迟的中位数 - AudioTransDelay：端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数 

        :return: The metric of this ListRtcHistoryQualityRequest.
        :rtype: list[str]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ListRtcHistoryQualityRequest.

        查询的数据类型 - JoinSuccessRate：加入房间成功率 - JoinSuccess5SecsRate：5秒加入成功率 - VideoFreezeRate：视频卡顿率 - AudioFreezeRate：音频卡顿率 - FirstVideoRecvTime：首帧视频接收耗时 - FirstAudioRecvTime：首帧音频接收耗时 - PullStreamSuccessRate：拉流成功率 - PushStreamSuccessRate：推流成功率 - VideoUpstreamExcellentTransRate：客户端视频上行优质传输率 - AudioUpstreamExcellentTransRate：客户端音频上行优质传输率 - VideoExcellentTransRate：端到端视频优质传输率 - AudioExcellentTransRate：端到端音频优质传输率 - VideoTransDelay：端到端视频网络时，单位为毫秒，取当天所有用户网络延迟的中位数 - AudioTransDelay：端到端音频网络时延，单位为毫秒，取当天所有用户网络延迟的中位数 

        :param metric: The metric of this ListRtcHistoryQualityRequest.
        :type metric: list[str]
        """
        self._metric = metric

    @property
    def start_date(self):
        """Gets the start_date of this ListRtcHistoryQualityRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23，不写默认读取过去1天数据数据。 

        :return: The start_date of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListRtcHistoryQualityRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23，不写默认读取过去1天数据数据。 

        :param start_date: The start_date of this ListRtcHistoryQualityRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListRtcHistoryQualityRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23 

        :return: The end_date of this ListRtcHistoryQualityRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListRtcHistoryQualityRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DD，如2020-04-23 

        :param end_date: The end_date of this ListRtcHistoryQualityRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ListRtcHistoryQualityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
