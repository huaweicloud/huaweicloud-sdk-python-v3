# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrozenInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'effect': 'int',
        'scene': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'effect': 'effect',
        'scene': 'scene'
    }

    def __init__(self, status=None, effect=None, scene=None):
        """FrozenInfo

        The model defined in huaweicloud sdk

        :param status: 云服务或资源实例状态，取值： - 0：解冻/正常（云服务恢复正常）。 - 1：冻结（资源和数据会保留，但租户无法再正常使用云服务）。 - 2：删除/终止（资源和数据将清除）。
        :type status: int
        :param effect: 在冻结/解冻操作下，取值： - 1（默认值）：冻结可释放。 - 2：冻结不可释放。 - 3：冻结后不可续费。
        :type effect: int
        :param scene: 更新云服务状态的业务场景列表，取值： - ARREAR（默认值）：欠费场景。为正常的运营业务场景，包括包周期资源到期、按需资源扣费失败。 - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。
        :type scene: list[str]
        """
        
        

        self._status = None
        self._effect = None
        self._scene = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if effect is not None:
            self.effect = effect
        if scene is not None:
            self.scene = scene

    @property
    def status(self):
        """Gets the status of this FrozenInfo.

        云服务或资源实例状态，取值： - 0：解冻/正常（云服务恢复正常）。 - 1：冻结（资源和数据会保留，但租户无法再正常使用云服务）。 - 2：删除/终止（资源和数据将清除）。

        :return: The status of this FrozenInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FrozenInfo.

        云服务或资源实例状态，取值： - 0：解冻/正常（云服务恢复正常）。 - 1：冻结（资源和数据会保留，但租户无法再正常使用云服务）。 - 2：删除/终止（资源和数据将清除）。

        :param status: The status of this FrozenInfo.
        :type status: int
        """
        self._status = status

    @property
    def effect(self):
        """Gets the effect of this FrozenInfo.

        在冻结/解冻操作下，取值： - 1（默认值）：冻结可释放。 - 2：冻结不可释放。 - 3：冻结后不可续费。

        :return: The effect of this FrozenInfo.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this FrozenInfo.

        在冻结/解冻操作下，取值： - 1（默认值）：冻结可释放。 - 2：冻结不可释放。 - 3：冻结后不可续费。

        :param effect: The effect of this FrozenInfo.
        :type effect: int
        """
        self._effect = effect

    @property
    def scene(self):
        """Gets the scene of this FrozenInfo.

        更新云服务状态的业务场景列表，取值： - ARREAR（默认值）：欠费场景。为正常的运营业务场景，包括包周期资源到期、按需资源扣费失败。 - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。

        :return: The scene of this FrozenInfo.
        :rtype: list[str]
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this FrozenInfo.

        更新云服务状态的业务场景列表，取值： - ARREAR（默认值）：欠费场景。为正常的运营业务场景，包括包周期资源到期、按需资源扣费失败。 - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。

        :param scene: The scene of this FrozenInfo.
        :type scene: list[str]
        """
        self._scene = scene

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
        if not isinstance(other, FrozenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
