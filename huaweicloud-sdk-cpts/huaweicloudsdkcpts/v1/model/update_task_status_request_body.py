# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'int',
        'cluster_type': 'str',
        'without_package': 'int',
        'network_info': 'NetworkInfo',
        'status': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'without_package': 'without_package',
        'network_info': 'network_info',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, cluster_id=None, cluster_type=None, without_package=None, network_info=None, status=None, enterprise_project_id=None):
        r"""UpdateTaskStatusRequestBody

        The model defined in huaweicloud sdk

        :param cluster_id: 资源组id
        :type cluster_id: int
        :param cluster_type: 资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）
        :type cluster_type: str
        :param without_package: 套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）
        :type without_package: int
        :param network_info: 
        :type network_info: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        :param status: 状态（9：启动任务；2：停止任务）
        :type status: int
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._cluster_id = None
        self._cluster_type = None
        self._without_package = None
        self._network_info = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.without_package = without_package
        self.network_info = network_info
        self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateTaskStatusRequestBody.

        资源组id

        :return: The cluster_id of this UpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateTaskStatusRequestBody.

        资源组id

        :param cluster_id: The cluster_id of this UpdateTaskStatusRequestBody.
        :type cluster_id: int
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this UpdateTaskStatusRequestBody.

        资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）

        :return: The cluster_type of this UpdateTaskStatusRequestBody.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this UpdateTaskStatusRequestBody.

        资源组类型（共享资源组：shared-cluster-internet；私有资源组：private-cluster）

        :param cluster_type: The cluster_type of this UpdateTaskStatusRequestBody.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def without_package(self):
        r"""Gets the without_package of this UpdateTaskStatusRequestBody.

        套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）

        :return: The without_package of this UpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._without_package

    @without_package.setter
    def without_package(self, without_package):
        r"""Sets the without_package of this UpdateTaskStatusRequestBody.

        套餐包VUM不足的情况下用户选择是不是要走按需计费模式（当前版本固定值：0）

        :param without_package: The without_package of this UpdateTaskStatusRequestBody.
        :type without_package: int
        """
        self._without_package = without_package

    @property
    def network_info(self):
        r"""Gets the network_info of this UpdateTaskStatusRequestBody.

        :return: The network_info of this UpdateTaskStatusRequestBody.
        :rtype: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        r"""Sets the network_info of this UpdateTaskStatusRequestBody.

        :param network_info: The network_info of this UpdateTaskStatusRequestBody.
        :type network_info: :class:`huaweicloudsdkcpts.v1.NetworkInfo`
        """
        self._network_info = network_info

    @property
    def status(self):
        r"""Gets the status of this UpdateTaskStatusRequestBody.

        状态（9：启动任务；2：停止任务）

        :return: The status of this UpdateTaskStatusRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateTaskStatusRequestBody.

        状态（9：启动任务；2：停止任务）

        :param status: The status of this UpdateTaskStatusRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateTaskStatusRequestBody.

        企业项目id

        :return: The enterprise_project_id of this UpdateTaskStatusRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateTaskStatusRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this UpdateTaskStatusRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, UpdateTaskStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
