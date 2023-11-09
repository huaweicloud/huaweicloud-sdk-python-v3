# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicDrugModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'task_id': 'str',
        'name': 'str',
        'creator': 'str',
        'type': 'str',
        'value_range': 'ValueRange2',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'name': 'name',
        'creator': 'creator',
        'type': 'type',
        'value_range': 'value_range',
        'description': 'description'
    }

    def __init__(self, id=None, task_id=None, name=None, creator=None, type=None, value_range=None, description=None):
        """BasicDrugModel

        The model defined in huaweicloud sdk

        :param id: 模型ID
        :type id: str
        :param task_id: 任务ID
        :type task_id: str
        :param name: 模型名称
        :type name: str
        :param creator: 模型创建者
        :type creator: str
        :param type: 模型类型
        :type type: str
        :param value_range: 
        :type value_range: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        :param description: 模型描述信息
        :type description: str
        """
        
        

        self._id = None
        self._task_id = None
        self._name = None
        self._creator = None
        self._type = None
        self._value_range = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if creator is not None:
            self.creator = creator
        if type is not None:
            self.type = type
        if value_range is not None:
            self.value_range = value_range
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this BasicDrugModel.

        模型ID

        :return: The id of this BasicDrugModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicDrugModel.

        模型ID

        :param id: The id of this BasicDrugModel.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        """Gets the task_id of this BasicDrugModel.

        任务ID

        :return: The task_id of this BasicDrugModel.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this BasicDrugModel.

        任务ID

        :param task_id: The task_id of this BasicDrugModel.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def name(self):
        """Gets the name of this BasicDrugModel.

        模型名称

        :return: The name of this BasicDrugModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicDrugModel.

        模型名称

        :param name: The name of this BasicDrugModel.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        """Gets the creator of this BasicDrugModel.

        模型创建者

        :return: The creator of this BasicDrugModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this BasicDrugModel.

        模型创建者

        :param creator: The creator of this BasicDrugModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def type(self):
        """Gets the type of this BasicDrugModel.

        模型类型

        :return: The type of this BasicDrugModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BasicDrugModel.

        模型类型

        :param type: The type of this BasicDrugModel.
        :type type: str
        """
        self._type = type

    @property
    def value_range(self):
        """Gets the value_range of this BasicDrugModel.

        :return: The value_range of this BasicDrugModel.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this BasicDrugModel.

        :param value_range: The value_range of this BasicDrugModel.
        :type value_range: :class:`huaweicloudsdkeihealth.v1.ValueRange2`
        """
        self._value_range = value_range

    @property
    def description(self):
        """Gets the description of this BasicDrugModel.

        模型描述信息

        :return: The description of this BasicDrugModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BasicDrugModel.

        模型描述信息

        :param description: The description of this BasicDrugModel.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, BasicDrugModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
