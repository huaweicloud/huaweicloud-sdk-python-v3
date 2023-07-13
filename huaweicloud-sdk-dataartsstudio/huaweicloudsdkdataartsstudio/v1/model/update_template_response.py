# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'category_id': 'int',
        'dimension': 'str',
        'type': 'str',
        'system_template': 'bool',
        'sql_info': 'str',
        'abnormal_table_template': 'str',
        'result_description': 'str',
        'create_time': 'int',
        'creator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category_id': 'category_id',
        'dimension': 'dimension',
        'type': 'type',
        'system_template': 'system_template',
        'sql_info': 'sql_info',
        'abnormal_table_template': 'abnormal_table_template',
        'result_description': 'result_description',
        'create_time': 'create_time',
        'creator': 'creator'
    }

    def __init__(self, id=None, name=None, category_id=None, dimension=None, type=None, system_template=None, sql_info=None, abnormal_table_template=None, result_description=None, create_time=None, creator=None):
        """UpdateTemplateResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: name
        :type name: str
        :param category_id: 目录ID
        :type category_id: int
        :param dimension: Completeness:完整性,Uniqueness:唯一性,Timeliness:及时性,Validity:有效性,Accuracy:准确性,Consistency:一致性
        :type dimension: str
        :param type: 规则类型，Field:字段级规则,Table:表级规则,Database:库级规则,Cross-field:跨字段级规则,Customize:自定义规则
        :type type: str
        :param system_template: 是否为系统模板
        :type system_template: bool
        :param sql_info: 定义关系
        :type sql_info: str
        :param abnormal_table_template: 异常表模板
        :type abnormal_table_template: str
        :param result_description: 结果说明
        :type result_description: str
        :param create_time: 创建时间,13位时间戳(精确到毫秒)
        :type create_time: int
        :param creator: 创建者,System代表系统自带
        :type creator: str
        """
        
        super(UpdateTemplateResponse, self).__init__()

        self._id = None
        self._name = None
        self._category_id = None
        self._dimension = None
        self._type = None
        self._system_template = None
        self._sql_info = None
        self._abnormal_table_template = None
        self._result_description = None
        self._create_time = None
        self._creator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category_id is not None:
            self.category_id = category_id
        if dimension is not None:
            self.dimension = dimension
        if type is not None:
            self.type = type
        if system_template is not None:
            self.system_template = system_template
        if sql_info is not None:
            self.sql_info = sql_info
        if abnormal_table_template is not None:
            self.abnormal_table_template = abnormal_table_template
        if result_description is not None:
            self.result_description = result_description
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator

    @property
    def id(self):
        """Gets the id of this UpdateTemplateResponse.

        id

        :return: The id of this UpdateTemplateResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTemplateResponse.

        id

        :param id: The id of this UpdateTemplateResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateTemplateResponse.

        name

        :return: The name of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTemplateResponse.

        name

        :param name: The name of this UpdateTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def category_id(self):
        """Gets the category_id of this UpdateTemplateResponse.

        目录ID

        :return: The category_id of this UpdateTemplateResponse.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this UpdateTemplateResponse.

        目录ID

        :param category_id: The category_id of this UpdateTemplateResponse.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def dimension(self):
        """Gets the dimension of this UpdateTemplateResponse.

        Completeness:完整性,Uniqueness:唯一性,Timeliness:及时性,Validity:有效性,Accuracy:准确性,Consistency:一致性

        :return: The dimension of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this UpdateTemplateResponse.

        Completeness:完整性,Uniqueness:唯一性,Timeliness:及时性,Validity:有效性,Accuracy:准确性,Consistency:一致性

        :param dimension: The dimension of this UpdateTemplateResponse.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def type(self):
        """Gets the type of this UpdateTemplateResponse.

        规则类型，Field:字段级规则,Table:表级规则,Database:库级规则,Cross-field:跨字段级规则,Customize:自定义规则

        :return: The type of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateTemplateResponse.

        规则类型，Field:字段级规则,Table:表级规则,Database:库级规则,Cross-field:跨字段级规则,Customize:自定义规则

        :param type: The type of this UpdateTemplateResponse.
        :type type: str
        """
        self._type = type

    @property
    def system_template(self):
        """Gets the system_template of this UpdateTemplateResponse.

        是否为系统模板

        :return: The system_template of this UpdateTemplateResponse.
        :rtype: bool
        """
        return self._system_template

    @system_template.setter
    def system_template(self, system_template):
        """Sets the system_template of this UpdateTemplateResponse.

        是否为系统模板

        :param system_template: The system_template of this UpdateTemplateResponse.
        :type system_template: bool
        """
        self._system_template = system_template

    @property
    def sql_info(self):
        """Gets the sql_info of this UpdateTemplateResponse.

        定义关系

        :return: The sql_info of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._sql_info

    @sql_info.setter
    def sql_info(self, sql_info):
        """Sets the sql_info of this UpdateTemplateResponse.

        定义关系

        :param sql_info: The sql_info of this UpdateTemplateResponse.
        :type sql_info: str
        """
        self._sql_info = sql_info

    @property
    def abnormal_table_template(self):
        """Gets the abnormal_table_template of this UpdateTemplateResponse.

        异常表模板

        :return: The abnormal_table_template of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._abnormal_table_template

    @abnormal_table_template.setter
    def abnormal_table_template(self, abnormal_table_template):
        """Sets the abnormal_table_template of this UpdateTemplateResponse.

        异常表模板

        :param abnormal_table_template: The abnormal_table_template of this UpdateTemplateResponse.
        :type abnormal_table_template: str
        """
        self._abnormal_table_template = abnormal_table_template

    @property
    def result_description(self):
        """Gets the result_description of this UpdateTemplateResponse.

        结果说明

        :return: The result_description of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description):
        """Sets the result_description of this UpdateTemplateResponse.

        结果说明

        :param result_description: The result_description of this UpdateTemplateResponse.
        :type result_description: str
        """
        self._result_description = result_description

    @property
    def create_time(self):
        """Gets the create_time of this UpdateTemplateResponse.

        创建时间,13位时间戳(精确到毫秒)

        :return: The create_time of this UpdateTemplateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateTemplateResponse.

        创建时间,13位时间戳(精确到毫秒)

        :param create_time: The create_time of this UpdateTemplateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this UpdateTemplateResponse.

        创建者,System代表系统自带

        :return: The creator of this UpdateTemplateResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this UpdateTemplateResponse.

        创建者,System代表系统自带

        :param creator: The creator of this UpdateTemplateResponse.
        :type creator: str
        """
        self._creator = creator

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
        if not isinstance(other, UpdateTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
