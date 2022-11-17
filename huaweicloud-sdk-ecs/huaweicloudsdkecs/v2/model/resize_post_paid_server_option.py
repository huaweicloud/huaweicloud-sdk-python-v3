# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizePostPaidServerOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'mode': 'mode'
    }

    def __init__(self, flavor_ref=None, mode=None):
        """ResizePostPaidServerOption

        The model defined in huaweicloud sdk

        :param flavor_ref: 变更后的云服务器规格ID。  可通过[查询云服务器规格变更支持列表](https://support.huaweicloud.com/api-ecs/ecs_02_0402.html)接口查询允许变更的规格列表。
        :type flavor_ref: str
        :param mode: 取值为withStopServer ，支持开机状态下变更规格。  mode取值为withStopServer时，对开机状态的云服务器执行变更规格操作，系统自动对云服务器先执行关机，再变更规格，变更成功后再执行开机。
        :type mode: str
        """
        
        

        self._flavor_ref = None
        self._mode = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        if mode is not None:
            self.mode = mode

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this ResizePostPaidServerOption.

        变更后的云服务器规格ID。  可通过[查询云服务器规格变更支持列表](https://support.huaweicloud.com/api-ecs/ecs_02_0402.html)接口查询允许变更的规格列表。

        :return: The flavor_ref of this ResizePostPaidServerOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this ResizePostPaidServerOption.

        变更后的云服务器规格ID。  可通过[查询云服务器规格变更支持列表](https://support.huaweicloud.com/api-ecs/ecs_02_0402.html)接口查询允许变更的规格列表。

        :param flavor_ref: The flavor_ref of this ResizePostPaidServerOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def mode(self):
        """Gets the mode of this ResizePostPaidServerOption.

        取值为withStopServer ，支持开机状态下变更规格。  mode取值为withStopServer时，对开机状态的云服务器执行变更规格操作，系统自动对云服务器先执行关机，再变更规格，变更成功后再执行开机。

        :return: The mode of this ResizePostPaidServerOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ResizePostPaidServerOption.

        取值为withStopServer ，支持开机状态下变更规格。  mode取值为withStopServer时，对开机状态的云服务器执行变更规格操作，系统自动对云服务器先执行关机，再变更规格，变更成功后再执行开机。

        :param mode: The mode of this ResizePostPaidServerOption.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ResizePostPaidServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
