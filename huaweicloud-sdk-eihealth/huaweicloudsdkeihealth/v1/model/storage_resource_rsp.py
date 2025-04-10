# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageResourceRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec': 'SpecDto',
        'size': 'int',
        'charge_mode': 'str',
        'create_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'spec': 'spec',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'create_time': 'create_time',
        'status': 'status'
    }

    def __init__(self, spec=None, size=None, charge_mode=None, create_time=None, status=None):
        r"""StorageResourceRsp

        The model defined in huaweicloud sdk

        :param spec: 
        :type spec: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        :param size: 使用量
        :type size: int
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param create_time: 购买时间
        :type create_time: str
        :param status: 状态
        :type status: str
        """
        
        

        self._spec = None
        self._size = None
        self._charge_mode = None
        self._create_time = None
        self._status = None
        self.discriminator = None

        self.spec = spec
        self.size = size
        self.charge_mode = charge_mode
        self.create_time = create_time
        self.status = status

    @property
    def spec(self):
        r"""Gets the spec of this StorageResourceRsp.

        :return: The spec of this StorageResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this StorageResourceRsp.

        :param spec: The spec of this StorageResourceRsp.
        :type spec: :class:`huaweicloudsdkeihealth.v1.SpecDto`
        """
        self._spec = spec

    @property
    def size(self):
        r"""Gets the size of this StorageResourceRsp.

        使用量

        :return: The size of this StorageResourceRsp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this StorageResourceRsp.

        使用量

        :param size: The size of this StorageResourceRsp.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this StorageResourceRsp.

        计费模式

        :return: The charge_mode of this StorageResourceRsp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this StorageResourceRsp.

        计费模式

        :param charge_mode: The charge_mode of this StorageResourceRsp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def create_time(self):
        r"""Gets the create_time of this StorageResourceRsp.

        购买时间

        :return: The create_time of this StorageResourceRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StorageResourceRsp.

        购买时间

        :param create_time: The create_time of this StorageResourceRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def status(self):
        r"""Gets the status of this StorageResourceRsp.

        状态

        :return: The status of this StorageResourceRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StorageResourceRsp.

        状态

        :param status: The status of this StorageResourceRsp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, StorageResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
