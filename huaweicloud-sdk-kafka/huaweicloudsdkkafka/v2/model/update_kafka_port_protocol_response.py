# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKafkaPortProtocolResponse(SdkResponse):

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
        'protocol': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'protocol': 'protocol',
        'enable': 'enable'
    }

    def __init__(self, job_id=None, protocol=None, enable=None):
        r"""UpdateKafkaPortProtocolResponse

        The model defined in huaweicloud sdk

        :param job_id: 后台任务id。
        :type job_id: str
        :param protocol: 开启或者关闭的Kafka接入方式。
        :type protocol: str
        :param enable: 开启动作或者关闭动作。
        :type enable: bool
        """
        
        super(UpdateKafkaPortProtocolResponse, self).__init__()

        self._job_id = None
        self._protocol = None
        self._enable = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if protocol is not None:
            self.protocol = protocol
        if enable is not None:
            self.enable = enable

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateKafkaPortProtocolResponse.

        后台任务id。

        :return: The job_id of this UpdateKafkaPortProtocolResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateKafkaPortProtocolResponse.

        后台任务id。

        :param job_id: The job_id of this UpdateKafkaPortProtocolResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def protocol(self):
        r"""Gets the protocol of this UpdateKafkaPortProtocolResponse.

        开启或者关闭的Kafka接入方式。

        :return: The protocol of this UpdateKafkaPortProtocolResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this UpdateKafkaPortProtocolResponse.

        开启或者关闭的Kafka接入方式。

        :param protocol: The protocol of this UpdateKafkaPortProtocolResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def enable(self):
        r"""Gets the enable of this UpdateKafkaPortProtocolResponse.

        开启动作或者关闭动作。

        :return: The enable of this UpdateKafkaPortProtocolResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateKafkaPortProtocolResponse.

        开启动作或者关闭动作。

        :param enable: The enable of this UpdateKafkaPortProtocolResponse.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, UpdateKafkaPortProtocolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
