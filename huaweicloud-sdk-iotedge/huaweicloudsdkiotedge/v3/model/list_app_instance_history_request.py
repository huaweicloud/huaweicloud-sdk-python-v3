# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppInstanceHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'app_instance_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'app_instance_id': 'app_instance_id',
        'namespace': 'namespace'
    }

    def __init__(self, cluster_id=None, app_instance_id=None, namespace=None):
        """ListAppInstanceHistoryRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 边缘集群ID
        :type cluster_id: str
        :param app_instance_id: 应用实例ID
        :type app_instance_id: str
        :param namespace: 命名空间
        :type namespace: str
        """
        
        

        self._cluster_id = None
        self._app_instance_id = None
        self._namespace = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.app_instance_id = app_instance_id
        if namespace is not None:
            self.namespace = namespace

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListAppInstanceHistoryRequest.

        边缘集群ID

        :return: The cluster_id of this ListAppInstanceHistoryRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListAppInstanceHistoryRequest.

        边缘集群ID

        :param cluster_id: The cluster_id of this ListAppInstanceHistoryRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def app_instance_id(self):
        """Gets the app_instance_id of this ListAppInstanceHistoryRequest.

        应用实例ID

        :return: The app_instance_id of this ListAppInstanceHistoryRequest.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id):
        """Sets the app_instance_id of this ListAppInstanceHistoryRequest.

        应用实例ID

        :param app_instance_id: The app_instance_id of this ListAppInstanceHistoryRequest.
        :type app_instance_id: str
        """
        self._app_instance_id = app_instance_id

    @property
    def namespace(self):
        """Gets the namespace of this ListAppInstanceHistoryRequest.

        命名空间

        :return: The namespace of this ListAppInstanceHistoryRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAppInstanceHistoryRequest.

        命名空间

        :param namespace: The namespace of this ListAppInstanceHistoryRequest.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, ListAppInstanceHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
