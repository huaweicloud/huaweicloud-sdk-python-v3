# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSourceInstanceDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'restore_time': 'str',
        'backup_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'restore_time': 'restore_time',
        'backup_id': 'backup_id'
    }

    def __init__(self, x_language=None, instance_id=None, restore_time=None, backup_id=None):
        r"""ShowSourceInstanceDetailRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。默认值：en-us。
        :type x_language: str
        :param instance_id: 原实例ID。  (instance_id 、restore_time为一组)
        :type instance_id: str
        :param restore_time: UNIX时间戳格式，单位是毫秒，时区是UTC，某时间点实例的信息。  (instance_id 、restore_time为一组)
        :type restore_time: str
        :param backup_id: 备份ID。  (backup_id为一组)  备份ID不为空时，可以不需要实例ID和时间戳。
        :type backup_id: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._restore_time = None
        self._backup_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if instance_id is not None:
            self.instance_id = instance_id
        if restore_time is not None:
            self.restore_time = restore_time
        if backup_id is not None:
            self.backup_id = backup_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowSourceInstanceDetailRequest.

        语言。默认值：en-us。

        :return: The x_language of this ShowSourceInstanceDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowSourceInstanceDetailRequest.

        语言。默认值：en-us。

        :param x_language: The x_language of this ShowSourceInstanceDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSourceInstanceDetailRequest.

        原实例ID。  (instance_id 、restore_time为一组)

        :return: The instance_id of this ShowSourceInstanceDetailRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSourceInstanceDetailRequest.

        原实例ID。  (instance_id 、restore_time为一组)

        :param instance_id: The instance_id of this ShowSourceInstanceDetailRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def restore_time(self):
        r"""Gets the restore_time of this ShowSourceInstanceDetailRequest.

        UNIX时间戳格式，单位是毫秒，时区是UTC，某时间点实例的信息。  (instance_id 、restore_time为一组)

        :return: The restore_time of this ShowSourceInstanceDetailRequest.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this ShowSourceInstanceDetailRequest.

        UNIX时间戳格式，单位是毫秒，时区是UTC，某时间点实例的信息。  (instance_id 、restore_time为一组)

        :param restore_time: The restore_time of this ShowSourceInstanceDetailRequest.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ShowSourceInstanceDetailRequest.

        备份ID。  (backup_id为一组)  备份ID不为空时，可以不需要实例ID和时间戳。

        :return: The backup_id of this ShowSourceInstanceDetailRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ShowSourceInstanceDetailRequest.

        备份ID。  (backup_id为一组)  备份ID不为空时，可以不需要实例ID和时间戳。

        :param backup_id: The backup_id of this ShowSourceInstanceDetailRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

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
        if not isinstance(other, ShowSourceInstanceDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
