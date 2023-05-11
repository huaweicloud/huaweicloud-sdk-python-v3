# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSinkTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_type': 'str',
        'task_name': 'str',
        'destination_type': 'str',
        'obs_destination_descriptor': 'ObsDestinationDescriptor'
    }

    attribute_map = {
        'source_type': 'source_type',
        'task_name': 'task_name',
        'destination_type': 'destination_type',
        'obs_destination_descriptor': 'obs_destination_descriptor'
    }

    def __init__(self, source_type=None, task_name=None, destination_type=None, obs_destination_descriptor=None):
        """CreateSinkTaskReq

        The model defined in huaweicloud sdk

        :param source_type: 源数据类型，目前只支持BLOB。 
        :type source_type: str
        :param task_name: 转储任务名称。 
        :type task_name: str
        :param destination_type: 转存的目标类型，当前只支持OBS。 
        :type destination_type: str
        :param obs_destination_descriptor: 
        :type obs_destination_descriptor: :class:`huaweicloudsdkkafka.v2.ObsDestinationDescriptor`
        """
        
        

        self._source_type = None
        self._task_name = None
        self._destination_type = None
        self._obs_destination_descriptor = None
        self.discriminator = None

        self.source_type = source_type
        self.task_name = task_name
        self.destination_type = destination_type
        self.obs_destination_descriptor = obs_destination_descriptor

    @property
    def source_type(self):
        """Gets the source_type of this CreateSinkTaskReq.

        源数据类型，目前只支持BLOB。 

        :return: The source_type of this CreateSinkTaskReq.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CreateSinkTaskReq.

        源数据类型，目前只支持BLOB。 

        :param source_type: The source_type of this CreateSinkTaskReq.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def task_name(self):
        """Gets the task_name of this CreateSinkTaskReq.

        转储任务名称。 

        :return: The task_name of this CreateSinkTaskReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateSinkTaskReq.

        转储任务名称。 

        :param task_name: The task_name of this CreateSinkTaskReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def destination_type(self):
        """Gets the destination_type of this CreateSinkTaskReq.

        转存的目标类型，当前只支持OBS。 

        :return: The destination_type of this CreateSinkTaskReq.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this CreateSinkTaskReq.

        转存的目标类型，当前只支持OBS。 

        :param destination_type: The destination_type of this CreateSinkTaskReq.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def obs_destination_descriptor(self):
        """Gets the obs_destination_descriptor of this CreateSinkTaskReq.

        :return: The obs_destination_descriptor of this CreateSinkTaskReq.
        :rtype: :class:`huaweicloudsdkkafka.v2.ObsDestinationDescriptor`
        """
        return self._obs_destination_descriptor

    @obs_destination_descriptor.setter
    def obs_destination_descriptor(self, obs_destination_descriptor):
        """Sets the obs_destination_descriptor of this CreateSinkTaskReq.

        :param obs_destination_descriptor: The obs_destination_descriptor of this CreateSinkTaskReq.
        :type obs_destination_descriptor: :class:`huaweicloudsdkkafka.v2.ObsDestinationDescriptor`
        """
        self._obs_destination_descriptor = obs_destination_descriptor

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
        if not isinstance(other, CreateSinkTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
