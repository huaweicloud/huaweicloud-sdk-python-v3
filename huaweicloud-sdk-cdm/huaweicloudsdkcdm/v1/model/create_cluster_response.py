# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

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
        'id': 'str',
        'task': 'Task',
        'datastore': 'Datastore',
        'instances': 'list[ClusterInstance]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'task': 'task',
        'datastore': 'datastore',
        'instances': 'instances'
    }

    def __init__(self, name=None, id=None, task=None, datastore=None, instances=None):
        """CreateClusterResponse

        The model defined in huaweicloud sdk

        :param name: 集群名称
        :type name: str
        :param id: 集群ID
        :type id: str
        :param task: 
        :type task: :class:`huaweicloudsdkcdm.v1.Task`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        :param instances: 集群的节点信息
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterInstance`]
        """
        
        super(CreateClusterResponse, self).__init__()

        self._name = None
        self._id = None
        self._task = None
        self._datastore = None
        self._instances = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if task is not None:
            self.task = task
        if datastore is not None:
            self.datastore = datastore
        if instances is not None:
            self.instances = instances

    @property
    def name(self):
        """Gets the name of this CreateClusterResponse.

        集群名称

        :return: The name of this CreateClusterResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterResponse.

        集群名称

        :param name: The name of this CreateClusterResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this CreateClusterResponse.

        集群ID

        :return: The id of this CreateClusterResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateClusterResponse.

        集群ID

        :param id: The id of this CreateClusterResponse.
        :type id: str
        """
        self._id = id

    @property
    def task(self):
        """Gets the task of this CreateClusterResponse.

        :return: The task of this CreateClusterResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.Task`
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this CreateClusterResponse.

        :param task: The task of this CreateClusterResponse.
        :type task: :class:`huaweicloudsdkcdm.v1.Task`
        """
        self._task = task

    @property
    def datastore(self):
        """Gets the datastore of this CreateClusterResponse.

        :return: The datastore of this CreateClusterResponse.
        :rtype: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateClusterResponse.

        :param datastore: The datastore of this CreateClusterResponse.
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        self._datastore = datastore

    @property
    def instances(self):
        """Gets the instances of this CreateClusterResponse.

        集群的节点信息

        :return: The instances of this CreateClusterResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterInstance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this CreateClusterResponse.

        集群的节点信息

        :param instances: The instances of this CreateClusterResponse.
        :type instances: list[:class:`huaweicloudsdkcdm.v1.ClusterInstance`]
        """
        self._instances = instances

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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
