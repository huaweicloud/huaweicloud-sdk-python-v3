# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDaemonsetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'auto_upgrade': 'bool',
        'runtime_info': 'list[RuntimeRequestBody]',
        'schedule_info': 'CreateDaemonsetRequestBodyScheduleInfo'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'auto_upgrade': 'auto_upgrade',
        'runtime_info': 'runtime_info',
        'schedule_info': 'schedule_info'
    }

    def __init__(self, cluster_name=None, auto_upgrade=None, runtime_info=None, schedule_info=None):
        r"""CreateDaemonsetRequestBody

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param auto_upgrade: 开启agent自动升级
        :type auto_upgrade: bool
        :param runtime_info: 容器运行时配置
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        :param schedule_info: 
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        
        

        self._cluster_name = None
        self._auto_upgrade = None
        self._runtime_info = None
        self._schedule_info = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if auto_upgrade is not None:
            self.auto_upgrade = auto_upgrade
        if runtime_info is not None:
            self.runtime_info = runtime_info
        if schedule_info is not None:
            self.schedule_info = schedule_info

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateDaemonsetRequestBody.

        集群名称

        :return: The cluster_name of this CreateDaemonsetRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateDaemonsetRequestBody.

        集群名称

        :param cluster_name: The cluster_name of this CreateDaemonsetRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def auto_upgrade(self):
        r"""Gets the auto_upgrade of this CreateDaemonsetRequestBody.

        开启agent自动升级

        :return: The auto_upgrade of this CreateDaemonsetRequestBody.
        :rtype: bool
        """
        return self._auto_upgrade

    @auto_upgrade.setter
    def auto_upgrade(self, auto_upgrade):
        r"""Sets the auto_upgrade of this CreateDaemonsetRequestBody.

        开启agent自动升级

        :param auto_upgrade: The auto_upgrade of this CreateDaemonsetRequestBody.
        :type auto_upgrade: bool
        """
        self._auto_upgrade = auto_upgrade

    @property
    def runtime_info(self):
        r"""Gets the runtime_info of this CreateDaemonsetRequestBody.

        容器运行时配置

        :return: The runtime_info of this CreateDaemonsetRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        return self._runtime_info

    @runtime_info.setter
    def runtime_info(self, runtime_info):
        r"""Sets the runtime_info of this CreateDaemonsetRequestBody.

        容器运行时配置

        :param runtime_info: The runtime_info of this CreateDaemonsetRequestBody.
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        self._runtime_info = runtime_info

    @property
    def schedule_info(self):
        r"""Gets the schedule_info of this CreateDaemonsetRequestBody.

        :return: The schedule_info of this CreateDaemonsetRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        return self._schedule_info

    @schedule_info.setter
    def schedule_info(self, schedule_info):
        r"""Sets the schedule_info of this CreateDaemonsetRequestBody.

        :param schedule_info: The schedule_info of this CreateDaemonsetRequestBody.
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        self._schedule_info = schedule_info

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
        if not isinstance(other, CreateDaemonsetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
