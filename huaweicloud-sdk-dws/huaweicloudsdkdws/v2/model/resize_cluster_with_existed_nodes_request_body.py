# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeClusterWithExistedNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale_out': 'ScaleOut',
        'force_backup': 'bool',
        'mode': 'str',
        'logical_cluster_name': 'str',
        'expand_with_existed_node': 'bool',
        'auto_redistribute': 'bool',
        'redis_conf': 'RedisConfReq'
    }

    attribute_map = {
        'scale_out': 'scale_out',
        'force_backup': 'force_backup',
        'mode': 'mode',
        'logical_cluster_name': 'logical_cluster_name',
        'expand_with_existed_node': 'expand_with_existed_node',
        'auto_redistribute': 'auto_redistribute',
        'redis_conf': 'redis_conf'
    }

    def __init__(self, scale_out=None, force_backup=None, mode=None, logical_cluster_name=None, expand_with_existed_node=None, auto_redistribute=None, redis_conf=None):
        r"""ResizeClusterWithExistedNodesRequestBody

        The model defined in huaweicloud sdk

        :param scale_out: 
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        :param force_backup: **参数解释**： 是否强制备份。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type force_backup: bool
        :param mode: **参数解释**： 扩容模式，不传默认离线read-only。 **约束限制**： 在线模式在大部分低版本集群不支持，请在联系运维人员确认后方才可用。 **取值范围**： read-only：离线模式 insert：在线模式 **默认取值**： 不涉及。
        :type mode: str
        :param logical_cluster_name: **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 非逻辑集群模式下该字段不填，逻辑集群模式下不传默认elastic_group。 **默认取值**： elastic_group
        :type logical_cluster_name: str
        :param expand_with_existed_node: **参数解释**： 是否是使用已添加的空闲节点进行扩容。 **约束限制**： 不涉及。 **取值范围**： true：使用空闲节点扩容 false：不使用空闲节点扩容 **默认取值**： false
        :type expand_with_existed_node: bool
        :param auto_redistribute: **参数解释**： 扩容完成后是否自动启动重分布，默认true。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： true
        :type auto_redistribute: bool
        :param redis_conf: 
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConfReq`
        """
        
        

        self._scale_out = None
        self._force_backup = None
        self._mode = None
        self._logical_cluster_name = None
        self._expand_with_existed_node = None
        self._auto_redistribute = None
        self._redis_conf = None
        self.discriminator = None

        self.scale_out = scale_out
        if force_backup is not None:
            self.force_backup = force_backup
        if mode is not None:
            self.mode = mode
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        self.expand_with_existed_node = expand_with_existed_node
        if auto_redistribute is not None:
            self.auto_redistribute = auto_redistribute
        if redis_conf is not None:
            self.redis_conf = redis_conf

    @property
    def scale_out(self):
        r"""Gets the scale_out of this ResizeClusterWithExistedNodesRequestBody.

        :return: The scale_out of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        return self._scale_out

    @scale_out.setter
    def scale_out(self, scale_out):
        r"""Sets the scale_out of this ResizeClusterWithExistedNodesRequestBody.

        :param scale_out: The scale_out of this ResizeClusterWithExistedNodesRequestBody.
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        self._scale_out = scale_out

    @property
    def force_backup(self):
        r"""Gets the force_backup of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 是否强制备份。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The force_backup of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        r"""Sets the force_backup of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 是否强制备份。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param force_backup: The force_backup of this ResizeClusterWithExistedNodesRequestBody.
        :type force_backup: bool
        """
        self._force_backup = force_backup

    @property
    def mode(self):
        r"""Gets the mode of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 扩容模式，不传默认离线read-only。 **约束限制**： 在线模式在大部分低版本集群不支持，请在联系运维人员确认后方才可用。 **取值范围**： read-only：离线模式 insert：在线模式 **默认取值**： 不涉及。

        :return: The mode of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 扩容模式，不传默认离线read-only。 **约束限制**： 在线模式在大部分低版本集群不支持，请在联系运维人员确认后方才可用。 **取值范围**： read-only：离线模式 insert：在线模式 **默认取值**： 不涉及。

        :param mode: The mode of this ResizeClusterWithExistedNodesRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 非逻辑集群模式下该字段不填，逻辑集群模式下不传默认elastic_group。 **默认取值**： elastic_group

        :return: The logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 非逻辑集群模式下该字段不填，逻辑集群模式下不传默认elastic_group。 **默认取值**： elastic_group

        :param logical_cluster_name: The logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def expand_with_existed_node(self):
        r"""Gets the expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 是否是使用已添加的空闲节点进行扩容。 **约束限制**： 不涉及。 **取值范围**： true：使用空闲节点扩容 false：不使用空闲节点扩容 **默认取值**： false

        :return: The expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._expand_with_existed_node

    @expand_with_existed_node.setter
    def expand_with_existed_node(self, expand_with_existed_node):
        r"""Sets the expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 是否是使用已添加的空闲节点进行扩容。 **约束限制**： 不涉及。 **取值范围**： true：使用空闲节点扩容 false：不使用空闲节点扩容 **默认取值**： false

        :param expand_with_existed_node: The expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.
        :type expand_with_existed_node: bool
        """
        self._expand_with_existed_node = expand_with_existed_node

    @property
    def auto_redistribute(self):
        r"""Gets the auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 扩容完成后是否自动启动重分布，默认true。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： true

        :return: The auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._auto_redistribute

    @auto_redistribute.setter
    def auto_redistribute(self, auto_redistribute):
        r"""Sets the auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.

        **参数解释**： 扩容完成后是否自动启动重分布，默认true。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： true

        :param auto_redistribute: The auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.
        :type auto_redistribute: bool
        """
        self._auto_redistribute = auto_redistribute

    @property
    def redis_conf(self):
        r"""Gets the redis_conf of this ResizeClusterWithExistedNodesRequestBody.

        :return: The redis_conf of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.RedisConfReq`
        """
        return self._redis_conf

    @redis_conf.setter
    def redis_conf(self, redis_conf):
        r"""Sets the redis_conf of this ResizeClusterWithExistedNodesRequestBody.

        :param redis_conf: The redis_conf of this ResizeClusterWithExistedNodesRequestBody.
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConfReq`
        """
        self._redis_conf = redis_conf

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
        if not isinstance(other, ResizeClusterWithExistedNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
