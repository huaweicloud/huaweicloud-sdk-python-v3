# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'type': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'type': 'type',
        'task_id': 'task_id'
    }

    def __init__(self, description=None, type=None, task_id=None):
        r"""CustomMetadata

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param type: 类型
        :type type: str
        :param task_id: 任务id
        :type task_id: str
        """
        
        

        self._description = None
        self._type = None
        self._task_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if task_id is not None:
            self.task_id = task_id

    @property
    def description(self):
        r"""Gets the description of this CustomMetadata.

        描述

        :return: The description of this CustomMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CustomMetadata.

        描述

        :param description: The description of this CustomMetadata.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CustomMetadata.

        类型

        :return: The type of this CustomMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CustomMetadata.

        类型

        :param type: The type of this CustomMetadata.
        :type type: str
        """
        self._type = type

    @property
    def task_id(self):
        r"""Gets the task_id of this CustomMetadata.

        任务id

        :return: The task_id of this CustomMetadata.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CustomMetadata.

        任务id

        :param task_id: The task_id of this CustomMetadata.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, CustomMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
