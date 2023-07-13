# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordRuleRequest:

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
        'default_record_config': 'DefaultRecordConfig'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'record_type': 'record_type',
        'default_record_config': 'default_record_config'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, record_type=None, default_record_config=None):
        """RecordRuleRequest

        The model defined in huaweicloud sdk

        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: 应用名，如需匹配任意应用则填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*
        :type app: str
        :param stream: 录制的流名，如需匹配任流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*
        :type stream: str
        :param record_type: 录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 
        :type record_type: str
        :param default_record_config: 
        :type default_record_config: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._record_type = None
        self._default_record_config = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream
        if record_type is not None:
            self.record_type = record_type
        self.default_record_config = default_record_config

    @property
    def publish_domain(self):
        """Gets the publish_domain of this RecordRuleRequest.

        直播推流域名

        :return: The publish_domain of this RecordRuleRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this RecordRuleRequest.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordRuleRequest.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this RecordRuleRequest.

        应用名，如需匹配任意应用则填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this RecordRuleRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RecordRuleRequest.

        应用名，如需匹配任意应用则填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this RecordRuleRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this RecordRuleRequest.

        录制的流名，如需匹配任流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :return: The stream of this RecordRuleRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this RecordRuleRequest.

        录制的流名，如需匹配任流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :param stream: The stream of this RecordRuleRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def record_type(self):
        """Gets the record_type of this RecordRuleRequest.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 

        :return: The record_type of this RecordRuleRequest.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this RecordRuleRequest.

        录制类型，包括：CONTINUOUS_RECORD，COMMAND_RECORD，PLAN_RECORD，ON_DEMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 - PLAN_RECORD：计划录制，在该规则类型配置后，推的流如果在计划录制的时间区间则触发录制。 - ON_DEMAND_RECORD：按需录制，在该规则类型配置后，录制系统收到推流后，需要调用租户提供的接口查询录制规则，并根据规则录制。 

        :param record_type: The record_type of this RecordRuleRequest.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def default_record_config(self):
        """Gets the default_record_config of this RecordRuleRequest.

        :return: The default_record_config of this RecordRuleRequest.
        :rtype: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        """
        return self._default_record_config

    @default_record_config.setter
    def default_record_config(self, default_record_config):
        """Sets the default_record_config of this RecordRuleRequest.

        :param default_record_config: The default_record_config of this RecordRuleRequest.
        :type default_record_config: :class:`huaweicloudsdklive.v1.DefaultRecordConfig`
        """
        self._default_record_config = default_record_config

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
        if not isinstance(other, RecordRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
