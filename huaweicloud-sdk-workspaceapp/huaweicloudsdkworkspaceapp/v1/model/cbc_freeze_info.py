# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcFreezeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'effect': 'int',
        'scene': 'CbcFreezeScene'
    }

    attribute_map = {
        'effect': 'effect',
        'scene': 'scene'
    }

    def __init__(self, effect=None, scene=None):
        """CbcFreezeInfo

        The model defined in huaweicloud sdk

        :param effect: 在冻结/解冻等操作下，云服务需要达到的主要效果：  - 1：（实现/去除）冻结可释放。（资源冻结后，客户可以手动删除/释放云资源和云资源上数据）  - 2：（实现/去除）冻结不可释放。（资源冻结后，客户不能手动删除/释放云资源以及云资源上数据，相当于云服务被贴了封条，不能改变数据和资源。对应解冻后，就可以删除和修改客户数据了）  - 3：（实现/去除）冻结后不可续费。（资源冻结后，资源不能发起续费操作；解冻后，才可以发起续费操作）  - effect字段和上面status字段(1冻结、0解冻)配合使用，表示在发起冻结/解冻命令下，云服务达到的冻结效果。  - 为空时，默认为effect&#x3D;1（云服务需要能兼容处理，默认当做effect&#x3D;1）。  - 注：云服务是根据status和effect在真实限制云服务的操作/API等。不是使用下文的scene字段去做云服务操作/API的限制。下文的scene字段，主要用于Console页面的tips、API错误码等客户体验使用。
        :type effect: int
        :param scene: 
        :type scene: :class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeScene`
        """
        
        

        self._effect = None
        self._scene = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if scene is not None:
            self.scene = scene

    @property
    def effect(self):
        """Gets the effect of this CbcFreezeInfo.

        在冻结/解冻等操作下，云服务需要达到的主要效果：  - 1：（实现/去除）冻结可释放。（资源冻结后，客户可以手动删除/释放云资源和云资源上数据）  - 2：（实现/去除）冻结不可释放。（资源冻结后，客户不能手动删除/释放云资源以及云资源上数据，相当于云服务被贴了封条，不能改变数据和资源。对应解冻后，就可以删除和修改客户数据了）  - 3：（实现/去除）冻结后不可续费。（资源冻结后，资源不能发起续费操作；解冻后，才可以发起续费操作）  - effect字段和上面status字段(1冻结、0解冻)配合使用，表示在发起冻结/解冻命令下，云服务达到的冻结效果。  - 为空时，默认为effect=1（云服务需要能兼容处理，默认当做effect=1）。  - 注：云服务是根据status和effect在真实限制云服务的操作/API等。不是使用下文的scene字段去做云服务操作/API的限制。下文的scene字段，主要用于Console页面的tips、API错误码等客户体验使用。

        :return: The effect of this CbcFreezeInfo.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this CbcFreezeInfo.

        在冻结/解冻等操作下，云服务需要达到的主要效果：  - 1：（实现/去除）冻结可释放。（资源冻结后，客户可以手动删除/释放云资源和云资源上数据）  - 2：（实现/去除）冻结不可释放。（资源冻结后，客户不能手动删除/释放云资源以及云资源上数据，相当于云服务被贴了封条，不能改变数据和资源。对应解冻后，就可以删除和修改客户数据了）  - 3：（实现/去除）冻结后不可续费。（资源冻结后，资源不能发起续费操作；解冻后，才可以发起续费操作）  - effect字段和上面status字段(1冻结、0解冻)配合使用，表示在发起冻结/解冻命令下，云服务达到的冻结效果。  - 为空时，默认为effect=1（云服务需要能兼容处理，默认当做effect=1）。  - 注：云服务是根据status和effect在真实限制云服务的操作/API等。不是使用下文的scene字段去做云服务操作/API的限制。下文的scene字段，主要用于Console页面的tips、API错误码等客户体验使用。

        :param effect: The effect of this CbcFreezeInfo.
        :type effect: int
        """
        self._effect = effect

    @property
    def scene(self):
        """Gets the scene of this CbcFreezeInfo.

        :return: The scene of this CbcFreezeInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeScene`
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this CbcFreezeInfo.

        :param scene: The scene of this CbcFreezeInfo.
        :type scene: :class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeScene`
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
        if not isinstance(other, CbcFreezeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
