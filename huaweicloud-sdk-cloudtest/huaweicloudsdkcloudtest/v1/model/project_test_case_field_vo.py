# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectTestCaseFieldVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'type': 'str',
        'options': 'str',
        'description': 'str',
        'creator': 'str',
        'updater': 'str',
        'custom_field_id': 'int',
        'custom_field_name': 'str',
        'custom_field_param': 'str',
        'type_name': 'str',
        'create_time': 'datetime',
        'create_time_timestamp': 'int',
        'update_time': 'datetime',
        'update_time_timestamp': 'int',
        'project_uuid': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'type': 'type',
        'options': 'options',
        'description': 'description',
        'creator': 'creator',
        'updater': 'updater',
        'custom_field_id': 'custom_field_id',
        'custom_field_name': 'custom_field_name',
        'custom_field_param': 'custom_field_param',
        'type_name': 'type_name',
        'create_time': 'create_time',
        'create_time_timestamp': 'create_time_timestamp',
        'update_time': 'update_time',
        'update_time_timestamp': 'update_time_timestamp',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, uri=None, name=None, type=None, options=None, description=None, creator=None, updater=None, custom_field_id=None, custom_field_name=None, custom_field_param=None, type_name=None, create_time=None, create_time_timestamp=None, update_time=None, update_time_timestamp=None, project_uuid=None):
        r"""ProjectTestCaseFieldVo

        The model defined in huaweicloud sdk

        :param uri: 项目用例自定义字段主键
        :type uri: str
        :param name: 项目用例自定义字段名称
        :type name: str
        :param type: 项目用例自定义字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）
        :type type: str
        :param options: 项目用例自定义字段选项（数字类型时，数组两个值，第一个是最小值，第二个是最大值）
        :type options: str
        :param description: 项目用例自定义字段描述
        :type description: str
        :param creator: 项目用例自定义字段创建人
        :type creator: str
        :param updater: 项目用例自定义字段更新人
        :type updater: str
        :param custom_field_id: 项目用例自定义字段id（1-25数字）
        :type custom_field_id: int
        :param custom_field_name: 项目用例自定义字段名称
        :type custom_field_name: str
        :param custom_field_param: 项目用例自定义字段入参或者返回参数名称
        :type custom_field_param: str
        :param type_name: 项目用例自定义字段类型国际化名称
        :type type_name: str
        :param create_time: 项目用例自定义字段创建时间
        :type create_time: datetime
        :param create_time_timestamp: 项目用例自定义字段创建时间时间戳
        :type create_time_timestamp: int
        :param update_time: 项目用例自定义字段更新时间
        :type update_time: datetime
        :param update_time_timestamp: 项目用例自定义字段更新时间时间戳
        :type update_time_timestamp: int
        :param project_uuid: 项目id
        :type project_uuid: str
        """
        
        

        self._uri = None
        self._name = None
        self._type = None
        self._options = None
        self._description = None
        self._creator = None
        self._updater = None
        self._custom_field_id = None
        self._custom_field_name = None
        self._custom_field_param = None
        self._type_name = None
        self._create_time = None
        self._create_time_timestamp = None
        self._update_time = None
        self._update_time_timestamp = None
        self._project_uuid = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if options is not None:
            self.options = options
        if description is not None:
            self.description = description
        if creator is not None:
            self.creator = creator
        if updater is not None:
            self.updater = updater
        if custom_field_id is not None:
            self.custom_field_id = custom_field_id
        if custom_field_name is not None:
            self.custom_field_name = custom_field_name
        if custom_field_param is not None:
            self.custom_field_param = custom_field_param
        if type_name is not None:
            self.type_name = type_name
        if create_time is not None:
            self.create_time = create_time
        if create_time_timestamp is not None:
            self.create_time_timestamp = create_time_timestamp
        if update_time is not None:
            self.update_time = update_time
        if update_time_timestamp is not None:
            self.update_time_timestamp = update_time_timestamp
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def uri(self):
        r"""Gets the uri of this ProjectTestCaseFieldVo.

        项目用例自定义字段主键

        :return: The uri of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ProjectTestCaseFieldVo.

        项目用例自定义字段主键

        :param uri: The uri of this ProjectTestCaseFieldVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this ProjectTestCaseFieldVo.

        项目用例自定义字段名称

        :return: The name of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectTestCaseFieldVo.

        项目用例自定义字段名称

        :param name: The name of this ProjectTestCaseFieldVo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ProjectTestCaseFieldVo.

        项目用例自定义字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）

        :return: The type of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProjectTestCaseFieldVo.

        项目用例自定义字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）

        :param type: The type of this ProjectTestCaseFieldVo.
        :type type: str
        """
        self._type = type

    @property
    def options(self):
        r"""Gets the options of this ProjectTestCaseFieldVo.

        项目用例自定义字段选项（数字类型时，数组两个值，第一个是最小值，第二个是最大值）

        :return: The options of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ProjectTestCaseFieldVo.

        项目用例自定义字段选项（数字类型时，数组两个值，第一个是最小值，第二个是最大值）

        :param options: The options of this ProjectTestCaseFieldVo.
        :type options: str
        """
        self._options = options

    @property
    def description(self):
        r"""Gets the description of this ProjectTestCaseFieldVo.

        项目用例自定义字段描述

        :return: The description of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProjectTestCaseFieldVo.

        项目用例自定义字段描述

        :param description: The description of this ProjectTestCaseFieldVo.
        :type description: str
        """
        self._description = description

    @property
    def creator(self):
        r"""Gets the creator of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建人

        :return: The creator of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建人

        :param creator: The creator of this ProjectTestCaseFieldVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updater(self):
        r"""Gets the updater of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新人

        :return: The updater of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新人

        :param updater: The updater of this ProjectTestCaseFieldVo.
        :type updater: str
        """
        self._updater = updater

    @property
    def custom_field_id(self):
        r"""Gets the custom_field_id of this ProjectTestCaseFieldVo.

        项目用例自定义字段id（1-25数字）

        :return: The custom_field_id of this ProjectTestCaseFieldVo.
        :rtype: int
        """
        return self._custom_field_id

    @custom_field_id.setter
    def custom_field_id(self, custom_field_id):
        r"""Sets the custom_field_id of this ProjectTestCaseFieldVo.

        项目用例自定义字段id（1-25数字）

        :param custom_field_id: The custom_field_id of this ProjectTestCaseFieldVo.
        :type custom_field_id: int
        """
        self._custom_field_id = custom_field_id

    @property
    def custom_field_name(self):
        r"""Gets the custom_field_name of this ProjectTestCaseFieldVo.

        项目用例自定义字段名称

        :return: The custom_field_name of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._custom_field_name

    @custom_field_name.setter
    def custom_field_name(self, custom_field_name):
        r"""Sets the custom_field_name of this ProjectTestCaseFieldVo.

        项目用例自定义字段名称

        :param custom_field_name: The custom_field_name of this ProjectTestCaseFieldVo.
        :type custom_field_name: str
        """
        self._custom_field_name = custom_field_name

    @property
    def custom_field_param(self):
        r"""Gets the custom_field_param of this ProjectTestCaseFieldVo.

        项目用例自定义字段入参或者返回参数名称

        :return: The custom_field_param of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._custom_field_param

    @custom_field_param.setter
    def custom_field_param(self, custom_field_param):
        r"""Sets the custom_field_param of this ProjectTestCaseFieldVo.

        项目用例自定义字段入参或者返回参数名称

        :param custom_field_param: The custom_field_param of this ProjectTestCaseFieldVo.
        :type custom_field_param: str
        """
        self._custom_field_param = custom_field_param

    @property
    def type_name(self):
        r"""Gets the type_name of this ProjectTestCaseFieldVo.

        项目用例自定义字段类型国际化名称

        :return: The type_name of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this ProjectTestCaseFieldVo.

        项目用例自定义字段类型国际化名称

        :param type_name: The type_name of this ProjectTestCaseFieldVo.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建时间

        :return: The create_time of this ProjectTestCaseFieldVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建时间

        :param create_time: The create_time of this ProjectTestCaseFieldVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_time_timestamp(self):
        r"""Gets the create_time_timestamp of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建时间时间戳

        :return: The create_time_timestamp of this ProjectTestCaseFieldVo.
        :rtype: int
        """
        return self._create_time_timestamp

    @create_time_timestamp.setter
    def create_time_timestamp(self, create_time_timestamp):
        r"""Sets the create_time_timestamp of this ProjectTestCaseFieldVo.

        项目用例自定义字段创建时间时间戳

        :param create_time_timestamp: The create_time_timestamp of this ProjectTestCaseFieldVo.
        :type create_time_timestamp: int
        """
        self._create_time_timestamp = create_time_timestamp

    @property
    def update_time(self):
        r"""Gets the update_time of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新时间

        :return: The update_time of this ProjectTestCaseFieldVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新时间

        :param update_time: The update_time of this ProjectTestCaseFieldVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_time_timestamp(self):
        r"""Gets the update_time_timestamp of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新时间时间戳

        :return: The update_time_timestamp of this ProjectTestCaseFieldVo.
        :rtype: int
        """
        return self._update_time_timestamp

    @update_time_timestamp.setter
    def update_time_timestamp(self, update_time_timestamp):
        r"""Sets the update_time_timestamp of this ProjectTestCaseFieldVo.

        项目用例自定义字段更新时间时间戳

        :param update_time_timestamp: The update_time_timestamp of this ProjectTestCaseFieldVo.
        :type update_time_timestamp: int
        """
        self._update_time_timestamp = update_time_timestamp

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ProjectTestCaseFieldVo.

        项目id

        :return: The project_uuid of this ProjectTestCaseFieldVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ProjectTestCaseFieldVo.

        项目id

        :param project_uuid: The project_uuid of this ProjectTestCaseFieldVo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

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
        if not isinstance(other, ProjectTestCaseFieldVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
