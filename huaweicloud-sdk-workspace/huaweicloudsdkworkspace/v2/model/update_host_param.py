# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_placement': 'str',
        'name': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'auto_placement': 'auto_placement',
        'name': 'name',
        'host_id': 'host_id'
    }

    def __init__(self, auto_placement=None, name=None, host_id=None):
        r"""UpdateHostParam

        The model defined in huaweicloud sdk

        :param auto_placement: 自动放置，off-取消自动放置，on-打开自动放置。
        :type auto_placement: str
        :param name: 云办公主机名称。
        :type name: str
        :param host_id: 云办公主机id。
        :type host_id: str
        """
        
        

        self._auto_placement = None
        self._name = None
        self._host_id = None
        self.discriminator = None

        if auto_placement is not None:
            self.auto_placement = auto_placement
        if name is not None:
            self.name = name
        if host_id is not None:
            self.host_id = host_id

    @property
    def auto_placement(self):
        r"""Gets the auto_placement of this UpdateHostParam.

        自动放置，off-取消自动放置，on-打开自动放置。

        :return: The auto_placement of this UpdateHostParam.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        r"""Sets the auto_placement of this UpdateHostParam.

        自动放置，off-取消自动放置，on-打开自动放置。

        :param auto_placement: The auto_placement of this UpdateHostParam.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def name(self):
        r"""Gets the name of this UpdateHostParam.

        云办公主机名称。

        :return: The name of this UpdateHostParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHostParam.

        云办公主机名称。

        :param name: The name of this UpdateHostParam.
        :type name: str
        """
        self._name = name

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdateHostParam.

        云办公主机id。

        :return: The host_id of this UpdateHostParam.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdateHostParam.

        云办公主机id。

        :param host_id: The host_id of this UpdateHostParam.
        :type host_id: str
        """
        self._host_id = host_id

    def to_dict(self):
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
        if not isinstance(other, UpdateHostParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
