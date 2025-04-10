# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlBackupListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'backup_id': 'str',
        'backup_type': 'str',
        'offset': 'str',
        'limit': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'name': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'name': 'name',
        'instance_name': 'instance_name'
    }

    def __init__(self, x_language=None, instance_id=None, backup_id=None, backup_type=None, offset=None, limit=None, begin_time=None, end_time=None, name=None, instance_name=None):
        r"""ShowGaussMySqlBackupListRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param backup_id: 备份ID。
        :type backup_id: str
        :param backup_type: 备份类型。  取值范围： - auto：自动全量备份。 - manual：手动全量备份。
        :type backup_type: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: str
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: str
        :param begin_time: 查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type begin_time: str
        :param end_time: 查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        :param name: 备份名称。
        :type name: str
        :param instance_name: 实例名称。
        :type instance_name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._backup_id = None
        self._backup_type = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self._name = None
        self._instance_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if instance_id is not None:
            self.instance_id = instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if name is not None:
            self.name = name
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowGaussMySqlBackupListRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowGaussMySqlBackupListRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowGaussMySqlBackupListRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowGaussMySqlBackupListRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowGaussMySqlBackupListRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowGaussMySqlBackupListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this ShowGaussMySqlBackupListRequest.

        备份ID。

        :return: The backup_id of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this ShowGaussMySqlBackupListRequest.

        备份ID。

        :param backup_id: The backup_id of this ShowGaussMySqlBackupListRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        r"""Gets the backup_type of this ShowGaussMySqlBackupListRequest.

        备份类型。  取值范围： - auto：自动全量备份。 - manual：手动全量备份。

        :return: The backup_type of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this ShowGaussMySqlBackupListRequest.

        备份类型。  取值范围： - auto：自动全量备份。 - manual：手动全量备份。

        :param backup_type: The backup_type of this ShowGaussMySqlBackupListRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def offset(self):
        r"""Gets the offset of this ShowGaussMySqlBackupListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowGaussMySqlBackupListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowGaussMySqlBackupListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowGaussMySqlBackupListRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowGaussMySqlBackupListRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowGaussMySqlBackupListRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowGaussMySqlBackupListRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The begin_time of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowGaussMySqlBackupListRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param begin_time: The begin_time of this ShowGaussMySqlBackupListRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowGaussMySqlBackupListRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowGaussMySqlBackupListRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this ShowGaussMySqlBackupListRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def name(self):
        r"""Gets the name of this ShowGaussMySqlBackupListRequest.

        备份名称。

        :return: The name of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowGaussMySqlBackupListRequest.

        备份名称。

        :param name: The name of this ShowGaussMySqlBackupListRequest.
        :type name: str
        """
        self._name = name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowGaussMySqlBackupListRequest.

        实例名称。

        :return: The instance_name of this ShowGaussMySqlBackupListRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowGaussMySqlBackupListRequest.

        实例名称。

        :param instance_name: The instance_name of this ShowGaussMySqlBackupListRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, ShowGaussMySqlBackupListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
