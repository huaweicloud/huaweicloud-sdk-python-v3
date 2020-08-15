# coding: utf-8

import pprint
import re

import six





class TenantInfoReq:


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
        'resources': 'list[Resource]',
        'effect': 'int',
        'scene': 'str'
    }

    attribute_map = {
        'status': 'status',
        'resources': 'resources',
        'effect': 'effect',
        'scene': 'scene'
    }

    def __init__(self, status=None, resources=None, effect=None, scene=None):
        """TenantInfoReq - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._resources = None
        self._effect = None
        self._scene = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if resources is not None:
            self.resources = resources
        if effect is not None:
            self.effect = effect
        if scene is not None:
            self.scene = scene

    @property
    def status(self):
        """Gets the status of this TenantInfoReq.

        租户状态。 - 0：解冻正常； - 1：冻结； - 2：删除/终止 

        :return: The status of this TenantInfoReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TenantInfoReq.

        租户状态。 - 0：解冻正常； - 1：冻结； - 2：删除/终止 

        :param status: The status of this TenantInfoReq.
        :type: int
        """
        self._status = status

    @property
    def resources(self):
        """Gets the resources of this TenantInfoReq.

        资源类型

        :return: The resources of this TenantInfoReq.
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this TenantInfoReq.

        资源类型

        :param resources: The resources of this TenantInfoReq.
        :type: list[Resource]
        """
        self._resources = resources

    @property
    def effect(self):
        """Gets the effect of this TenantInfoReq.

        云服务根据该字段，实现相应的效果。 - 1:冻结可释放； - 2：冻结不可释放； - 3：冻结后不可续费；  默认值：1 

        :return: The effect of this TenantInfoReq.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this TenantInfoReq.

        云服务根据该字段，实现相应的效果。 - 1:冻结可释放； - 2：冻结不可释放； - 3：冻结后不可续费；  默认值：1 

        :param effect: The effect of this TenantInfoReq.
        :type: int
        """
        self._effect = effect

    @property
    def scene(self):
        """Gets the scene of this TenantInfoReq.

        云服务状态的业务场景。只作为场景描述，CBC不使用这个字段去控制云服务操作。 - ARREAR：欠费 - POLICE：公安冻结 - ILLEGAL：违规冻结 - VERIFY：客户未实名认证 - PARTNER：合作伙伴冻结  默认值：ARREAR 

        :return: The scene of this TenantInfoReq.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this TenantInfoReq.

        云服务状态的业务场景。只作为场景描述，CBC不使用这个字段去控制云服务操作。 - ARREAR：欠费 - POLICE：公安冻结 - ILLEGAL：违规冻结 - VERIFY：客户未实名认证 - PARTNER：合作伙伴冻结  默认值：ARREAR 

        :param scene: The scene of this TenantInfoReq.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TenantInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
