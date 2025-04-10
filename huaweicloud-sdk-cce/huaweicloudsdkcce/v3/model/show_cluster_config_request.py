# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterConfigRequest:

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
        'cluster_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, type=None, cluster_id=None):
        r"""ShowClusterConfigRequest

        The model defined in huaweicloud sdk

        :param type: 组件类型 , 合法取值为control，audit，system-addon。不填写则查询全部类型。 - control 控制面组件日志。 - audit 控制面审计日志。 - system-addon 系统插件日志。
        :type type: str
        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        """
        
        

        self._type = None
        self._cluster_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this ShowClusterConfigRequest.

        组件类型 , 合法取值为control，audit，system-addon。不填写则查询全部类型。 - control 控制面组件日志。 - audit 控制面审计日志。 - system-addon 系统插件日志。

        :return: The type of this ShowClusterConfigRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowClusterConfigRequest.

        组件类型 , 合法取值为control，audit，system-addon。不填写则查询全部类型。 - control 控制面组件日志。 - audit 控制面审计日志。 - system-addon 系统插件日志。

        :param type: The type of this ShowClusterConfigRequest.
        :type type: str
        """
        self._type = type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterConfigRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ShowClusterConfigRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterConfigRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ShowClusterConfigRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ShowClusterConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
