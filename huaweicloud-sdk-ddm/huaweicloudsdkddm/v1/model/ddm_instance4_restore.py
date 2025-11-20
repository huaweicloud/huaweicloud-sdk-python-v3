# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DDMInstance4Restore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'instance_id': 'str',
        'status': 'str',
        'available': 'bool',
        'unavailable_reason': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'status': 'status',
        'available': 'available',
        'unavailable_reason': 'unavailable_reason',
        'vpc_name': 'vpc_name'
    }

    def __init__(self, instance_name=None, instance_id=None, status=None, available=None, unavailable_reason=None, vpc_name=None):
        r"""DDMInstance4Restore

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param status: 状态。
        :type status: str
        :param available: 是否可用。
        :type available: bool
        :param unavailable_reason: 无法使用原因。
        :type unavailable_reason: str
        :param vpc_name: 虚拟私有云名称。
        :type vpc_name: str
        """
        
        

        self._instance_name = None
        self._instance_id = None
        self._status = None
        self._available = None
        self._unavailable_reason = None
        self._vpc_name = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if available is not None:
            self.available = available
        if unavailable_reason is not None:
            self.unavailable_reason = unavailable_reason
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DDMInstance4Restore.

        实例名称。

        :return: The instance_name of this DDMInstance4Restore.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DDMInstance4Restore.

        实例名称。

        :param instance_name: The instance_name of this DDMInstance4Restore.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DDMInstance4Restore.

        实例ID。

        :return: The instance_id of this DDMInstance4Restore.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DDMInstance4Restore.

        实例ID。

        :param instance_id: The instance_id of this DDMInstance4Restore.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this DDMInstance4Restore.

        状态。

        :return: The status of this DDMInstance4Restore.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DDMInstance4Restore.

        状态。

        :param status: The status of this DDMInstance4Restore.
        :type status: str
        """
        self._status = status

    @property
    def available(self):
        r"""Gets the available of this DDMInstance4Restore.

        是否可用。

        :return: The available of this DDMInstance4Restore.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this DDMInstance4Restore.

        是否可用。

        :param available: The available of this DDMInstance4Restore.
        :type available: bool
        """
        self._available = available

    @property
    def unavailable_reason(self):
        r"""Gets the unavailable_reason of this DDMInstance4Restore.

        无法使用原因。

        :return: The unavailable_reason of this DDMInstance4Restore.
        :rtype: str
        """
        return self._unavailable_reason

    @unavailable_reason.setter
    def unavailable_reason(self, unavailable_reason):
        r"""Sets the unavailable_reason of this DDMInstance4Restore.

        无法使用原因。

        :param unavailable_reason: The unavailable_reason of this DDMInstance4Restore.
        :type unavailable_reason: str
        """
        self._unavailable_reason = unavailable_reason

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this DDMInstance4Restore.

        虚拟私有云名称。

        :return: The vpc_name of this DDMInstance4Restore.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this DDMInstance4Restore.

        虚拟私有云名称。

        :param vpc_name: The vpc_name of this DDMInstance4Restore.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

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
        if not isinstance(other, DDMInstance4Restore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
