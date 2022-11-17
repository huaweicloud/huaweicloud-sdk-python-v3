# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordContentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'record_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'record_type': 'record_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, record_type=None, start_time=None, end_time=None, offset=None, limit=None):
        """ListRecordContentsRequest

        The model defined in huaweicloud sdk

        :param publish_domain: 直播推流放域名
        :type publish_domain: str
        :param app: 流应用名称
        :type app: str
        :param stream: 流名称
        :type stream: str
        :param record_type: 录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 
        :type record_type: str
        :param start_time: 开始时间,格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间
        :type start_time: str
        :param end_time: 结束时间，格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间
        :type end_time: str
        :param offset: 分页编号，从0开始算
        :type offset: int
        :param limit: 每页记录数，取值范围[1,100]
        :type limit: int
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._record_type = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if record_type is not None:
            self.record_type = record_type
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def publish_domain(self):
        """Gets the publish_domain of this ListRecordContentsRequest.

        直播推流放域名

        :return: The publish_domain of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this ListRecordContentsRequest.

        直播推流放域名

        :param publish_domain: The publish_domain of this ListRecordContentsRequest.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this ListRecordContentsRequest.

        流应用名称

        :return: The app of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRecordContentsRequest.

        流应用名称

        :param app: The app of this ListRecordContentsRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListRecordContentsRequest.

        流名称

        :return: The stream of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListRecordContentsRequest.

        流名称

        :param stream: The stream of this ListRecordContentsRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def record_type(self):
        """Gets the record_type of this ListRecordContentsRequest.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 

        :return: The record_type of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this ListRecordContentsRequest.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 

        :param record_type: The record_type of this ListRecordContentsRequest.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def start_time(self):
        """Gets the start_time of this ListRecordContentsRequest.

        开始时间,格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :return: The start_time of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRecordContentsRequest.

        开始时间,格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :param start_time: The start_time of this ListRecordContentsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRecordContentsRequest.

        结束时间，格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :return: The end_time of this ListRecordContentsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRecordContentsRequest.

        结束时间，格式为：yyyy-mm-ddThh:mm:ssZ，UTC时间

        :param end_time: The end_time of this ListRecordContentsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListRecordContentsRequest.

        分页编号，从0开始算

        :return: The offset of this ListRecordContentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRecordContentsRequest.

        分页编号，从0开始算

        :param offset: The offset of this ListRecordContentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRecordContentsRequest.

        每页记录数，取值范围[1,100]

        :return: The limit of this ListRecordContentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRecordContentsRequest.

        每页记录数，取值范围[1,100]

        :param limit: The limit of this ListRecordContentsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRecordContentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
