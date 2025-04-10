# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandElementValueVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fd_name': 'str',
        'fd_value': 'str',
        'fd_id': 'str',
        'directory_id': 'str',
        'row_id': 'str',
        'id': 'str',
        'status': 'BizStatusEnum',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'fd_name': 'fd_name',
        'fd_value': 'fd_value',
        'fd_id': 'fd_id',
        'directory_id': 'directory_id',
        'row_id': 'row_id',
        'id': 'id',
        'status': 'status',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, fd_name=None, fd_value=None, fd_id=None, directory_id=None, row_id=None, id=None, status=None, create_by=None, update_by=None, create_time=None, update_time=None):
        r"""StandElementValueVO

        The model defined in huaweicloud sdk

        :param fd_name: 属性名称。
        :type fd_name: str
        :param fd_value: 属性值。
        :type fd_value: str
        :param fd_id: 属性定义的ID，ID字符串。
        :type fd_id: str
        :param directory_id: 标准所属目录，ID字符串。
        :type directory_id: str
        :param row_id: 标准所属行，ID字符串。
        :type row_id: str
        :param id: 数据标准的ID，ID字符串。
        :type id: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        """
        
        

        self._fd_name = None
        self._fd_value = None
        self._fd_id = None
        self._directory_id = None
        self._row_id = None
        self._id = None
        self._status = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.fd_name = fd_name
        if fd_value is not None:
            self.fd_value = fd_value
        if fd_id is not None:
            self.fd_id = fd_id
        if directory_id is not None:
            self.directory_id = directory_id
        if row_id is not None:
            self.row_id = row_id
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def fd_name(self):
        r"""Gets the fd_name of this StandElementValueVO.

        属性名称。

        :return: The fd_name of this StandElementValueVO.
        :rtype: str
        """
        return self._fd_name

    @fd_name.setter
    def fd_name(self, fd_name):
        r"""Sets the fd_name of this StandElementValueVO.

        属性名称。

        :param fd_name: The fd_name of this StandElementValueVO.
        :type fd_name: str
        """
        self._fd_name = fd_name

    @property
    def fd_value(self):
        r"""Gets the fd_value of this StandElementValueVO.

        属性值。

        :return: The fd_value of this StandElementValueVO.
        :rtype: str
        """
        return self._fd_value

    @fd_value.setter
    def fd_value(self, fd_value):
        r"""Sets the fd_value of this StandElementValueVO.

        属性值。

        :param fd_value: The fd_value of this StandElementValueVO.
        :type fd_value: str
        """
        self._fd_value = fd_value

    @property
    def fd_id(self):
        r"""Gets the fd_id of this StandElementValueVO.

        属性定义的ID，ID字符串。

        :return: The fd_id of this StandElementValueVO.
        :rtype: str
        """
        return self._fd_id

    @fd_id.setter
    def fd_id(self, fd_id):
        r"""Sets the fd_id of this StandElementValueVO.

        属性定义的ID，ID字符串。

        :param fd_id: The fd_id of this StandElementValueVO.
        :type fd_id: str
        """
        self._fd_id = fd_id

    @property
    def directory_id(self):
        r"""Gets the directory_id of this StandElementValueVO.

        标准所属目录，ID字符串。

        :return: The directory_id of this StandElementValueVO.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        r"""Sets the directory_id of this StandElementValueVO.

        标准所属目录，ID字符串。

        :param directory_id: The directory_id of this StandElementValueVO.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def row_id(self):
        r"""Gets the row_id of this StandElementValueVO.

        标准所属行，ID字符串。

        :return: The row_id of this StandElementValueVO.
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        r"""Sets the row_id of this StandElementValueVO.

        标准所属行，ID字符串。

        :param row_id: The row_id of this StandElementValueVO.
        :type row_id: str
        """
        self._row_id = row_id

    @property
    def id(self):
        r"""Gets the id of this StandElementValueVO.

        数据标准的ID，ID字符串。

        :return: The id of this StandElementValueVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StandElementValueVO.

        数据标准的ID，ID字符串。

        :param id: The id of this StandElementValueVO.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this StandElementValueVO.

        :return: The status of this StandElementValueVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StandElementValueVO.

        :param status: The status of this StandElementValueVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def create_by(self):
        r"""Gets the create_by of this StandElementValueVO.

        创建人。

        :return: The create_by of this StandElementValueVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this StandElementValueVO.

        创建人。

        :param create_by: The create_by of this StandElementValueVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this StandElementValueVO.

        更新人。

        :return: The update_by of this StandElementValueVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this StandElementValueVO.

        更新人。

        :param update_by: The update_by of this StandElementValueVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this StandElementValueVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this StandElementValueVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StandElementValueVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this StandElementValueVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this StandElementValueVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this StandElementValueVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this StandElementValueVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this StandElementValueVO.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, StandElementValueVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
