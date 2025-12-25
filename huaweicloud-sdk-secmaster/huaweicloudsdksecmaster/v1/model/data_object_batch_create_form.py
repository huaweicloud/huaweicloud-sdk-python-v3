# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataObjectBatchCreateForm:

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
        'format_version': 'int',
        'name': 'str',
        'type': 'str',
        'trigger_flag': 'bool',
        'data_object_list': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'format_version': 'format_version',
        'name': 'name',
        'type': 'type',
        'trigger_flag': 'trigger_flag',
        'data_object_list': 'data_object_list'
    }

    def __init__(self, id=None, format_version=None, name=None, type=None, trigger_flag=None, data_object_list=None):
        r"""DataObjectBatchCreateForm

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID
        :type id: str
        :param format_version: 对齐的模板版本号，默认传1
        :type format_version: int
        :param name: 名称
        :type name: str
        :param type: 描述
        :type type: str
        :param trigger_flag: 触发标志
        :type trigger_flag: bool
        :param data_object_list: 数据对象列表
        :type data_object_list: list[object]
        """
        
        

        self._id = None
        self._format_version = None
        self._name = None
        self._type = None
        self._trigger_flag = None
        self._data_object_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if format_version is not None:
            self.format_version = format_version
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if trigger_flag is not None:
            self.trigger_flag = trigger_flag
        if data_object_list is not None:
            self.data_object_list = data_object_list

    @property
    def id(self):
        r"""Gets the id of this DataObjectBatchCreateForm.

        唯一标识ID

        :return: The id of this DataObjectBatchCreateForm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataObjectBatchCreateForm.

        唯一标识ID

        :param id: The id of this DataObjectBatchCreateForm.
        :type id: str
        """
        self._id = id

    @property
    def format_version(self):
        r"""Gets the format_version of this DataObjectBatchCreateForm.

        对齐的模板版本号，默认传1

        :return: The format_version of this DataObjectBatchCreateForm.
        :rtype: int
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        r"""Sets the format_version of this DataObjectBatchCreateForm.

        对齐的模板版本号，默认传1

        :param format_version: The format_version of this DataObjectBatchCreateForm.
        :type format_version: int
        """
        self._format_version = format_version

    @property
    def name(self):
        r"""Gets the name of this DataObjectBatchCreateForm.

        名称

        :return: The name of this DataObjectBatchCreateForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataObjectBatchCreateForm.

        名称

        :param name: The name of this DataObjectBatchCreateForm.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DataObjectBatchCreateForm.

        描述

        :return: The type of this DataObjectBatchCreateForm.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataObjectBatchCreateForm.

        描述

        :param type: The type of this DataObjectBatchCreateForm.
        :type type: str
        """
        self._type = type

    @property
    def trigger_flag(self):
        r"""Gets the trigger_flag of this DataObjectBatchCreateForm.

        触发标志

        :return: The trigger_flag of this DataObjectBatchCreateForm.
        :rtype: bool
        """
        return self._trigger_flag

    @trigger_flag.setter
    def trigger_flag(self, trigger_flag):
        r"""Sets the trigger_flag of this DataObjectBatchCreateForm.

        触发标志

        :param trigger_flag: The trigger_flag of this DataObjectBatchCreateForm.
        :type trigger_flag: bool
        """
        self._trigger_flag = trigger_flag

    @property
    def data_object_list(self):
        r"""Gets the data_object_list of this DataObjectBatchCreateForm.

        数据对象列表

        :return: The data_object_list of this DataObjectBatchCreateForm.
        :rtype: list[object]
        """
        return self._data_object_list

    @data_object_list.setter
    def data_object_list(self, data_object_list):
        r"""Sets the data_object_list of this DataObjectBatchCreateForm.

        数据对象列表

        :param data_object_list: The data_object_list of this DataObjectBatchCreateForm.
        :type data_object_list: list[object]
        """
        self._data_object_list = data_object_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataObjectBatchCreateForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
