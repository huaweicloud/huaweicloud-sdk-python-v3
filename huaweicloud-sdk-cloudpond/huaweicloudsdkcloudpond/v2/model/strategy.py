# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Strategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'scene': 'str',
        'effect': 'str'
    }

    attribute_map = {
        'status': 'status',
        'scene': 'scene',
        'effect': 'effect'
    }

    def __init__(self, status=None, scene=None, effect=None):
        r"""Strategy

        The model defined in huaweicloud sdk

        :param status: 运维状态说明： - FREEZE - 已冻结
        :type status: str
        :param scene: 资源运营状态场景： ARREAR：欠费场景 POLICE：公安场景 ILLEGAL：违规场景 VERIFY：客户未实名认证冻结场景
        :type scene: str
        :param effect: 资源运营功能： DELETABLE：可删除 UNDELETABLE：不可删除
        :type effect: str
        """
        
        

        self._status = None
        self._scene = None
        self._effect = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if scene is not None:
            self.scene = scene
        if effect is not None:
            self.effect = effect

    @property
    def status(self):
        r"""Gets the status of this Strategy.

        运维状态说明： - FREEZE - 已冻结

        :return: The status of this Strategy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Strategy.

        运维状态说明： - FREEZE - 已冻结

        :param status: The status of this Strategy.
        :type status: str
        """
        self._status = status

    @property
    def scene(self):
        r"""Gets the scene of this Strategy.

        资源运营状态场景： ARREAR：欠费场景 POLICE：公安场景 ILLEGAL：违规场景 VERIFY：客户未实名认证冻结场景

        :return: The scene of this Strategy.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this Strategy.

        资源运营状态场景： ARREAR：欠费场景 POLICE：公安场景 ILLEGAL：违规场景 VERIFY：客户未实名认证冻结场景

        :param scene: The scene of this Strategy.
        :type scene: str
        """
        self._scene = scene

    @property
    def effect(self):
        r"""Gets the effect of this Strategy.

        资源运营功能： DELETABLE：可删除 UNDELETABLE：不可删除

        :return: The effect of this Strategy.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this Strategy.

        资源运营功能： DELETABLE：可删除 UNDELETABLE：不可删除

        :param effect: The effect of this Strategy.
        :type effect: str
        """
        self._effect = effect

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
        if not isinstance(other, Strategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
