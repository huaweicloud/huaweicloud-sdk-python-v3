# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessSites:

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
        'name': 'str',
        'proxy_region': 'str',
        'iec_az_code': 'str',
        'en_name': 'str',
        'cn_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'proxy_region': 'proxy_region',
        'iec_az_code': 'iec_az_code',
        'en_name': 'en_name',
        'cn_name': 'cn_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, proxy_region=None, iec_az_code=None, en_name=None, cn_name=None, created_at=None, updated_at=None):
        """ListAccessSites

        The model defined in huaweicloud sdk

        :param id: 接入点的ID
        :type id: str
        :param name: - 功能说明：接入点名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param proxy_region: pop站点托管的region(id)
        :type proxy_region: str
        :param iec_az_code: 边缘站点az
        :type iec_az_code: str
        :param en_name: 英文名称
        :type en_name: str
        :param cn_name: 中文名称
        :type cn_name: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._proxy_region = None
        self._iec_az_code = None
        self._en_name = None
        self._cn_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if proxy_region is not None:
            self.proxy_region = proxy_region
        if iec_az_code is not None:
            self.iec_az_code = iec_az_code
        if en_name is not None:
            self.en_name = en_name
        if cn_name is not None:
            self.cn_name = cn_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ListAccessSites.

        接入点的ID

        :return: The id of this ListAccessSites.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAccessSites.

        接入点的ID

        :param id: The id of this ListAccessSites.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListAccessSites.

        - 功能说明：接入点名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this ListAccessSites.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAccessSites.

        - 功能说明：接入点名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this ListAccessSites.
        :type name: str
        """
        self._name = name

    @property
    def proxy_region(self):
        """Gets the proxy_region of this ListAccessSites.

        pop站点托管的region(id)

        :return: The proxy_region of this ListAccessSites.
        :rtype: str
        """
        return self._proxy_region

    @proxy_region.setter
    def proxy_region(self, proxy_region):
        """Sets the proxy_region of this ListAccessSites.

        pop站点托管的region(id)

        :param proxy_region: The proxy_region of this ListAccessSites.
        :type proxy_region: str
        """
        self._proxy_region = proxy_region

    @property
    def iec_az_code(self):
        """Gets the iec_az_code of this ListAccessSites.

        边缘站点az

        :return: The iec_az_code of this ListAccessSites.
        :rtype: str
        """
        return self._iec_az_code

    @iec_az_code.setter
    def iec_az_code(self, iec_az_code):
        """Sets the iec_az_code of this ListAccessSites.

        边缘站点az

        :param iec_az_code: The iec_az_code of this ListAccessSites.
        :type iec_az_code: str
        """
        self._iec_az_code = iec_az_code

    @property
    def en_name(self):
        """Gets the en_name of this ListAccessSites.

        英文名称

        :return: The en_name of this ListAccessSites.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        """Sets the en_name of this ListAccessSites.

        英文名称

        :param en_name: The en_name of this ListAccessSites.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def cn_name(self):
        """Gets the cn_name of this ListAccessSites.

        中文名称

        :return: The cn_name of this ListAccessSites.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        """Sets the cn_name of this ListAccessSites.

        中文名称

        :param cn_name: The cn_name of this ListAccessSites.
        :type cn_name: str
        """
        self._cn_name = cn_name

    @property
    def created_at(self):
        """Gets the created_at of this ListAccessSites.

        创建时间

        :return: The created_at of this ListAccessSites.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListAccessSites.

        创建时间

        :param created_at: The created_at of this ListAccessSites.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListAccessSites.

        更新时间

        :return: The updated_at of this ListAccessSites.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListAccessSites.

        更新时间

        :param updated_at: The updated_at of this ListAccessSites.
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
        if not isinstance(other, ListAccessSites):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
