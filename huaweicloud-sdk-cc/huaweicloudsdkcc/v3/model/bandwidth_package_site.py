# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPackageSite:

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
        'site_code': 'str',
        'region_id': 'str',
        'site_type': 'str',
        'name_cn': 'str',
        'name_en': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'site_code': 'site_code',
        'region_id': 'region_id',
        'site_type': 'site_type',
        'name_cn': 'name_cn',
        'name_en': 'name_en',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, site_code=None, region_id=None, site_type=None, name_cn=None, name_en=None, description=None, created_at=None, updated_at=None):
        r"""BandwidthPackageSite

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param site_code: 站点编码。
        :type site_code: str
        :param region_id: RegionID。
        :type region_id: str
        :param site_type: 站点类型。默认Region级别。
        :type site_type: str
        :param name_cn: 实例名称。
        :type name_cn: str
        :param name_en: 实例名称。
        :type name_en: str
        :param description: 描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._site_code = None
        self._region_id = None
        self._site_type = None
        self._name_cn = None
        self._name_en = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if site_code is not None:
            self.site_code = site_code
        if region_id is not None:
            self.region_id = region_id
        if site_type is not None:
            self.site_type = site_type
        if name_cn is not None:
            self.name_cn = name_cn
        if name_en is not None:
            self.name_en = name_en
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this BandwidthPackageSite.

        实例ID。

        :return: The id of this BandwidthPackageSite.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandwidthPackageSite.

        实例ID。

        :param id: The id of this BandwidthPackageSite.
        :type id: str
        """
        self._id = id

    @property
    def site_code(self):
        r"""Gets the site_code of this BandwidthPackageSite.

        站点编码。

        :return: The site_code of this BandwidthPackageSite.
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        r"""Sets the site_code of this BandwidthPackageSite.

        站点编码。

        :param site_code: The site_code of this BandwidthPackageSite.
        :type site_code: str
        """
        self._site_code = site_code

    @property
    def region_id(self):
        r"""Gets the region_id of this BandwidthPackageSite.

        RegionID。

        :return: The region_id of this BandwidthPackageSite.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this BandwidthPackageSite.

        RegionID。

        :param region_id: The region_id of this BandwidthPackageSite.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def site_type(self):
        r"""Gets the site_type of this BandwidthPackageSite.

        站点类型。默认Region级别。

        :return: The site_type of this BandwidthPackageSite.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this BandwidthPackageSite.

        站点类型。默认Region级别。

        :param site_type: The site_type of this BandwidthPackageSite.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def name_cn(self):
        r"""Gets the name_cn of this BandwidthPackageSite.

        实例名称。

        :return: The name_cn of this BandwidthPackageSite.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this BandwidthPackageSite.

        实例名称。

        :param name_cn: The name_cn of this BandwidthPackageSite.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def name_en(self):
        r"""Gets the name_en of this BandwidthPackageSite.

        实例名称。

        :return: The name_en of this BandwidthPackageSite.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this BandwidthPackageSite.

        实例名称。

        :param name_en: The name_en of this BandwidthPackageSite.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def description(self):
        r"""Gets the description of this BandwidthPackageSite.

        描述。不支持 <>。

        :return: The description of this BandwidthPackageSite.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BandwidthPackageSite.

        描述。不支持 <>。

        :param description: The description of this BandwidthPackageSite.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this BandwidthPackageSite.

        创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this BandwidthPackageSite.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BandwidthPackageSite.

        创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this BandwidthPackageSite.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this BandwidthPackageSite.

        更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this BandwidthPackageSite.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this BandwidthPackageSite.

        更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this BandwidthPackageSite.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, BandwidthPackageSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
