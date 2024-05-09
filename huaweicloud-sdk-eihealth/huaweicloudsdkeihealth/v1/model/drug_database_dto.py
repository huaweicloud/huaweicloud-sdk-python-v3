# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DrugDatabaseDto:

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
        'type': 'str',
        'status': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'creator': 'str',
        'failed_message': 'str',
        'css_id': 'str',
        'css_name': 'str',
        'files': 'list[DetailDatabaseFile]',
        'columns': 'list[str]',
        'shareable': 'bool',
        'data_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator': 'creator',
        'failed_message': 'failed_message',
        'css_id': 'css_id',
        'css_name': 'css_name',
        'files': 'files',
        'columns': 'columns',
        'shareable': 'shareable',
        'data_num': 'data_num'
    }

    def __init__(self, id=None, name=None, type=None, status=None, description=None, create_time=None, update_time=None, creator=None, failed_message=None, css_id=None, css_name=None, files=None, columns=None, shareable=None, data_num=None):
        """DrugDatabaseDto

        The model defined in huaweicloud sdk

        :param id: 数据库id
        :type id: str
        :param name: 数据库名称
        :type name: str
        :param type: 数据库类型
        :type type: str
        :param status: 数据库状态
        :type status: str
        :param description: 数据库描述
        :type description: str
        :param create_time: 数据库创建时间
        :type create_time: str
        :param update_time: 数据库更新时间
        :type update_time: str
        :param creator: 创建数据库的用户名称
        :type creator: str
        :param failed_message: 失败提示，当作业执行失败时会返回
        :type failed_message: str
        :param css_id: css集群id
        :type css_id: str
        :param css_name: css集群名称
        :type css_name: str
        :param files: 数据库文件列表
        :type files: list[:class:`huaweicloudsdkeihealth.v1.DetailDatabaseFile`]
        :param columns: 数据库列名
        :type columns: list[str]
        :param shareable: 是否打开组织共享
        :type shareable: bool
        :param data_num: 分子数量
        :type data_num: int
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._creator = None
        self._failed_message = None
        self._css_id = None
        self._css_name = None
        self._files = None
        self._columns = None
        self._shareable = None
        self._data_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator
        if failed_message is not None:
            self.failed_message = failed_message
        if css_id is not None:
            self.css_id = css_id
        if css_name is not None:
            self.css_name = css_name
        if files is not None:
            self.files = files
        if columns is not None:
            self.columns = columns
        if shareable is not None:
            self.shareable = shareable
        if data_num is not None:
            self.data_num = data_num

    @property
    def id(self):
        """Gets the id of this DrugDatabaseDto.

        数据库id

        :return: The id of this DrugDatabaseDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DrugDatabaseDto.

        数据库id

        :param id: The id of this DrugDatabaseDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DrugDatabaseDto.

        数据库名称

        :return: The name of this DrugDatabaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DrugDatabaseDto.

        数据库名称

        :param name: The name of this DrugDatabaseDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this DrugDatabaseDto.

        数据库类型

        :return: The type of this DrugDatabaseDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DrugDatabaseDto.

        数据库类型

        :param type: The type of this DrugDatabaseDto.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this DrugDatabaseDto.

        数据库状态

        :return: The status of this DrugDatabaseDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DrugDatabaseDto.

        数据库状态

        :param status: The status of this DrugDatabaseDto.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this DrugDatabaseDto.

        数据库描述

        :return: The description of this DrugDatabaseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DrugDatabaseDto.

        数据库描述

        :param description: The description of this DrugDatabaseDto.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this DrugDatabaseDto.

        数据库创建时间

        :return: The create_time of this DrugDatabaseDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DrugDatabaseDto.

        数据库创建时间

        :param create_time: The create_time of this DrugDatabaseDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DrugDatabaseDto.

        数据库更新时间

        :return: The update_time of this DrugDatabaseDto.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DrugDatabaseDto.

        数据库更新时间

        :param update_time: The update_time of this DrugDatabaseDto.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def creator(self):
        """Gets the creator of this DrugDatabaseDto.

        创建数据库的用户名称

        :return: The creator of this DrugDatabaseDto.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DrugDatabaseDto.

        创建数据库的用户名称

        :param creator: The creator of this DrugDatabaseDto.
        :type creator: str
        """
        self._creator = creator

    @property
    def failed_message(self):
        """Gets the failed_message of this DrugDatabaseDto.

        失败提示，当作业执行失败时会返回

        :return: The failed_message of this DrugDatabaseDto.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this DrugDatabaseDto.

        失败提示，当作业执行失败时会返回

        :param failed_message: The failed_message of this DrugDatabaseDto.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def css_id(self):
        """Gets the css_id of this DrugDatabaseDto.

        css集群id

        :return: The css_id of this DrugDatabaseDto.
        :rtype: str
        """
        return self._css_id

    @css_id.setter
    def css_id(self, css_id):
        """Sets the css_id of this DrugDatabaseDto.

        css集群id

        :param css_id: The css_id of this DrugDatabaseDto.
        :type css_id: str
        """
        self._css_id = css_id

    @property
    def css_name(self):
        """Gets the css_name of this DrugDatabaseDto.

        css集群名称

        :return: The css_name of this DrugDatabaseDto.
        :rtype: str
        """
        return self._css_name

    @css_name.setter
    def css_name(self, css_name):
        """Sets the css_name of this DrugDatabaseDto.

        css集群名称

        :param css_name: The css_name of this DrugDatabaseDto.
        :type css_name: str
        """
        self._css_name = css_name

    @property
    def files(self):
        """Gets the files of this DrugDatabaseDto.

        数据库文件列表

        :return: The files of this DrugDatabaseDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DetailDatabaseFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this DrugDatabaseDto.

        数据库文件列表

        :param files: The files of this DrugDatabaseDto.
        :type files: list[:class:`huaweicloudsdkeihealth.v1.DetailDatabaseFile`]
        """
        self._files = files

    @property
    def columns(self):
        """Gets the columns of this DrugDatabaseDto.

        数据库列名

        :return: The columns of this DrugDatabaseDto.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this DrugDatabaseDto.

        数据库列名

        :param columns: The columns of this DrugDatabaseDto.
        :type columns: list[str]
        """
        self._columns = columns

    @property
    def shareable(self):
        """Gets the shareable of this DrugDatabaseDto.

        是否打开组织共享

        :return: The shareable of this DrugDatabaseDto.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this DrugDatabaseDto.

        是否打开组织共享

        :param shareable: The shareable of this DrugDatabaseDto.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def data_num(self):
        """Gets the data_num of this DrugDatabaseDto.

        分子数量

        :return: The data_num of this DrugDatabaseDto.
        :rtype: int
        """
        return self._data_num

    @data_num.setter
    def data_num(self, data_num):
        """Sets the data_num of this DrugDatabaseDto.

        分子数量

        :param data_num: The data_num of this DrugDatabaseDto.
        :type data_num: int
        """
        self._data_num = data_num

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
        if not isinstance(other, DrugDatabaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
