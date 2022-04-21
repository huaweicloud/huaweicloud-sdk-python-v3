# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action_progress': 'ActionProgress',
        'actions': 'list[str]',
        'auth_mode': 'str',
        'az_code': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'created': 'str',
        'enable_dfv': 'str',
        'enable_free': 'str',
        'enable_lemon': 'str',
        'enable_open_tsdb': 'str',
        'status': 'str',
        'tags': 'str',
        'version': 'str',
        'zookeeper_link': 'str'
    }

    attribute_map = {
        'action_progress': 'action_progress',
        'actions': 'actions',
        'auth_mode': 'auth_mode',
        'az_code': 'az_code',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'created': 'created',
        'enable_dfv': 'enable_dfv',
        'enable_free': 'enable_free',
        'enable_lemon': 'enable_lemon',
        'enable_open_tsdb': 'enable_openTSDB',
        'status': 'status',
        'tags': 'tags',
        'version': 'version',
        'zookeeper_link': 'zookeeper_link'
    }

    def __init__(self, action_progress=None, actions=None, auth_mode=None, az_code=None, cluster_id=None, cluster_name=None, created=None, enable_dfv=None, enable_free=None, enable_lemon=None, enable_open_tsdb=None, status=None, tags=None, version=None, zookeeper_link=None):
        """ClusterDetail

        The model defined in huaweicloud sdk

        :param action_progress: 
        :type action_progress: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        :param actions: 集群操作记录
        :type actions: list[str]
        :param auth_mode: 是否开启IAM权限认证。 - false：不开启 - true：开启
        :type auth_mode: str
        :param az_code: 集群所在的可用区（AZ)。
        :type az_code: str
        :param cluster_id: 集群ID，集群唯一标识。
        :type cluster_id: str
        :param cluster_name: CloudTable集群名称。
        :type cluster_name: str
        :param created: 集群创建时间。
        :type created: str
        :param enable_dfv: 是否开启DFV。 - false：不开启 - true：开启
        :type enable_dfv: str
        :param enable_free: 集群是否免费。 - false：不免费 - true：免费
        :type enable_free: str
        :param enable_lemon: 是否开启Lemon。 - false：不开启 - true：开启
        :type enable_lemon: str
        :param enable_open_tsdb: 是否开启OpenTSDB。 - false：不开启 - true：开启
        :type enable_open_tsdb: str
        :param status: 集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除
        :type status: str
        :param tags: 集群标识符。
        :type tags: str
        :param version: 集群版本号。
        :type version: str
        :param zookeeper_link: CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181
        :type zookeeper_link: str
        """
        
        

        self._action_progress = None
        self._actions = None
        self._auth_mode = None
        self._az_code = None
        self._cluster_id = None
        self._cluster_name = None
        self._created = None
        self._enable_dfv = None
        self._enable_free = None
        self._enable_lemon = None
        self._enable_open_tsdb = None
        self._status = None
        self._tags = None
        self._version = None
        self._zookeeper_link = None
        self.discriminator = None

        if action_progress is not None:
            self.action_progress = action_progress
        if actions is not None:
            self.actions = actions
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if az_code is not None:
            self.az_code = az_code
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if created is not None:
            self.created = created
        if enable_dfv is not None:
            self.enable_dfv = enable_dfv
        if enable_free is not None:
            self.enable_free = enable_free
        if enable_lemon is not None:
            self.enable_lemon = enable_lemon
        if enable_open_tsdb is not None:
            self.enable_open_tsdb = enable_open_tsdb
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if version is not None:
            self.version = version
        if zookeeper_link is not None:
            self.zookeeper_link = zookeeper_link

    @property
    def action_progress(self):
        """Gets the action_progress of this ClusterDetail.


        :return: The action_progress of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ClusterDetail.


        :param action_progress: The action_progress of this ClusterDetail.
        :type action_progress: :class:`huaweicloudsdkcloudtable.v2.ActionProgress`
        """
        self._action_progress = action_progress

    @property
    def actions(self):
        """Gets the actions of this ClusterDetail.

        集群操作记录

        :return: The actions of this ClusterDetail.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ClusterDetail.

        集群操作记录

        :param actions: The actions of this ClusterDetail.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def auth_mode(self):
        """Gets the auth_mode of this ClusterDetail.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :return: The auth_mode of this ClusterDetail.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this ClusterDetail.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :param auth_mode: The auth_mode of this ClusterDetail.
        :type auth_mode: str
        """
        self._auth_mode = auth_mode

    @property
    def az_code(self):
        """Gets the az_code of this ClusterDetail.

        集群所在的可用区（AZ)。

        :return: The az_code of this ClusterDetail.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this ClusterDetail.

        集群所在的可用区（AZ)。

        :param az_code: The az_code of this ClusterDetail.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterDetail.

        集群ID，集群唯一标识。

        :return: The cluster_id of this ClusterDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterDetail.

        集群ID，集群唯一标识。

        :param cluster_id: The cluster_id of this ClusterDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ClusterDetail.

        CloudTable集群名称。

        :return: The cluster_name of this ClusterDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ClusterDetail.

        CloudTable集群名称。

        :param cluster_name: The cluster_name of this ClusterDetail.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def created(self):
        """Gets the created of this ClusterDetail.

        集群创建时间。

        :return: The created of this ClusterDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClusterDetail.

        集群创建时间。

        :param created: The created of this ClusterDetail.
        :type created: str
        """
        self._created = created

    @property
    def enable_dfv(self):
        """Gets the enable_dfv of this ClusterDetail.

        是否开启DFV。 - false：不开启 - true：开启

        :return: The enable_dfv of this ClusterDetail.
        :rtype: str
        """
        return self._enable_dfv

    @enable_dfv.setter
    def enable_dfv(self, enable_dfv):
        """Sets the enable_dfv of this ClusterDetail.

        是否开启DFV。 - false：不开启 - true：开启

        :param enable_dfv: The enable_dfv of this ClusterDetail.
        :type enable_dfv: str
        """
        self._enable_dfv = enable_dfv

    @property
    def enable_free(self):
        """Gets the enable_free of this ClusterDetail.

        集群是否免费。 - false：不免费 - true：免费

        :return: The enable_free of this ClusterDetail.
        :rtype: str
        """
        return self._enable_free

    @enable_free.setter
    def enable_free(self, enable_free):
        """Sets the enable_free of this ClusterDetail.

        集群是否免费。 - false：不免费 - true：免费

        :param enable_free: The enable_free of this ClusterDetail.
        :type enable_free: str
        """
        self._enable_free = enable_free

    @property
    def enable_lemon(self):
        """Gets the enable_lemon of this ClusterDetail.

        是否开启Lemon。 - false：不开启 - true：开启

        :return: The enable_lemon of this ClusterDetail.
        :rtype: str
        """
        return self._enable_lemon

    @enable_lemon.setter
    def enable_lemon(self, enable_lemon):
        """Sets the enable_lemon of this ClusterDetail.

        是否开启Lemon。 - false：不开启 - true：开启

        :param enable_lemon: The enable_lemon of this ClusterDetail.
        :type enable_lemon: str
        """
        self._enable_lemon = enable_lemon

    @property
    def enable_open_tsdb(self):
        """Gets the enable_open_tsdb of this ClusterDetail.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :return: The enable_open_tsdb of this ClusterDetail.
        :rtype: str
        """
        return self._enable_open_tsdb

    @enable_open_tsdb.setter
    def enable_open_tsdb(self, enable_open_tsdb):
        """Sets the enable_open_tsdb of this ClusterDetail.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :param enable_open_tsdb: The enable_open_tsdb of this ClusterDetail.
        :type enable_open_tsdb: str
        """
        self._enable_open_tsdb = enable_open_tsdb

    @property
    def status(self):
        """Gets the status of this ClusterDetail.

        集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除

        :return: The status of this ClusterDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterDetail.

        集群状态： - 200：集群正常 - 300：集群异常 - 303：集群创建失败 - 400：集群已删除

        :param status: The status of this ClusterDetail.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ClusterDetail.

        集群标识符。

        :return: The tags of this ClusterDetail.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClusterDetail.

        集群标识符。

        :param tags: The tags of this ClusterDetail.
        :type tags: str
        """
        self._tags = tags

    @property
    def version(self):
        """Gets the version of this ClusterDetail.

        集群版本号。

        :return: The version of this ClusterDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterDetail.

        集群版本号。

        :param version: The version of this ClusterDetail.
        :type version: str
        """
        self._version = version

    @property
    def zookeeper_link(self):
        """Gets the zookeeper_link of this ClusterDetail.

        CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181

        :return: The zookeeper_link of this ClusterDetail.
        :rtype: str
        """
        return self._zookeeper_link

    @zookeeper_link.setter
    def zookeeper_link(self, zookeeper_link):
        """Sets the zookeeper_link of this ClusterDetail.

        CloudTable集群ZooKeeper的链接地址。例如：cloudtable-3058-zk3-Dqcwuh6R.mycloudtable.com:2181,cloudtable-3058-zk2-TCwkZEie.mycloudtable.com:2181,cloudtable-3058-zk1-TBELUFOK.mycloudtable.com:2181

        :param zookeeper_link: The zookeeper_link of this ClusterDetail.
        :type zookeeper_link: str
        """
        self._zookeeper_link = zookeeper_link

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
        if not isinstance(other, ClusterDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
