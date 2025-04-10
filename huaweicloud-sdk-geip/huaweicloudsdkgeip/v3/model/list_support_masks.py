# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupportMasks:

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
        'ip_version': 'int',
        'mask': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'ip_version': 'ip_version',
        'mask': 'mask',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, ip_version=None, mask=None, created_at=None, updated_at=None):
        r"""ListSupportMasks

        The model defined in huaweicloud sdk

        :param id: 全域弹性公网IP段支持的掩码的ID
        :type id: str
        :param ip_version: - 功能说明：全域弹性公网IP的版本 - 取值范围：4、6
        :type ip_version: int
        :param mask: 掩码长度
        :type mask: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._ip_version = None
        self._mask = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if mask is not None:
            self.mask = mask
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ListSupportMasks.

        全域弹性公网IP段支持的掩码的ID

        :return: The id of this ListSupportMasks.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSupportMasks.

        全域弹性公网IP段支持的掩码的ID

        :param id: The id of this ListSupportMasks.
        :type id: str
        """
        self._id = id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListSupportMasks.

        - 功能说明：全域弹性公网IP的版本 - 取值范围：4、6

        :return: The ip_version of this ListSupportMasks.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListSupportMasks.

        - 功能说明：全域弹性公网IP的版本 - 取值范围：4、6

        :param ip_version: The ip_version of this ListSupportMasks.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def mask(self):
        r"""Gets the mask of this ListSupportMasks.

        掩码长度

        :return: The mask of this ListSupportMasks.
        :rtype: int
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        r"""Sets the mask of this ListSupportMasks.

        掩码长度

        :param mask: The mask of this ListSupportMasks.
        :type mask: int
        """
        self._mask = mask

    @property
    def created_at(self):
        r"""Gets the created_at of this ListSupportMasks.

        创建时间

        :return: The created_at of this ListSupportMasks.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListSupportMasks.

        创建时间

        :param created_at: The created_at of this ListSupportMasks.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ListSupportMasks.

        更新时间

        :return: The updated_at of this ListSupportMasks.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ListSupportMasks.

        更新时间

        :param updated_at: The updated_at of this ListSupportMasks.
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
        if not isinstance(other, ListSupportMasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
