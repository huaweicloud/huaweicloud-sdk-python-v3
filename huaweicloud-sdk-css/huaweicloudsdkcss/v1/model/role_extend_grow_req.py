# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleExtendGrowReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'nodesize': 'int',
        'disksize': 'int'
    }

    attribute_map = {
        'type': 'type',
        'nodesize': 'nodesize',
        'disksize': 'disksize'
    }

    def __init__(self, type=None, nodesize=None, disksize=None):
        r"""RoleExtendGrowReq

        The model defined in huaweicloud sdk

        :param type: 扩容实例类型。取值为ess、ess-master或ess-client，可以选择其中一个或多个之间的组合但不可以重复选择。  ess-master、ess-client节点只支持增加实例个数。
        :type type: str
        :param nodesize: 扩容实例个数。集群已有实例个数和增加实例个数总和不能超过32。若无需扩容该参数将该参数设置为0即可。
        :type nodesize: int
        :param disksize: 扩容实例存储容量。集群原实例存储容量和扩容实例存储容量之和不能超过创建集群时对应默认实例存储容量上限。若无需扩容该参数将该参数设置为0即可。[当集群为包周期集群时不支持同时修改节点个数和磁盘容量。](tag: hc,tag: hws)  单位：GB。  - ess节点、ess-cold节点扩容步长为20。  - ess-master节点、ess-client节点不允许扩容存储。
        :type disksize: int
        """
        
        

        self._type = None
        self._nodesize = None
        self._disksize = None
        self.discriminator = None

        self.type = type
        self.nodesize = nodesize
        self.disksize = disksize

    @property
    def type(self):
        r"""Gets the type of this RoleExtendGrowReq.

        扩容实例类型。取值为ess、ess-master或ess-client，可以选择其中一个或多个之间的组合但不可以重复选择。  ess-master、ess-client节点只支持增加实例个数。

        :return: The type of this RoleExtendGrowReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RoleExtendGrowReq.

        扩容实例类型。取值为ess、ess-master或ess-client，可以选择其中一个或多个之间的组合但不可以重复选择。  ess-master、ess-client节点只支持增加实例个数。

        :param type: The type of this RoleExtendGrowReq.
        :type type: str
        """
        self._type = type

    @property
    def nodesize(self):
        r"""Gets the nodesize of this RoleExtendGrowReq.

        扩容实例个数。集群已有实例个数和增加实例个数总和不能超过32。若无需扩容该参数将该参数设置为0即可。

        :return: The nodesize of this RoleExtendGrowReq.
        :rtype: int
        """
        return self._nodesize

    @nodesize.setter
    def nodesize(self, nodesize):
        r"""Sets the nodesize of this RoleExtendGrowReq.

        扩容实例个数。集群已有实例个数和增加实例个数总和不能超过32。若无需扩容该参数将该参数设置为0即可。

        :param nodesize: The nodesize of this RoleExtendGrowReq.
        :type nodesize: int
        """
        self._nodesize = nodesize

    @property
    def disksize(self):
        r"""Gets the disksize of this RoleExtendGrowReq.

        扩容实例存储容量。集群原实例存储容量和扩容实例存储容量之和不能超过创建集群时对应默认实例存储容量上限。若无需扩容该参数将该参数设置为0即可。[当集群为包周期集群时不支持同时修改节点个数和磁盘容量。](tag: hc,tag: hws)  单位：GB。  - ess节点、ess-cold节点扩容步长为20。  - ess-master节点、ess-client节点不允许扩容存储。

        :return: The disksize of this RoleExtendGrowReq.
        :rtype: int
        """
        return self._disksize

    @disksize.setter
    def disksize(self, disksize):
        r"""Sets the disksize of this RoleExtendGrowReq.

        扩容实例存储容量。集群原实例存储容量和扩容实例存储容量之和不能超过创建集群时对应默认实例存储容量上限。若无需扩容该参数将该参数设置为0即可。[当集群为包周期集群时不支持同时修改节点个数和磁盘容量。](tag: hc,tag: hws)  单位：GB。  - ess节点、ess-cold节点扩容步长为20。  - ess-master节点、ess-client节点不允许扩容存储。

        :param disksize: The disksize of this RoleExtendGrowReq.
        :type disksize: int
        """
        self._disksize = disksize

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
        if not isinstance(other, RoleExtendGrowReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
