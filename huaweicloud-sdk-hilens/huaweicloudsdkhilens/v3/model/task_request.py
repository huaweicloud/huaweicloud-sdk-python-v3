# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business': 'str',
        'data': 'TaskData',
        'description': 'str',
        'instance_id': 'str',
        'name': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'business': 'business',
        'data': 'data',
        'description': 'description',
        'instance_id': 'instance_id',
        'name': 'name',
        'timestamp': 'timestamp'
    }

    def __init__(self, business=None, data=None, description=None, instance_id=None, name=None, timestamp=None):
        """TaskRequest

        The model defined in huaweicloud sdk

        :param business: 作业动作，创建作业或者是删除作业又或是更新作业等
        :type business: str
        :param data: 
        :type data: :class:`huaweicloudsdkhilens.v3.TaskData`
        :param description: 作业描述
        :type description: str
        :param instance_id: 实例ID，非必选
        :type instance_id: str
        :param name: 作业名称
        :type name: str
        :param timestamp: 时间戳，非必选
        :type timestamp: str
        """
        
        

        self._business = None
        self._data = None
        self._description = None
        self._instance_id = None
        self._name = None
        self._timestamp = None
        self.discriminator = None

        if business is not None:
            self.business = business
        self.data = data
        if description is not None:
            self.description = description
        if instance_id is not None:
            self.instance_id = instance_id
        self.name = name
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def business(self):
        """Gets the business of this TaskRequest.

        作业动作，创建作业或者是删除作业又或是更新作业等

        :return: The business of this TaskRequest.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this TaskRequest.

        作业动作，创建作业或者是删除作业又或是更新作业等

        :param business: The business of this TaskRequest.
        :type business: str
        """
        self._business = business

    @property
    def data(self):
        """Gets the data of this TaskRequest.

        :return: The data of this TaskRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.TaskData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskRequest.

        :param data: The data of this TaskRequest.
        :type data: :class:`huaweicloudsdkhilens.v3.TaskData`
        """
        self._data = data

    @property
    def description(self):
        """Gets the description of this TaskRequest.

        作业描述

        :return: The description of this TaskRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskRequest.

        作业描述

        :param description: The description of this TaskRequest.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this TaskRequest.

        实例ID，非必选

        :return: The instance_id of this TaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this TaskRequest.

        实例ID，非必选

        :param instance_id: The instance_id of this TaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this TaskRequest.

        作业名称

        :return: The name of this TaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskRequest.

        作业名称

        :param name: The name of this TaskRequest.
        :type name: str
        """
        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this TaskRequest.

        时间戳，非必选

        :return: The timestamp of this TaskRequest.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TaskRequest.

        时间戳，非必选

        :param timestamp: The timestamp of this TaskRequest.
        :type timestamp: str
        """
        self._timestamp = timestamp

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
        if not isinstance(other, TaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
