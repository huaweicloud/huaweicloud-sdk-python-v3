# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoScalingRecordInfo:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'scaling_type': 'str',
        'original_value': 'str',
        'target_value': 'str',
        'result': 'str',
        'create_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'scaling_type': 'scaling_type',
        'original_value': 'original_value',
        'target_value': 'target_value',
        'result': 'result',
        'create_at': 'create_at'
    }

    def __init__(self, id=None, instance_id=None, instance_name=None, scaling_type=None, original_value=None, target_value=None, result=None, create_at=None):
        """AutoScalingRecordInfo

        The model defined in huaweicloud sdk

        :param id: 记录ID。
        :type id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param scaling_type: 变配类型。
        :type scaling_type: str
        :param original_value: 原始值。
        :type original_value: str
        :param target_value: 目标值。
        :type target_value: str
        :param result: 变配结果。
        :type result: str
        :param create_at: 变配时间。
        :type create_at: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._instance_name = None
        self._scaling_type = None
        self._original_value = None
        self._target_value = None
        self._result = None
        self._create_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if scaling_type is not None:
            self.scaling_type = scaling_type
        if original_value is not None:
            self.original_value = original_value
        if target_value is not None:
            self.target_value = target_value
        if result is not None:
            self.result = result
        if create_at is not None:
            self.create_at = create_at

    @property
    def id(self):
        """Gets the id of this AutoScalingRecordInfo.

        记录ID。

        :return: The id of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AutoScalingRecordInfo.

        记录ID。

        :param id: The id of this AutoScalingRecordInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this AutoScalingRecordInfo.

        实例ID。

        :return: The instance_id of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AutoScalingRecordInfo.

        实例ID。

        :param instance_id: The instance_id of this AutoScalingRecordInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this AutoScalingRecordInfo.

        实例名称。

        :return: The instance_name of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this AutoScalingRecordInfo.

        实例名称。

        :param instance_name: The instance_name of this AutoScalingRecordInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def scaling_type(self):
        """Gets the scaling_type of this AutoScalingRecordInfo.

        变配类型。

        :return: The scaling_type of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._scaling_type

    @scaling_type.setter
    def scaling_type(self, scaling_type):
        """Sets the scaling_type of this AutoScalingRecordInfo.

        变配类型。

        :param scaling_type: The scaling_type of this AutoScalingRecordInfo.
        :type scaling_type: str
        """
        self._scaling_type = scaling_type

    @property
    def original_value(self):
        """Gets the original_value of this AutoScalingRecordInfo.

        原始值。

        :return: The original_value of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """Sets the original_value of this AutoScalingRecordInfo.

        原始值。

        :param original_value: The original_value of this AutoScalingRecordInfo.
        :type original_value: str
        """
        self._original_value = original_value

    @property
    def target_value(self):
        """Gets the target_value of this AutoScalingRecordInfo.

        目标值。

        :return: The target_value of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this AutoScalingRecordInfo.

        目标值。

        :param target_value: The target_value of this AutoScalingRecordInfo.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def result(self):
        """Gets the result of this AutoScalingRecordInfo.

        变配结果。

        :return: The result of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AutoScalingRecordInfo.

        变配结果。

        :param result: The result of this AutoScalingRecordInfo.
        :type result: str
        """
        self._result = result

    @property
    def create_at(self):
        """Gets the create_at of this AutoScalingRecordInfo.

        变配时间。

        :return: The create_at of this AutoScalingRecordInfo.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this AutoScalingRecordInfo.

        变配时间。

        :param create_at: The create_at of this AutoScalingRecordInfo.
        :type create_at: str
        """
        self._create_at = create_at

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
        if not isinstance(other, AutoScalingRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
