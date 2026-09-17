# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelInstanceProcessRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'processes': 'list[CancelInstanceProcessInfo]'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'processes': 'processes'
    }

    def __init__(self, engine_type=None, processes=None):
        r"""CancelInstanceProcessRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param processes: 会话列表
        :type processes: list[:class:`huaweicloudsdkdas.v3.CancelInstanceProcessInfo`]
        """
        
        

        self._engine_type = None
        self._processes = None
        self.discriminator = None

        self.engine_type = engine_type
        self.processes = processes

    @property
    def engine_type(self):
        r"""Gets the engine_type of this CancelInstanceProcessRequestBody.

        数据库引擎类型

        :return: The engine_type of this CancelInstanceProcessRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this CancelInstanceProcessRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this CancelInstanceProcessRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def processes(self):
        r"""Gets the processes of this CancelInstanceProcessRequestBody.

        会话列表

        :return: The processes of this CancelInstanceProcessRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.CancelInstanceProcessInfo`]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        r"""Sets the processes of this CancelInstanceProcessRequestBody.

        会话列表

        :param processes: The processes of this CancelInstanceProcessRequestBody.
        :type processes: list[:class:`huaweicloudsdkdas.v3.CancelInstanceProcessInfo`]
        """
        self._processes = processes

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
        if not isinstance(other, CancelInstanceProcessRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
