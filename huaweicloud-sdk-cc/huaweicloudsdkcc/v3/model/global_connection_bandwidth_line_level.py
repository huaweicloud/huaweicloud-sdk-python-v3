# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthLineLevel:

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
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'local_area': 'str',
        'remote_area': 'str',
        'levels': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'local_area': 'local_area',
        'remote_area': 'remote_area',
        'levels': 'levels'
    }

    def __init__(self, id=None, description=None, created_at=None, updated_at=None, local_area=None, remote_area=None, levels=None):
        r"""GlobalConnectionBandwidthLineLevel

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param local_area: 功能说明：线路分级本端接入点。
        :type local_area: str
        :param remote_area: 功能描述：线路分级远端接入点。
        :type remote_area: str
        :param levels: 支持的铂金、金、银分级。
        :type levels: list[str]
        """
        
        

        self._id = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._local_area = None
        self._remote_area = None
        self._levels = None
        self.discriminator = None

        self.id = id
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        if local_area is not None:
            self.local_area = local_area
        if remote_area is not None:
            self.remote_area = remote_area
        if levels is not None:
            self.levels = levels

    @property
    def id(self):
        r"""Gets the id of this GlobalConnectionBandwidthLineLevel.

        实例ID。

        :return: The id of this GlobalConnectionBandwidthLineLevel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GlobalConnectionBandwidthLineLevel.

        实例ID。

        :param id: The id of this GlobalConnectionBandwidthLineLevel.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this GlobalConnectionBandwidthLineLevel.

        实例描述。不支持 <>。

        :return: The description of this GlobalConnectionBandwidthLineLevel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GlobalConnectionBandwidthLineLevel.

        实例描述。不支持 <>。

        :param description: The description of this GlobalConnectionBandwidthLineLevel.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this GlobalConnectionBandwidthLineLevel.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this GlobalConnectionBandwidthLineLevel.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GlobalConnectionBandwidthLineLevel.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this GlobalConnectionBandwidthLineLevel.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GlobalConnectionBandwidthLineLevel.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this GlobalConnectionBandwidthLineLevel.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GlobalConnectionBandwidthLineLevel.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this GlobalConnectionBandwidthLineLevel.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def local_area(self):
        r"""Gets the local_area of this GlobalConnectionBandwidthLineLevel.

        功能说明：线路分级本端接入点。

        :return: The local_area of this GlobalConnectionBandwidthLineLevel.
        :rtype: str
        """
        return self._local_area

    @local_area.setter
    def local_area(self, local_area):
        r"""Sets the local_area of this GlobalConnectionBandwidthLineLevel.

        功能说明：线路分级本端接入点。

        :param local_area: The local_area of this GlobalConnectionBandwidthLineLevel.
        :type local_area: str
        """
        self._local_area = local_area

    @property
    def remote_area(self):
        r"""Gets the remote_area of this GlobalConnectionBandwidthLineLevel.

        功能描述：线路分级远端接入点。

        :return: The remote_area of this GlobalConnectionBandwidthLineLevel.
        :rtype: str
        """
        return self._remote_area

    @remote_area.setter
    def remote_area(self, remote_area):
        r"""Sets the remote_area of this GlobalConnectionBandwidthLineLevel.

        功能描述：线路分级远端接入点。

        :param remote_area: The remote_area of this GlobalConnectionBandwidthLineLevel.
        :type remote_area: str
        """
        self._remote_area = remote_area

    @property
    def levels(self):
        r"""Gets the levels of this GlobalConnectionBandwidthLineLevel.

        支持的铂金、金、银分级。

        :return: The levels of this GlobalConnectionBandwidthLineLevel.
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        r"""Sets the levels of this GlobalConnectionBandwidthLineLevel.

        支持的铂金、金、银分级。

        :param levels: The levels of this GlobalConnectionBandwidthLineLevel.
        :type levels: list[str]
        """
        self._levels = levels

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
        if not isinstance(other, GlobalConnectionBandwidthLineLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
