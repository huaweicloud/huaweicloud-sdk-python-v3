# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyComputeFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'str',
        'ram': 'str',
        'db_type': 'str',
        'id': 'str',
        'spec_code': 'str',
        'az_status': 'object'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram',
        'db_type': 'db_type',
        'id': 'id',
        'spec_code': 'spec_code',
        'az_status': 'az_status'
    }

    def __init__(self, vcpus=None, ram=None, db_type=None, id=None, spec_code=None, az_status=None):
        r"""MysqlProxyComputeFlavor

        The model defined in huaweicloud sdk

        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param db_type: 数据库类型。
        :type db_type: str
        :param id: Proxy规格ID。
        :type id: str
        :param spec_code: Proxy规格码。
        :type spec_code: str
        :param az_status: 其中key是可用区编号，value是规格所在az的状态。
        :type az_status: object
        """
        
        

        self._vcpus = None
        self._ram = None
        self._db_type = None
        self._id = None
        self._spec_code = None
        self._az_status = None
        self.discriminator = None

        self.vcpus = vcpus
        self.ram = ram
        self.db_type = db_type
        self.id = id
        self.spec_code = spec_code
        self.az_status = az_status

    @property
    def vcpus(self):
        r"""Gets the vcpus of this MysqlProxyComputeFlavor.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this MysqlProxyComputeFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this MysqlProxyComputeFlavor.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this MysqlProxyComputeFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this MysqlProxyComputeFlavor.

        内存大小，单位为GB。

        :return: The ram of this MysqlProxyComputeFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this MysqlProxyComputeFlavor.

        内存大小，单位为GB。

        :param ram: The ram of this MysqlProxyComputeFlavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def db_type(self):
        r"""Gets the db_type of this MysqlProxyComputeFlavor.

        数据库类型。

        :return: The db_type of this MysqlProxyComputeFlavor.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this MysqlProxyComputeFlavor.

        数据库类型。

        :param db_type: The db_type of this MysqlProxyComputeFlavor.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def id(self):
        r"""Gets the id of this MysqlProxyComputeFlavor.

        Proxy规格ID。

        :return: The id of this MysqlProxyComputeFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MysqlProxyComputeFlavor.

        Proxy规格ID。

        :param id: The id of this MysqlProxyComputeFlavor.
        :type id: str
        """
        self._id = id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this MysqlProxyComputeFlavor.

        Proxy规格码。

        :return: The spec_code of this MysqlProxyComputeFlavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this MysqlProxyComputeFlavor.

        Proxy规格码。

        :param spec_code: The spec_code of this MysqlProxyComputeFlavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def az_status(self):
        r"""Gets the az_status of this MysqlProxyComputeFlavor.

        其中key是可用区编号，value是规格所在az的状态。

        :return: The az_status of this MysqlProxyComputeFlavor.
        :rtype: object
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this MysqlProxyComputeFlavor.

        其中key是可用区编号，value是规格所在az的状态。

        :param az_status: The az_status of this MysqlProxyComputeFlavor.
        :type az_status: object
        """
        self._az_status = az_status

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
        if not isinstance(other, MysqlProxyComputeFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
