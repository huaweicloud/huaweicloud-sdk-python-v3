# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllocateSpResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assignment_record_id': 'str',
        'resource_spec_code': 'str',
        'charging_mode': 'str',
        'resource_num': 'float',
        'resource_used_num': 'float',
        'resource_allocate_time': 'int',
        'resource_expire_time': 'int'
    }

    attribute_map = {
        'assignment_record_id': 'assignment_record_id',
        'resource_spec_code': 'resource_spec_code',
        'charging_mode': 'charging_mode',
        'resource_num': 'resource_num',
        'resource_used_num': 'resource_used_num',
        'resource_allocate_time': 'resource_allocate_time',
        'resource_expire_time': 'resource_expire_time'
    }

    def __init__(self, assignment_record_id=None, resource_spec_code=None, charging_mode=None, resource_num=None, resource_used_num=None, resource_allocate_time=None, resource_expire_time=None):
        r"""AllocateSpResourceInfo

        The model defined in huaweicloud sdk

        :param assignment_record_id: 资源分配id。
        :type assignment_record_id: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param charging_mode: 资源计费类型。
        :type charging_mode: str
        :param resource_num: 资源数量。
        :type resource_num: float
        :param resource_used_num: 资源已使用数量。
        :type resource_used_num: float
        :param resource_allocate_time: 资源分配时间（UTC时间）,unix时间,精确到秒。
        :type resource_allocate_time: int
        :param resource_expire_time: 资源到期时间(UTC时间),unix时间,精确到秒。
        :type resource_expire_time: int
        """
        
        

        self._assignment_record_id = None
        self._resource_spec_code = None
        self._charging_mode = None
        self._resource_num = None
        self._resource_used_num = None
        self._resource_allocate_time = None
        self._resource_expire_time = None
        self.discriminator = None

        if assignment_record_id is not None:
            self.assignment_record_id = assignment_record_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_num is not None:
            self.resource_num = resource_num
        if resource_used_num is not None:
            self.resource_used_num = resource_used_num
        if resource_allocate_time is not None:
            self.resource_allocate_time = resource_allocate_time
        if resource_expire_time is not None:
            self.resource_expire_time = resource_expire_time

    @property
    def assignment_record_id(self):
        r"""Gets the assignment_record_id of this AllocateSpResourceInfo.

        资源分配id。

        :return: The assignment_record_id of this AllocateSpResourceInfo.
        :rtype: str
        """
        return self._assignment_record_id

    @assignment_record_id.setter
    def assignment_record_id(self, assignment_record_id):
        r"""Sets the assignment_record_id of this AllocateSpResourceInfo.

        资源分配id。

        :param assignment_record_id: The assignment_record_id of this AllocateSpResourceInfo.
        :type assignment_record_id: str
        """
        self._assignment_record_id = assignment_record_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this AllocateSpResourceInfo.

        资源规格编码

        :return: The resource_spec_code of this AllocateSpResourceInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this AllocateSpResourceInfo.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this AllocateSpResourceInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this AllocateSpResourceInfo.

        资源计费类型。

        :return: The charging_mode of this AllocateSpResourceInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this AllocateSpResourceInfo.

        资源计费类型。

        :param charging_mode: The charging_mode of this AllocateSpResourceInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_num(self):
        r"""Gets the resource_num of this AllocateSpResourceInfo.

        资源数量。

        :return: The resource_num of this AllocateSpResourceInfo.
        :rtype: float
        """
        return self._resource_num

    @resource_num.setter
    def resource_num(self, resource_num):
        r"""Sets the resource_num of this AllocateSpResourceInfo.

        资源数量。

        :param resource_num: The resource_num of this AllocateSpResourceInfo.
        :type resource_num: float
        """
        self._resource_num = resource_num

    @property
    def resource_used_num(self):
        r"""Gets the resource_used_num of this AllocateSpResourceInfo.

        资源已使用数量。

        :return: The resource_used_num of this AllocateSpResourceInfo.
        :rtype: float
        """
        return self._resource_used_num

    @resource_used_num.setter
    def resource_used_num(self, resource_used_num):
        r"""Sets the resource_used_num of this AllocateSpResourceInfo.

        资源已使用数量。

        :param resource_used_num: The resource_used_num of this AllocateSpResourceInfo.
        :type resource_used_num: float
        """
        self._resource_used_num = resource_used_num

    @property
    def resource_allocate_time(self):
        r"""Gets the resource_allocate_time of this AllocateSpResourceInfo.

        资源分配时间（UTC时间）,unix时间,精确到秒。

        :return: The resource_allocate_time of this AllocateSpResourceInfo.
        :rtype: int
        """
        return self._resource_allocate_time

    @resource_allocate_time.setter
    def resource_allocate_time(self, resource_allocate_time):
        r"""Sets the resource_allocate_time of this AllocateSpResourceInfo.

        资源分配时间（UTC时间）,unix时间,精确到秒。

        :param resource_allocate_time: The resource_allocate_time of this AllocateSpResourceInfo.
        :type resource_allocate_time: int
        """
        self._resource_allocate_time = resource_allocate_time

    @property
    def resource_expire_time(self):
        r"""Gets the resource_expire_time of this AllocateSpResourceInfo.

        资源到期时间(UTC时间),unix时间,精确到秒。

        :return: The resource_expire_time of this AllocateSpResourceInfo.
        :rtype: int
        """
        return self._resource_expire_time

    @resource_expire_time.setter
    def resource_expire_time(self, resource_expire_time):
        r"""Sets the resource_expire_time of this AllocateSpResourceInfo.

        资源到期时间(UTC时间),unix时间,精确到秒。

        :param resource_expire_time: The resource_expire_time of this AllocateSpResourceInfo.
        :type resource_expire_time: int
        """
        self._resource_expire_time = resource_expire_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AllocateSpResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
