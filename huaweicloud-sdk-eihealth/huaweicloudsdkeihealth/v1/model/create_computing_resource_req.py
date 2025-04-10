# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComputingResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_id': 'str',
        'spec_code': 'str',
        'count': 'int',
        'data_disk_spec_code': 'str',
        'data_disk_size': 'int'
    }

    attribute_map = {
        'availability_zone_id': 'availability_zone_id',
        'spec_code': 'spec_code',
        'count': 'count',
        'data_disk_spec_code': 'data_disk_spec_code',
        'data_disk_size': 'data_disk_size'
    }

    def __init__(self, availability_zone_id=None, spec_code=None, count=None, data_disk_spec_code=None, data_disk_size=None):
        r"""CreateComputingResourceReq

        The model defined in huaweicloud sdk

        :param availability_zone_id: 可用区
        :type availability_zone_id: str
        :param spec_code: 规格编码
        :type spec_code: str
        :param count: 购买数量
        :type count: int
        :param data_disk_spec_code: 额外数据盘规格编码
        :type data_disk_spec_code: str
        :param data_disk_size: 额外数据盘大小
        :type data_disk_size: int
        """
        
        

        self._availability_zone_id = None
        self._spec_code = None
        self._count = None
        self._data_disk_spec_code = None
        self._data_disk_size = None
        self.discriminator = None

        self.availability_zone_id = availability_zone_id
        self.spec_code = spec_code
        self.count = count
        if data_disk_spec_code is not None:
            self.data_disk_spec_code = data_disk_spec_code
        if data_disk_size is not None:
            self.data_disk_size = data_disk_size

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this CreateComputingResourceReq.

        可用区

        :return: The availability_zone_id of this CreateComputingResourceReq.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this CreateComputingResourceReq.

        可用区

        :param availability_zone_id: The availability_zone_id of this CreateComputingResourceReq.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateComputingResourceReq.

        规格编码

        :return: The spec_code of this CreateComputingResourceReq.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateComputingResourceReq.

        规格编码

        :param spec_code: The spec_code of this CreateComputingResourceReq.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def count(self):
        r"""Gets the count of this CreateComputingResourceReq.

        购买数量

        :return: The count of this CreateComputingResourceReq.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateComputingResourceReq.

        购买数量

        :param count: The count of this CreateComputingResourceReq.
        :type count: int
        """
        self._count = count

    @property
    def data_disk_spec_code(self):
        r"""Gets the data_disk_spec_code of this CreateComputingResourceReq.

        额外数据盘规格编码

        :return: The data_disk_spec_code of this CreateComputingResourceReq.
        :rtype: str
        """
        return self._data_disk_spec_code

    @data_disk_spec_code.setter
    def data_disk_spec_code(self, data_disk_spec_code):
        r"""Sets the data_disk_spec_code of this CreateComputingResourceReq.

        额外数据盘规格编码

        :param data_disk_spec_code: The data_disk_spec_code of this CreateComputingResourceReq.
        :type data_disk_spec_code: str
        """
        self._data_disk_spec_code = data_disk_spec_code

    @property
    def data_disk_size(self):
        r"""Gets the data_disk_size of this CreateComputingResourceReq.

        额外数据盘大小

        :return: The data_disk_size of this CreateComputingResourceReq.
        :rtype: int
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        r"""Sets the data_disk_size of this CreateComputingResourceReq.

        额外数据盘大小

        :param data_disk_size: The data_disk_size of this CreateComputingResourceReq.
        :type data_disk_size: int
        """
        self._data_disk_size = data_disk_size

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
        if not isinstance(other, CreateComputingResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
