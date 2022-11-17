# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecordRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'record_type': 'str',
        'default_record_config': 'DefaultRecordConfig',
        'create_time': 'date',
        'update_time': 'date'
    }

    attribute_map = {
        'id': 'id',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'record_type': 'record_type',
        'default_record_config': 'default_record_config',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, publish_domain=None, app=None, stream=None, record_type=None, default_record_config=None, create_time=None, update_time=None):
        """UpdateRecordRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id，由服务端返回。创建或修改的时候不携带
        :type id: str
        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: 应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*
        :type app: str
        :param stream: 录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*
        :type stream: str
        :param record_type: 录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD, ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD: 持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD: 命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。命令控制的接口参考/v1/{project_id}/record/control - PLAN_RECORD: 计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD: 按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。租户提供的接口定义参考：/customer-record-ondemand-url 
        :type record_type: str
        :param default_record_config: 
        :type default_record_config: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        :param create_time: 创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回
        :type create_time: date
        :param update_time: 修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回
        :type update_time: date
        """
        
        super(UpdateRecordRuleResponse, self).__init__()

        self._id = None
        self._publish_domain = None
        self._app = None
        self._stream = None
        self._record_type = None
        self._default_record_config = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if record_type is not None:
            self.record_type = record_type
        if default_record_config is not None:
            self.default_record_config = default_record_config
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this UpdateRecordRuleResponse.

        规则id，由服务端返回。创建或修改的时候不携带

        :return: The id of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateRecordRuleResponse.

        规则id，由服务端返回。创建或修改的时候不携带

        :param id: The id of this UpdateRecordRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def publish_domain(self):
        """Gets the publish_domain of this UpdateRecordRuleResponse.

        直播推流域名

        :return: The publish_domain of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this UpdateRecordRuleResponse.

        直播推流域名

        :param publish_domain: The publish_domain of this UpdateRecordRuleResponse.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this UpdateRecordRuleResponse.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this UpdateRecordRuleResponse.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this UpdateRecordRuleResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this UpdateRecordRuleResponse.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :return: The stream of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this UpdateRecordRuleResponse.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :param stream: The stream of this UpdateRecordRuleResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def record_type(self):
        """Gets the record_type of this UpdateRecordRuleResponse.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD, ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD: 持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD: 命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。命令控制的接口参考/v1/{project_id}/record/control - PLAN_RECORD: 计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD: 按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。租户提供的接口定义参考：/customer-record-ondemand-url 

        :return: The record_type of this UpdateRecordRuleResponse.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this UpdateRecordRuleResponse.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD, ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD: 持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD: 命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。命令控制的接口参考/v1/{project_id}/record/control - PLAN_RECORD: 计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD: 按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。租户提供的接口定义参考：/customer-record-ondemand-url 

        :param record_type: The record_type of this UpdateRecordRuleResponse.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def default_record_config(self):
        """Gets the default_record_config of this UpdateRecordRuleResponse.

        :return: The default_record_config of this UpdateRecordRuleResponse.
        :rtype: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        """
        return self._default_record_config

    @default_record_config.setter
    def default_record_config(self, default_record_config):
        """Sets the default_record_config of this UpdateRecordRuleResponse.

        :param default_record_config: The default_record_config of this UpdateRecordRuleResponse.
        :type default_record_config: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        """
        self._default_record_config = default_record_config

    @property
    def create_time(self):
        """Gets the create_time of this UpdateRecordRuleResponse.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The create_time of this UpdateRecordRuleResponse.
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateRecordRuleResponse.

        创建时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param create_time: The create_time of this UpdateRecordRuleResponse.
        :type create_time: date
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateRecordRuleResponse.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :return: The update_time of this UpdateRecordRuleResponse.
        :rtype: date
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateRecordRuleResponse.

        修改时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。 在查询的时候返回

        :param update_time: The update_time of this UpdateRecordRuleResponse.
        :type update_time: date
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateRecordRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
