# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventStreamingSink:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sink_fg': 'SinkFGParameters',
        'sink_kafka': 'SinkKafkaParameters',
        'sink_obs': 'SinkObsParameters',
        'name': 'str'
    }

    attribute_map = {
        'sink_fg': 'sink_fg',
        'sink_kafka': 'sink_kafka',
        'sink_obs': 'sink_obs',
        'name': 'name'
    }

    def __init__(self, sink_fg=None, sink_kafka=None, sink_obs=None, name=None):
        r"""EventStreamingSink

        The model defined in huaweicloud sdk

        :param sink_fg: 
        :type sink_fg: :class:`huaweicloudsdkeg.v1.SinkFGParameters`
        :param sink_kafka: 
        :type sink_kafka: :class:`huaweicloudsdkeg.v1.SinkKafkaParameters`
        :param sink_obs: 
        :type sink_obs: :class:`huaweicloudsdkeg.v1.SinkObsParameters`
        :param name: 事件目标类型名称
        :type name: str
        """
        
        

        self._sink_fg = None
        self._sink_kafka = None
        self._sink_obs = None
        self._name = None
        self.discriminator = None

        if sink_fg is not None:
            self.sink_fg = sink_fg
        if sink_kafka is not None:
            self.sink_kafka = sink_kafka
        if sink_obs is not None:
            self.sink_obs = sink_obs
        if name is not None:
            self.name = name

    @property
    def sink_fg(self):
        r"""Gets the sink_fg of this EventStreamingSink.

        :return: The sink_fg of this EventStreamingSink.
        :rtype: :class:`huaweicloudsdkeg.v1.SinkFGParameters`
        """
        return self._sink_fg

    @sink_fg.setter
    def sink_fg(self, sink_fg):
        r"""Sets the sink_fg of this EventStreamingSink.

        :param sink_fg: The sink_fg of this EventStreamingSink.
        :type sink_fg: :class:`huaweicloudsdkeg.v1.SinkFGParameters`
        """
        self._sink_fg = sink_fg

    @property
    def sink_kafka(self):
        r"""Gets the sink_kafka of this EventStreamingSink.

        :return: The sink_kafka of this EventStreamingSink.
        :rtype: :class:`huaweicloudsdkeg.v1.SinkKafkaParameters`
        """
        return self._sink_kafka

    @sink_kafka.setter
    def sink_kafka(self, sink_kafka):
        r"""Sets the sink_kafka of this EventStreamingSink.

        :param sink_kafka: The sink_kafka of this EventStreamingSink.
        :type sink_kafka: :class:`huaweicloudsdkeg.v1.SinkKafkaParameters`
        """
        self._sink_kafka = sink_kafka

    @property
    def sink_obs(self):
        r"""Gets the sink_obs of this EventStreamingSink.

        :return: The sink_obs of this EventStreamingSink.
        :rtype: :class:`huaweicloudsdkeg.v1.SinkObsParameters`
        """
        return self._sink_obs

    @sink_obs.setter
    def sink_obs(self, sink_obs):
        r"""Sets the sink_obs of this EventStreamingSink.

        :param sink_obs: The sink_obs of this EventStreamingSink.
        :type sink_obs: :class:`huaweicloudsdkeg.v1.SinkObsParameters`
        """
        self._sink_obs = sink_obs

    @property
    def name(self):
        r"""Gets the name of this EventStreamingSink.

        事件目标类型名称

        :return: The name of this EventStreamingSink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventStreamingSink.

        事件目标类型名称

        :param name: The name of this EventStreamingSink.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, EventStreamingSink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
