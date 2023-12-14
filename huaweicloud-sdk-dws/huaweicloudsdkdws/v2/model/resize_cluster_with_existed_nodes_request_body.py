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
        'resize': 'Resize',
        'force_backup': 'bool',
        'mode': 'str',
        'logical_cluster_name': 'str',
        'expand_with_existed_node': 'bool',
        'create_node_only': 'bool',
        'auto_redistribute': 'bool',
        'is_scheduler_build_mode': 'bool',
        'redis_conf': 'RedisConf',
        'build_task_info': 'BuildTaskInfo',
        'order_id': 'str'
    }

    attribute_map = {
        'scale_out': 'scale_out',
        'resize': 'resize',
        'force_backup': 'force_backup',
        'mode': 'mode',
        'logical_cluster_name': 'logical_cluster_name',
        'expand_with_existed_node': 'expand_with_existed_node',
        'create_node_only': 'create_node_only',
        'auto_redistribute': 'auto_redistribute',
        'is_scheduler_build_mode': 'is_scheduler_build_mode',
        'redis_conf': 'redis_conf',
        'build_task_info': 'build_task_info',
        'order_id': 'order_id'
    }

    def __init__(self, scale_out=None, resize=None, force_backup=None, mode=None, logical_cluster_name=None, expand_with_existed_node=None, create_node_only=None, auto_redistribute=None, is_scheduler_build_mode=None, redis_conf=None, build_task_info=None, order_id=None):
        """ResizeClusterWithExistedNodesRequestBody

        The model defined in huaweicloud sdk

        :param scale_out: 
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        :param resize: 
        :type resize: :class:`huaweicloudsdkdws.v2.Resize`
        :param force_backup: 是否强制备份
        :type force_backup: bool
        :param mode: 扩容模式
        :type mode: str
        :param logical_cluster_name: 逻辑集群名称
        :type logical_cluster_name: str
        :param expand_with_existed_node: 是否是使用已添加的空闲节点进行扩容
        :type expand_with_existed_node: bool
        :param create_node_only: 否只是添加节点
        :type create_node_only: bool
        :param auto_redistribute: 扩容完成后是否自动启动重分布，默认是
        :type auto_redistribute: bool
        :param is_scheduler_build_mode: 是否调度模式扩容加节点
        :type is_scheduler_build_mode: bool
        :param redis_conf: 
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConf`
        :param build_task_info: 
        :type build_task_info: :class:`huaweicloudsdkdws.v2.BuildTaskInfo`
        :param order_id: 扩容订单ID
        :type order_id: str
        """
        
        

        self._scale_out = None
        self._resize = None
        self._force_backup = None
        self._mode = None
        self._logical_cluster_name = None
        self._expand_with_existed_node = None
        self._create_node_only = None
        self._auto_redistribute = None
        self._is_scheduler_build_mode = None
        self._redis_conf = None
        self._build_task_info = None
        self._order_id = None
        self.discriminator = None

        self.scale_out = scale_out
        if resize is not None:
            self.resize = resize
        self.force_backup = force_backup
        self.mode = mode
        self.logical_cluster_name = logical_cluster_name
        self.expand_with_existed_node = expand_with_existed_node
        self.create_node_only = create_node_only
        self.auto_redistribute = auto_redistribute
        self.is_scheduler_build_mode = is_scheduler_build_mode
        self.redis_conf = redis_conf
        self.build_task_info = build_task_info
        if order_id is not None:
            self.order_id = order_id

    @property
    def scale_out(self):
        """Gets the scale_out of this ResizeClusterWithExistedNodesRequestBody.

        :return: The scale_out of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        return self._scale_out

    @scale_out.setter
    def scale_out(self, scale_out):
        """Sets the scale_out of this ResizeClusterWithExistedNodesRequestBody.

        :param scale_out: The scale_out of this ResizeClusterWithExistedNodesRequestBody.
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        self._scale_out = scale_out

    @property
    def resize(self):
        """Gets the resize of this ResizeClusterWithExistedNodesRequestBody.

        :return: The resize of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.Resize`
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this ResizeClusterWithExistedNodesRequestBody.

        :param resize: The resize of this ResizeClusterWithExistedNodesRequestBody.
        :type resize: :class:`huaweicloudsdkdws.v2.Resize`
        """
        self._resize = resize

    @property
    def force_backup(self):
        """Gets the force_backup of this ResizeClusterWithExistedNodesRequestBody.

        是否强制备份

        :return: The force_backup of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        """Sets the force_backup of this ResizeClusterWithExistedNodesRequestBody.

        是否强制备份

        :param force_backup: The force_backup of this ResizeClusterWithExistedNodesRequestBody.
        :type force_backup: bool
        """
        self._force_backup = force_backup

    @property
    def mode(self):
        """Gets the mode of this ResizeClusterWithExistedNodesRequestBody.

        扩容模式

        :return: The mode of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ResizeClusterWithExistedNodesRequestBody.

        扩容模式

        :param mode: The mode of this ResizeClusterWithExistedNodesRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.

        逻辑集群名称

        :return: The logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.

        逻辑集群名称

        :param logical_cluster_name: The logical_cluster_name of this ResizeClusterWithExistedNodesRequestBody.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def expand_with_existed_node(self):
        """Gets the expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.

        是否是使用已添加的空闲节点进行扩容

        :return: The expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._expand_with_existed_node

    @expand_with_existed_node.setter
    def expand_with_existed_node(self, expand_with_existed_node):
        """Sets the expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.

        是否是使用已添加的空闲节点进行扩容

        :param expand_with_existed_node: The expand_with_existed_node of this ResizeClusterWithExistedNodesRequestBody.
        :type expand_with_existed_node: bool
        """
        self._expand_with_existed_node = expand_with_existed_node

    @property
    def create_node_only(self):
        """Gets the create_node_only of this ResizeClusterWithExistedNodesRequestBody.

        否只是添加节点

        :return: The create_node_only of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._create_node_only

    @create_node_only.setter
    def create_node_only(self, create_node_only):
        """Sets the create_node_only of this ResizeClusterWithExistedNodesRequestBody.

        否只是添加节点

        :param create_node_only: The create_node_only of this ResizeClusterWithExistedNodesRequestBody.
        :type create_node_only: bool
        """
        self._create_node_only = create_node_only

    @property
    def auto_redistribute(self):
        """Gets the auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.

        扩容完成后是否自动启动重分布，默认是

        :return: The auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._auto_redistribute

    @auto_redistribute.setter
    def auto_redistribute(self, auto_redistribute):
        """Sets the auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.

        扩容完成后是否自动启动重分布，默认是

        :param auto_redistribute: The auto_redistribute of this ResizeClusterWithExistedNodesRequestBody.
        :type auto_redistribute: bool
        """
        self._auto_redistribute = auto_redistribute

    @property
    def is_scheduler_build_mode(self):
        """Gets the is_scheduler_build_mode of this ResizeClusterWithExistedNodesRequestBody.

        是否调度模式扩容加节点

        :return: The is_scheduler_build_mode of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: bool
        """
        return self._is_scheduler_build_mode

    @is_scheduler_build_mode.setter
    def is_scheduler_build_mode(self, is_scheduler_build_mode):
        """Sets the is_scheduler_build_mode of this ResizeClusterWithExistedNodesRequestBody.

        是否调度模式扩容加节点

        :param is_scheduler_build_mode: The is_scheduler_build_mode of this ResizeClusterWithExistedNodesRequestBody.
        :type is_scheduler_build_mode: bool
        """
        self._is_scheduler_build_mode = is_scheduler_build_mode

    @property
    def redis_conf(self):
        """Gets the redis_conf of this ResizeClusterWithExistedNodesRequestBody.

        :return: The redis_conf of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.RedisConf`
        """
        return self._redis_conf

    @redis_conf.setter
    def redis_conf(self, redis_conf):
        """Sets the redis_conf of this ResizeClusterWithExistedNodesRequestBody.

        :param redis_conf: The redis_conf of this ResizeClusterWithExistedNodesRequestBody.
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConf`
        """
        self._redis_conf = redis_conf

    @property
    def build_task_info(self):
        """Gets the build_task_info of this ResizeClusterWithExistedNodesRequestBody.

        :return: The build_task_info of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.BuildTaskInfo`
        """
        return self._build_task_info

    @build_task_info.setter
    def build_task_info(self, build_task_info):
        """Sets the build_task_info of this ResizeClusterWithExistedNodesRequestBody.

        :param build_task_info: The build_task_info of this ResizeClusterWithExistedNodesRequestBody.
        :type build_task_info: :class:`huaweicloudsdkdws.v2.BuildTaskInfo`
        """
        self._build_task_info = build_task_info

    @property
    def order_id(self):
        """Gets the order_id of this ResizeClusterWithExistedNodesRequestBody.

        扩容订单ID

        :return: The order_id of this ResizeClusterWithExistedNodesRequestBody.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ResizeClusterWithExistedNodesRequestBody.

        扩容订单ID

        :param order_id: The order_id of this ResizeClusterWithExistedNodesRequestBody.
        :type order_id: str
        """
        self._order_id = order_id

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
