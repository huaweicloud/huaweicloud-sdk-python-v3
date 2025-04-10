# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavor:

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
        'code': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'az_status': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'az_status': 'az_status'
    }

    def __init__(self, id=None, code=None, vcpus=None, ram=None, az_status=None):
        r"""ComputeFlavor

        The model defined in huaweicloud sdk

        :param id: 规格ID，该字段唯一。
        :type id: str
        :param code: 资源规格编码。例如：rds.pg.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “pg”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。
        :type code: str
        :param vcpus: CPU大小。例如：1表示1U。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param az_status: 规格所在az的状态，包含以下状态：  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。
        :type az_status: dict(str, str)
        """
        
        

        self._id = None
        self._code = None
        self._vcpus = None
        self._ram = None
        self._az_status = None
        self.discriminator = None

        self.id = id
        self.code = code
        self.vcpus = vcpus
        self.ram = ram
        self.az_status = az_status

    @property
    def id(self):
        r"""Gets the id of this ComputeFlavor.

        规格ID，该字段唯一。

        :return: The id of this ComputeFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComputeFlavor.

        规格ID，该字段唯一。

        :param id: The id of this ComputeFlavor.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this ComputeFlavor.

        资源规格编码。例如：rds.pg.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “pg”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。

        :return: The code of this ComputeFlavor.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ComputeFlavor.

        资源规格编码。例如：rds.pg.m1.xlarge.rr。  更多规格说明请参考数据库实例规格。  “rds”代表RDS产品。 “pg”代表数据库引擎。 “m1.xlarge”代表性能规格，为高内存类型。 “rr”表示只读实例（“.ha”表示主备实例）。

        :param code: The code of this ComputeFlavor.
        :type code: str
        """
        self._code = code

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ComputeFlavor.

        CPU大小。例如：1表示1U。

        :return: The vcpus of this ComputeFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ComputeFlavor.

        CPU大小。例如：1表示1U。

        :param vcpus: The vcpus of this ComputeFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this ComputeFlavor.

        内存大小，单位为GB。

        :return: The ram of this ComputeFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ComputeFlavor.

        内存大小，单位为GB。

        :param ram: The ram of this ComputeFlavor.
        :type ram: str
        """
        self._ram = ram

    @property
    def az_status(self):
        r"""Gets the az_status of this ComputeFlavor.

        规格所在az的状态，包含以下状态：  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。

        :return: The az_status of this ComputeFlavor.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        r"""Sets the az_status of this ComputeFlavor.

        规格所在az的状态，包含以下状态：  normal：在售。 unsupported：暂不支持该规格。 sellout：售罄。

        :param az_status: The az_status of this ComputeFlavor.
        :type az_status: dict(str, str)
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
        if not isinstance(other, ComputeFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
