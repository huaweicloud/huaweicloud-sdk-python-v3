# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckWeakPasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'engine': 'str'
    }

    attribute_map = {
        'target': 'target',
        'engine': 'engine'
    }

    def __init__(self, target=None, engine=None):
        r"""CheckWeakPasswordRequest

        The model defined in huaweicloud sdk

        :param target: 需要检验的密码。
        :type target: str
        :param engine: 引擎名称，取值范围：sqlserver, mysql, postgresql，区分大小写。
        :type engine: str
        """
        
        

        self._target = None
        self._engine = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if engine is not None:
            self.engine = engine

    @property
    def target(self):
        r"""Gets the target of this CheckWeakPasswordRequest.

        需要检验的密码。

        :return: The target of this CheckWeakPasswordRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this CheckWeakPasswordRequest.

        需要检验的密码。

        :param target: The target of this CheckWeakPasswordRequest.
        :type target: str
        """
        self._target = target

    @property
    def engine(self):
        r"""Gets the engine of this CheckWeakPasswordRequest.

        引擎名称，取值范围：sqlserver, mysql, postgresql，区分大小写。

        :return: The engine of this CheckWeakPasswordRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CheckWeakPasswordRequest.

        引擎名称，取值范围：sqlserver, mysql, postgresql，区分大小写。

        :param engine: The engine of this CheckWeakPasswordRequest.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, CheckWeakPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
