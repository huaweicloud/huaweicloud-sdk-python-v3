# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace_name': 'str',
        'cluster_name': 'str',
        'status': 'str',
        'pods_num': 'int',
        'image_name': 'str',
        'match_labels': 'list[LabelInfo]',
        'execute_time': 'int',
        'create_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'status': 'status',
        'pods_num': 'pods_num',
        'image_name': 'image_name',
        'match_labels': 'match_labels',
        'execute_time': 'execute_time',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, namespace_name=None, cluster_name=None, status=None, pods_num=None, image_name=None, match_labels=None, execute_time=None, create_time=None):
        r"""ServerlessJobInfo

        The model defined in huaweicloud sdk

        :param name: 普通任务名称
        :type name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param cluster_name: 所属集群
        :type cluster_name: str
        :param status: 状态，包含以下几种 -Running：正常运行 -Failed：存在异常
        :type status: str
        :param pods_num: 实例个数
        :type pods_num: int
        :param image_name: 镜像名称
        :type image_name: str
        :param match_labels: 标签
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        :param execute_time: 执行时间
        :type execute_time: int
        :param create_time: 创建时间
        :type create_time: int
        """
        
        

        self._name = None
        self._namespace_name = None
        self._cluster_name = None
        self._status = None
        self._pods_num = None
        self._image_name = None
        self._match_labels = None
        self._execute_time = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if status is not None:
            self.status = status
        if pods_num is not None:
            self.pods_num = pods_num
        if image_name is not None:
            self.image_name = image_name
        if match_labels is not None:
            self.match_labels = match_labels
        if execute_time is not None:
            self.execute_time = execute_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this ServerlessJobInfo.

        普通任务名称

        :return: The name of this ServerlessJobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerlessJobInfo.

        普通任务名称

        :param name: The name of this ServerlessJobInfo.
        :type name: str
        """
        self._name = name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ServerlessJobInfo.

        命名空间名称

        :return: The namespace_name of this ServerlessJobInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ServerlessJobInfo.

        命名空间名称

        :param namespace_name: The namespace_name of this ServerlessJobInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ServerlessJobInfo.

        所属集群

        :return: The cluster_name of this ServerlessJobInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ServerlessJobInfo.

        所属集群

        :param cluster_name: The cluster_name of this ServerlessJobInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def status(self):
        r"""Gets the status of this ServerlessJobInfo.

        状态，包含以下几种 -Running：正常运行 -Failed：存在异常

        :return: The status of this ServerlessJobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerlessJobInfo.

        状态，包含以下几种 -Running：正常运行 -Failed：存在异常

        :param status: The status of this ServerlessJobInfo.
        :type status: str
        """
        self._status = status

    @property
    def pods_num(self):
        r"""Gets the pods_num of this ServerlessJobInfo.

        实例个数

        :return: The pods_num of this ServerlessJobInfo.
        :rtype: int
        """
        return self._pods_num

    @pods_num.setter
    def pods_num(self, pods_num):
        r"""Sets the pods_num of this ServerlessJobInfo.

        实例个数

        :param pods_num: The pods_num of this ServerlessJobInfo.
        :type pods_num: int
        """
        self._pods_num = pods_num

    @property
    def image_name(self):
        r"""Gets the image_name of this ServerlessJobInfo.

        镜像名称

        :return: The image_name of this ServerlessJobInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ServerlessJobInfo.

        镜像名称

        :param image_name: The image_name of this ServerlessJobInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def match_labels(self):
        r"""Gets the match_labels of this ServerlessJobInfo.

        标签

        :return: The match_labels of this ServerlessJobInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        r"""Sets the match_labels of this ServerlessJobInfo.

        标签

        :param match_labels: The match_labels of this ServerlessJobInfo.
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        self._match_labels = match_labels

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ServerlessJobInfo.

        执行时间

        :return: The execute_time of this ServerlessJobInfo.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ServerlessJobInfo.

        执行时间

        :param execute_time: The execute_time of this ServerlessJobInfo.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ServerlessJobInfo.

        创建时间

        :return: The create_time of this ServerlessJobInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ServerlessJobInfo.

        创建时间

        :param create_time: The create_time of this ServerlessJobInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ServerlessJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
