# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportNetWorkTypeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'net_work': 'str',
        'engine_types': 'list[str]'
    }

    attribute_map = {
        'net_work': 'net_work',
        'engine_types': 'engine_types'
    }

    def __init__(self, net_work=None, engine_types=None):
        r"""SupportNetWorkTypeResponse

        The model defined in huaweicloud sdk

        :param net_work: 网络类型
        :type net_work: str
        :param engine_types: 引擎类型
        :type engine_types: list[str]
        """
        
        

        self._net_work = None
        self._engine_types = None
        self.discriminator = None

        if net_work is not None:
            self.net_work = net_work
        if engine_types is not None:
            self.engine_types = engine_types

    @property
    def net_work(self):
        r"""Gets the net_work of this SupportNetWorkTypeResponse.

        网络类型

        :return: The net_work of this SupportNetWorkTypeResponse.
        :rtype: str
        """
        return self._net_work

    @net_work.setter
    def net_work(self, net_work):
        r"""Sets the net_work of this SupportNetWorkTypeResponse.

        网络类型

        :param net_work: The net_work of this SupportNetWorkTypeResponse.
        :type net_work: str
        """
        self._net_work = net_work

    @property
    def engine_types(self):
        r"""Gets the engine_types of this SupportNetWorkTypeResponse.

        引擎类型

        :return: The engine_types of this SupportNetWorkTypeResponse.
        :rtype: list[str]
        """
        return self._engine_types

    @engine_types.setter
    def engine_types(self, engine_types):
        r"""Sets the engine_types of this SupportNetWorkTypeResponse.

        引擎类型

        :param engine_types: The engine_types of this SupportNetWorkTypeResponse.
        :type engine_types: list[str]
        """
        self._engine_types = engine_types

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
        if not isinstance(other, SupportNetWorkTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
