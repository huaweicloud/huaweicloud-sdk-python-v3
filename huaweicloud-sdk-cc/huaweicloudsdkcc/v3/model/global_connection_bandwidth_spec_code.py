# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthSpecCode:

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
        'local_area': 'str',
        'remote_area': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'name_zh': 'str',
        'name_en': 'str',
        'level': 'str',
        'sku': 'str',
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'level': 'level',
        'sku': 'sku',
        'size': 'size'
    }

    def __init__(self, id=None, local_area=None, remote_area=None, created_at=None, updated_at=None, name_zh=None, name_en=None, level=None, sku=None, size=None):
        r"""GlobalConnectionBandwidthSpecCode

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param local_area: 功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 
        :type local_area: str
        :param remote_area: 功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 
        :type remote_area: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param name_zh: 功能说明：线路规格中文名。
        :type name_zh: str
        :param name_en: 功能说明：线路规格英文名。
        :type name_en: str
        :param level: 支持的线路等级： - Pt: 铂金 - Au: 金 - Ag: 银
        :type level: str
        :param sku: 功能描述：GCB特定线路规格产品编码。
        :type sku: str
        :param size: 功能描述：带宽起售值，单位Mbps。
        :type size: int
        """
        
        

        self._id = None
        self._local_area = None
        self._remote_area = None
        self._created_at = None
        self._updated_at = None
        self._name_zh = None
        self._name_en = None
        self._level = None
        self._sku = None
        self._size = None
        self.discriminator = None

        self.id = id
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        self.created_at = created_at
        self.updated_at = updated_at
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if level is not None:
            self.level = level
        if sku is not None:
            self.sku = sku
        if size is not None:
            self.size = size

    @property
    def id(self):
        r"""Gets the id of this GlobalConnectionBandwidthSpecCode.

        实例ID。

        :return: The id of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GlobalConnectionBandwidthSpecCode.

        实例ID。

        :param id: The id of this GlobalConnectionBandwidthSpecCode.
        :type id: str
        """
        self._id = id

    @property
    def local_area(self):
        r"""Gets the local_area of this GlobalConnectionBandwidthSpecCode.

        功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :return: The local_area of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        r"""Sets the local_area of this GlobalConnectionBandwidthSpecCode.

        功能说明：本端接入点，配合remote_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :param local_area: The local_area of this GlobalConnectionBandwidthSpecCode.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        r"""Gets the remote_area of this GlobalConnectionBandwidthSpecCode.

        功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :return: The remote_area of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        r"""Sets the remote_area of this GlobalConnectionBandwidthSpecCode.

        功能说明：远端接入点，配合local_area信息描述带宽实例应用的范围。 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），站点编码通过接口获取，带宽类型为Region可不传，其他类型必传 

        :param remote_area: The remote_area of this GlobalConnectionBandwidthSpecCode.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def created_at(self):
        r"""Gets the created_at of this GlobalConnectionBandwidthSpecCode.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this GlobalConnectionBandwidthSpecCode.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GlobalConnectionBandwidthSpecCode.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this GlobalConnectionBandwidthSpecCode.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GlobalConnectionBandwidthSpecCode.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this GlobalConnectionBandwidthSpecCode.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GlobalConnectionBandwidthSpecCode.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this GlobalConnectionBandwidthSpecCode.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def name_zh(self):
        r"""Gets the name_zh of this GlobalConnectionBandwidthSpecCode.

        功能说明：线路规格中文名。

        :return: The name_zh of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this GlobalConnectionBandwidthSpecCode.

        功能说明：线路规格中文名。

        :param name_zh: The name_zh of this GlobalConnectionBandwidthSpecCode.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this GlobalConnectionBandwidthSpecCode.

        功能说明：线路规格英文名。

        :return: The name_en of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this GlobalConnectionBandwidthSpecCode.

        功能说明：线路规格英文名。

        :param name_en: The name_en of this GlobalConnectionBandwidthSpecCode.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def level(self):
        r"""Gets the level of this GlobalConnectionBandwidthSpecCode.

        支持的线路等级： - Pt: 铂金 - Au: 金 - Ag: 银

        :return: The level of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this GlobalConnectionBandwidthSpecCode.

        支持的线路等级： - Pt: 铂金 - Au: 金 - Ag: 银

        :param level: The level of this GlobalConnectionBandwidthSpecCode.
        :type level: str
        """
        self._level = level

    @property
    def sku(self):
        r"""Gets the sku of this GlobalConnectionBandwidthSpecCode.

        功能描述：GCB特定线路规格产品编码。

        :return: The sku of this GlobalConnectionBandwidthSpecCode.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        r"""Sets the sku of this GlobalConnectionBandwidthSpecCode.

        功能描述：GCB特定线路规格产品编码。

        :param sku: The sku of this GlobalConnectionBandwidthSpecCode.
        :type sku: str
        """
        self._sku = sku

    @property
    def size(self):
        r"""Gets the size of this GlobalConnectionBandwidthSpecCode.

        功能描述：带宽起售值，单位Mbps。

        :return: The size of this GlobalConnectionBandwidthSpecCode.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this GlobalConnectionBandwidthSpecCode.

        功能描述：带宽起售值，单位Mbps。

        :param size: The size of this GlobalConnectionBandwidthSpecCode.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, GlobalConnectionBandwidthSpecCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
