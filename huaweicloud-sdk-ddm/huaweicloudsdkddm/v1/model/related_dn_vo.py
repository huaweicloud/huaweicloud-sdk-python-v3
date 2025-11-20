# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedDnVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'data_volume_size': 'float',
        'version': 'str',
        'engine_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'data_volume_size': 'data_volume_size',
        'version': 'version',
        'engine_name': 'engine_name'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_status=None, data_volume_size=None, version=None, engine_name=None):
        r"""RelatedDnVO

        The model defined in huaweicloud sdk

        :param instance_id: DN实例id。
        :type instance_id: str
        :param instance_name: DN实例名称。
        :type instance_name: str
        :param instance_status: DN实例状态。
        :type instance_status: str
        :param data_volume_size: 磁盘大小。
        :type data_volume_size: float
        :param version: 版本。
        :type version: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._data_volume_size = None
        self._version = None
        self._engine_name = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if version is not None:
            self.version = version
        if engine_name is not None:
            self.engine_name = engine_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RelatedDnVO.

        DN实例id。

        :return: The instance_id of this RelatedDnVO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RelatedDnVO.

        DN实例id。

        :param instance_id: The instance_id of this RelatedDnVO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RelatedDnVO.

        DN实例名称。

        :return: The instance_name of this RelatedDnVO.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RelatedDnVO.

        DN实例名称。

        :param instance_name: The instance_name of this RelatedDnVO.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this RelatedDnVO.

        DN实例状态。

        :return: The instance_status of this RelatedDnVO.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this RelatedDnVO.

        DN实例状态。

        :param instance_status: The instance_status of this RelatedDnVO.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def data_volume_size(self):
        r"""Gets the data_volume_size of this RelatedDnVO.

        磁盘大小。

        :return: The data_volume_size of this RelatedDnVO.
        :rtype: float
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        r"""Sets the data_volume_size of this RelatedDnVO.

        磁盘大小。

        :param data_volume_size: The data_volume_size of this RelatedDnVO.
        :type data_volume_size: float
        """
        self._data_volume_size = data_volume_size

    @property
    def version(self):
        r"""Gets the version of this RelatedDnVO.

        版本。

        :return: The version of this RelatedDnVO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RelatedDnVO.

        版本。

        :param version: The version of this RelatedDnVO.
        :type version: str
        """
        self._version = version

    @property
    def engine_name(self):
        r"""Gets the engine_name of this RelatedDnVO.

        引擎名称。

        :return: The engine_name of this RelatedDnVO.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this RelatedDnVO.

        引擎名称。

        :param engine_name: The engine_name of this RelatedDnVO.
        :type engine_name: str
        """
        self._engine_name = engine_name

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
        if not isinstance(other, RelatedDnVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
