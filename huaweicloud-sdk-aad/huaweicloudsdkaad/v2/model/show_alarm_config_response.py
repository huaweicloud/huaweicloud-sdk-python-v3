# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blackhole': 'str',
        'ddos': 'str',
        'topic_name': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'blackhole': 'blackhole',
        'ddos': 'ddos',
        'topic_name': 'topic_name',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, blackhole=None, ddos=None, topic_name=None, topic_urn=None):
        r"""ShowAlarmConfigResponse

        The model defined in huaweicloud sdk

        :param blackhole: 0开启 1关闭
        :type blackhole: str
        :param ddos: 0开启 1关闭
        :type ddos: str
        :param topic_name: topic名称
        :type topic_name: str
        :param topic_urn: topic订阅链接
        :type topic_urn: str
        """
        
        super().__init__()

        self._blackhole = None
        self._ddos = None
        self._topic_name = None
        self._topic_urn = None
        self.discriminator = None

        if blackhole is not None:
            self.blackhole = blackhole
        if ddos is not None:
            self.ddos = ddos
        if topic_name is not None:
            self.topic_name = topic_name
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def blackhole(self):
        r"""Gets the blackhole of this ShowAlarmConfigResponse.

        0开启 1关闭

        :return: The blackhole of this ShowAlarmConfigResponse.
        :rtype: str
        """
        return self._blackhole

    @blackhole.setter
    def blackhole(self, blackhole):
        r"""Sets the blackhole of this ShowAlarmConfigResponse.

        0开启 1关闭

        :param blackhole: The blackhole of this ShowAlarmConfigResponse.
        :type blackhole: str
        """
        self._blackhole = blackhole

    @property
    def ddos(self):
        r"""Gets the ddos of this ShowAlarmConfigResponse.

        0开启 1关闭

        :return: The ddos of this ShowAlarmConfigResponse.
        :rtype: str
        """
        return self._ddos

    @ddos.setter
    def ddos(self, ddos):
        r"""Sets the ddos of this ShowAlarmConfigResponse.

        0开启 1关闭

        :param ddos: The ddos of this ShowAlarmConfigResponse.
        :type ddos: str
        """
        self._ddos = ddos

    @property
    def topic_name(self):
        r"""Gets the topic_name of this ShowAlarmConfigResponse.

        topic名称

        :return: The topic_name of this ShowAlarmConfigResponse.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this ShowAlarmConfigResponse.

        topic名称

        :param topic_name: The topic_name of this ShowAlarmConfigResponse.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this ShowAlarmConfigResponse.

        topic订阅链接

        :return: The topic_urn of this ShowAlarmConfigResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this ShowAlarmConfigResponse.

        topic订阅链接

        :param topic_urn: The topic_urn of this ShowAlarmConfigResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    def to_dict(self):
        import warnings
        warnings.warn("ShowAlarmConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAlarmConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
