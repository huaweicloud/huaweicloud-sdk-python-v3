# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateRO:

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
        'directory_id': 'int',
        'dimension_id': 'int',
        'description': 'str',
        'sql_info': 'str',
        'result_description': 'str',
        'publish': 'bool',
        'origin_name': 'str',
        'abnormal_table_template': 'str',
        'user_define_version_name': 'str',
        'version_num': 'int',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'directory_id': 'directory_id',
        'dimension_id': 'dimension_id',
        'description': 'description',
        'sql_info': 'sql_info',
        'result_description': 'result_description',
        'publish': 'publish',
        'origin_name': 'origin_name',
        'abnormal_table_template': 'abnormal_table_template',
        'user_define_version_name': 'user_define_version_name',
        'version_num': 'version_num',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, directory_id=None, dimension_id=None, description=None, sql_info=None, result_description=None, publish=None, origin_name=None, abnormal_table_template=None, user_define_version_name=None, version_num=None, status=None):
        """TemplateRO

        The model defined in huaweicloud sdk

        :param id: template id
        :type id: str
        :param name: template name
        :type name: str
        :param directory_id: 目录
        :type directory_id: int
        :param dimension_id: 维度ID, 1:完整性,2:唯一性,3:及时性,4:有效性,5:准确性,6:一致性
        :type dimension_id: int
        :param description: 描述
        :type description: str
        :param sql_info: 模板中的sql内容
        :type sql_info: str
        :param result_description: 结果说明
        :type result_description: str
        :param publish: 是否是发布操作， true：发布新版本  false：普通的保存操作
        :type publish: bool
        :param origin_name: 修改前的模板名
        :type origin_name: str
        :param abnormal_table_template: 异常表模板
        :type abnormal_table_template: str
        :param user_define_version_name: 用户自定义版本名
        :type user_define_version_name: str
        :param version_num: 获取模板信息时候的版本号
        :type version_num: int
        :param status: 规则模板状态,0表示下线1表示已发布
        :type status: int
        """
        
        

        self._id = None
        self._name = None
        self._directory_id = None
        self._dimension_id = None
        self._description = None
        self._sql_info = None
        self._result_description = None
        self._publish = None
        self._origin_name = None
        self._abnormal_table_template = None
        self._user_define_version_name = None
        self._version_num = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if directory_id is not None:
            self.directory_id = directory_id
        if dimension_id is not None:
            self.dimension_id = dimension_id
        if description is not None:
            self.description = description
        if sql_info is not None:
            self.sql_info = sql_info
        if result_description is not None:
            self.result_description = result_description
        if publish is not None:
            self.publish = publish
        if origin_name is not None:
            self.origin_name = origin_name
        if abnormal_table_template is not None:
            self.abnormal_table_template = abnormal_table_template
        if user_define_version_name is not None:
            self.user_define_version_name = user_define_version_name
        if version_num is not None:
            self.version_num = version_num
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this TemplateRO.

        template id

        :return: The id of this TemplateRO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateRO.

        template id

        :param id: The id of this TemplateRO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateRO.

        template name

        :return: The name of this TemplateRO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateRO.

        template name

        :param name: The name of this TemplateRO.
        :type name: str
        """
        self._name = name

    @property
    def directory_id(self):
        """Gets the directory_id of this TemplateRO.

        目录

        :return: The directory_id of this TemplateRO.
        :rtype: int
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this TemplateRO.

        目录

        :param directory_id: The directory_id of this TemplateRO.
        :type directory_id: int
        """
        self._directory_id = directory_id

    @property
    def dimension_id(self):
        """Gets the dimension_id of this TemplateRO.

        维度ID, 1:完整性,2:唯一性,3:及时性,4:有效性,5:准确性,6:一致性

        :return: The dimension_id of this TemplateRO.
        :rtype: int
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this TemplateRO.

        维度ID, 1:完整性,2:唯一性,3:及时性,4:有效性,5:准确性,6:一致性

        :param dimension_id: The dimension_id of this TemplateRO.
        :type dimension_id: int
        """
        self._dimension_id = dimension_id

    @property
    def description(self):
        """Gets the description of this TemplateRO.

        描述

        :return: The description of this TemplateRO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateRO.

        描述

        :param description: The description of this TemplateRO.
        :type description: str
        """
        self._description = description

    @property
    def sql_info(self):
        """Gets the sql_info of this TemplateRO.

        模板中的sql内容

        :return: The sql_info of this TemplateRO.
        :rtype: str
        """
        return self._sql_info

    @sql_info.setter
    def sql_info(self, sql_info):
        """Sets the sql_info of this TemplateRO.

        模板中的sql内容

        :param sql_info: The sql_info of this TemplateRO.
        :type sql_info: str
        """
        self._sql_info = sql_info

    @property
    def result_description(self):
        """Gets the result_description of this TemplateRO.

        结果说明

        :return: The result_description of this TemplateRO.
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description):
        """Sets the result_description of this TemplateRO.

        结果说明

        :param result_description: The result_description of this TemplateRO.
        :type result_description: str
        """
        self._result_description = result_description

    @property
    def publish(self):
        """Gets the publish of this TemplateRO.

        是否是发布操作， true：发布新版本  false：普通的保存操作

        :return: The publish of this TemplateRO.
        :rtype: bool
        """
        return self._publish

    @publish.setter
    def publish(self, publish):
        """Sets the publish of this TemplateRO.

        是否是发布操作， true：发布新版本  false：普通的保存操作

        :param publish: The publish of this TemplateRO.
        :type publish: bool
        """
        self._publish = publish

    @property
    def origin_name(self):
        """Gets the origin_name of this TemplateRO.

        修改前的模板名

        :return: The origin_name of this TemplateRO.
        :rtype: str
        """
        return self._origin_name

    @origin_name.setter
    def origin_name(self, origin_name):
        """Sets the origin_name of this TemplateRO.

        修改前的模板名

        :param origin_name: The origin_name of this TemplateRO.
        :type origin_name: str
        """
        self._origin_name = origin_name

    @property
    def abnormal_table_template(self):
        """Gets the abnormal_table_template of this TemplateRO.

        异常表模板

        :return: The abnormal_table_template of this TemplateRO.
        :rtype: str
        """
        return self._abnormal_table_template

    @abnormal_table_template.setter
    def abnormal_table_template(self, abnormal_table_template):
        """Sets the abnormal_table_template of this TemplateRO.

        异常表模板

        :param abnormal_table_template: The abnormal_table_template of this TemplateRO.
        :type abnormal_table_template: str
        """
        self._abnormal_table_template = abnormal_table_template

    @property
    def user_define_version_name(self):
        """Gets the user_define_version_name of this TemplateRO.

        用户自定义版本名

        :return: The user_define_version_name of this TemplateRO.
        :rtype: str
        """
        return self._user_define_version_name

    @user_define_version_name.setter
    def user_define_version_name(self, user_define_version_name):
        """Sets the user_define_version_name of this TemplateRO.

        用户自定义版本名

        :param user_define_version_name: The user_define_version_name of this TemplateRO.
        :type user_define_version_name: str
        """
        self._user_define_version_name = user_define_version_name

    @property
    def version_num(self):
        """Gets the version_num of this TemplateRO.

        获取模板信息时候的版本号

        :return: The version_num of this TemplateRO.
        :rtype: int
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        """Sets the version_num of this TemplateRO.

        获取模板信息时候的版本号

        :param version_num: The version_num of this TemplateRO.
        :type version_num: int
        """
        self._version_num = version_num

    @property
    def status(self):
        """Gets the status of this TemplateRO.

        规则模板状态,0表示下线1表示已发布

        :return: The status of this TemplateRO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplateRO.

        规则模板状态,0表示下线1表示已发布

        :param status: The status of this TemplateRO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, TemplateRO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
