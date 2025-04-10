# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesResult:

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
        'volume_type': 'str',
        'data_volume_size': 'float',
        'version': 'str',
        'mode': 'str',
        'instance_mode': 'str'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'volume_type': 'volume_type',
        'data_volume_size': 'data_volume_size',
        'version': 'version',
        'mode': 'mode',
        'instance_mode': 'instance_mode'
    }

    def __init__(self, instance_name=None, instance_id=None, volume_type=None, data_volume_size=None, version=None, mode=None, instance_mode=None):
        r"""InstancesResult

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param volume_type: 存储类型。
        :type volume_type: str
        :param data_volume_size: 磁盘大小，单位：GB。
        :type data_volume_size: float
        :param version: 实例版本信息。
        :type version: str
        :param mode: 部署形态。
        :type mode: str
        :param instance_mode: 实例模型，企业版，标准版，基础版。
        :type instance_mode: str
        """
        
        

        self._instance_name = None
        self._instance_id = None
        self._volume_type = None
        self._data_volume_size = None
        self._version = None
        self._mode = None
        self._instance_mode = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if volume_type is not None:
            self.volume_type = volume_type
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if version is not None:
            self.version = version
        if mode is not None:
            self.mode = mode
        if instance_mode is not None:
            self.instance_mode = instance_mode

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InstancesResult.

        实例名称。

        :return: The instance_name of this InstancesResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InstancesResult.

        实例名称。

        :param instance_name: The instance_name of this InstancesResult.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstancesResult.

        实例id。

        :return: The instance_id of this InstancesResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstancesResult.

        实例id。

        :param instance_id: The instance_id of this InstancesResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def volume_type(self):
        r"""Gets the volume_type of this InstancesResult.

        存储类型。

        :return: The volume_type of this InstancesResult.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this InstancesResult.

        存储类型。

        :param volume_type: The volume_type of this InstancesResult.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def data_volume_size(self):
        r"""Gets the data_volume_size of this InstancesResult.

        磁盘大小，单位：GB。

        :return: The data_volume_size of this InstancesResult.
        :rtype: float
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        r"""Sets the data_volume_size of this InstancesResult.

        磁盘大小，单位：GB。

        :param data_volume_size: The data_volume_size of this InstancesResult.
        :type data_volume_size: float
        """
        self._data_volume_size = data_volume_size

    @property
    def version(self):
        r"""Gets the version of this InstancesResult.

        实例版本信息。

        :return: The version of this InstancesResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstancesResult.

        实例版本信息。

        :param version: The version of this InstancesResult.
        :type version: str
        """
        self._version = version

    @property
    def mode(self):
        r"""Gets the mode of this InstancesResult.

        部署形态。

        :return: The mode of this InstancesResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this InstancesResult.

        部署形态。

        :param mode: The mode of this InstancesResult.
        :type mode: str
        """
        self._mode = mode

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this InstancesResult.

        实例模型，企业版，标准版，基础版。

        :return: The instance_mode of this InstancesResult.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this InstancesResult.

        实例模型，企业版，标准版，基础版。

        :param instance_mode: The instance_mode of this InstancesResult.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

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
        if not isinstance(other, InstancesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
